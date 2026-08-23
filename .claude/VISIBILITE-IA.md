# Être trouvé par les assistants (ChatGPT, Claude, Gemini, Perplexity)

Note de travail, pas une page du site. Elle vit dans `.claude/`, exclu de l'indexation
par `robots.txt`.

## Le constat du 8 août 2026

Un utilisateur demande à Claude quelles voitures vintage sont disponibles pour un mariage
à La Réunion. La réponse cite Vintage Run Services, Tinhobus, RM Location Prestige, AKL,
AGAT — et pas nous. Vérification faite, une recherche sur le nom exact « Une 2CV mille
histoires » ne remonte pas non plus le site.

Ce n'est pas un problème de balisage. Le site est déjà mieux équipé que ses concurrents :
JSON-LD complet sur chaque page, `llms.txt`, FAQPage, titres et descriptions écrits pour
la question réelle du visiteur. Search Console confirme que Google indexe les pages
(`/` et `/mariage` : « Submitted and indexed », verdict PASS, rich results PASS).

Le problème est ailleurs, et il tient en deux chiffres relevés dans Search Console :

- **21 impressions en 28 jours.** Le site est indexé mais ne sort jamais.
- **« Referring URLs known: 1 ».** Google ne connaît quasiment aucun lien entrant.

Un assistant ne connaît pas les sites : il lance une recherche et lit les premiers
résultats. Un site sans lien entrant et sans mention ailleurs n'atteint jamais ces
premiers résultats, quelle que soit la qualité de son balisage. Et les réponses des
assistants s'appuient massivement sur les **annuaires** — mariages.net, PagesJaunes,
cartedelareunion.fr — parce que ces pages agrègent, se citent entre elles et sont
anciennes. C'est exactement ce que montrait la réponse citée plus haut.

## Ce qui a été fait dans le dépôt (8 août 2026)

- `robots.txt` : autorisation nominative des robots d'assistants (ClaudeBot, GPTBot,
  OAI-SearchBot, PerplexityBot, Google-Extended, Applebot, DuckAssistBot, etc.).
  `Allow: /` les couvrait déjà ; les nommer évite qu'un robot qui cherche sa propre
  ligne passe son chemin, et coupe court aux faux positifs des outils d'audit.
- **IndexNow** (`.github/workflows/indexnow.yml` + clé à la racine) : à chaque push
  touchant une page, Bing et Yandex sont prévenus immédiatement. C'est le seul canal
  où l'on pousse au lieu d'attendre, et Bing alimente une partie des réponses de
  ChatGPT, Copilot et DuckDuckGo.
- `llms-full.txt` : le texte intégral des pages, sans HTML, régénéré par
  `python3 .claude/build-llms-full.py`. **À relancer après toute modification de
  contenu**, sinon il ment.
- `sitemap.xml` : les douze pages, `lastmod` à jour (il en manquait une).
- Données structurées de l'accueil : l'association `Collectif Ensemble` (NGO) et
  `Jonathan` (Person) sont devenus des nœuds à part entière, reliés au commerce par
  `@id`. Un assistant qui lit la page sait maintenant qui porte le projet et qui conduit.

Tout cela consolide. **Rien de tout cela ne suffira** : le blocage est hors du dépôt.

## Ce qui débloquera vraiment, dans l'ordre

1. **Google Business Profile.** Gratuit, c'est la fiche que Google et Gemini lisent en
   premier pour une recherche locale, et elle porte les avis. Le `sameAs` du JSON-LD
   pointe déjà vers une fiche Maps : la revendiquer, la compléter (photos, horaires,
   prestations, zone desservie) et y récolter des avis clients.
2. **Mariages.net.** L'annuaire cité en premier dans presque toutes les réponses
   d'assistants sur le mariage à La Réunion. Les concurrents y sont, nous non.
   Une fiche gratuite y crée à la fois un lien entrant et une présence dans la source
   même que les assistants recensent.
3. **PagesJaunes**, puis les annuaires locaux (cartedelareunion.fr, Réunion Tourisme,
   les offices de tourisme de l'Ouest). Même logique.
4. **Bing Webmaster Tools.** Soumettre le domaine et le sitemap. Sans cela, IndexNow
   pousse dans un index où le site n'existe pas encore. C'est l'étape qui ouvre
   Bing → DuckDuckGo → une partie des réponses de ChatGPT et Copilot.
5. **Les liens des partenaires.** La page `/histoires` cite nommément une dizaine de
   prestataires d'un même mariage (fleuriste, traiteur, DJ, photographe, robe…).
   Leur demander un lien en retour est la manière la plus naturelle d'obtenir des
   liens réels, locaux, thématiquement justes — exactement ce qui manque.

## Une page par histoire (fait le 9 août 2026)

`/histoires` est devenu le carnet — une carte par récit — et chaque mariage a sa propre
URL : `/histoires/emma-fabien`. Le récit y porte un `BlogPosting` complet, le carnet un
`Blog` qui le référence, et le fil d'Ariane compte trois niveaux.

**Pour ajouter un mariage**, copier `histoires/emma-fabien.html`, puis quatre gestes
qu'il ne faut pas oublier :

1. Ajouter une carte dans `histoires.html` et une entrée dans son `blogPost`.
2. Ajouter l'URL au `sitemap.xml`.
3. Ajouter la page à `PAGES` dans `.claude/build-llms-full.py`, puis relancer le script.
4. Ajouter la ligne correspondante dans `llms.txt`.

Deux pièges rencontrés, notés pour ne pas les reproduire :

- **Le chemin du fichier EST l'URL.** Le workflow IndexNow construisait les URL avec
  `basename`, ce qui aurait aplati `histoires/emma-fabien.html` en `/emma-fabien`.
  Il utilise maintenant le chemin complet moins l'extension.
- **`histoires.html` et le dossier `histoires/` cohabitent volontairement.** GitHub Pages
  sert `histoires.html` pour `/histoires` et `histoires/emma-fabien.html` pour
  `/histoires/emma-fabien` : aucune redirection, et l'URL `/histoires`, déjà indexée par
  Google, ne bouge pas. Ne pas créer `histoires/index.html` : il entrerait en concurrence
  avec `histoires.html` sur la même URL.

## À faire ensuite sur le site

- **Les avis en `Review`.** Dès qu'il y a des avis Google, les reprendre sur le site en
  `Review` / `AggregateRating` — jamais inventés, jamais reformulés. Les assistants
  citent volontiers ce qui est chiffré et attribué.

## Où en est le chantier (23 août 2026)

Un audit externe a été commandé, puis contre-expertisé par trois agents et vérifié en
production. Sa conclusion de fond est juste, mais sa liste de travaux visait une version
périmée du site : titres, descriptions, canonical, données structurées, images locales,
URL propres, blocs citables — tout cela était déjà fait. Deux choses seulement lui ont
échappé côté dépôt, et elles sont corrigées : le `robots.txt` qui laissait Bingbot lire
`/.claude/`, et les `@id` JSON-LD qui ne définissaient rien hors de l'accueil.

Ce qui est mesuré, en revanche, n'a pas bougé, et c'est le seul chiffre qui compte :
`"une2cvmillehistoires.re" -site:une2cvmillehistoires.re` **ne renvoie aucun résultat**.
Zéro citation externe. Trois pages sur quatorze ressortent avec un extrait ; les onze
autres sont découvertes et jamais retenues. Aucun balisage ne débloquera cela.

Ce qui a été fait ici pour préparer le terrain :

- **Les dix artisans du mariage d'Emma & Fabien sont liés** (huit sur dix ; la violoniste
  n'a qu'un compte privé, et le photographe n'est pas nommé dans le récit). C'est le
  point 5 de la liste ci-dessus, et il est maintenant prêt : il ne reste qu'à leur
  demander le lien en retour.
- **Le carnet est sorti du pied de page** : « Histoires » entre au menu, et l'accueil
  porte un bloc « la dernière histoire ». Le récit recevait deux liens internes contre
  quinze pour les autres pages.
- **Un sitemap images** déclare soixante photos, sur un canal jusqu'ici à zéro.
- **`.claude/verifier.py`** contrôle ce qui se reperd : sitemap dans les deux sens,
  fraîcheur des `lastmod`, `@id` orphelins, synchronisation FAQ, images absentes,
  version des assets, IndexNow, `llms-full.txt`.

Ce qui reste hors du dépôt, par ordre de rendement — inchangé depuis le 8 août, et c'est
le problème : Google Business Profile et les avis, le nom de la fiche Mariages.net (elle
s'appelle encore « Association Collectif Ensemble » et compte zéro avis face à 22 chez
Sea Cox & Sun), Bing Webmaster Tools, les annuaires, les liens des partenaires, et une
propriété GA4 — il n'en existe aucune, donc rien n'est mesuré côté site.

**Sur `llms.txt`, une mise au point.** Le fichier est bon et doit rester à jour, mais il
ne crée aucune découverte : il n'a d'effet que pour un agent qui visite déjà le domaine.
Tant qu'aucun lien externe ne mène ici, c'est un panneau d'accueil sur une route où
personne ne passe. Ne pas le compter comme un levier d'acquisition.
