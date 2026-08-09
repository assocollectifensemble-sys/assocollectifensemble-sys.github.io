# Scan des tunnels d'inscription — écoles de doula & écoles de yoga périnatal

**Date du scan : 9 août 2026.** Toutes les pages ont été relevées en direct ce jour-là.
Question posée : *les écoles font-elles payer d'abord (scénario A) ou remplir le dossier d'abord (scénario B) ?*

---

## 1. La réponse en une phrase

Le marché se coupe en deux, et **la ligne de partage n'est pas le métier enseigné — c'est le prix et la sélectivité** :

| | Scénario A — paiement d'abord | Scénario B — dossier d'abord |
|---|---|---|
| **Prix typique** | 300 € – 1 500 € | 2 500 € – 6 600 € |
| **Sélection à l'entrée** | aucune | lettre de motivation + entretien |
| **Format** | e-learning, module court, week-end | cursus long, présentiel, promo fermée |
| **Ce qui déclenche** | un bouton « Ajouter au panier » | un formulaire de candidature |
| **Qui valide** | la carte bancaire | l'équipe pédagogique |

En dessous d'environ 1 500 €, la formation est vendue **comme un produit** : on l'achète, point.
Au-dessus d'environ 2 500 €, elle est vendue **comme un cursus** : on candidate, on est reçu, on signe, puis on paie.

**L'École Yoga Doula applique déjà, sans l'avoir formalisé, exactement cette règle :** le Programme Yoga Maternité (1 050 €) est en scénario A pur, la formation Yoga Doula & Yoga Périnatal (3 350 €) est en scénario B. C'est cohérent avec le marché.

---

## 2. Votre processus actuel, relevé pas à pas

### 2.1 Programme Yoga Maternité — 1 050 € — **scénario A**

| # | Étape | URL | Ce qui s'y passe |
|---|---|---|---|
| 1 | Page de vente | `/formation-yoga-maternite/` | Tarif 1 050 €, « 5 fois sans frais — 210 €/mois », mention *Paiement sécurisé via Stripe*. 3 boutons « Je m'inscris ». Un 4ᵉ bouton renvoie à l'ancre `#tarif` |
| 2 | *(optionnel)* | Calendly 20 min | « Je réserve un appel gratuit » — non bloquant |
| 3 | **Empreinte de carte** | `/inscription-yoga-maternite/` | Stripe **SetupIntent** : la carte est enregistrée, **0 € débité**. hCaptcha. Acceptation des CGV. Page en `noindex,nofollow` |
| 4 | Confirmation | `/paiement-enregistre/` | « Aucun débit n'a été effectué aujourd'hui ». Annonce le 1ᵉʳ prélèvement à J+14 |
| 5 | **Dossier d'inscription** | `/dossier-dinscription/dossier-inscription-pym-formulaire/` | Formulaire multi-étapes, sauvegarde automatique, reprise par email |
| 6 | J+14 | — | 1ᵉʳ prélèvement de 210 €, puis 4 mensualités |
| 7 | Accès | Teachable | « dès lors que votre dossier d'inscription a bien été reçu » |

**Signature de votre tunnel : l'empreinte de carte sans débit.** Personne d'autre dans le scan ne fait ça. Toutes les écoles en scénario A prennent de l'argent réel (acompte ou 1ᵉʳ versement). Vous prenez un engagement sans prendre d'argent. C'est la version la plus douce du scénario A qui existe sur ce marché.

### 2.2 Formation Yoga Doula & Yoga Périnatal — 3 350 € (tarif Hirondelle) — **scénario B de fait**

Aucun bouton d'achat en ligne sur la page. Le bouton « J'en profite » du bloc tarif renvoie vers **Calendly**. Mention : *« nouvelle promo 2027 — inscriptions ouvertes très bientôt »*. Le parcours réel est donc : page → RDV téléphonique → échange → inscription hors ligne.

### 2.3 Trois écarts relevés dans le tunnel PYM

1. **Le dossier n'est pas verrouillé.** Rien n'empêche d'enregistrer sa carte puis de ne jamais remplir le dossier. Les prélèvements démarrent à J+14 quand même ; seul l'accès Teachable est bloqué. Vous pouvez donc facturer quelqu'un dont vous n'avez ni l'adresse, ni le profil, ni les prérequis.
2. **Contradiction entre deux pages.** La FAQ dit *« Dès ton inscription, tu reçois l'accès à la plateforme Teachable »*. La page `/paiement-enregistre/` dit que l'accès arrive *« dès lors que votre dossier a bien été reçu »*. Deux promesses différentes.
3. **La page dossier est indexable.** `/inscription-yoga-maternite/` est bien en `noindex`, mais `/dossier-dinscription/dossier-inscription-pym-formulaire/` est en `index, follow` alors que sa méta-description précise qu'elle est *« réservée aux personnes ayant validé leur pré-inscription »*. À passer en `noindex`.

---

## 3. Le scan — 20 écoles

### 3.1 Écoles de doula

| École | Pays | Prix | Scénario | Séquence exacte |
|---|---|---|---|---|
| **Doula des Lunes** | FR | 3 780 € | **A** | Page tarifs → bouton « S'inscrire » → **checkout Schoolmaker direct** (CB, 5× 780 € ou 7× 570 €). Aucun dossier, aucun entretien. Le paiement comptant passe par un PDF |
| **Institut Doulē** (ex-Quantik) | QC/FR | 4 900 CAD | **A** | « Pour vous inscrire, vous devez le faire en deux étapes » — **étape 1 = paiement de 1 200 CAD en checkout** qui « garantit votre inscription » ; étape 2 = solde avant la rentrée. Aucun prérequis, aucune candidature |
| **DONA International** | US | variable | **A** | Inscription à l'atelier chez le formateur (paiement en ligne), puis achat du *certification packet* dans la boutique DONA |
| **Envol & Matrescence — Doula 360®** | FR | 4 390 € / 4 690 € | **B** | 1) positionnement en ligne · 2) pré-inscription plateforme · 3) réception dossier par l'assistante · 4) **entretien visio** · 5) signature électronique CGV + contrat · 6) **« une fois le délai légal de rétractation de 15 jours passé, il vous sera demandé de vous acquitter de l'acompte et des frais d'inscription »** · 7) démarrage si seuil atteint |
| **Centre Galanthis** | FR | 4 929 € (+185 € dossier +15 € adhésion) | **B** | 1) lettre de motivation PDF + photo d'identité · 2) formulaire en ligne · 3) email de confirmation avec lien de RDV · 4) **RDV téléphonique de validation** · 5) traitement par ordre d'arrivée · puis paiement |
| **Doulam** | FR | 3 400 € | **B** | 1) *(recommandé)* JPO visio gratuite · 2) pré-inscription en ligne · 3) **entretien individuel avec une référente** · 4) validation du dossier + envoi du contrat · 5) **acompte de réservation**, puis paiement en 8× |
| **Matrëa** (Formation Doula & Naissance) | CH | 6 625 CHF | **B** | 1) formulaire + **lettre de motivation** · 2) contact téléphonique / entretien sous 15 j · 3) **« une fois votre candidature validée »**, signature du contrat · 4) **acompte 580 CHF** — *« c'est le versement de ton acompte qui valide fermement ton inscription »* |
| **Formation Doula Suisse** | CH | — | **B** | Le plus formel du scan : formulaire d'admission PDF + photo + **lettre de motivation** + **scan du plus haut diplôme** → envoi postal ou mail → **entretien avec Elena** → sélection → « paquet d'acceptation » en juillet → règlement → signature du contrat → accès plateforme en septembre |
| **Mère et Monde** | QC | 1 450 – 1 950 $ CAD | **B** | Demande d'inscription en ligne, analyse de dossier / reconnaissance des acquis facturée 90–150 $ |

### 3.2 Écoles de yoga prénatal & périnatal

| École | Pays | Prix | Scénario | Séquence exacte |
|---|---|---|---|---|
| **Institut de Gasquet** | FR | 550 € | **A** | Fiche **produit Shopify**. On choisit la date, le type de paiement = « Acompte », on **ajoute 165 € au panier**. « Inscription possible jusqu'au dernier moment ». Les prérequis sont « vérifiés à l'inscription », donc après |
| **Green Yoga** (F.F. Green Yoga®) | FR | — | **A** | Bouton « Je m'inscris » → page `elearning.green-yoga.fr/reglement-ppn-en-ligne/`. Accès « immédiat », « pas de limite de place ». Le RDV découverte existe mais n'est pas bloquant |
| **Prenatal Yoga Center** | US | — | **A** | « Enroll Now » → checkout avec plan en 4 versements. Prérequis 200 h déclaré sur l'honneur |
| **Birthlight** | UK | — | **A** | WooCommerce : « Book a course » → panier → checkout. *« Participants receive access to this online learning component upon purchase »* |
| **Bliss Baby Yoga** | AUS | — | **A** | Inscription en ligne, acompte + plan de paiement |
| **Yoga Montagne** (C. Sigwalt) | FR | 917 € / 1 087 € | **B** | Bouton principal = **« Je demande un dossier de candidature »**. « Contacter l'organisme pour validation des prérequis. **Après acceptation de votre candidature**, vous procédez aux modalités contractuelles (signature du contrat et règlement) » |
| **Sattvic Element** | FR | 1 250 – 1 600 € | **B** | « Le candidat doit remplir un **formulaire de candidature**. Le responsable pédagogique répond par mail **sous quinzaine** ». Paiement en 3× ensuite, intégral avant le début |
| **Māyāshala** | FR | 550 – 690 € | **B** | Les boutons « S'inscrire » sont des **mailto** : on demande le formulaire par email, on le renvoie **signé et paraphé accompagné du justificatif de virement de l'acompte de 250 €**. Dossier et paiement arrivent ensemble |
| **YUJ Paris** | FR | 390 – 490 € | **B** | Site Shopify, mais la formation n'est **pas** un produit : le bouton « Infos & inscription » descend vers un **formulaire de contact**. Aucun panier |
| **Silverlake / Bloom / Bliss Yoga Studios** | US | — | **B** | Modèle américain classique : *application* → *acceptance* → **deposit de 500 $ qui réserve la place** → solde ou plan de paiement |
| **Yoga District** | US | — | **B** | *« Once the application, references, and deposit are received, you'll receive a decision by email »* — dossier + références **et** acompte, décision ensuite |

### 3.3 Le décompte

- **Scénario A pur : 8 écoles** — toutes à moins de ~1 500 €, ou 100 % en ligne sans sélection.
- **Scénario B : 12 écoles** — toutes les formations longues, présentielles, Qualiopi, ou à plus de 2 500 €.
- **Écoles qui prennent une empreinte de carte sans débit : 1.** Vous.

---

## 4. Ce que le scan apprend vraiment

### 4.1 Le scénario B a presque toujours un verrou de paiement à la fin

Ce n'est pas « dossier d'abord, paiement quand vous voulez ». Chez Matrëa c'est écrit noir sur blanc : *« c'est le versement de ton acompte qui valide fermement ton inscription »*. Chez Doulam, « acompte de réservation ». Chez les studios américains, « a 500 $ deposit will reserve your space ».

**La séquence dominante n'est donc ni A ni B, c'est B + acompte :**
candidature → entretien → acceptation → contrat signé → **acompte** → place réservée → solde échelonné.

Le dossier sert à filtrer. L'acompte sert à engager. Les deux sont utilisés, dans cet ordre.

### 4.2 Le scénario A n'est jamais « nu »

Aucune école ne demande une carte avant d'avoir affiché le prix, l'échéancier et les CGV sur la même page. De Gasquet met l'acompte, le solde et l'échéance dans le sélecteur produit. Institut Doulē numérote ses deux paiements. Vous faites la même chose — votre page `/inscription-yoga-maternite/` récapitule « Ce que vous réservez », le total, l'échéancier et la date du 1ᵉʳ prélèvement avant le champ carte. C'est conforme aux meilleures pratiques du groupe A.

### 4.3 L'entretien téléphonique est la vraie frontière

Ce qui distingue les écoles à 4 000 € des écoles à 800 €, ce n'est pas le formulaire, c'est **l'entretien humain obligatoire**. Galanthis, Doulam, Envol, Matrëa, Doula Suisse : tous imposent un échange avant de prendre un centime. Vous proposez un Calendly de 20 min sur les deux formations — mais il est **facultatif** sur le PYM et **la seule porte d'entrée** sur la YD/YP.

### 4.4 Un point de vigilance juridique à faire vérifier

Deux régimes possibles s'appliquent à votre échéancier PYM, et ils ne disent pas la même chose :

- **Vente à distance (art. L221-18 Code de la consommation)** — 14 jours de rétractation. C'est ce que vous appliquez et affichez.
- **Contrat de formation professionnelle (art. L6353-3 à L6353-6 Code du travail)**, qui s'applique si l'École est déclarée comme organisme de formation et que la personne finance sur ses fonds propres : **10 jours** de rétractation, **aucune somme exigible avant leur expiration**, et **maximum 30 % du prix** encaissable à ce moment-là, le solde devant être échelonné au fur et à mesure du déroulement de l'action.

Bonne nouvelle : votre échéancier passe les deux tests. 210 € = 20 % de 1 050 €, donc sous le plafond de 30 %, et le premier prélèvement tombe à J+14, donc après les 10 jours comme après les 14. **À faire confirmer par votre comptable ou votre juriste** — je signale la double lecture, je ne tranche pas le statut de l'École.

C'est d'ailleurs exactement ce qu'Envol & Matrescence applique : *« une fois le délai légal de rétractation passé, il vous sera demandé de vous acquitter de l'acompte »*.

---

## 5. Recommandations

### 5.1 Garder le scénario A sur le Programme Yoga Maternité

À 1 050 €, en hybride, sans prérequis, sans sélection : c'est le bon modèle, et le marché le confirme. De Gasquet (550 €), Green Yoga, Birthlight, Prenatal Yoga Center font tous pareil. Passer en B ajouterait de la friction sur un produit qui n'en a pas besoin, et vous perdriez le principal atout de votre tunnel : **l'inscription se boucle en une session, sans attendre une réponse humaine**.

### 5.2 Mais fermer le trou du dossier

Le problème n'est pas l'ordre A, c'est que le dossier soit *après* et *facultatif*. Trois correctifs, du plus léger au plus lourd :

1. **Un mini-bloc avant la carte** — nom, prénom, email, téléphone, profil en une question (« déjà enseignant·e de yoga ? »), case CGV. Cinq champs, trente secondes. Vous ne prenez plus jamais une empreinte anonyme, et vous gagnez une adresse email exploitable même si la personne abandonne au moment de la carte. **C'est le correctif à faire en premier.**
2. **Une relance automatique** à J+2, J+5 et J+10 tant que le dossier n'est pas complet — avant le premier prélèvement, pas après.
3. **Aligner les deux pages** sur une seule promesse d'accès Teachable (je recommande : « dès réception de votre dossier », qui est la version qui protège l'École).

### 5.3 Garder le scénario B sur la formation Yoga Doula & Yoga Périnatal

À 3 350 €, avec 14 journées résidentielles et un engagement de 12 mois, **aucune** des écoles comparables du scan ne vend en un clic. Toutes filtrent. Votre entrée par Calendly est le bon réflexe — mais elle est aujourd'hui informelle. Deux ajouts qui vous mettraient au niveau de Galanthis et Doulam :

- Un **formulaire de candidature** en amont du RDV (parcours, motivation, disponibilité sur les dates résidentielles). Il vous permet de préparer l'appel au lieu de le découvrir, et de trier par ordre d'arrivée.
- Un **acompte explicite qui réserve la place**, encaissé après l'entretien et la signature. C'est la norme absolue du segment : Matrëa 580 CHF, Galanthis 185 € de frais de dossier, Doulam « acompte de réservation ». Sans lui, vous n'avez aucun engagement ferme avant le démarrage — et sur une promo à places limitées, c'est le seul outil qui empêche les désistements tardifs.

### 5.4 Un avantage à exploiter en argument de vente

**« Aucun débit aujourd'hui »** est votre différenciateur, et il n'est écrit nulle part sur la page de vente `/formation-yoga-maternite/` — seulement sur la page de paiement, c'est-à-dire une fois la décision déjà prise. Toutes les écoles en scénario A demandent de l'argent immédiatement : 165 € chez de Gasquet, 250 € chez Māyāshala, 780 € chez Doula des Lunes, 1 200 CAD chez Institut Doulē.

À côté du prix, sur la page de vente, la phrase à ajouter est :

> **Inscription sans débit immédiat.** Vous enregistrez votre carte, rien n'est prélevé avant 14 jours. Vous gardez votre droit de rétractation entier.

C'est le seul argument du scan que personne d'autre ne peut écrire.

---

## 6. Récapitulatif décisionnel

| Formation | Scénario aujourd'hui | Scénario recommandé | Action |
|---|---|---|---|
| Programme Yoga Maternité — 1 050 € | A pur, dossier optionnel | **A + identification préalable** | Mini-bloc 5 champs avant la carte ; relances ; aligner la promesse Teachable ; `noindex` sur la page dossier |
| Yoga Doula & Yoga Périnatal — 3 350 € | B informel (Calendly seul) | **B + acompte de réservation** | Formulaire de candidature avant le RDV ; acompte après signature |

---

*Sources : pages relevées en direct le 9 août 2026 sur yoga-doula.eu, douladeslunes.com, institutdoule.com (ex-ecolequantik.com), envol-et-matrescence.com, centregalanthis.fr, doulam.com, formation-doula-naissance.ch, doulasuisse.org, mereetmonde.com, dona.org, degasquet.com, green-yoga.fr, yoga-montagne.com, sattvicelement.com, mayashala.com, yujparis.com, birthlight.com, prenatalyogacenter.com, blissyogastudios.org, yogadistrict.com.*
