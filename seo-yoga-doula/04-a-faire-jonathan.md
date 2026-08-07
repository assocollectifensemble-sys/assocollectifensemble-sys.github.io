# Ce que je ne peux pas faire — à toi de jouer

Rangé par rentabilité. Le n°1 vaut plus que tous les autres réunis.

---

## 1. 🔴 Bing Webmaster Tools — 15 min — **c'est LE truc**

ChatGPT s'appuie sur l'index de Bing. Aujourd'hui le site n'y est pas déclaré : quoi qu'on écrive, il ne peut pas apparaître dans les réponses de ChatGPT.

1. Va sur <https://www.bing.com/webmasters>
2. Connecte-toi et clique **« Importer depuis Google Search Console »** — c'est le chemin le plus rapide, ça récupère tout automatiquement.
3. Vérifie ensuite que le sitemap `https://yoga-doula.eu/sitemap_index.xml` apparaît bien dans l'onglet **Sitemaps**. Si non, ajoute-le à la main.

C'est gratuit, ça prend un quart d'heure, et presque personne ne le fait.
Compte 6 à 12 semaines avant que ça produise un effet — d'où l'urgence.

---

## 2. 🟠 Le snippet Rank Math — 10 min — débloque toute l'automatisation

Le plugin **Code Snippets** est déjà installé et actif sur le site (pas besoin de WPCode).

1. **D'abord : vérifie ta sauvegarde UpdraftPlus.** WordPress → UpdraftPlus → l'onglet doit montrer une sauvegarde récente. Si elle date, lance-en une.
2. WordPress → **Code Snippets** → **Ajouter**.
3. Titre : `Rank Math REST — titres SEO et métas`
4. Colle le contenu du fichier `01-snippet-rank-math-rest.php` **sans la première ligne `<?php`**.
5. Coche **« Run snippet everywhere »**.
6. **Enregistrer et activer**.
7. Dis-le-moi : je teste tout de suite sur l'article 12052 (un brouillon de test, zéro risque) et je te confirme que ça marche.

**Si ça casse quelque chose :** Code Snippets → décoche le snippet → tout revient à l'état d'avant. Instantané.

**Ce que ça change :** sans lui, tu copies-colles 3 champs à la main sur chacun des 10 articles = 30 copier-collers. Avec lui, je les écris tous en 2 minutes.

---

## 3. 🟠 Dans Elementor — 30-45 min — voir le fichier `03`

Deux choses, sur des pages **publiées** (donc je n'y touche pas sans ton accord) :

- **Les 4 schemas FAQ concurrents** sur la page Programme Yoga Maternité → n'en garder qu'un. C'est le défaut technique le plus coûteux du site en ce moment.
- **Les H1 multiples** : 9 sur l'accueil, 8 sur la page Formation Yoga Doula. À passer en H2 sauf un.

Détails et mode d'emploi : `03-schema-course-pym.md`.
Si tu préfères confier ça à Fabien, c'est exactement son périmètre — c'est une demi-heure de son temps.

---

## 4. 🟠 Faire relire les 10 articles par Gurujagat

Ils sont tous **en brouillon**, signés à son nom, prêts à publier. Rien ne part en ligne sans elle.

Trois choses à lui demander :

- **Valider le fond** — surtout les articles santé (yoga prénatal, yoga postnatal) et les fourchettes de tarifs de l'article « Combien gagne une doula ».
- **Remplir les blocs `[GJK]`.** J'ai laissé 3 emplacements marqués en italique dans les articles yoga, à des endroits où son vécu réel ferait la différence. C'est ce qui distingue un article de l'École d'un article générique — et pour Google, en santé, c'est décisif. Deux à cinq phrases suffisent à chaque fois.
- **Confirmer les chiffres :** j'ai retiré la mention « plus de 500 personnes formées » (invérifiable) et corrigé « 275 heures » en **261 heures**, ainsi que « prochaine session janvier 2027 » en **session 2027-2028**. Si les vrais chiffres sont différents, dis-le-moi et je corrige partout d'un coup.

**Cadence de publication recommandée : 2 à 3 articles par jour, pas les 10 d'un coup.** En santé, une rafale de contenu d'un coup ressemble à du contenu de masse et peut être pénalisée.

⚠️ **Ordre important :** les articles se lient entre eux. Publie d'abord **12051 (Comment devenir doula)** et **12200 (Yoga prénatal)** — ce sont les deux piliers vers lesquels les autres pointent.

---

## 5. ⚪ Deux questions auxquelles j'ai besoin d'une réponse

1. **Les autres conversations sont-elles fermées ?** Si une autre écrit encore sur WordPress, on va créer des doublons. J'ai déjà trouvé 5 brouillons dont le brief ne parlait pas.
2. **Les 3 articles publiés (5751, 9450, 10032) sont classés dans « Uncategorized ».** J'aimerais les reclasser dans « Devenir doula » / « Yoga périnatal ». Ce sont des contenus publiés : je ne le fais que si tu me le dis.

---

## 6. ⚪ Après la mi-août (pas urgent, mais à ne pas oublier)

- **Page Auteur Gurujagat + schema `Person`** — sa bio est aujourd'hui enterrée dans un accordéon de « Qui sommes-nous ». C'est le plus gros actif E-E-A-T du site, et il est invisible.
- **Corriger « plus de 15 ans »** sur la page Formation Yoga Doula (c'est faux : 19 ans d'école, 46 ans de pratique).
- **La frise de « Qui sommes-nous » s'arrête à automne 2022.** On est en 2026.
- **Backlinks** : demander un lien retour à chaque yoga-doula formée. Quentin le désignait comme le levier le plus puissant dès 2023 — jamais actionné.
- **Baseline GEO** : une fois par mois, poser les mêmes questions à ChatGPT et Perplexity (« quelle formation pour devenir doula en France ? », « meilleure formation yoga prénatal ») et noter si l'École apparaît, et face à qui.
