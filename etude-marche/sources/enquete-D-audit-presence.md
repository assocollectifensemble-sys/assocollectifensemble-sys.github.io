# AGENT D — Audit de la présence en ligne « Une 2CV, mille histoires » + diagnostic Mariages.net

Date de l'audit : 8 août 2026
Méthode : Search Console (compte propriétaire), Firecrawl (scrape + search géolocalisé Réunion/France), API GitHub, DNS/redirects, PageSpeed Insights.
Convention : **[V]** = vérifié par outil pendant l'audit · **[E]** = estimé / déduit · **[NV]** = non vérifiable avec les outils disponibles.

---

## AVERTISSEMENT MÉTHODOLOGIQUE — le brief était périmé

Le brief annonçait « un dépôt GitHub Pages avec les pages index, mariage, balades, shooting-evenements, rosalie-et-soizig, faq, contact, mentions-legales, merci, sitemap.xml, robots.txt ». **C'est la description d'une ancienne version.** Le répertoire de travail local était positionné sur la branche `claude/publish-2cv-site-ud72gf` (commit `bc94841`), très en retard sur `main` (`9633295`). **[V]**

Le site réellement en ligne est bien plus avancé : il contient en plus `tarifs`, `histoires`, `evjf-evjg`, `location-2cv-reunion`, un `404.html`, un `llms.txt`, un `CNAME`, un `.nojekyll`, un `DESIGN.md` et des images WebP responsives. **Tout l'audit ci-dessous porte sur la version réellement en ligne**, pas sur le contenu du répertoire local.

> **Conséquence pratique immédiate :** quiconque travaille depuis ce répertoire local risque d'écraser plusieurs semaines de travail. Faire `git checkout main && git pull` avant toute modification.

---

## 1. INVENTAIRE DES ACTIFS

### 1.1 Actifs TROUVÉS

| Actif | URL exacte | Statut |
|---|---|---|
| **Site web** | `https://une2cvmillehistoires.re/` | **[V]** En ligne, HTTP 200, 1 seul hop, pas de chaîne de redirection |
| Dépôt source | `https://github.com/assocollectifensemble-sys/assocollectifensemble-sys.github.io` | **[V]** branche `main` = production |
| **Instagram** | `https://www.instagram.com/une2cv.millehistoires/` | **[V]** existe |
| **Facebook (page pro)** | `https://www.facebook.com/profile.php?id=61586545132399` | **[V]** existe, publie des vidéos |
| **Google Business Profile** | `https://maps.app.goo.gl/eB1CGDT7FjFVzcnCA` | **[V]** existe et **revendiquée** |
| Facebook perso du porteur | `https://www.facebook.com/monjonjonn` | **[V]** Jonathan Bou, relaie la marque |
| Association (RNA) | `https://repertoiredesassociations.fr/france/reunion/reunion/saint-leu/collectif-ensemble/w122009051.html` | **[V]** COLLECTIF ENSEMBLE, RNA **W122009051**, créée le **17/10/2024**, Saint-Leu |
| Search Console | propriété `sc-domain:une2cvmillehistoires.re` | **[V]** accès **siteOwner** confirmé |

**Hébergement — vérifié :** le site est servi par **GitHub Pages sur domaine personnalisé**, pas sur `.github.io`.
- Enregistrements A : `185.199.108.153`, `.109.153`, `.110.153`, `.111.153` → plage officielle GitHub Pages **[V]**
- Fichier `CNAME` présent sur `main`, contenu : `une2cvmillehistoires.re` **[V]**
- DNS et messagerie chez **OVH** (`ns106.ovh.net`, MX `mx1/2/3.mail.ovh.net`, SPF `v=spf1 include:mx.ovh.com -all`) **[V]**
- TXT `google-site-verification=KEb1bHIsRCz00GTO0wKDsByTT1t5TgFB1LtnnDICOl8` **[V]**

**Fiche Google Business Profile — contenu vérifié :**
- Nom : « Une 2CV, mille histoires 🌿 »
- Catégorie : **« Sightseeing tour agency »** (agence de visites touristiques)
- Adresse : 36 chemin bois de nèfle, **Saint-Leu 97424**
- Téléphone : +262 693 82 81 08 · Site : `https://une2cvmillehistoires.re/`
- **Avis : 0** **[V]**

### 1.2 Actifs INTROUVABLES

| Actif | Verdict | Où j'ai cherché |
|---|---|---|
| **Page Mariages.net** | **INTROUVABLE — confirmé absent** | Catégorie `voiture-mariage/la-reunion` scrapée intégralement (21 prestataires listés, aucun ne correspond) + `site:mariages.net` |
| **Site de la Compagnie ATMA** | **INTROUVABLE** | Recherches géolocalisées Réunion sur « Compagnie ATMA », croisé avec Jonathan Bou / Saint-Leu. Aucun site propre ni fiche |
| Pages Jaunes / annuaires locaux | **INTROUVABLE** | Recherches marque + 974. Aucune fiche |
| Presse locale (Zinfos974, Imaz Press, JIR, Le Quotidien) | **INTROUVABLE** | Recherches marque. **Zéro retombée presse** |
| TripAdvisor / Google Things to do | **INTROUVABLE** | — |
| Compte TikTok propre à la marque | **INTROUVABLE** | Une seule mention : un tiers (`@les_bons_plans_yolo`) qui tague la marque. Pas de compte officiel **[V]** |
| Profil Trustpilot / avis tiers | **INTROUVABLE** | — |

**L'absence est ici l'information principale.** La marque n'existe, hors de son propre site, que sur Instagram, Facebook et une fiche Google sans aucun avis. Il n'y a **aucun signal de tiers** : pas un annuaire, pas un article, pas un avis client public. Pour du référencement local, c'est le trou le plus béant du dispositif.

---

## 2. AUDIT DU SITE

### 2.1 Verdict général : le site n'est PAS le problème

C'est la conclusion la plus contre-intuitive de cet audit, et il faut la dire clairement pour éviter de dépenser du temps là où il n'y en a pas besoin. **Le SEO on-page est déjà proche de l'état de l'art.** Le brief laissait entendre qu'il fallait auditer un site amateur ; ce n'est pas ce que j'ai trouvé.

### 2.2 Balises title et meta description — toutes présentes et localisées **[V]**

| Page | Title (longueur) | Meta description |
|---|---|---|
| `/` | Voiture de mariage en 2CV à La Réunion \| Une 2CV, mille histoires (65c) | 160c |
| `/mariage` | Voiture de mariage à La Réunion \| Une 2CV, mille histoires (58c) | 170c |
| `/tarifs` | Tarifs 2CV à La Réunion — mariage & balade \| … (69c) | 151c |
| `/balades` | Balades en 2CV à La Réunion \| … (54c) | 147c |
| `/location-2cv-reunion` | Location de 2CV à La Réunion \| … (55c) | 148c |
| `/evjf-evjg` | EVJF & EVJG en 2CV à La Réunion \| … (58c) | 152c |
| `/shooting-evenements` | 2CV pour shooting & tournage à La Réunion \| … (68c) | 151c |
| `/rosalie-et-soizig` | Rosalie & Soizig, nos 2CV de collection \| … (66c) | 150c |
| `/histoires` | Histoires de mariages en 2CV à La Réunion \| … (68c) | 150c |
| `/faq` | FAQ — 2CV mariage & balades à La Réunion \| … (67c) | 157c |
| `/contact` | Contact — … \| 2CV avec chauffeur à La Réunion (68c) | 165c |

Longueurs dans les clous (50–70c / 130–170c), un H1 unique par page, canoniques absolues et correctes partout. Les requêtes locales visées sont bien couvertes : « voiture de mariage La Réunion », « location 2CV Réunion », « balade 2CV Réunion » ont chacune leur page dédiée. **Rien à corriger ici.**

*Réserve honnête :* `404.html` n'a pas de canonique — c'est normal et sans impact.

### 2.3 Données structurées Schema.org — le « quick win majeur » n'en est pas un **[V]**

Contrairement à l'hypothèse du brief, le balisage est **déjà en place et riche** :

| Page | Types JSON-LD |
|---|---|
| `/` | `LocalBusiness` + `WebSite` |
| `/mariage`, `/balades`, `/evjf-evjg`, `/shooting-evenements` | `Service` + `BreadcrumbList` |
| `/location-2cv-reunion` | `Service` + `FAQPage` + `BreadcrumbList` |
| `/faq` | `FAQPage` (15 questions) + `BreadcrumbList` |
| `/tarifs` | `OfferCatalog` + `BreadcrumbList` |
| `/rosalie-et-soizig` | `BreadcrumbList` + `Vehicle` ×2 |
| `/histoires` | `Article` + `BreadcrumbList` |

Le `LocalBusiness` d'accueil est complet : téléphone, email, `geo` (-21.1703, 55.2884), `openingHoursSpecification` 7j/7, `priceRange` « 125 € - 550 € », `areaServed` sur 14 communes + l'île, `makesOffer` avec prix planchers, `sameAs` vers Instagram/Facebook/Google Maps, `legalName` « Association Collectif Ensemble ».

**La seule vraie lacune :** `AggregateRating`, `Review` et `Product` sont **absents de toutes les pages** **[V]**. C'est le balisage qui déclenche les étoiles dans les résultats Google. Mais — point crucial — **on ne peut pas le poser légitimement tant qu'il n'y a pas d'avis réels**. Le blocage n'est pas technique, il est en amont : **il n'existe aucun avis client public**. Poser un `AggregateRating` sans avis vérifiables est une violation des règles Google et expose à une pénalité manuelle. La solution est de collecter des avis, pas d'ajouter une balise.

### 2.4 Couverture géographique — bonne à l'échelle communale, absente à l'échelle micro **[V]**

Occurrences tous fichiers confondus : Saint-Leu 35 · 974 35 · Ouest 22 · Saint-Gilles 10 · Saint-Paul 10 · La Saline 8 · Boucan 2 · Hermitage 2.

**Manques réels :**
- **« Piton Saint-Leu » : 0 occurrence** alors que c'est le lieu d'implantation déclaré du porteur **[V]**
- « L'Ermitage » (graphie locale usuelle) : 0 ; seul « Hermitage » apparaît 2 fois
- Cilaos : 0, Salazie : 0 — alors qu'un post Facebook de la marque évoque explicitement un mariage à Cilaos **[V]**

Les 14 communes du `areaServed` sont bien citées, donc la couverture départementale est correcte. Ce qui manque, ce sont les **micro-zones à intention de mariage** (L'Ermitage, Boucan Canot, Cilaos, les domaines de réception).

### 2.5 Prix, CTA, contact — tous présents **[V]**

- **Prix affichés** : mariage 350 € (Ouest), 450 € (Sud/Nord), 550 € (Est) ; balade 125 € (~2 h). Carburant, déplacement et chauffeur inclus. Zonage tarifaire explicite par communes.
- **Téléphone cliquable** : `tel:+262693828108` sur toutes les pages
- **WhatsApp** : `https://wa.me/262693828108?text=…` avec message pré-rempli, jusqu'à **11 occurrences** sur `/balades`
- **Email** : `mailto:asso.collectif.ensemble@gmail.com`
- **Formulaire** : sur `/` et `/contact`, 6 champs, POST vers **`https://formsubmit.co/e5f3ef62b92b78601726c3d4f38d3ade`**, page de confirmation `/merci`

> **Point de fragilité à vérifier :** le formulaire dépend d'un service tiers gratuit (formsubmit.co). Rien ne prouve qu'il fonctionne encore. **[NV]** — il faut faire un test d'envoi réel. Un formulaire silencieusement cassé sur un site à 0 trafic est indétectable et coûterait chaque demande entrante.

### 2.6 robots.txt et sitemap.xml — corrects **[V]**

`robots.txt` : `Allow: /`, désindexe proprement `/DESIGN.md`, `/.claude/`, `/.impeccable/`, déclare le sitemap. Correct.

`sitemap.xml` : 11 URL, absolues, extensionless (cohérentes avec les canoniques), avec `lastmod` 2026-08-03. Correct.
*Détail cosmétique :* la dernière entrée (`location-2cv-reunion`) est la seule à porter `changefreq`/`priority` et n'est pas indentée comme les autres — sans aucun impact SEO (Google ignore ces deux balises).

### 2.7 Performance mobile — bonne **[V]**

PageSpeed Insights, `/mariage`, mobile : **score performance 91/100**. LCP 2,9 s · TBT 20 ms · CLS 0 · FCP 2,0 s · Speed Index 4,5 s.
**Aucune donnée terrain (CrUX)** : pas assez d'utilisateurs réels — cohérent avec un trafic nul.
Le LCP labo à 2,9 s est le seul point perfectible (seuil « bon » = 2,5 s), mais sur une connexion mobile réunionnaise réelle c'est acceptable. **Ce n'est pas une priorité.**

### 2.8 Indexation — le vrai problème : le site vient de naître **[V]**

| Mesure | Valeur |
|---|---|
| Sitemap soumis le | **2026-08-03** (il y a **5 jours**) |
| URL soumises | 11 |
| Dernier téléchargement du sitemap par Google | 2026-08-06 |
| Erreurs / avertissements sitemap | 0 / 0 |
| Inspection de `/` | **PASS — « Submitted and indexed »**, dernier crawl 2026-08-03, crawlé en **MOBILE**, canonique retenue = canonique déclarée |
| **URL référentes connues** | **1** |
| **Clics / impressions sur 90 jours** | **AUCUNE LIGNE — 0 clic, 0 impression** |
| URL réellement remontées en `site:` | **2 sur 11** (`/` et `/mariage`) |

**Diagnostic honnête :** il n'y a pas de « problème SEO » à réparer. Le site a **5 jours d'existence** dans Google. L'accueil est indexé, ce qui est le signe que tout fonctionne. Le reste des pages est en file d'attente normale. Attendre 4 à 8 semaines est le comportement attendu — **[E]**.

Le chiffre qui doit alerter est ailleurs : **« Referring URLs known: 1 »**. Le site n'a quasiment **aucun lien entrant**. C'est ça qui va plafonner l'indexation et le classement, pas la technique. Et c'est exactement ce que révèle la section 1.2 : aucun annuaire, aucune presse, aucun partenaire ne pointe vers le site.

### 2.9 Incohérence NAP à corriger **[V]**

| Source | Code postal |
|---|---|
| Schema.org `LocalBusiness` du site | **97436** |
| Fiche Google Business Profile | **97424** |

97436 = Saint-Leu centre ; 97424 = Piton Saint-Leu. La cohérence Nom-Adresse-Téléphone est un facteur direct de référencement local. **Les deux doivent dire la même chose**, et ce doit être l'adresse réelle (Piton Saint-Leu, donc 97424 selon la fiche Google). Le nom diffère aussi (« Une 2CV, mille histoires 🌿 » avec emoji sur Google vs sans emoji dans le schema).

---

## 3. AUDIT DES RÉSEAUX SOCIAUX

### 3.1 Limite d'accès à déclarer franchement

Instagram et Facebook **bloquent le scraping** (Firecrawl refuse explicitement Instagram ; Facebook est derrière un mur de connexion). Je n'ai donc **pas pu vérifier directement** les bios, boutons de contact, fréquences de publication ni les compteurs à jour. Les éléments ci-dessous viennent d'**extraits de résultats de recherche**, qui peuvent être datés. **Ils doivent être reconfirmés à l'œil sur les comptes.**

### 3.2 Instagram — `@une2cv.millehistoires`

- **Abonnés : 221** · **Abonnements : 84** — **[V via extrait de recherche, non revérifié en direct, susceptible d'être daté]**
- Bio (extrait) : « NOUVEAU à la RÉUNION 🏝️ Balades • Spectacles • Mariages — Chaque trajet devient un… » (tronqué)
- Contenu actif : plusieurs Reels identifiés, dont un daté du **4 août 2026** (« 31 Juillet — Coralie & Fabien »). **Le compte publie et est vivant** **[V]**
- La marque est reprise par des tiers : un compte de mariage a interviewé Jonathan (Reel `DUnrq7uEWb3`), un compte de bons plans l'a taguée sur TikTok. **Il y a un début de bouche-à-oreille.**
- Lien en bio, statut de compte professionnel, boutons de contact/réservation : **[NV]**

### 3.3 Facebook — `facebook.com/profile.php?id=61586545132399`

- Page active : publie des vidéos (ex. « Un moment hors du temps au domaine des 1000 coco »), utilise `#mariage974` **[V]**
- Présente dans des groupes locaux à forte intention : **« Pro du Mariage et Événementiel 974 »** (post de janvier sur un mariage à Cilaos) **[V]** — c'est un excellent réflexe déjà en place
- Nombre d'abonnés, bio, bouton de contact : **[NV]**

### 3.4 Cohérence de marque — un défaut structurel visible

| Plateforme | Nom affiché |
|---|---|
| Site / Schema | Une 2CV, mille histoires |
| Instagram | Une 2CV • mille histoires (handle `une2cv.millehistoires`) |
| Facebook | Une 2CV, mille histoires |
| Google Business | Une 2CV, mille histoires 🌿 |

Le séparateur change (virgule / point médian / emoji). C'est mineur pour un humain, mais ça disperse les signaux d'entité pour Google.

**Le vrai défaut est ailleurs : l'URL Facebook.** `facebook.com/profile.php?id=61586545132399` est une URL brute, impossible à dicter, à imprimer sur une carte ou à retenir. **Aucun nom d'utilisateur personnalisé n'a été défini.** C'est corrigeable en 10 minutes.

**Positionnement incohérent entre canaux :** la bio Instagram annonce « Balades • Spectacles • Mariages » et Google classe l'activité en « agence de visites touristiques », alors que le site est massivement construit autour du **mariage** (page mariage, tarifs mariage, EVJF/EVJG, histoires de mariages). Les canaux ne racontent pas la même activité.

---

## 4. DIAGNOSTIC MARIAGES.NET — le point central

### 4.1 Constat factuel de départ **[V]**

J'ai scrapé intégralement la catégorie `https://www.mariages.net/voiture-mariage/la-reunion` :

- La page annonce **21 résultats**, tous affichés sur une seule page.
- Liste complète : RM Location Prestige (Saint-Paul, 4.8/10 avis), Sea Cox & Sun (Saint-Pierre, 5/22), Saïd Boudriou (Saint-Leu, 0), Lebon Transport 974 (Saint-Pierre, 0), ConfortVTC (Saint-Leu, 0), AGAT Prestige (La Saline, 5/20), Diamond's Cars Location (Saint-André, 5/1), Luxe Car Réunion (Saint-Joseph, 5/2), Saveur Event (Sainte-Marie, 0), Tessa Transport (Le Port, 0), SB SUD VTC EI (Petite-Île, 0), LDA Wedding (Sainte-Marie, 0), Caro Island (Saint-Leu, 0), Prestige VTC (Sainte Clotilde, 0), Combi Show (Saint-Paul, 0), AKL Location (Saint-André, 0), EVN Réunion Limousine (La Possession, 0), Les Authentiques (Petite-Île, 0), Run Car Events (Le Port, 0), Montransport.re (Saint-Denis, 0), **Bat Kare Méhari 2CV (Saint-Louis, 0 avis)**.
- **« Une 2CV, mille histoires » n'y figure pas.** Confirmé aussi par `site:mariages.net`.

Trois enseignements immédiats :

1. **La catégorie existe et le territoire existe.** « Voiture mariage » est une catégorie officielle du formulaire d'inscription, et « La Réunion » figure dans la liste des départements. **L'hypothèse « catégorie inexistante » est éliminée.** **[V]**
2. **La catégorie n'est pas saturée** — 21 prestataires pour tout un département, dont **15 avec 0 avis**. **L'hypothèse « catégorie saturée » est éliminée.** **[V]**
3. **Un concurrent frontal existe déjà : « Bat Kare Méhari 2CV »** (Saint-Louis), positionné sur exactement le même imaginaire 2CV/Méhari, avec des avis clients rédigés. C'est le concurrent à surveiller.

### 4.2 La question décisive : un profil gratuit est-il réellement affiché ?

**Réponse : OUI, sans ambiguïté.** **[V]**

Preuve directe : sur les 21 prestataires affichés, **15 ont 0 avis** et plusieurs sont des micro-structures (« SB SUD VTC EI », « Saïd Boudriou »). Un annuaire qui n'afficherait que les abonnés payants ne présenterait pas 15 fiches vides pour un département d'outre-mer. **Les profils gratuits sont bien listés et visibles.**

Ce que l'abonnement achète, c'est la **position**, pas l'existence. La page officielle des Packs Premium l'écrit noir sur blanc **[V, cité verbatim]** :

- **Pack Top Gold** — « Apparaissez à partir de la **1ère position** dans les résultats de recherche » · « Position garantie sur la **première page** »
- **Pack Top Silver** — « Apparaissez à partir de la **13ème position** » · « Position garantie sur la **première page** »
- **Pack Premium** — « Apparaissez à partir de la **22ème position** »
- **Pack Start** — « **Testez** les **fonctionnalités basiques** · Recevez des demandes de couples par message et répondez-leur via Mariages.net »

Les autres avantages payants : vitrine sans publicité des concurrents, **accès au numéro de téléphone et à l'e-mail des couples**, assistance téléphonique, formation « Campus ».

**Lecture stratégique — et c'est une bonne nouvelle spécifique à La Réunion :** le plancher « 22ème position » du Pack Premium serait rédhibitoire dans un département métropolitain à 400 prestataires. Ici, **la catégorie entière ne compte que 21 fiches sur une seule page**. Un profil gratuit atterrit donc en bas de la première page — visible sans payer un centime. **[E, déduction directe des chiffres vérifiés]**

**Conclusion nette : l'absence de la fiche ne s'explique PAS par le fait qu'elle soit gratuite.** Il faut chercher ailleurs.

### 4.3 (a) Diagnostic hiérarchisé des causes probables

Je n'ai pas accès à l'espace pro du compte : je ne peux donc pas trancher entre ces causes, seulement les ordonner par vraisemblance. **[E]**

**Cause n°1 — Le profil n'a jamais été soumis à validation (probabilité forte).**
C'est de loin l'explication la plus fréquente. Le tunnel d'inscription de Mariages.net est long et sauvegarde en brouillon. Une fiche « créée » reste en statut *brouillon / non publiée* tant que l'ultime bouton de soumission n'a pas été actionné. Le porteur croit sincèrement avoir terminé. **Symptôme distinctif :** en se connectant à l'espace pro, un bandeau ou un pourcentage de complétion est affiché.

**Cause n°2 — Profil incomplet sous le seuil de publication (probabilité forte).**
Mariages.net exige un minimum de contenu avant publication : photos, description, catégorie, zone d'intervention, coordonnées. Tant que le seuil n'est pas atteint, la fiche reste invisible. **[E — je n'ai pas pu vérifier les seuils numériques exacts : ils ne sont pas publiés en clair sur le site public, ils apparaissent dans l'espace pro connecté.]** Ne pas propager de chiffre inventé ici.

**Cause n°3 — Validation manuelle encore en attente (probabilité moyenne).**
Les mentions légales confirment que la plateforme exerce un contrôle discrétionnaire **[V, verbatim]** : « Mariages.net se réserve le droit, sans besoin de préavis et à tout moment, de refuser l'accès au Site concernant les Utilisateurs enfreignant une de ces Mentions Légales ou Conditions Particulières qui leur sont applicables ou qui, de l'avis discrétionnaire de Mariages.net, n'utilisent pas correctement le Site Web ». **Le délai typique de modération n'est documenté nulle part publiquement — [NV].** Ne pas annoncer « 48 h » ou « 5 jours » : ce serait inventé.

**Cause n°4 — Vérification d'identité / SIRET non aboutie (probabilité moyenne).**
C'est le point le plus spécifique à ce dossier, et il mérite une attention particulière. La structure est une **association loi 1901** (RNA W122009051), dont l'objet déclaré est « favoriser, développer et promouvoir la création artistique, le bien-être et les arts du spectacle vivants » **[V]** — un objet **artistique, sans rapport avec le transport de personnes**. Le brief indique que l'auto-entreprise et la licence VTC sont « en cours ».

Une plateforme commerciale qui demande un SIRET pour une catégorie « Voiture mariage » peut légitimement bloquer un dossier où : soit le SIRET fourni est celui d'une association dont l'objet ne couvre pas l'activité, soit aucun SIRET valide n'est encore disponible, soit le nom commercial (« Une 2CV, mille histoires ») ne correspond à aucune entité juridique enregistrée. **C'est la cause la plus susceptible de produire un blocage durable et silencieux** — et celle qui ne se résoudra pas toute seule.

**Cause n°5 — Mauvaise catégorie ou mauvais département saisis (probabilité faible).**
La fiche pourrait exister sous une autre catégorie (« Animation mariage », « Organisation mariage ») ou un autre département. Vérifiable en 2 minutes depuis l'espace pro.

**Cause écartée — offre gratuite :** démontrée fausse en 4.2.
**Cause écartée — catégorie inexistante ou saturée :** démontrée fausse en 4.1.

### 4.4 (b) Procédure exacte de mise en ligne, pas à pas

1. **Se connecter à l'espace pro** : `https://www.mariages.net/emp-Acceso.php` (page « Accès entreprises », qui sert à la fois d'inscription et de connexion) **[V]**. Utiliser l'adresse e-mail employée à la création. En cas d'oubli, passer par la récupération de mot de passe **avant** de créer un second compte — un doublon compliquerait le dossier.
2. **Identifier le statut réel de la fiche.** Chercher la mention de statut (brouillon / en attente de validation / publiée) et l'indicateur de complétion. **C'est cette information qui tranche entre les causes 1, 2 et 3.** Tout le reste en découle.
3. **Vérifier catégorie et zone** : catégorie **« Voiture mariage »**, département **« La Réunion »** (tous deux confirmés présents dans le formulaire officiel **[V]**).
4. **Compléter la fiche à 100 %** : description longue, galerie photo fournie (les visuels existent déjà : Rosalie et Soizig, couple au coucher de soleil, intérieur, décoration florale), grille tarifaire (350/450/550 € mariage, 125 € balade), zone d'intervention, coordonnées, lien vers `https://une2cvmillehistoires.re/`.
5. **Régler la question juridique en amont** si elle bloque : fournir un SIRET dont l'activité couvre le transport de personnes / la prestation de mariage. Si l'auto-entreprise et la licence VTC ne sont pas finalisées, **c'est le préalable, pas une formalité annexe.**
6. **Soumettre explicitement à publication** et noter la date de soumission.
7. **Si rien ne bouge sous ~7 jours ouvrés**, relancer le support (§4.5) en demandant explicitement : *« Quel est le statut de ma vitrine et que manque-t-il pour sa publication ? »*
8. **Contrôler le résultat** en naviguant en navigation privée sur `https://www.mariages.net/voiture-mariage/la-reunion` et en vérifiant que la fiche apparaît parmi les résultats.

### 4.5 (c) Coordonnées du support Mariages.net

**Attention — un piège documenté :** une première extraction automatique m'a retourné une adresse `contact@mariages.net` et une URL `https://www.mariages.net/contact.php`. **J'ai vérifié : `contact.php` renvoie une erreur 404 « Page non trouvée »** **[V]**. Ces coordonnées étaient une hallucination de l'outil d'extraction. Je les signale pour qu'elles ne soient pas réutilisées.

**Coordonnées réellement vérifiées :**

| Canal | Coordonnée | Source |
|---|---|---|
| **Téléphone** | **(+33) 1 73 06 86 89** | **[V]** Mentions légales de Mariages.net |
| **Espace pro (inscription + connexion)** | `https://www.mariages.net/emp-Acceso.php` | **[V]** |
| **Formulaire commercial** | Formulaire en bas de `https://www.mariages.net/emp-AccesoPremium.php` — « Remplissez le formulaire et nous vous contacterons au plus vite » (nom, e-mail, téléphone, entreprise, catégorie, département) | **[V]** |
| **Entité juridique** | **Wedding Planner, S.L.U.**, C/ Pau Claris, 89, Bajos, 08010 Barcelone, Espagne | **[V]** |
| **Signalement / centre juridique** | `https://www.theknotww.com/legalhub/fr/reporting/` | **[V]** |
| Application pro | « Mariages.net pour l'entreprise » (iOS / Android) | **[V]** |

`info@mariages.net` apparaît comme e-mail de support sur la fiche Google Play de l'application pro **[E — non confirmé sur le site officiel]**.

**Recommandation :** privilégier le **téléphone (+33 1 73 06 86 89)**. C'est le canal vérifié le plus direct, et un appel tranche en quelques minutes une question de statut de fiche qui traînerait des semaines par e-mail. Le formulaire de la page Premium est traité par l'équipe commerciale : il obtient une réponse rapide, mais dans une logique de vente d'abonnement.

### 4.6 (d) Checklist d'optimisation du profil une fois actif

- [ ] **Catégorie principale « Voiture mariage » + département La Réunion**
- [ ] **Nom exact** « Une 2CV, mille histoires » — identique au site, à Google et aux réseaux
- [ ] **15–25 photos minimum**, horizontales, haute définition, sans sous-titres incrustés. Mettre en avant la capote entièrement ouvrante (argument différenciant réel) et les mariés en situation
- [ ] **Photo de couverture** : la plus forte émotionnellement, pas une photo de véhicule à l'arrêt
- [ ] **Description longue** reprenant les mots-clés des pages du site (« 2CV de collection », « chauffeur VTC agréé », « Ouest », « Saint-Gilles », « Saint-Leu », « cortège », « sortie de cérémonie »)
- [ ] **Tarifs renseignés** (350/450/550 € et 125 €) — la transparence tarifaire est déjà la force du site, elle filtre les demandes non qualifiées
- [ ] **Zone d'intervention** : toute l'île, avec le zonage tarifaire expliqué
- [ ] **Deux véhicules distingués** : Rosalie (1983) et Soizig (1990) — le convoi de deux voitures est un argument unique pour les EVJF/EVJG et les grandes noces
- [ ] **Lien vers le site** `https://une2cvmillehistoires.re/` — **au passage, c'est un lien entrant, et le site n'en a qu'un seul aujourd'hui**
- [ ] **FAQ de la fiche** alimentée depuis les 15 questions déjà rédigées sur `/faq`
- [ ] **Demander un avis à chaque couple servi**, dès le lendemain du mariage. Sur les 21 prestataires du département, **15 ont zéro avis** : 3 à 5 avis suffisent à passer devant la plupart d'entre eux
- [ ] **Répondre publiquement à chaque avis** (la plateforme l'autorise et l'affiche sous l'avis)
- [ ] **Délai de réponse aux demandes < 24 h** : les annuaires nuptiaux valorisent la réactivité dans leur classement **[E]**
- [ ] **Vidéos** : la marque en produit déjà pour Instagram et Facebook, les réutiliser

### 4.7 (e) Tarifs réels d'un abonnement pro

**Aucun tarif n'est publié publiquement par Mariages.net.** **[V]** — la page des Packs Premium détaille les quatre formules et leurs avantages mais **n'affiche aucun prix** : elle renvoie systématiquement vers un formulaire de rappel commercial. Les prix sont donc négociés au cas par cas selon la catégorie et le département.

Ordres de grandeur trouvés dans des témoignages publics de professionnels, **[E — à traiter comme des indications, non comme des tarifs officiels, et invérifiables]** :
- Un article de conseil aux pros du mariage évoque « entre 1 000 et 1 500 € par an pour un abonnement premium »
- Un forum de consommateurs mentionne « ~1 700 € » pour un abonnement premium
- Une vidéo de retour d'expérience affiche « 2 400 € » dans son titre

Ces montants concernent des départements métropolitains à forte concurrence. **Ils ne sont pas transposables à La Réunion**, où la catégorie compte 21 prestataires.

**Recommandation ferme : ne rien payer pour l'instant.** Publier la fiche gratuite, collecter 3 à 5 avis, mesurer les demandes entrantes pendant une saison. Dans une catégorie à 21 fiches dont 15 sans avis, la gratuité bien exploitée bat l'abonnement mal exploité. Les retours publics de professionnels sur la rentabilité de ces abonnements sont d'ailleurs majoritairement négatifs **[V — Trustpilot, forum Que Choisir, témoignages vidéo]**. À revoir seulement si le volume de demandes le justifie.

---

## 5. QUICK WINS — 10 actions à fort impact, < 2 h chacune

Classées par ratio impact/effort décroissant.

| # | Action | Effort | Impact | Justification |
|---|---|---|---|---|
| **1** | **Débloquer la fiche Mariages.net** : se connecter à l'espace pro, lire le statut réel, compléter, soumettre ; appeler le **(+33) 1 73 06 86 89** si blocage | **1 h** | **FORT** | Catégorie non saturée (21 fiches), 15 concurrents à 0 avis, profils gratuits réellement affichés. C'est le canal d'acquisition à intention d'achat la plus haute, et il est à portée immédiate |
| **2** | **Demander un avis Google aux clients déjà servis** (Coralie & Fabien du 31 juillet, mariage de Cilaos, etc.) via un lien d'avis court envoyé par WhatsApp | **1 h** | **FORT** | La fiche Google est revendiquée mais à **0 avis**. C'est le facteur n°1 du référencement local et le principal frein à la conversion. Des clients satisfaits existent déjà — il suffit de demander |
| **3** | **Corriger l'incohérence NAP** : aligner le code postal (97436 dans le schema vs 97424 sur Google) et le nom exact sur les 4 canaux | **30 min** | **FORT** | La cohérence NAP est un critère direct du référencement local. Incohérence actuelle vérifiée, correction triviale |
| **4** | **Ajouter une catégorie mariage à la fiche Google** (aujourd'hui : « Sightseeing tour agency ») et compléter photos, horaires, prestations, zone | **1 h** | **FORT** | La catégorie actuelle ne correspond pas à l'activité principale du site. Google ne peut pas faire remonter la fiche sur « voiture mariage Réunion » avec une catégorie « visites touristiques » |
| **5** | **Définir un nom d'utilisateur Facebook** (`facebook.com/une2cvmillehistoires`) à la place de `profile.php?id=61586545132399` | **10 min** | **MOYEN** | URL actuelle indictable et non mémorisable. 10 minutes pour un actif de marque permanent |
| **6** | **Tester le formulaire de contact de bout en bout** (envoi réel depuis mobile, vérification de réception, contrôle de `/merci`) | **20 min** | **FORT** | Le formulaire dépend d'un tiers gratuit (formsubmit.co) et n'a jamais été vérifié. Un formulaire cassé sur un site à 0 trafic est invisible — et chaque demande perdue est un mariage perdu |
| **7** | **S'inscrire dans 3–5 annuaires locaux gratuits** (annuaires mariage 974, offices de tourisme de l'Ouest, annuaires d'associations) | **1 h 30** | **FORT** | Search Console ne connaît **qu'une seule URL référente**. C'est le plafond structurel de l'indexation et du classement. Chaque inscription est un lien entrant et une citation NAP |
| **8** | **Ajouter les micro-zones manquantes** au contenu : « Piton Saint-Leu » (0 occurrence), « L'Ermitage », « Boucan Canot », « Cilaos », noms des domaines de réception | **1 h 30** | **MOYEN** | Le maillage communal est bon, la granularité fine manque. Ce sont des requêtes à faible volume mais à très forte intention, sans concurrence |
| **9** | **Aligner le discours entre canaux** : la bio Instagram annonce « Balades • Spectacles • Mariages », le site est centré mariage. Réécrire bio + lien en bio vers `/mariage` ou `/tarifs` | **30 min** | **MOYEN** | 221 abonnés déjà acquis et un compte vivant, mais l'entonnoir ne mène nulle part de précis. Diriger le trafic social vers la page qui convertit |
| **10** | **Publier une première « histoire » complète** sur `/histoires` (un vrai mariage, avec lieu, prestataires cités et liens) | **2 h** | **MOYEN** | La page existe avec un balisage `Article` mais a besoin de contenu réel. Citer photographe, fleuriste et domaine crée des occasions de liens réciproques — la réponse directe au problème du lien entrant unique |

**Explicitement NON recommandé :** ajouter un balisage `AggregateRating` sans avis réels (violation des règles Google, risque de pénalité manuelle) ; payer un abonnement Mariages.net avant d'avoir testé la fiche gratuite ; refaire le site ou optimiser la performance (91/100, ce n'est pas là que se joue la partie).

---

## 6. SYNTHÈSE DU DIAGNOSTIC

**Ce qui va bien — et qu'il ne faut pas toucher :** le site est techniquement excellent. Titles, meta descriptions, canoniques, Schema.org riche (LocalBusiness, Service, FAQPage, OfferCatalog, Vehicle, BreadcrumbList), prix affichés, WhatsApp et téléphone cliquables partout, robots.txt et sitemap corrects, 91/100 en performance mobile. Le brief anticipait un site à corriger ; il n'y a presque rien à y corriger.

**Le vrai diagnostic :** le problème n'est pas la qualité du site, c'est qu'**il n'existe pour personne**. Cinq jours d'indexation, **une seule URL référente**, **zéro impression** sur 90 jours, **zéro avis** sur Google, **aucune présence** dans le moindre annuaire, aucune fiche Mariages.net en ligne. Un site parfait sans signaux externes reste invisible.

**Le levier :** tout se joue hors du site. Avis clients, fiche Mariages.net, annuaires locaux, liens de partenaires. Les actions 1, 2, 4, 6 et 7 traitent ce déficit et coûtent moins d'une journée de travail cumulée.

**Le point de vigilance :** le statut juridique. Une association loi 1901 à objet artistique qui opère une activité de transport de mariage, avec auto-entreprise et licence VTC « en cours », est probablement la cause du blocage silencieux sur Mariages.net — et le sera pour toute plateforme exigeant un SIRET. C'est un préalable, pas un détail administratif.
