#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Publication programmée des posts « Une 2CV, mille histoires ».

Deux mécaniques différentes, parce que Meta ne traite pas les deux réseaux
de la même façon :

  - Facebook  : l'API sait programmer. Le post est déposé chez Meta à l'avance
                (published=false + scheduled_publish_time) et c'est Meta qui
                publie à l'heure dite, à la seconde près.
  - Instagram : l'API ne sait pas programmer. Le post doit être envoyé au
                moment exact de la publication — d'où le cron GitHub Actions.

Les posts vivent dans posts/*.md (en-tête YAML + texte). L'état de ce qui a
déjà été publié est gardé dans posts/.etat.json, réécrit puis commité par le
workflow : c'est lui qui garantit qu'un post ne part jamais deux fois.

Usage :
    python scripts/publier_meta.py --valider      # contrôle les fichiers, rien d'autre
    python scripts/publier_meta.py --simulation   # montre ce qui partirait
    python scripts/publier_meta.py                # publie pour de vrai
"""
import argparse, datetime, json, os, sys, time
from zoneinfo import ZoneInfo

import requests
import yaml

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOSSIER = os.path.join(RACINE, "posts")
ETAT = os.path.join(DOSSIER, ".etat.json")

TZ = ZoneInfo("Indian/Reunion")
API = os.environ.get("META_API_VERSION", "v23.0")
BASE = "https://graph.facebook.com/%s" % API
MEDIA_BASE = os.environ.get("MEDIA_BASE_URL", "https://assocollectifensemble-sys.github.io").rstrip("/")

CIBLES = ("facebook", "instagram")
# Meta refuse une programmation à moins de 10 min. On garde de la marge : en
# dessous de ce seuil on ne programme pas, on laissera un passage suivant du
# cron publier en direct.
MARGE = datetime.timedelta(minutes=15)
# Garde-fou : un post daté d'il y a plus longtemps que ça ne part pas tout
# seul (sinon ajouter un vieux fichier déclencherait une publication surprise).
PEREMPTION = datetime.timedelta(hours=48)

IG_LEGENDE_MAX = 2200
IG_CARROUSEL_MAX = 10


class Erreur(Exception):
    pass


# --------------------------------------------------------------------------
# Lecture des posts
# --------------------------------------------------------------------------

def lire_posts():
    """Retourne (posts triés par date, erreurs de lecture).

    Un fichier illisible n'interrompt pas les autres : on veut pouvoir corriger
    toutes les coquilles en une seule fois.
    """
    posts, erreurs = [], []
    if not os.path.isdir(DOSSIER):
        return posts, erreurs
    for nom in sorted(os.listdir(DOSSIER)):
        if not nom.endswith(".md") or nom.startswith(".") or nom.lower() == "readme.md":
            continue
        chemin = os.path.join(DOSSIER, nom)
        with open(chemin, encoding="utf-8") as f:
            brut = f.read()
        try:
            posts.append(decouper(nom, brut))
        except Erreur as e:
            erreurs.append(str(e))
    posts.sort(key=lambda p: p["date"] or datetime.datetime.max.replace(tzinfo=TZ))
    return posts, erreurs


def decouper(nom, brut):
    """Sépare l'en-tête YAML du corps du post."""
    slug = nom[:-3]
    if not brut.startswith("---"):
        raise Erreur("%s : en-tête manquant (le fichier doit commencer par ---)" % nom)
    fin = brut.find("\n---", 3)
    if fin == -1:
        raise Erreur("%s : en-tête non refermé (il manque une ligne ---)" % nom)
    try:
        tete = yaml.safe_load(brut[3:fin]) or {}
    except yaml.YAMLError as e:
        raise Erreur("%s : en-tête illisible — %s" % (nom, e))
    if not isinstance(tete, dict):
        raise Erreur("%s : l'en-tête doit être une liste de clés" % nom)

    corps = brut[fin + 4:].lstrip("\n").rstrip()
    post = {
        "slug": slug,
        "fichier": nom,
        "texte": corps,
        "brouillon": bool(tete.get("brouillon", False)),
        "lien": tete.get("lien"),
        "cibles": tete.get("cibles") or ["facebook", "instagram"],
        "images": normaliser_images(tete),
        "date": None,
        "date_brute": tete.get("date"),
    }
    if isinstance(post["cibles"], str):
        post["cibles"] = [post["cibles"]]
    post["date"] = lire_date(nom, tete.get("date"))
    return post


def normaliser_images(tete):
    val = tete.get("images", tete.get("image"))
    if not val:
        return []
    if isinstance(val, str):
        return [val]
    return list(val)


def lire_date(nom, val):
    """Accepte « 2026-08-20 18:30 » (heure de La Réunion) ou une vraie date YAML."""
    if val is None:
        raise Erreur("%s : clé « date » manquante" % nom)
    if isinstance(val, datetime.datetime):
        d = val
    elif isinstance(val, datetime.date):
        d = datetime.datetime(val.year, val.month, val.day, 9, 0)
    else:
        texte = str(val).strip().replace("T", " ")
        for forme in ("%Y-%m-%d %H:%M", "%Y-%m-%d %H:%M:%S", "%Y-%m-%d"):
            try:
                d = datetime.datetime.strptime(texte, forme)
                break
            except ValueError:
                continue
        else:
            raise Erreur("%s : date « %s » illisible, attendu « 2026-08-20 18:30 »" % (nom, val))
    if d.tzinfo is None:
        d = d.replace(tzinfo=TZ)
    return d


# --------------------------------------------------------------------------
# Validation
# --------------------------------------------------------------------------

def valider(posts):
    """Contrôle les posts.

    Retourne (erreurs, alertes). Un brouillon est un travail en cours : ses
    problèmes sont signalés sans faire échouer la validation.
    """
    erreurs, alertes = [], []
    vus = {}
    for p in posts:
        n = p["fichier"]
        soucis = alertes if p["brouillon"] else erreurs
        for c in p["cibles"]:
            if c not in CIBLES:
                soucis.append("%s : cible « %s » inconnue (attendu : %s)" % (n, c, ", ".join(CIBLES)))
        if not p["texte"] and not p["images"]:
            soucis.append("%s : ni texte ni image, il n'y a rien à publier" % n)

        for chemin in p["images"]:
            if chemin.startswith("http://") or chemin.startswith("https://"):
                continue
            if not os.path.isfile(os.path.join(DOSSIER, chemin)):
                soucis.append("%s : image introuvable — posts/%s" % (n, chemin))

        if "instagram" in p["cibles"]:
            if not p["images"]:
                soucis.append("%s : Instagram exige au moins une image" % n)
            if len(p["images"]) > IG_CARROUSEL_MAX:
                soucis.append("%s : %d images, Instagram en accepte %d au maximum"
                              % (n, len(p["images"]), IG_CARROUSEL_MAX))
            if len(p["texte"]) > IG_LEGENDE_MAX:
                soucis.append("%s : légende de %d caractères, Instagram en accepte %d"
                              % (n, len(p["texte"]), IG_LEGENDE_MAX))
            if p["lien"]:
                soucis.append("%s : « lien » est ignoré par Instagram — mets l'URL dans le texte"
                              " ou retire instagram des cibles" % n)

        # Les brouillons ne partant pas, ils n'entrent pas en collision.
        cle = p["date"].isoformat() if p["date"] and not p["brouillon"] else None
        if cle and cle in vus:
            soucis.append("%s : même date que %s, décale l'un des deux" % (n, vus[cle]))
        if cle:
            vus[cle] = n
    return erreurs, alertes


# --------------------------------------------------------------------------
# Appels Graph API
# --------------------------------------------------------------------------

def appel(chemin, donnees=None, methode="POST", jeton=None):
    url = "%s/%s" % (BASE, chemin.lstrip("/"))
    donnees = dict(donnees or {})
    donnees["access_token"] = jeton
    if methode == "GET":
        r = requests.get(url, params=donnees, timeout=60)
    else:
        r = requests.post(url, data=donnees, timeout=120)
    try:
        rep = r.json()
    except ValueError:
        raise Erreur("réponse illisible de Meta (HTTP %s) : %s" % (r.status_code, r.text[:300]))
    if "error" in rep:
        e = rep["error"]
        raise Erreur("Meta a refusé : %s (type %s, code %s)"
                     % (e.get("message"), e.get("type"), e.get("code")))
    return rep


def url_image(chemin):
    """Chemin local → URL publique servie par GitHub Pages."""
    if chemin.startswith("http://") or chemin.startswith("https://"):
        return chemin
    return "%s/posts/%s" % (MEDIA_BASE, chemin.lstrip("/"))


# --------------------------------------------------------------------------
# Facebook
# --------------------------------------------------------------------------

def publier_facebook(post, page_id, jeton, quand=None):
    """quand = timestamp unix pour programmer, None pour publier tout de suite."""
    prog = {}
    if quand:
        prog = {"published": "false", "scheduled_publish_time": str(quand)}

    images = post["images"]
    if not images:
        d = {"message": post["texte"]}
        if post["lien"]:
            d["link"] = post["lien"]
        d.update(prog)
        return appel("%s/feed" % page_id, d, jeton=jeton)["id"]

    if len(images) == 1:
        d = {"url": url_image(images[0]), "caption": post["texte"]}
        d.update(prog)
        return appel("%s/photos" % page_id, d, jeton=jeton)["id"]

    # Plusieurs photos : on téléverse chaque image non publiée, puis on les
    # rattache à un post de fil d'actualité.
    fbids = []
    for chemin in images:
        rep = appel("%s/photos" % page_id,
                    {"url": url_image(chemin), "published": "false"}, jeton=jeton)
        fbids.append(rep["id"])
    d = {"message": post["texte"]}
    for i, fbid in enumerate(fbids):
        d["attached_media[%d]" % i] = json.dumps({"media_fbid": fbid})
    d.update(prog)
    return appel("%s/feed" % page_id, d, jeton=jeton)["id"]


# --------------------------------------------------------------------------
# Instagram
# --------------------------------------------------------------------------

def attendre_conteneur(cid, jeton, limite=120):
    """Meta télécharge l'image de son côté : il faut attendre FINISHED."""
    fin = time.time() + limite
    while time.time() < fin:
        rep = appel(cid, {"fields": "status_code,status"}, methode="GET", jeton=jeton)
        statut = rep.get("status_code")
        if statut == "FINISHED":
            return
        if statut == "ERROR":
            raise Erreur("Instagram n'a pas pu préparer le média : %s" % rep.get("status"))
        time.sleep(5)
    raise Erreur("Instagram n'a pas fini de préparer le média en %ds" % limite)


def publier_instagram(post, ig_id, jeton):
    images = post["images"]
    if not images:
        raise Erreur("%s : Instagram exige au moins une image" % post["fichier"])

    if len(images) == 1:
        rep = appel("%s/media" % ig_id,
                    {"image_url": url_image(images[0]), "caption": post["texte"]}, jeton=jeton)
        cid = rep["id"]
    else:
        enfants = []
        for chemin in images:
            r = appel("%s/media" % ig_id,
                      {"image_url": url_image(chemin), "is_carousel_item": "true"}, jeton=jeton)
            enfants.append(r["id"])
        for e in enfants:
            attendre_conteneur(e, jeton)
        rep = appel("%s/media" % ig_id,
                    {"media_type": "CAROUSEL", "children": ",".join(enfants),
                     "caption": post["texte"]}, jeton=jeton)
        cid = rep["id"]

    attendre_conteneur(cid, jeton)
    return appel("%s/media_publish" % ig_id, {"creation_id": cid}, jeton=jeton)["id"]


# --------------------------------------------------------------------------
# État
# --------------------------------------------------------------------------

def lire_etat():
    if not os.path.isfile(ETAT):
        return {}
    with open(ETAT, encoding="utf-8") as f:
        return json.load(f)


def ecrire_etat(etat):
    with open(ETAT, "w", encoding="utf-8") as f:
        json.dump(etat, f, ensure_ascii=False, indent=2, sort_keys=True)
        f.write("\n")


def noter(etat, post, cible, statut, ident):
    etat.setdefault(post["slug"], {})[cible] = {
        "statut": statut,
        "id": ident,
        "le": datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat(),
    }


# --------------------------------------------------------------------------
# Boucle principale
# --------------------------------------------------------------------------

def traiter(posts, etat, opts, jeton, page_id, ig_id):
    maintenant = datetime.datetime.now(TZ)
    agi = False

    for post in posts:
        if post["brouillon"]:
            continue
        deja = etat.get(post["slug"], {})
        ecart = post["date"] - maintenant

        for cible in post["cibles"]:
            if cible in deja:
                continue
            if ecart < -PEREMPTION and not opts.forcer:
                print("· %-42s %-9s ignoré — daté du %s, trop ancien (--forcer pour passer outre)"
                      % (post["fichier"], cible, post["date"].strftime("%d/%m/%Y %H:%M")))
                continue

            # Facebook : on confie la programmation à Meta dès qu'on a la marge.
            if cible == "facebook" and ecart > MARGE:
                quand = int(post["date"].timestamp())
                print("→ %-42s facebook  programmation chez Meta pour le %s"
                      % (post["fichier"], post["date"].strftime("%d/%m/%Y %H:%M")))
                if not opts.simulation:
                    ident = publier_facebook(post, page_id, jeton, quand=quand)
                    noter(etat, post, cible, "programme", ident)
                agi = True
                continue

            # Sinon : l'heure est passée (ou presque), on publie en direct.
            if ecart > datetime.timedelta(0):
                continue

            print("→ %-42s %-9s publication immédiate" % (post["fichier"], cible))
            if not opts.simulation:
                if cible == "facebook":
                    ident = publier_facebook(post, page_id, jeton)
                else:
                    ident = publier_instagram(post, ig_id, jeton)
                noter(etat, post, cible, "publie", ident)
            agi = True

    return agi


def main():
    ap = argparse.ArgumentParser(description="Publie les posts programmés sur Facebook et Instagram.")
    ap.add_argument("--valider", action="store_true", help="contrôle les fichiers et s'arrête")
    ap.add_argument("--simulation", action="store_true", help="affiche sans rien publier")
    ap.add_argument("--forcer", action="store_true",
                    help="publie même les posts périmés (plus de 48 h de retard)")
    opts = ap.parse_args()

    posts, erreurs = lire_posts()
    soucis, alertes = valider(posts)
    erreurs += soucis
    for a in alertes:
        print("! brouillon — %s" % a)
    if erreurs:
        print("✗ %d problème(s) :" % len(erreurs), file=sys.stderr)
        for e in erreurs:
            print("  · %s" % e, file=sys.stderr)
        return 1

    publiables = [p for p in posts if not p["brouillon"]]
    print("✓ %d post(s) valides, dont %d brouillon(s)"
          % (len(posts), len(posts) - len(publiables)))
    if opts.valider:
        return 0

    jeton = os.environ.get("META_ACCESS_TOKEN")
    page_id = os.environ.get("META_PAGE_ID")
    ig_id = os.environ.get("META_IG_USER_ID")
    if not opts.simulation:
        manquants = [n for n, v in (("META_ACCESS_TOKEN", jeton), ("META_PAGE_ID", page_id)) if not v]
        if any("instagram" in p["cibles"] for p in publiables) and not ig_id:
            manquants.append("META_IG_USER_ID")
        if manquants:
            print("✗ secret(s) manquant(s) : %s" % ", ".join(manquants), file=sys.stderr)
            return 1

    etat = lire_etat()
    try:
        agi = traiter(publiables, etat, opts, jeton, page_id, ig_id)
    except Erreur as e:
        if not opts.simulation:
            ecrire_etat(etat)  # on garde ce qui est déjà parti, pour ne pas republier
        print("✗ %s" % e, file=sys.stderr)
        return 1

    if not opts.simulation:
        ecrire_etat(etat)
    if not agi:
        print("· rien à publier pour l'instant")
    return 0


if __name__ == "__main__":
    sys.exit(main())
