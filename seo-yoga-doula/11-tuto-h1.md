# Tuto : les titres H1 (et pourquoi il n'en faut qu'un)

⏱️ 30-45 min · 💻 ordinateur uniquement (Elementor)

## C'est quoi, un H1 ?

Sur une page web, les titres ont un **niveau**, comme dans un livre :

- **H1** = le titre du livre. Un seul, en haut.
- **H2** = les titres de chapitre. Autant qu'on veut.
- **H3** = les sous-titres à l'intérieur d'un chapitre.

Visuellement, ça se traduit juste par une taille de texte. Mais pour Google, c'est bien plus que ça : **le H1 est la phrase qui dit de quoi parle la page.** C'est le premier endroit qu'un moteur regarde pour comprendre où il est.

## Le problème sur le site

Quand on construit une page avec Elementor, chaque bloc de titre qu'on ajoute a un réglage « quel niveau ? ». Par défaut, beaucoup de modèles mettent H1 partout, parce que c'est ce qui rend le texte le plus gros. Résultat :

| Page | Nombre de H1 | Devrait être |
|---|---|---|
| Page d'accueil | **9** | 1 |
| Formation Yoga Doula | **8** | 1 |
| Programme Yoga Maternité | 1 ✅ | — |

Neuf H1, c'est comme si la page criait neuf choses différentes en même temps. Google ne sait pas laquelle compter, donc il n'en retient aucune vraiment. Quentin l'avait déjà signalé dans son audit de mars 2023 — ça n'a jamais été corrigé.

**Ce n'est pas une pénalité.** C'est un signal gaspillé. On a un mégaphone et on parle dans le vide.

## Comment corriger, pas à pas

### Page Formation Yoga Doula (la plus rentable — commence par elle)

Cette page est en **position 21 sur « formation doula »**, une requête qui lui apporte 1 828 affichages par an. Et le mot « formation » n'apparaît nulle part dans son H1 actuel, qui est « Deviens DOULA ».

1. WordPress → **Pages** → survole *Formation Yoga Doula & Yoga Périnatal* → **Modifier avec Elementor**.
2. Attends le chargement complet de l'éditeur.
3. **Repère les titres.** Clique sur chaque gros texte de la page, l'un après l'autre. À chaque clic, un panneau s'ouvre à gauche.
4. Dans ce panneau, onglet **Contenu**, cherche une ligne appelée **« Balise HTML »** (ou *HTML Tag* si l'interface est en anglais). C'est un menu déroulant avec H1, H2, H3, H4, H5, H6, div, span, p.
5. **Règle :** un seul titre reste en **H1**. Tous les autres passent en **H2**.
6. Pour cette page, les titres à passer en H2 sont :
   - « La formation Yoga Doula & Yoga Périnatal couvre les thèmes suivants »
   - « Les + de la formation »
   - « A qui s'adresse la formation »
   - « Comment s'inscrire »
   - « Témoignages des anciennes étudiantes »
   - « Foire aux questions »
   - « Je suis intéressé.e par la formation »
7. Le seul qui reste en H1 : **« Deviens DOULA »** — et je te conseille de le remplacer par **« Formation de doula & yoga périnatal »**. Tu perds un peu de punch, tu gagnes le mot-clé sur lequel la page se bat.

   *Si tu tiens au « Deviens DOULA » pour l'impact visuel : garde-le comme texte affiché en H2, et mets « Formation de doula & yoga périnatal » en H1 juste au-dessus ou en dessous. C'est un arbitrage entre esthétique et référencement — à toi de voir.*

8. **Bouton vert PUBLIER**, en bas à gauche.

   ⚠️ **« Enregistrer le brouillon » ne suffit pas.** Seul **PUBLIER** met la modification en ligne. C'est le piège classique d'Elementor.

### Page d'accueil

Même méthode. Les titres à passer en H2 :
- « Nos formations »
- « Formation complète Yoga DOULA & YOGA périnatal »
- « Programme YOGA Maternité »
- « Parcours Devenir PARENTS »
- « Nos modules de formation à la carte »
- « Les Évènements proposés par l'École de Doula »
- « Témoignages des Doulas diplômées »
- « Ecole Yoga Doula fondée en 2007 »

Celui qui reste en H1 : **« Deviens DOULA »** (le premier, tout en haut).

## Vérifier que ça a marché

Trois façons, de la plus simple à la plus fiable :

1. **Le plus simple :** dis-le-moi, je relis le code source de la page en trente secondes et je te confirme le compte.
2. Sur ordinateur : ouvre la page, **clic droit → Afficher le code source**, puis `Ctrl+F` et cherche `<h1`. Le navigateur t'indique le nombre d'occurrences.
3. Un outil en ligne gratuit type *SEO Meta in 1 Click* (extension Chrome) affiche la liste des H1/H2/H3 d'une page en un clic.

## Si tu ne trouves pas le réglage « Balise HTML »

Certains widgets n'en ont pas — notamment les titres intégrés dans un widget « Heading » d'un pack tiers (ElementsKit, Qi Addons). Dans ce cas :

- Regarde dans l'onglet **Avancé** du widget, il y est parfois.
- Sinon, envoie-moi une capture d'écran du panneau de gauche, je te dirai où chercher.
- En dernier recours, c'est exactement le genre de micro-tâche à confier à Fabien : dix minutes pour quelqu'un qui connaît le thème.

## Ce que ça rapporte, honnêtement

C'est une correction **de fond, pas un coup de baguette**. Elle ne fera pas bondir la page de la 21ᵉ à la 3ᵉ place à elle seule. Mais combinée au schema `Course`, aux nouveaux articles qui pointent vers ces pages, et à l'indexation Bing, elle fait partie du socle. Ce sont ces corrections cumulées qui déplacent une page — jamais une seule d'entre elles.
