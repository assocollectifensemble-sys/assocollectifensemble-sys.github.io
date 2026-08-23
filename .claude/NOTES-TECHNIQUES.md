# Arbitrages techniques

Ce que l'on a regardé et volontairement laissé en l'état, pour ne pas y revenir à chaque
passe d'optimisation. Ce fichier vit dans `.claude/` : il s'adresse à qui travaille sur le
site, pas aux visiteurs.

## Laissé tel quel, et pourquoi

**La musique (`assets/musique.mp3`, 2 Mo).** Déjà en `preload="none"` : rien n'est
téléchargé tant que le visiteur ne clique pas. Aucun gain de chargement à espérer.
Ré-encoder en 96 kbps mono la ferait tomber sous 700 Ko, mais c'est un arbitrage de
qualité sonore, pas une optimisation gratuite.

**CSS et JS non minifiés** (environ 590 et 153 lignes). Le gain serait de l'ordre de 5 Ko
une fois la compression du serveur appliquée, contre une perte nette de lisibilité. Le
rapport n'est pas favorable sur un site de cette taille.

**`grand1.jpg` et `grand2.jpg`** (380 et 402 Ko) ne gagnent que 10 à 13 % en WebP : elles
sont déjà très compressées à la source, et descendre plus bas dégraderait visiblement le
grain. Elles restent les deux fichiers les plus lourds du site.

**Pas de palier 320px.** Aucune image n'est surdimensionnée à 1440 px ni à 390 px — sauf
le logo, ce que ce paragraphe a longtemps manqué : voir « La passe du 23 août 2026 ». Le seul
palier manquant serait un 320 px pour les portraits ronds de 158 px, qui économiserait
quelques dizaines de kilo-octets sur desktop uniquement.

**Le dépôt pèse une quarantaine de mégaoctets** (`.git` compris, avec les variantes
d'images générées). Ça n'a aucun effet sur le visiteur, qui télécharge autour de 130 Ko sur
une page comme `/tarifs`. Le seul coût est un clone un peu plus long.

## Ce qui était déjà en place avant la passe d'août 2026

Utile à savoir avant de « corriger » quelque chose qui va bien : les balises `<img>` ont
toutes `width`, `height` et `alt` renseignés (aucun décalage de mise en page), les polices
sont auto-hébergées et préchargées, `prefers-reduced-motion` est respecté, le JSON-LD est
complet, et le détecteur d'Impeccable ne remonte aucun anti-pattern de design sur les
14 pages.

## Photos du récit d'Emma et Fabien

Les images de la galerie sont des captures du film de la journée : elles portent toutes le
filigrane Instagram du compte, et souvent un texte incrusté en bas. `object-fit: cover` sur
260 px de haut recadre l'essentiel de ce texte. `02-fleurs-capot.jpg` a été détourée de sa
bande noire (le cadre utile va de y=388 à y=1044 dans l'original), ce qui a fait tomber
au passage l'incrustation. `06-preparatifs.jpg` a été supprimée : la vignette ne montrait
que de la végétation, aucun sujet.

## Deux pièges du 12 août 2026, à ne pas reproduire

**`:nth-child` ne traverse pas `<picture>`.** Le diaporama du hero n'a jamais défilé : ses
délais visaient `.dp:nth-child(2..5)`, alors que chaque image est enveloppée dans son propre
`<picture>` et y est toujours le 2ᵉ enfant, après le `<source>`. Résultat, `:nth-child(2)`
attrapait les cinq images et les autres règles ne visaient rien — les cinq photos jouaient
l'animation en même temps, on n'en voyait qu'une. Les délais portent désormais sur les
`picture:nth-of-type()`. Dès qu'on emballe une image dans un `<picture>`, tout sélecteur
positionnel écrit pour l'`<img>` est à revoir.

**Une transition « toutes propriétés » anime aussi `backdrop-filter`.** Le menu mobile se
repliait dans la barre dès que la page était défilée : `nav.menu-ouvert{backdrop-filter:none
!important}` fixait bien la valeur, mais `nav{transition:.4s}` l'interpolait pendant 400 ms,
et un élément qui porte un flou reste bloc conteneur pour ses descendants `position:fixed`.
La transition nomme maintenant ses propriétés. Ce bug avait déjà été corrigé une fois sous
une autre forme : il revient tant qu'on écrit `transition:<durée>` toute seule.

**Un `<a>` ne peut pas en contenir un autre.** Les cartes de l'accueil sont des liens ; y
insérer un lien dans la description faisait éclater la grille (le navigateur ferme la carte
avant le lien imbriqué). Vérification rapide : `document.querySelectorAll('a a').length`
doit valoir 0 sur chaque page.

## Ce que la contre-expertise du 12 août a rattrapé

Trois régressions introduites par mes propres correctifs, trouvées par un agent mandaté pour
me contredire. À relire avant de « nettoyer » quoi que ce soit dans ce fichier.

**Le `background-image` du hero avait deux rôles, pas un.** Je l'avais supprimé comme doublon
du diaporama. Il bouchait aussi le trou sous les fondus — deux photos à demi opaques laissent
passer le fond 21 % du temps — et surtout il était la seule image visible sous
`prefers-reduced-motion`, où le hero devenait un aplat brun. Un fond CSS léger l'a remplacé.

**`prefers-reduced-motion` sans `animation-iteration-count:1`** ne fait qu'accélérer les
animations infinies : elles tournent à ~100 000 itérations par seconde au lieu de s'arrêter.
C'est ce qui vidait le diaporama de ses images.

**Un « filet de sécurité » doit s'écrire avec `:where()`.** `main a:not([class])` a une
spécificité de (0,1,2) et passait devant `.balade a` (0,1,1) : 22 liens de cartes se
retrouvaient soulignés deux fois. `main :where(a:not([class]))` tombe à (0,0,0) et ne rattrape
que ce qui n'est habillé par personne.

Et deux leçons de méthode :

- **Un test qui échoue n'est pas toujours un défaut.** Trois de mes contrôles mesuraient
  pendant une transition (`.reveal` à l'impression), pendant un défilement fluide (la bulle),
  ou avant la fin d'un `scroll-behavior:smooth` (les ancres). Mesurer l'état stable, pas
  l'état transitoire.
- **Une correction non écrite n'existe pas.** Un script Python a levé une exception avant son
  `open(..., "w")` : les trois premiers remplacements avaient l'air appliqués — ils étaient
  affichés — mais rien n'avait touché le disque. Vérifier le fichier, pas la sortie du script.

## Le sitemap ne doit lister que des pages indexables (17 août 2026)

Google a envoyé « Exclue par la balise noindex » : `mentions-legales.html` porte un
`noindex` volontaire, et elle avait été ajoutée au sitemap. Demander l'indexation d'une
page qui l'interdit est une contradiction que Search Console remonte comme une erreur.

Trois pages portent un `noindex` — `mentions-legales`, `merci`, `404` — et aucune ne doit
figurer dans `sitemap.xml`. Le contrôle est désormais dans la suite de tests.

À ne pas confondre avec l'autre état, visible sur les pages du sitemap : **« Discovered –
currently not indexed », dernier crawl vide**. Là, rien n'est cassé : Google connaît l'URL
par le sitemap mais ne l'a jamais explorée. C'est une question de budget d'exploration, et
il se gagne avec des liens entrants, pas avec du balisage.

## La passe du 23 août 2026

**Un groupe robots.txt qui nommait des robots annulait les Disallow du groupe `*`.**
La spécification est sans détour : un robot qui trouve un groupe le nommant ignore
entièrement le groupe `*`. Nos quatre `Disallow` ne vivaient que dans ce dernier ; les
vingt-deux robots nommés plus bas — Bingbot compris — étaient donc explicitement
autorisés à explorer `/.claude/` et `/DESIGN.md`. Vérifié en production avant correction :
Bingbot était ALLOWED sur `/.claude/VISIBILITE-IA.md`, qui répondait 200. Les quatre
lignes sont maintenant répétées dans le second groupe. **Toute nouvelle règle d'exclusion
doit être écrite dans les deux groupes.** Et un `Disallow` reste une consigne
d'exploration, pas une protection : si ces notes doivent devenir privées, il faudra les
sortir du dépôt publié.

**Un `@id` ne traverse pas les pages.** Onze pages renvoyaient à `#business` par `@id`
sans que le nœud soit défini chez elles — il ne l'était que sur l'accueil. Google analyse
les données structurées page par page : sur `/mariage`, le `provider` du `Service` était
un nœud vide, sans type ni nom. Chaque page porte désormais une souche compacte, que le
`@id` identique fait fusionner avec le nœud complet. **En ajoutant une page qui cite
`#business`, `#jonathan` ou `#carnet`, copier la souche correspondante** — ou lancer
`.claude/verifier.py`, qui le contrôle.

**`loading="lazy"` diffère bien les diapositives du hero.** Un audit a conclu l'inverse,
et l'argument était solide : les cinq images sont en `position:absolute` dans un hero en
`100svh`, donc dans le viewport, et le lazy-loading ne défère que ce qui en sort. Mesure
faite au navigateur avant/après : **strictement identique** — 259 Ko avant l'événement
`load`, 128 Ko après, dans les deux versions. Chromium les défère déjà. La tentative de
les promouvoir en JavaScript après `load` a donc été retirée : elle n'apportait rien et
ajoutait un chemin sans JS à maintenir. **Ne pas recommencer sans mesurer d'abord.**

**Le vrai poids du chemin critique était la bande parallaxe.** `creole.jpg`, 152 Ko en
JPEG pleine taille, était chargé avant `load` alors que la bande est sous la ligne de
flottaison — plus lourd, à lui seul, que les cinq photos du hero réunies. Le fond est
passé de l'attribut `style` en ligne à une classe `.pause-creole` qui sert le WebP par
`image-set()`, avec un palier 760 sous 900 px. Mesuré sur un viewport de 390 px :
**259 Ko → 186 Ko avant l'événement `load`**, sans changement visible.

**Le logo était la seule image surdimensionnée du site**, et ce fichier disait le
contraire. Sa plus petite variante faisait 480 px et 35 Ko pour un emplacement de 95 px,
sur les dix-sept pages. Un palier `logo-200` (8 Ko en WebP) a été généré.

**Le préchargement de police visait la mauvaise graisse.** Playfair 400 était préchargé,
alors que `h1` et `h2` sont en 600 : la graisse réellement affichée n'était découverte
qu'après le parsing du CSS.

**Un huitième lien ne tenait plus dans la barre.** L'entrée « Histoires » a fait passer
le seuil du menu burger de 1080 à 1180 px — mesuré au navigateur, la liste passait à
trois lignes et touchait le logo à 1081 px. **Le seuil est écrit à trois endroits** : deux
`@media` dans `style.css` et un `innerWidth` dans `site.js`. Les trois doivent bouger
ensemble.

**Le récit disait « Raphaël le maquilleur ».** La personne créditée est Raphaëlle, « la
Fée Raphinée », maquilleuse. Corrigé dans la page, dans `llms.txt` et dans
`llms-full.txt`. Rappel de méthode : avant de lier un prestataire, ouvrir la page et lire
le nom affiché, l'activité et l'ancrage — un homonyme métropolitain existe pour « 33
Tours », avec une fiche Mariages.net crédible et un site infecté de spam.
