# Rapport Bing du 7 août 2026 — décryptage et plan

Le scan « 1ère analyse YD » a remonté 6 types de problèmes. Voici ce que chacun veut dire, sa gravité réelle, et qui le traite.

| Problème Bing | Gravité Bing | Gravité réelle | Nombre | Qui traite |
|---|---|---|---|---|
| Balise de description meta manquante | 🔴 Erreur | 🔴 réel | 8 pages | moi, **après le snippet n°3** |
| Erreurs HTTP 400-499 | 🔴 Erreur | 🟠 à voir | 2 pages | toi (2 min) |
| Attribut alternatif d'image manquant | 🟠 Avertissement | 🟠 réel mais surévalué | 30 pages | moi + toi |
| Titre trop long | 🟠 Avertissement | 🟡 mineur | 23 pages | moi, **après le snippet n°3** |
| Plusieurs balises meta description | 🔵 Info | 🟡 mineur | 4 pages | **snippet n°4** |
| Plusieurs balises h1 | 🔵 Info | 🟠 réel | 3 pages | toi, dans Elementor (tuto 11) |

**Ce que Bing ne voit pas et qui compte plus que tout ça :** aucun contenu ne cible « yoga prénatal » (2 900 recherches/mois), et la page Programme Yoga Maternité n'a pas de schema `Course`. Ces deux points-là sont en cours de traitement et pèsent bien plus lourd que les six lignes du rapport.

---

## 1. 🔴 Descriptions meta manquantes — 8 pages

**Ce que ça veut dire :** huit pages n'ont aucun petit paragraphe de résumé à afficher sous le lien bleu dans les résultats de recherche. Google et Bing en fabriquent alors un tout seuls, en piochant une phrase au hasard dans la page. Le résultat est souvent mauvais et fait perdre des clics.

**Pourquoi les articles ne sont pas concernés :** sur les articles, quand le champ Rank Math est vide, Rank Math reprend automatiquement l'extrait. Les pages, elles, n'ont pas d'extrait — donc rien.

**Je peux les corriger moi-même, mais seulement si le snippet n°3 est installé.** C'est ce qui change la donne : je pensais ce snippet devenu inutile, le rapport Bing lui redonne tout son intérêt. Avec lui, je remplis les 8 descriptions manquantes et les 23 titres trop longs en quelques minutes. Sans lui, c'est 31 copier-collers à la main.

**→ Installe le snippet n°3 et dis-le-moi.**

## 2. 🔴 Erreurs HTTP 400-499 — 2 pages

**Ce que ça veut dire :** deux adresses renvoient une page d'erreur, presque toujours une 404 (« page non trouvée »). Soit un lien pointe vers une page supprimée, soit une ancienne adresse traîne quelque part.

**Ce qu'il faut faire — 2 minutes :**
1. Dans Bing Webmaster, clique sur la ligne « Erreurs HTTP 400-499 » : il te donne les deux adresses exactes.
2. Envoie-les-moi, ou traite-les directement : WordPress → **Redirection** (le plugin est installé) → **Ajouter une redirection** → adresse cassée en source, bonne adresse en destination, type 301.

Attention à un faux positif possible : le fichier `/llms.txt` renverra une 404 tant que le snippet n°1 n'est pas installé — mais Bing ne peut pas encore le connaître.

## 3. 🟠 Images sans texte alternatif — 30 pages

**Ce que ça veut dire :** le « texte alternatif » (ou *alt*) est la phrase qui décrit une image. Elle sert à deux choses : les personnes aveugles l'entendent lue par leur lecteur d'écran, et les moteurs de recherche s'en servent pour comprendre l'image (c'est ce qui fait ressortir dans Google Images).

**Deux nuances importantes :**

- **Toutes les images ne doivent pas avoir un alt.** Une image purement décorative — un séparateur, un motif de fond — doit avoir un alt **vide**. C'est la bonne pratique d'accessibilité, et Bing la compte quand même comme un problème. Le séparateur `separateur-uoga-doula.jpg`, présent sur beaucoup de pages, est dans ce cas : il ne faut **pas** le corriger.
- **Un mauvais alt est pire que pas d'alt.** Décrire une image qu'on n'a pas vue, c'est mentir à une personne aveugle.

**Ce que j'ai fait :** j'ai corrigé les 5 images dont le contenu était certain d'après leur nom et leur usage :

| ID | Image | Alt ajouté |
|---|---|---|
| 11513, 11515, 11516 | EARLY BIRD offre limitée | *Tarif Early Bird — offre limitée sur la formation de doula de l'École Yoga Doula* |
| 11483 | Photo d'équipe (Orsolya Elek) | *L'équipe des formatrices de l'École Yoga Doula* |
| 10093 | Atelier yoga | *Atelier de yoga périnatal organisé par l'École Yoga Doula* |

**Ce que je ne peux pas faire :** il reste une douzaine d'images sans alt dont je ne peux pas deviner le contenu — elles s'appellent « Design sans titre(16) », « Photos Site YD(5) », « 1.jpg », « WhatsApp Image 2025-07-08 »… Je ne vois pas les images, je ne vais pas inventer.

**Deux options :**
- **Tu me dis ce qu'elles montrent** (une phrase par image suffit) et je remplis tout d'un coup.
- **Tu le fais directement :** WordPress → Médias → clique sur une image → champ **Texte alternatif** dans la colonne de droite. Décris ce qu'on voit, simplement, en une phrase. Si un mot-clé s'y glisse naturellement (« yoga prénatal », « doula »), tant mieux — mais la description passe avant.

Les IDs concernés : 12116, 11929, 11850, 11284, 11283, 11475, 11474, 10949, 10948, 10655.
*(11834 et 11296 sont des fichiers techniques d'Elementor, invisibles pour les visiteurs — à ignorer.)*

## 4. 🟡 Titres trop longs — 23 pages

**Ce que ça veut dire :** le titre affiché dans les résultats de recherche est coupé au-delà d'environ 60 caractères. Ça ne pénalise pas le classement, mais un titre tronqué en plein milieu donne moins envie de cliquer.

**Les 10 articles de blog sont déjà réglés** — j'ai réécrit leurs titres cet après-midi aux bonnes longueurs. Restent les pages.

**Là encore, le snippet n°3 me permet de tout faire moi-même**, et avec un avantage : le titre SEO peut alors être différent du titre affiché sur la page. On garde donc « Deviens DOULA » à l'écran et on met « Formation de doula 261 h — École Yoga Doula » dans Google. Le beurre et l'argent du beurre.

## 5. 🟡 Plusieurs meta descriptions — 4 pages

Déjà diagnostiqué de mon côté avant le rapport : les articles envoient deux descriptions au lieu d'une, la seconde étant injectée par le thème. Google lit la première et ignore la seconde, l'impact est faible.
**→ snippet n°4.** C'est le plus invasif des quatre : si tu n'en installes que trois, laisse celui-là de côté.

## 6. 🟠 Plusieurs balises H1 — 3 pages

Bing le classe en simple information ; je le classe plus haut. Neuf H1 sur la page d'accueil et huit sur la page Formation, ce n'est pas une pénalité, mais c'est un signal fort gaspillé — et sur la page Formation, le H1 actuel ne contient même pas le mot « formation », alors que la page se bat sur « formation doula » (1 828 affichages par an, position 21).

**→ C'est le seul point qui demande vraiment Elementor.** Tuto complet, avec la liste exacte des titres à basculer : `11-tuto-h1.md`.

---

## L'ordre que je te recommande

1. **Importer les 4 snippets** (fichier `12-import-code-snippets.json`) — 5 minutes, et ça débloque deux lignes du rapport.
2. **Me dire quand c'est fait** → je remplis les 8 descriptions manquantes et les 23 titres trop longs.
3. **Récupérer les 2 URLs en erreur** dans Bing et me les envoyer.
4. **Les H1 dans Elementor** quand tu as trois quarts d'heure.
5. **Les alt d'images** — soit tu me décris les 10 images, soit tu les remplis toi-même au fil de l'eau.

Une fois les quatre premières faites, il ne restera plus, dans ce rapport, que des lignes marginales.
