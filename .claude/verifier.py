#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Les contrôles que le dépôt s'est promis d'écrire.

`NOTES-TECHNIQUES.md` annonce depuis le 17 août que « le contrôle est désormais
dans la suite de tests ». La suite n'existait pas. La voici : elle rassemble les
règles déjà payées une fois en erreur Search Console ou en bug de mise en page,
pour qu'aucune ne se reperde.

    python3 .claude/verifier.py

Sortie : une ligne par contrôle, et un code de retour non nul si l'un échoue.
Aucune dépendance, aucun accès réseau — la bibliothèque standard suffit.
"""
import json
import os
import re
import subprocess
import sys

BASE = "https://une2cvmillehistoires.re"
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

echecs = []


def pages():
    """Toutes les pages HTML publiées, chemin relatif à la racine du dépôt."""
    trouvees = sorted(f for f in os.listdir(RACINE) if f.endswith(".html"))
    dossier = os.path.join(RACINE, "histoires")
    if os.path.isdir(dossier):
        trouvees += sorted("histoires/" + f for f in os.listdir(dossier) if f.endswith(".html"))
    return trouvees


def lire(chemin):
    with open(os.path.join(RACINE, chemin), encoding="utf-8") as f:
        return f.read()


def url_de(page):
    return BASE + "/" + ("" if page == "index.html" else page[:-5])


def indexable(html):
    return 'content="noindex' not in html


def controle(nom, problemes):
    if problemes:
        echecs.append(nom)
        print(f"✗ {nom}")
        for p in problemes[:12]:
            print(f"    {p}")
        if len(problemes) > 12:
            print(f"    … et {len(problemes) - 12} autre(s)")
    else:
        print(f"✓ {nom}")


# ---------------------------------------------------------------- structure
def un_seul_h1():
    mauvais = []
    for p in pages():
        n = len(re.findall(r"<h1[\s>]", lire(p)))
        if n != 1:
            mauvais.append(f"{p} : {n} balise(s) h1")
    return mauvais


def canonical_present():
    mauvais = []
    for p in pages():
        html = lire(p)
        if not indexable(html):
            continue
        m = re.search(r'<link rel="canonical" href="([^"]+)"', html)
        if not m:
            mauvais.append(f"{p} : pas de canonical")
        elif m.group(1) != url_de(p):
            mauvais.append(f"{p} : canonical {m.group(1)} au lieu de {url_de(p)}")
    return mauvais


def liens_sans_extension():
    """GitHub Pages sert /mariage et /mariage.html. Une seule forme circule."""
    mauvais = []
    for p in pages():
        for lien in set(re.findall(r'href="(/[^"]*\.html)"', lire(p))):
            mauvais.append(f"{p} → {lien}")
    return mauvais


def liens_internes_valides():
    mauvais = []
    connues = {url_de(p).replace(BASE, "") or "/" for p in pages()}
    connues.add("/")
    for p in pages():
        for lien in set(re.findall(r'href="(/[^"#?]*)"', lire(p))):
            if re.search(r"\.[a-z0-9]{2,12}$", lien):  # fichier (image, police, manifeste)
                if not os.path.exists(os.path.join(RACINE, lien.lstrip("/"))):
                    mauvais.append(f"{p} → {lien} (fichier absent)")
            elif lien.rstrip("/") and lien not in connues:
                mauvais.append(f"{p} → {lien} (page inconnue)")
    return mauvais


# ---------------------------------------------------------------- sitemap
def sitemap_pages_indexables():
    """Une page en noindex au sitemap est une contradiction que Search Console remonte."""
    sm = lire("sitemap.xml")
    declarees = set(re.findall(r"<loc>([^<]+)</loc>", sm))
    attendues = {url_de(p) for p in pages() if indexable(lire(p))}
    mauvais = [f"au sitemap mais pas indexable ou inexistante : {u}" for u in sorted(declarees - attendues)]
    mauvais += [f"indexable mais absente du sitemap : {u}" for u in sorted(attendues - declarees)]
    return mauvais


def sitemap_lastmod_a_jour():
    """Un lastmod qui ne bouge pas quand la page change finit ignoré par Google."""
    mauvais = []
    for loc, lastmod in re.findall(r"<loc>([^<]+)</loc><lastmod>([^<]+)</lastmod>", lire("sitemap.xml")):
        chemin = loc.replace(BASE, "").strip("/")
        page = "index.html" if not chemin else chemin + ".html"
        commit = subprocess.run(["git", "log", "-1", "--format=%cs", "--", page],
                                cwd=RACINE, capture_output=True, text=True).stdout.strip()
        if commit and lastmod < commit:
            mauvais.append(f"{page} : lastmod {lastmod}, dernier commit {commit}")
    return mauvais


# ---------------------------------------------------------------- JSON-LD
def _noeuds(objet, definis, references):
    if isinstance(objet, list):
        for x in objet:
            _noeuds(x, definis, references)
    elif isinstance(objet, dict):
        identifiant = objet.get("@id")
        if identifiant and "#" in str(identifiant):
            (definis if objet.get("@type") else references).add(str(identifiant))
        for v in objet.values():
            _noeuds(v, definis, references)


def jsonld_valide_et_referme():
    """Google lit les données structurées page par page : un @id défini ailleurs
    ne vaut rien. Chaque page doit porter au moins une souche des nœuds qu'elle cite."""
    mauvais = []
    for p in pages():
        definis, references = set(), set()
        for bloc in re.findall(r'<script type="application/ld\+json">(.*?)</script>', lire(p), re.S):
            try:
                _noeuds(json.loads(bloc), definis, references)
            except json.JSONDecodeError as e:
                mauvais.append(f"{p} : JSON-LD invalide — {e}")
        for orphelin in sorted(references - definis):
            mauvais.append(f"{p} : @id cité sans définition sur la page — {orphelin}")
    return mauvais


def faq_synchrone():
    """Google veut que le balisage FAQ reflète un contenu visible, au mot près.

    Deux balisages coexistent sur le site : l'accordéon <details> de /faq, et les
    questions en <h2> suivies de leur réponse en prose sur les pages de prestation.
    Le contrôle porte donc sur le texte visible, quel que soit le contenant — et,
    quand l'accordéon existe, sur l'ordre exact des paires."""
    mauvais = []
    for p in pages():
        html = lire(p)
        balisees = []
        for bloc in re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
            try:
                donnees = json.loads(bloc)
            except json.JSONDecodeError:
                continue
            for noeud in (donnees if isinstance(donnees, list) else [donnees]):
                if isinstance(noeud, dict) and noeud.get("@type") == "FAQPage":
                    balisees = [(q["name"].strip(), q["acceptedAnswer"]["text"].strip())
                                for q in noeud["mainEntity"]]
        if not balisees:
            continue

        visible = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html))
        for question, reponse in balisees:
            if question[:45] not in visible:
                mauvais.append(f"{p} : question balisée mais invisible — « {question[:60]} »")
            elif reponse[:60] not in visible:
                mauvais.append(f"{p} : réponse balisée mais invisible — « {question[:60]} »")

        accordeon = [(re.sub(r"<[^>]+>", "", q).strip(), re.sub(r"<[^>]+>", "", r).strip())
                     for q, r in re.findall(r'<summary>(.*?)</summary><div class="rep">(.*?)</div>', html, re.S)]
        if accordeon and accordeon != balisees:
            if len(accordeon) != len(balisees):
                mauvais.append(f"{p} : {len(accordeon)} paire(s) dans l'accordéon, {len(balisees)} dans le balisage")
            else:
                for (qv, rv), (qb, rb) in zip(accordeon, balisees):
                    if qv != qb:
                        mauvais.append(f"{p} : question désynchronisée — « {qv[:60]} »")
                    elif rv != rb:
                        mauvais.append(f"{p} : réponse désynchronisée — « {qv[:60]} »")
    return mauvais


# ---------------------------------------------------------------- ressources
def images_presentes():
    mauvais = []
    for p in pages():
        html = lire(p)
        refs = re.findall(r'(?:src|href)="(/img/[^"]+)"', html)
        refs += re.findall(r'(/img/[^\s",\')]+)\s+\d+w', html)
        refs += [u.replace(BASE, "") for u in re.findall(BASE + r"(/img/[^\s\"',)]+)", html)]
        for r in set(refs):
            if not os.path.exists(os.path.join(RACINE, r.lstrip("/"))):
                mauvais.append(f"{p} → {r}")
    return mauvais


def version_des_assets():
    """Sans bump du ?v=, un visiteur récurrent garde l'ancien CSS en cache."""
    versions = set(re.findall(r"assets/(?:style\.css|site\.js)\?v=([0-9a-z]+)",
                              "".join(lire(p) for p in pages())))
    if len(versions) > 1:
        return [f"plusieurs versions en circulation : {sorted(versions)}"]
    return []


def indexnow_sans_noindex():
    chemin = ".github/workflows/indexnow.yml"
    if not os.path.exists(os.path.join(RACINE, chemin)):
        return []
    flux = lire(chemin)
    mauvais = []
    for p in pages():
        if not indexable(lire(p)) and p not in flux:
            mauvais.append(f"{p} est en noindex mais n'est pas exclue du workflow")
    return mauvais


def llms_full_a_jour():
    """« À relancer après toute modification de contenu, sinon il ment. »"""
    script = os.path.join(RACINE, ".claude", "build-llms-full.py")
    if not os.path.exists(script):
        return []
    avant = lire("llms-full.txt")
    subprocess.run([sys.executable, script], cwd=RACINE, capture_output=True)
    apres = lire("llms-full.txt")
    # la ligne de date change à chaque exécution : on compare le reste
    normalise = lambda t: re.sub(r"\d{1,2} \w+ 2\d{3}", "", t)
    if normalise(avant) != normalise(apres):
        return ["llms-full.txt n'était pas à jour — il vient d'être régénéré, pensez à le commiter"]
    return []


CONTROLES = [
    ("Un seul <h1> par page", un_seul_h1),
    ("Canonical présent et exact sur les pages indexables", canonical_present),
    ("Aucun lien interne en .html", liens_sans_extension),
    ("Tous les liens internes mènent quelque part", liens_internes_valides),
    ("Le sitemap ne liste que des pages indexables, et les liste toutes", sitemap_pages_indexables),
    ("Les lastmod du sitemap ne sont pas antérieurs au dernier commit", sitemap_lastmod_a_jour),
    ("JSON-LD valide, et aucun @id cité sans définition sur la page", jsonld_valide_et_referme),
    ("FAQ visible et FAQPage synchrones", faq_synchrone),
    ("Toutes les images référencées existent", images_presentes),
    ("Une seule version d'assets en circulation", version_des_assets),
    ("IndexNow ne soumet aucune page en noindex", indexnow_sans_noindex),
    ("llms-full.txt reflète les pages", llms_full_a_jour),
]

if __name__ == "__main__":
    for nom, fonction in CONTROLES:
        controle(nom, fonction())
    print()
    if echecs:
        print(f"{len(echecs)} contrôle(s) en échec : " + ", ".join(echecs))
        sys.exit(1)
    print(f"Les {len(CONTROLES)} contrôles passent.")
