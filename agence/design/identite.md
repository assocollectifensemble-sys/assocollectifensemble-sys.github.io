# Identité visuelle — système de référence

> Agent design — 2026-08-23. Direction incarnée : **Otonom** (recommandation de
> `noms-de-marque.md`, en attente de l'arbitrage de Jon — le système est nommé par
> rôles et reste valable si le nom final change).
>
> Règle de cohérence : une fois ce fichier validé par Jon, tout écart demande une mise à
> jour ici — jamais d'exception silencieuse. Les variables prêtes à l'emploi sont dans
> `tokens.css` (clair + sombre via `prefers-color-scheme`, forçable via `data-theme`).

## 1. Intention

Incarner l'**artisan-expert local** : fiable, moderne, chaleureux. Zéro cliché tech
(pas de bleu corporate, pas de robots, pas de circuits imprimés, pas de dégradés néon).
L'ancrage réunionnais passe par la **matière** — basalte, sable, canne, braise, curcuma —
jamais par le folklore (pas de palmiers, pas de cases créoles en illustration, pas de
créole plaqué en décor).

La référence mentale : un **atelier d'artisan bien tenu** — plan de travail clair, outils
rangés, une couleur d'accent franche, de la lumière chaude.

## 2. Palette

Nommée par matière (ancrage subtil), déclinée par rôle. Tous les couples texte/fond
listés en §5 sont **vérifiés ≥ 4,5:1 (AA)**, la plupart AAA.

### Mode clair (par défaut)

| Rôle | Nom matière | Hex | Usage |
|---|---|---|---|
| Fond | Sable | `#FAF6F0` | Fond de page — blanc cassé chaud, jamais de blanc pur en pleine page |
| Surface | Coton | `#FFFDF9` | Cartes, panneaux, champs de formulaire |
| Bordure | Sable foncé | `#E5DCCE` | Filets, séparateurs, contours de champs |
| Texte | Basalte | `#23201B` | Titres et corps de texte |
| Texte secondaire | Bois de goyavier | `#5C554B` | Légendes, métadonnées, placeholders |
| **Accent** | **Vert canne** | `#1F6A4A` | Liens, boutons primaires, éléments interactifs |
| Accent appuyé | Vétyver | `#175239` | Hover/actif de l'accent, titres ponctuels |
| Accent chaud | Braise | `#A03F14` | Emphase rare : chiffre clé, badge « échéance sept. 2026 », CTA secondaire |
| Décor | Curcuma | `#E0A320` | **Jamais en texte sur fond clair** — soulignés épais, puces, fonds de badge (texte Basalte dessus) |
| Texte inversé | Coton | `#FFFDF9` | Texte sur boutons Vert canne ou Braise |

### Mode sombre

Pas un simple négatif : un **noir chaud basalte**, jamais de noir bleuté.

| Rôle | Hex | Note |
|---|---|---|
| Fond | `#191512` | Basalte nuit |
| Surface | `#221E19` | Cartes, panneaux |
| Bordure | `#3A342C` | Filets |
| Texte | `#F2EDE4` | Blanc sable, jamais `#FFFFFF` pur |
| Texte secondaire | `#B5AC9E` | |
| Accent | `#7FC9A2` | Vert canne éclairci (les accents s'éclaircissent en sombre) |
| Accent appuyé | `#A4DDBF` | Hover/actif |
| Accent chaud | `#E88B57` | Braise éclaircie |
| Décor | `#E8B84B` | Curcuma — utilisable en texte court en sombre (9,8:1) |
| Texte inversé | `#14100D` | Texte sur boutons Vert canne clair |

### États (feedback)

| État | Clair | Sombre | Note |
|---|---|---|---|
| Succès | `#1F6A4A` | `#7FC9A2` | = accent : « ça marche » est notre couleur de marque |
| Avertissement | `#8A6100` | `#E8B84B` | Curcuma assombri pour tenir l'AA en clair |
| Erreur | `#B2361F` | `#F09580` | Rouge terre, pas rouge vif |
| Focus | anneau `#1F6A4A` / `#7FC9A2`, 2 px, décalé de 2 px | | Toujours visible au clavier |

Pas d'état « info » bleu : l'information neutre se dit en Texte secondaire sur Surface.

## 3. Typographie (Google Fonts)

| Rôle | Fonte | Graisses | Pourquoi |
|---|---|---|---|
| Display (titres, chiffres clés, logo provisoire) | **Fraunces** | 500, 600 (SoftMode : `"opsz"` auto) | Serif contemporaine à fort caractère : chaleur d'imprimeur-artisan, zéro connotation tech, très différenciante face aux sans-serif froides des agences locales. |
| Texte (corps, UI, formulaires) | **Work Sans** | 400, 500, 600 | Grotesque humaniste très lisible en petit corps et sur mobile (usage dominant à La Réunion), dessinée pour l'écran, neutre sans être froide. |

Chargement : `https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Work+Sans:wght@400;500;600&display=swap`
Fallbacks obligatoires : Fraunces → `Georgia, "Times New Roman", serif` ; Work Sans → `system-ui, "Segoe UI", Arial, sans-serif`.

Échelle (base 16 px, ratio ~1,25) : 13 / 16 / 20 / 25 / 31 / 39 / 49.
Corps de texte : Work Sans 400, interlignage 1,6, largeur de colonne max 70 caractères.
Titres : Fraunces 600, interlignage 1,15, jamais en majuscules forcées.
Chiffres clés (prix, délais) : Fraunces 500 en grand corps — les prix sont affichés
publiquement (règle commerciale), donc on les assume typographiquement.

## 4. Ton visuel

**Ce qu'on fait :**
- Aplats francs, angles doux (rayon 8 px cartes / 6 px boutons), ombres très discrètes.
- Beaucoup de blanc cassé, une seule couleur d'accent par écran ; la Braise en touche rare.
- Photos réelles : Jon en situation, mains sur clavier, ateliers de formation, vrais
  commerces réunionnais en lumière naturelle chaude. Léger voile Sable si besoin d'unifier.
- Pictos au trait (2 px, bouts ronds, style outil/main/geste), teinte Basalte ou Vert canne.
- Motif géométrique discret autorisé : trame inspirée du bardeau / de la tôle nervurée
  (lignes parallèles), en Bordure, à 10–15 % de contraste maximum.
- Le créole en typographie assumée quand il porte le sens (« Installé. Formé. Otonom. »).

**Ce qu'on ne fait jamais :**
- Bleu corporate, dégradés « SaaS », néon, glassmorphism.
- Robots, cerveaux, circuits imprimés, code qui pleut, avatars IA.
- Folklore plaqué : palmiers, dodo, volcan en éruption, madras décoratif, cases créoles
  en clipart, créole utilisé comme gadget.
- Banques d'images génériques (poignées de main, open-spaces parisiens).
- Plus de deux couleurs d'accent sur un même écran ; texte Curcuma sur fond clair ;
  blanc pur `#FFFFFF` ou noir pur `#000000` en aplat de page.

## 5. Contrastes vérifiés (WCAG)

Calculés le 2026-08-23 (formule de luminance relative WCAG 2.1). AA texte normal = 4,5:1.

| Couple | Ratio | Niveau |
|---|---|---|
| Basalte `#23201B` / Sable `#FAF6F0` | 15,07 | AAA |
| Texte secondaire `#5C554B` / Sable | 6,83 | AA (AAA grand texte) |
| Vert canne `#1F6A4A` / Sable | 6,06 | AA |
| Vétyver `#175239` / Sable | 8,47 | AAA |
| Coton `#FFFDF9` / bouton Vert canne | 6,42 | AA |
| Braise texte `#A03F14` / Sable | 6,07 | AA |
| Coton / bouton Braise `#A03F14` | 6,43 | AA |
| Erreur `#B2361F` / Sable | 5,67 | AA |
| Avertissement `#8A6100` / Sable | 5,15 | AA |
| Texte `#F2EDE4` / Fond sombre `#191512` | 15,56 | AAA |
| Texte secondaire `#B5AC9E` / Fond sombre | 8,09 | AAA |
| Texte secondaire `#B5AC9E` / Surface sombre `#221E19` | 7,38 | AAA |
| Vert canne clair `#7FC9A2` / Fond sombre | 9,31 | AAA |
| Vert canne clair / Surface sombre | 8,50 | AAA |
| Braise claire `#E88B57` / Fond sombre | 7,14 | AAA |
| Curcuma `#E8B84B` / Fond sombre | 9,84 | AAA |
| Texte inversé `#14100D` / bouton `#7FC9A2` | 9,71 | AAA |
| Erreur sombre `#F09580` / Fond sombre | 8,05 | AAA |

## 6. Usage par rôle (résumé pour les autres agents)

- **Fond de page** : Sable (clair) / Basalte nuit (sombre). Sections alternées avec Surface.
- **Texte** : Basalte ; secondaire pour ce qui peut être ignoré sans perdre le sens.
- **Un seul accent interactif** : Vert canne — liens, boutons primaires, éléments actifs,
  icônes cliquables. Hover/actif : Vétyver (clair) / accent appuyé (sombre).
- **Braise** : au plus un élément par écran (chiffre clé, badge d'urgence conformité, CTA
  secondaire). Si tout est important, rien ne l'est.
- **Curcuma** : décor uniquement en clair (souligné, puce, fond de badge avec texte
  Basalte) ; texte court autorisé en sombre.
- **États** : succès = accent ; avertissement = curcuma assombri ; erreur = rouge terre ;
  focus toujours en anneau visible.
- Boutons primaires : fond Vert canne, texte Coton, rayon 6 px, sans ombre portée.
  Boutons secondaires : contour Bordure, texte Vert canne, fond transparent.
