# Site vitrine de l'agence

> Agent web — 2026-08-23. Statique portable : HTML/CSS/JS sans dépendance serveur,
> sans build, sans framework. Déployable tel quel sur GitHub Pages ou n'importe
> quel hébergeur.

## Contenu

| Fichier | Rôle |
|---|---|
| `index.html` | Accueil : promesse, cycle 4 temps, références, aperçu des offres, CTA diagnostic |
| `offres.html` | Les 5 packs + les 3 niveaux d'abonnement, prix affichés, passerelles pack→abonnement |
| `facture-electronique.html` | Coin d'entrée : échéance 01/09/2026, la loi sans jargon, offre Solo/Équipe, FAQ |
| `contact.html` | Coordonnées (placeholders) + formulaire **mailto** (aucun backend) |
| `mentions-legales.html` | Squelette à compléter avant mise en ligne (`noindex` tant que ce n'est pas fait) |
| `assets/tokens.css` | **Copie** de `agence/design/tokens.css` (source de vérité : `agence/design/`) |
| `assets/site.css` | Styles du site, construits sur les tokens |
| `assets/site.js` | Année du footer, compte à rebours J−N, composition du mailto. Optionnel : tout fonctionne sans JS |

Aucune donnée client inventée : les références (École Yoga Doula, Croc Parc) ne
citent que les prestations réalisées, sans chiffres. Les chiffres viendront de Jon.

## Ce qui attend Jon avant mise en ligne

Chercher `À COMPLÉTER PAR JON` dans les fichiers :

```bash
grep -rn "À COMPLÉTER PAR JON" agence/site/
```

1. **Coordonnées** : téléphone/WhatsApp, email — pied de page des 5 pages,
   `contact.html` (y compris l'attribut `data-mailto` du formulaire et les liens
   `tel:`/`wa.me` en commentaire HTML prêts à activer), JSON-LD de `index.html`
   et `contact.html`.
2. **Nom de marque définitif** (décision ouverte — voir ci-dessous).
3. **Mentions légales** : SIREN, adresse, statut, TVA, hébergeur, médiation.
   Retirer alors la balise `<meta name="robots" content="noindex">`.
4. **URL définitive** du site dans les JSON-LD (`"url"`).

## Changer le nom de marque

Le site est construit avec l'identité recommandée **« Otonom Digital »**
(baseline « Installé. Formé. Otonom. »). Le nom définitif est une décision
ouverte de Jon (`agence/cerveau/decisions.md`).

Le nom est écrit en dur dans le HTML (nécessaire pour le SEO : titres, metas,
JSON-LD). Pour changer, un rechercher-remplacer suffit — trois chaînes :

```bash
cd agence/site
# 1. Le nom complet (titres, metas, JSON-LD, footer)
grep -rl "Otonom Digital" . | xargs sed -i 's/Otonom Digital/NOUVEAU NOM/g'
# 2. L'usage court (logo texte du header : « Otonom » + suffixe « Digital »)
grep -rn 'class="brand"' *.html   # ajuster à la main le contenu de <a class="brand">
# 3. La baseline si elle change (elle joue sur le mot « Otonom »)
grep -rn "Installé. Formé. Otonom." . 
```

Vérification finale : `grep -rni "otonom" agence/site/` ne doit plus rien
retourner (hors ce README). Penser aussi aux commentaires d'en-tête de
`assets/site.css` et `assets/site.js`.

## Modifier le site

- **Textes et prix** : directement dans les `.html`. Les prix viennent de
  `agence/offre/` (les fiches font foi) — toute modification de prix se fait
  d'abord là-bas, puis ici.
- **Couleurs, typos, espacements** : ne jamais modifier `assets/site.css` en
  contradiction avec l'identité. La source de vérité est
  `agence/design/identite.md` + `agence/design/tokens.css` ; après une évolution
  des tokens, resynchroniser la copie :
  `cp agence/design/tokens.css agence/site/assets/tokens.css`
- **Navigation** : le header/footer est dupliqué dans chaque page (choix assumé :
  zéro build). Une modification de nav = 5 fichiers. Marquer la page courante
  avec `aria-current="page"`.
- **Mode sombre** : automatique (`prefers-color-scheme`), forçable en posant
  `data-theme="dark"` ou `"light"` sur `<html>`.
- **Date de l'échéance** : le compte à rebours lit `data-deadline="2026-09-01"`
  dans `facture-electronique.html` ; après le 01/09/2026 il affiche
  « Obligation en vigueur » tout seul.

## Tester en local

Ouvrir `index.html` dans un navigateur suffit (aucun serveur requis).
Ou : `python3 -m http.server -d agence/site 8000` → http://localhost:8000

## Déployer sur un dépôt GitHub Pages dédié

L'hébergement définitif est une décision ouverte (recommandation : dépôt dédié
+ domaine `.re`/`.fr`). Le site est prêt tel quel :

1. Créer un dépôt GitHub (ex. `otonom-digital/otonom-digital.github.io`, ou
   n'importe quel nom + Pages activé).
2. Copier **le contenu** de `agence/site/` à la **racine** du nouveau dépôt
   (les chemins sont tous relatifs, aucun ajustement nécessaire) :
   ```bash
   cp -r agence/site/. ../nouveau-depot/
   ```
3. Dans le nouveau dépôt : Settings → Pages → Source : branche `main`, dossier `/`.
4. Domaine personnalisé (recommandé) : Settings → Pages → Custom domain →
   renseigner le domaine (ex. `otonom.re`) ; créer chez le registrar un
   enregistrement `CNAME` vers `<compte>.github.io` (ou les 4 A records GitHub
   Pages pour l'apex) ; cocher « Enforce HTTPS ».
5. Après mise en ligne : compléter les mentions légales, retirer le `noindex`,
   renseigner l'URL dans les JSON-LD, puis ajouter un `sitemap.xml` et un
   `robots.txt` (volontairement absents tant que l'URL définitive n'est pas connue).

Le site fonctionne aussi sur n'importe quel hébergeur statique (Netlify, OVH,
o2switch…) : téléverser le contenu du dossier, rien d'autre.
