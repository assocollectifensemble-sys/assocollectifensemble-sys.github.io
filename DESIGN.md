---
name: Une 2CV, mille histoires
description: Location de 2CV de collection avec chauffeur à La Réunion — mariages, balades, shootings
colors:
  blanc: "#ffffff"
  creme: "#faf7f2"
  sable: "#f1eae0"
  nude: "#c9a98d"
  terre: "#a97e5f"
  terre-lien: "#8a6244"
  brun: "#453930"
  encre: "#3a3129"
  sauge: "#8a9a83"
  vert-note: "#4c6b53"
  wa: "#157f45"
  wa-fonce: "#0f6437"
typography:
  script:
    fontFamily: "Pinyon Script, cursive"
    fontSize: "clamp(38px, 6vw, 66px)"
    fontWeight: 400
    lineHeight: 1.2
  display:
    fontFamily: "Playfair Display, serif"
    fontSize: "clamp(30px, 5vw, 54px)"
    fontWeight: 600
    lineHeight: 1.12
  headline:
    fontFamily: "Playfair Display, serif"
    fontSize: "clamp(28px, 3.8vw, 42px)"
    fontWeight: 600
    lineHeight: 1.2
  title:
    fontFamily: "Playfair Display, serif"
    fontSize: "clamp(24px, 3.4vw, 34px)"
    fontWeight: 600
    lineHeight: 1.3
  body:
    fontFamily: "Jost, sans-serif"
    fontSize: "16.5px"
    fontWeight: 300
    lineHeight: 1.85
  label:
    fontFamily: "Jost, sans-serif"
    fontSize: "14px"
    fontWeight: 500
    letterSpacing: "0.12em"
rounded:
  net: "2px"
  doux: "18px"
  carte: "30px"
  pilule: "40px"
  cercle: "50%"
spacing:
  xs: "10px"
  sm: "14px"
  md: "22px"
  lg: "34px"
  xl: "46px"
  xxl: "60px"
components:
  button-whatsapp:
    backgroundColor: "{colors.wa}"
    textColor: "{colors.blanc}"
    rounded: "{rounded.pilule}"
    padding: "14px 28px"
    typography: "{typography.label}"
  button-whatsapp-hover:
    backgroundColor: "{colors.wa-fonce}"
  button-brun:
    backgroundColor: "{colors.brun}"
    textColor: "{colors.blanc}"
    rounded: "{rounded.pilule}"
    padding: "14px 28px"
  button-contour:
    backgroundColor: "transparent"
    textColor: "{colors.terre}"
    rounded: "{rounded.pilule}"
    padding: "14px 28px"
  carte-prestation:
    backgroundColor: "{colors.blanc}"
    textColor: "{colors.encre}"
    rounded: "{rounded.net}"
    padding: "10px"
    height: "330px"
---

# Design System: Une 2CV, mille histoires

## Overview

**Creative North Star: "Le Carnet du Lagon"**

Un carnet de voyage tenu dans la lumière du lagon. Le papier crème, l'encre brune et l'écriture manuscrite d'un côté ; la lenteur, le sel et la lumière rasante de fin de journée de l'autre. Le site n'est pas une vitrine commerciale : c'est le carnet où l'on consigne des trajets déjà vécus, ouvert sur une table en fin d'après-midi.

Cette double nature commande tout le reste. Le fond n'est jamais blanc pur là où le contenu respire : il est crème (#faf7f2) ou sable (#f1eae0), comme une page qui a pris le soleil. Les titres sont en Playfair Display, une serif de livre, jamais une sans-serif de tableau de bord. Et les moments d'émotion — le nom d'une voiture, une phrase de bascule entre deux sections — passent en Pinyon Script, une anglaise manuscrite qui joue le rôle de la note écrite à la main dans la marge.

La densité est basse et assumée. Les sections respirent (34 à 60 px de gouttière), les colonnes sont larges, le texte courant plafonne à 760 px. Rien ne se bouscule, parce que le produit vendu est précisément le contraire de la vitesse : une 2CV qui ne dépasse pas les hauts, un trajet où l'on prend le temps.

**Key Characteristics:**
- Papier crème et encre brune, jamais de blanc clinique sur les grandes surfaces
- Trois voix typographiques strictement séparées : manuscrite, livre, courante
- Photographie pleine largeur, non recadrée en vignette : l'île est le décor
- Vert WhatsApp comme unique couleur vive, réservée à l'action
- Basse densité, longues respirations verticales

## Colors

Une palette de terre et de papier, tirée de la carrosserie, du cuir et du sable, à laquelle se greffe un seul vert vif fonctionnel.

### Primary
- **Terre Cuite Patinée** (`{colors.terre}`) : l'accent chaud du site, en usage **décoratif uniquement**. Filets, encadrements, contours de boutons, chiffres décoratifs, survol de la navigation transparente. C'est la couleur de la 2CV vieillie au soleil.
- **Terre Lisible** (`{colors.terre-lien}`) : la version assombrie de la précédente, réservée au **texte**. Liens dans le corps de texte, en-têtes de tableau, survol de la navigation opaque. Même famille chromatique, contraste suffisant.
- **Nude Sable** (`{colors.nude}`) : la version claire de l'accent. Bordures, encadrements, soulignements. Jamais du texte.

### Secondary
- **Vert WhatsApp Profond** (`{colors.wa}`) : strictement fonctionnel. Le seul vert saturé du site, réservé au bouton de contact et à la bulle flottante. Sa version foncée (`{colors.wa-fonce}`) ne sert qu'au survol. Ce n'est pas le `#25d366` officiel de WhatsApp : celui-ci ne donne que 1,98:1 avec du blanc, illisible en plein soleil. L'icône porte la reconnaissance de la marque, la couleur porte la lisibilité.
- **Sauge** (`{colors.sauge}`) : accent végétal rare, pour les touches secondaires qui ne doivent pas devenir des appels à l'action.
- **Vert Note** (`{colors.vert-note}`) : le texte secondaire posé sur la carte WhatsApp de la page contact, dont le fond est un dégradé vert pâle. Seul endroit où il apparaît.

### Neutral
- **Papier Crème** (`{colors.creme}`) : le fond dominant des sections de contenu. C'est la page du carnet.
- **Sable Clair** (`{colors.sable}`) : fond alterné, utilisé pour distinguer deux sections successives sans introduire de trait.
- **Brun Reliure** (`{colors.brun}`) : tous les titres. La couleur de l'encre du carnet.
- **Encre** (`{colors.encre}`) : le texte courant. Légèrement plus froid et plus sombre que le brun des titres.
- **Blanc** (`{colors.blanc}`) : réservé aux cartes et aux cadres photo posés sur un fond crème ou sable. Jamais en fond de page entière.

### Named Rules

**La Règle du Vert Unique.** Le vert WhatsApp est la seule couleur saturée du site. Elle ne désigne qu'une chose : écrire à Jonathan. Aucun titre, aucun filet, aucune icône décorative n'a le droit de la porter. Sa rareté est ce qui la rend efficace.

**La Règle du Papier.** Aucune grande surface n'est en blanc pur. Le blanc est un matériau de carte posée sur du papier, pas un fond de page. Si une section paraît vide et froide, le correctif est le crème, pas une bordure.

**La Règle des Deux Terres.** `{colors.terre}` dessine, `{colors.terre-lien}` se lit. Un filet, un cadre, un chiffre décoratif prennent la première ; dès qu'il s'agit d'un mot que quelqu'un doit déchiffrer, c'est la seconde. Cette paire existe parce que le terre d'origine plafonne à 3,37:1 sur le crème.

## Typography

**Display Font:** Playfair Display (serif, 400 à 700)
**Body Font:** Jost (sans-serif géométrique, 300 à 500)
**Script Font:** Pinyon Script (anglaise manuscrite, 400)

**Character:** Une serif de livre pour l'autorité, une géométrique légère pour la lisibilité, une anglaise manuscrite pour l'émotion. Le contraste vient de la graisse, pas de la taille : le corps de texte est en 300, ce qui laisse aux titres en 600 tout l'espace de hiérarchie.

### Hierarchy
- **Script** (Pinyon Script 400, `clamp(38px, 6vw, 66px)`) : les phrases de bascule et les mots posés sur une photo. Jamais plus d'une occurrence visible à l'écran.
- **Display** (Playfair 600, `clamp(30px, 5vw, 54px)`, interligne 1.12) : le H1 d'une page, toujours sur photographie, toujours en blanc avec ombre portée.
- **Headline** (Playfair 600, `clamp(28px, 3.8vw, 42px)`) : les titres de blocs `.feature`, en regard d'une image.
- **Title** (Playfair 600, `clamp(24px, 3.4vw, 34px)`) : les H2 dans le corps de texte long.
- **Body** (Jost 300, 16.5 px, interligne 1.75 à 1.85) : le texte courant, plafonné à 760 px de large.
- **Label** (Jost 500, 14 px, interlettrage 0.12em, capitales) : boutons, éléments de navigation, surtitres.

### Named Rules

**La Règle des Trois Voix.** Manuscrite pour l'émotion, serif pour l'autorité, sans-serif pour l'information. Une voix ne fait jamais le travail d'une autre : un prix ne s'écrit pas en Pinyon Script, une phrase de bascule ne s'écrit pas en Jost.

**La Règle du Trois Cent.** Le texte courant est en graisse 300, jamais 400. C'est ce qui donne au site son air de page imprimée plutôt que d'interface.

## Layout

Grilles fluides en `repeat(auto-fit, minmax(...))`, jamais de nombre de colonnes figé : les cartes se réorganisent seules entre 1 et 4 colonnes. Les largeurs maximales sont graduées selon la densité du contenu — 1150 px pour les grilles de prestations, 1080 px pour les blocs image-texte, 760 px pour le texte courant, 640 px pour les chapôs centrés.

Les gouttières suivent l'échelle 14 / 22 / 28 / 34 / 46 / 50 px, les plus larges étant réservées aux grilles éditoriales. Les ruptures se font à 1080 px (passage au menu burger), 900 px et 820 px (empilement des blocs à deux colonnes), 620 px et 560 px (cartes en pleine largeur).

Les sections alternent crème et sable pour se séparer, jamais par un filet horizontal.

## Elevation & Depth

Le système est presque plat. La profondeur vient de la superposition de tons (une carte blanche sur un fond crème) et non de l'ombre. Là où une ombre existe, elle est large, très diffuse et faiblement opaque — une lumière d'après-midi, pas un halo d'interface.

### Shadow Vocabulary
- **Repos** (`box-shadow: 0 12px 34px rgba(58,49,41,.08)`) : les cartes de prestation et les cadres photo au repos.
- **Survol** (`box-shadow: 0 20px 48px rgba(58,49,41,.15)`) : la même carte soulevée de 7 px au survol.
- **Flottant** (`box-shadow: 0 10px 30px rgba(37,211,102,.5)`) : réservé aux boutons WhatsApp, la seule ombre teintée du site.
- **Panneau** (`box-shadow: -12px 0 44px rgba(58,49,41,.2)`) : le menu mobile qui glisse depuis la droite.

### Named Rules

**La Règle de l'Ombre Longue.** Toute ombre a un flou d'au moins 22 px et une opacité inférieure à 0.2. Une ombre courte et dure appartient à une interface logicielle, pas à ce site.

## Shapes

Deux langages de forme coexistent, et leur séparation est stricte. Les **actions** sont des pilules (rayon 40 px) ou des cercles (50 %) : boutons, bulle WhatsApp, bouton son, portraits ronds. Les **contenus** sont à angles vifs (rayon 0 à 2 px) : cartes de prestation, cadres photo, encadrés. Le cadre photo se distingue par un filet de 1 px en nude doublé d'un `outline` décalé de 6 px, qui imite la marge d'un tirage papier collé dans un carnet.

## Components

### Buttons
- **Shape:** pilule complète (rayon 40 px), padding 14 × 28 px, capitales interlettrées à 0.12em.
- **WhatsApp (primaire):** fond vert `{colors.wa}`, texte blanc, ombre teintée. C'est l'action par défaut partout sur le site.
- **Brun (secondaire):** fond `{colors.brun}`, texte blanc. Pour les actions de navigation interne.
- **Ligne (sur photo):** bordure blanche à 85 % d'opacité, `backdrop-filter: blur(3px)`. Uniquement sur une image de fond.
- **Contour (tertiaire):** bordure `{colors.terre}`, fond transparent. Sur fond clair uniquement.
- **Hover / Focus:** élévation de 3 px (`translateY(-3px)`) en 0.3 s, plus assombrissement du fond pour les variantes pleines.

### Cards / Containers
- **Corner Style:** angles vifs (0 à 2 px).
- **Background:** blanc sur fond crème ou sable.
- **Border:** filet 1 px `#ecdfd0`, et pour les cadres photo un `outline` `{colors.nude}` décalé de 6 px.
- **Shadow Strategy:** ombre Repos, ombre Survol au pointeur (voir Elevation & Depth).
- **Internal Padding:** 10 px pour un cadre photo, `clamp(24px, 5vw, 54px)` pour un encadré de section.
- **Comportement:** au survol, la carte s'élève de 7 px et l'image intérieure grandit de 6 % en 0.8 s, contenue par `overflow: hidden`.

### Navigation
Barre fixe transparente sur la photographie du hero, qui bascule sur fond opaque après 60 px de défilement. Liens en Jost 500, 13 px, capitales, interlettrage 0.11em, blancs avec ombre portée tant que le fond est photographique. Sous 1080 px, menu burger et panneau latéral de 80vw (330 px maximum) qui glisse depuis la droite en 0.35 s.

### Signature: le cadre photo de carnet
Le motif identitaire du site. Une photographie dans un cadre blanc de 10 px, bordé d'un filet nude, doublé d'un `outline` décalé de 6 px. L'effet est celui d'un tirage papier posé sur la page d'un carnet, avec sa marge et son ombre portée. C'est ce composant qui porte la métaphore ; il ne doit pas être remplacé par une image à bord perdu et coins arrondis.

## Do's and Don'ts

### Do:
- **Do** utiliser crème (`#faf7f2`) ou sable (`#f1eae0`) en fond de section, et réserver le blanc aux cartes posées dessus.
- **Do** séparer deux sections successives par une alternance de fond, jamais par un filet horizontal.
- **Do** garder le texte courant en Jost 300 à 16.5 px, plafonné à 760 px de large.
- **Do** limiter Pinyon Script à une occurrence visible par écran.
- **Do** définir les grilles en `repeat(auto-fit, minmax(...))` pour qu'elles se réorganisent seules.
- **Do** respecter `prefers-reduced-motion` pour toute nouvelle animation, comme le fait déjà la feuille de style.

### Don't:
- **Don't** employer le vert WhatsApp ailleurs que sur une action de contact.
- **Don't** arrondir les angles d'une carte de contenu : les coins ronds appartiennent aux actions.
- **Don't** poser une ombre courte et dure (flou inférieur à 22 px ou opacité supérieure à 0.2).
- **Don't** écrire un prix, une date ou une information pratique en Pinyon Script.
- **Don't** introduire une quatrième famille typographique.
- **Don't** recadrer les photographies en petites vignettes carrées : le paysage fait partie du produit.
