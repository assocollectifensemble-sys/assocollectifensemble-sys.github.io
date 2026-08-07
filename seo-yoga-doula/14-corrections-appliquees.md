# Corrections appliquées après activation des snippets — 7 août 2026

## ✅ Les 4 snippets fonctionnent

| Snippet | Vérification | Résultat |
|---|---|---|
| 1 — llms.txt | `yoga-doula.eu/llms.txt` | ✅ HTTP 200, `text/plain`, contenu complet |
| 2 — Schema Course | code source de la page PYM | ✅ `Course` détecté |
| 3 — Rank Math REST | écriture test sur l'article 12052 | ✅ les 3 champs s'écrivent, `ignored_keys` vide |
| 4 — Meta description unique | à revérifier après purge du cache | ⏳ |

*(L'article de test 12052 porte un titre SEO « TEST — écriture API Rank Math ». C'est un brouillon, aucune importance, mais autant le supprimer.)*

---

## 🐛 Deux vraies erreurs trouvées et corrigées

Les deux pages **Dijon**, créées en octobre 2025, ont été dupliquées depuis d'autres villes sans que le bloc SEO soit mis à jour. Le contenu visible parlait bien de Dijon, mais tout ce que Google lit annonçait une autre ville.

| Page | Ce qu'il y avait | Corrigé en |
|---|---|---|
| **11871** Cours de yoga Dijon | titre : *« …postnatal **Bordeaux**… »*<br>description : *« …à **Bordeaux** et alentours »*<br>mot-clé : `doula bordeaux` | titre : *« Cours de yoga prénatal & postnatal à Dijon \| École Yoga Doula »*<br>description : *« …à Dijon et alentours »*<br>mot-clé : `yoga prénatal dijon` |
| **11855** Doula Dijon | titre : *« Trouver une Doula diplômée à **Annecy** »*<br>description : *« …à **Annecy** et alentours »*<br>mot-clé : `doula annecy` | titre : *« Trouver une doula à Dijon \| École Yoga Doula »*<br>description : *« …à Dijon et alentours »*<br>mot-clé : `doula dijon` |

Ces deux pages étaient donc invisibles sur « doula Dijon » et « yoga prénatal Dijon », tout en concurrençant Bordeaux et Annecy sur leurs propres mots-clés.

---

## ✅ Les 9 descriptions manquantes — écrites

Bing en signalait 8, j'en ai trouvé 9.

| ID | Page | Description écrite |
|---|---|---|
| 10431 | Évènements de l'École | Stages, ateliers et rencontres de l'École Yoga Doula… |
| 3049 | Galerie | En images : les formations, les stages et les rencontres… |
| 3687 | Module Métamorphose | Le massage métamorphique : module de formation… |
| 12083 | Feuille de route PYM | Calendrier, étapes et informations pratiques… |
| 12139 | Paiement enregistré | Confirmation de paiement — votre règlement a bien été enregistré. |
| 12070 | Renoncer au contrat | Modalités de renonciation : délai légal, procédure… |
| 12081 | Formulaire inscription PYM | Réservé aux personnes ayant validé leur pré-inscription. |
| 12144 | CGV | Inscription, tarifs, paiement, annulation, rétractation. |
| 12147 | Mentions légales | Éditeur, hébergement, propriété intellectuelle, données. |

**Note :** cinq de ces pages (12083, 12139, 12070, 12081, et le formulaire) sont des pages transactionnelles qui n'ont rien à faire dans Google. Le vrai réglage serait de les passer en **noindex** plutôt que de leur écrire une description. Ça se fait en 30 secondes par page : ouvrir la page → onglet Rank Math → **Avancé** → *Index* → choisir **noindex**. À faire quand tu auras cinq minutes ; en attendant, la description évite l'erreur Bing.

---

## ✅ Textes alternatifs — 5 images

11513, 11515, 11516 (visuels Early Bird) · 11483 (photo d'équipe) · 10093 (atelier yoga).

Restent une dizaine d'images dont je ne peux pas deviner le contenu : **12116, 11929, 11850, 11284, 11283, 11475, 11474, 10949, 10948, 10655**. Décris-les-moi en une phrase chacune et je remplis, ou fais-le dans Médias.

---

## ⚠️ Découvert au passage : la date « janvier 2027 » est aussi dans les pages

Le bloc d'appel à l'action en bas des pages d'annuaire (au moins la page Doula Dijon, probablement les 26 pages de villes) contient :

> « Depuis 2007, l'École Yoga Doula forme à l'accompagnement périnatal… **Prochaine session : janvier 2027.** »

C'est la même erreur que celle corrigée dans les articles. La bonne mention est **session 2027-2028**.

Ce texte est stocké dans les données Elementor, que l'API ne peut pas modifier. Deux options :

1. **Plugin « Better Search Replace »** (gratuit, officiel) : installer → Outils → Better Search Replace → chercher `Prochaine session : janvier 2027` → remplacer par `Prochaine session : 2027-2028` → **cocher d'abord « Simulation »** pour voir combien d'occurrences avant de lancer pour de vrai. Sauvegarde UpdraftPlus d'abord.
2. Le faire à la main dans Elementor sur chaque page — long.

*(À vérifier aussi : le CTA de la page Cours de yoga Dijon annonce « Prochaine session : 1er octobre 2026 » pour le PYM — celui-là est correct.)*

---

## ⏳ Ce qui reste : les 23 titres trop longs

Je peux les écrire, mais chaque écriture sur une page Elementor me renvoie tout le code de la page en réponse, ce qui sature très vite. **À reprendre dans une nouvelle conversation** — l'accès technique est en place, ça prendra dix minutes.

Voici les titres que je propose, prêts à coller si tu préfères le faire toi-même (Rank Math → Modifier l'extrait → Titre SEO) :

| Page | Titre actuel | Longueur | Titre proposé | Longueur |
|---|---|---|---|---|
| Accueil (10904) | Devenez Doula & Enseignante de Yoga Périnatal avec les formations de Doula de l'École Yoga Doula Officielle | **107** | `École Yoga Doula — Devenir doula & prof de yoga périnatal` | 57 |
| PYM (7018) | Programme Yoga Maternité – Formation yoga prénatal & postnatal \| Yoga Doula | **75** | `Formation yoga prénatal & postnatal — 84 h \| Yoga Doula` | 55 |
| Formation YD (6468) | Formation Yoga Doula & Yoga Périnatal - Devenez Doula et enseignante périnatale | **79** | `Formation de doula 261 h — Devenir doula \| École Yoga Doula` | 59 |
| Contact (937) | Contactez l'école Yoga Doula - Formations Doula, Yoga maternité | 62 | `Contact — École Yoga Doula` | 26 |
| Pages « Cours de yoga [Ville] » | Cours de yoga prénatal & postnatal [Ville], trouver une enseignante \| École Yoga Doula | **~85** | `Cours de yoga prénatal à [Ville] \| École Yoga Doula` | ~52 |
| Pages « Doula [Ville] » | variable | — | `Trouver une doula à [Ville] \| École Yoga Doula` | ~46 |

Le gain sur les titres est réel mais modeste — c'est du confort de clic, pas du classement. **Le schema `Course` et les H1 pèsent bien plus lourd.**

---

## L'ordre pour la suite

1. **Les H1 dans Elementor** — tuto `11`. C'est ce qui reste de plus rentable, et seul toi peux le faire.
2. **Les 2 URLs en erreur 400-499** : clique sur la ligne dans Bing, envoie-les-moi.
3. **La date « janvier 2027 »** dans les pages de villes (Better Search Replace).
4. **Le noindex** sur les 5 pages transactionnelles.
5. **Les titres trop longs** — dans une nouvelle conversation.
6. **Les 10 alt d'images** — dès que tu me dis ce qu'elles montrent.
