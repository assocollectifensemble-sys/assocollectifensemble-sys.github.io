# Audit du site — remarques non appliquées

Passe du 7 août 2026. Le périmètre demandé était **technique uniquement** : tout ce qui
touche à l'apparence est listé ici sans avoir été modifié, pour que vous décidiez.

Ce qui a été appliqué se lit dans les trois commits précédents (images WebP responsive,
préchargement LCP par page, `sizes` corrects, `decoding="async"`).

---

## 1. Contrastes insuffisants (accessibilité)

Trois couleurs ne passent pas le seuil WCAG AA. Aucune n'a été touchée : les corriger
change l'apparence, et l'une d'elles est une couleur de marque.

| Élément | Couleurs | Rapport | Seuil requis |
|---|---|---|---|
| Texte blanc sur le bouton WhatsApp | `#ffffff` sur `#25d366` | **1,98:1** | 4,5:1 |
| Liens de navigation au survol | `#c9a98d` sur `#faf7f2` | **2,20:1** | 4,5:1 |
| Grands chiffres du déroulé (`.temps .num`, Pinyon Script 44px) | `#c9a98d` sur `#faf7f2` | **2,20:1** | 3:1 (texte large) |

**Le bouton WhatsApp est le cas sérieux** : c'est votre appel à l'action principal, présent
sur toutes les pages. Le vert `#25d366` est la couleur officielle de WhatsApp, et l'assombrir
casse la reconnaissance immédiate du bouton. Deux sorties possibles : garder le vert et passer
le texte en `#0b3d1e` (ratio 7,4:1, lisible mais inhabituel), ou utiliser `#128c4a` — que vous
avez déjà défini comme `--wa-fonce` pour le survol — en fond permanent, ce qui donne 4,6:1
avec du blanc tout en restant identifiable comme WhatsApp. La seconde option est la plus
propre, mais elle assombrit visiblement le bouton.

Le survol de navigation et les chiffres du déroulé sont mineurs : le premier ne dure qu'un
instant, le second est décoratif et l'information est portée par le libellé voisin. Passer
`--nude` à `--terre` (`#a97e5f`, 3,37:1) sur ces deux usages suffirait à corriger le cas
« texte large » sans dénaturer la palette.

## 2. Densité de tirets cadratins

Le détecteur d'Impeccable signale une saturation de « — » sur 8 pages : `faq.html` (19),
`index.html` (16), `balades.html` et `evjf-evjg.html` (12), `histoires.html` (11),
`rosalie-et-soizig.html` (10), et deux autres.

C'est une alerte consultative, pas une faute. Elle existe parce qu'une densité élevée de
tirets cadratins est devenue un marqueur de texte écrit par IA. Sur un site dont l'argument
est l'authenticité et l'artisanat, ça mérite un coup d'œil : remplacer un tiret sur deux par
une virgule, un deux-points ou un point suffit à casser la cadence. C'est de la copie, donc
votre décision, pas la mienne.

## 3. Deux photos jamais publiées

`img/histoires/emma-fabien/02-fleurs-capot.jpg` et `06-preparatifs.jpg` existent dans le dépôt
mais aucune page ne les affiche. Les originaux ont été conservés ; seules les variantes
générées ont été retirées. Soit elles ont leur place dans le récit d'Emma et Fabien et il faut
les y ajouter, soit elles sont un reste d'une sélection précédente et peuvent partir.

## 4. Points techniques laissés en l'état, volontairement

**La musique (`assets/musique.mp3`, 2 Mo).** Déjà en `preload="none"` : rien n'est téléchargé
tant que le visiteur ne clique pas. Aucun gain à espérer côté chargement. Si vous vouliez
alléger le dépôt, ré-encoder en 96 kbps mono la ferait tomber sous 700 Ko, mais c'est un
arbitrage de qualité sonore, pas une optimisation gratuite.

**CSS et JS non minifiés** (566 et 153 lignes). Le gain serait de l'ordre de 5 Ko une fois la
compression du serveur appliquée, contre une perte nette de lisibilité pour vous. Le rapport
n'est pas favorable sur un site de cette taille.

**Les photos les plus lourdes.** `grand1.jpg` et `grand2.jpg` (380 et 402 Ko) ne gagnent que
10 à 13 % en WebP : elles sont déjà très compressées à la source. Descendre plus bas
dégraderait visiblement le grain. Elles restent les deux fichiers les plus lourds du site.

**Le déroulé responsive.** Aucune image n'est plus surdimensionnée à aucune largeur testée
(1440px et 390px). Le seul palier manquant serait un 320px pour les portraits ronds de 158px,
qui économiserait quelques dizaines de kilo-octets sur desktop uniquement. Non fait : le
rapport travail/gain ne le justifie pas.

## 5. Ce qui était déjà bien fait

À noter, parce que ça explique pourquoi la marge de progression était surtout sur les images :
les 102 balises `<img>` avaient déjà `width`, `height` et `alt` renseignés (aucun décalage de
mise en page, accessibilité correcte), les polices sont auto-hébergées et préchargées,
`prefers-reduced-motion` est respecté, le JSON-LD est complet et détaillé, et le détecteur
d'Impeccable ne remonte **aucun** anti-pattern de design réel sur les 14 pages.
