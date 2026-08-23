# Journal de l'agence

> Chaque agent ajoute une entrée À LA FIN de sa mission : date, agent, mission,
> livrables (chemins de fichiers), points ouverts. Ordre antichronologique.

## 2026-08-23 — automatisation — playbooks de livraison + machine interne

- Playbooks sous `agence/playbooks/` (un par pack, alignés sur les fiches `agence/offre/` : déroulé jour par jour, checklist, outils, prompts à variables, pièges, critère de « fini ») :
  - `playbook-diagnostic.md` — 1re livraison 2 j → cible 1 j
  - `playbook-facture-electronique.md` — Solo 2 j → 1 j ; Équipe 3,5 j → 2 j (annexe RGPD obligatoire avant reprise des fiches clients)
  - `playbook-presence.md` — 8 j → 4 j (le ÷2 vient du site-mère + gabarits)
  - `playbook-automatisation.md` — 6 j → 3 j (processus suivant même client : 2 j) ; règle : notification d'échec + reprise manuelle documentée sur chaque flux
  - `playbook-video-formation.md` — Format A 4 j → 2 j ; Format B 9 j → 4,5–5 j
- Machine interne sous `agence/machine/` :
  - `crm.md` — 3 tables (pipeline / clients actifs / abonnements + idées d'optimisation), vues, règles de mise à jour, automatisations minimales avec reprise manuelle ; CRM = registre responsable de traitement (renvoi rgpd.md)
  - `rapport-mensuel-modele.md` — 6 sections, ton sans jargon, données à injecter par niveau, prompt de génération, relecture Jon obligatoire (anti-hallucination : comparaison chiffre à chiffre)
  - `sequence-prospection-fe.md` — email + WhatsApp initial, relances J+7 et J+21 (annoncée comme dernière), script d'appel 2 min, règles B2B (identification, STOP → liste Opposé définitive, 3 messages + 1 appel max, pas d'envoi en masse)
  - `routine-hebdo.md` — semaine type à 10 abonnés (~10–11 h/sem d'abonnements, mardi/jeudi terrain sanctuarisés, max 2 chantiers de packs en parallèle) ; ligne rouge écrite : RDV, formations, appels jamais automatisés
- Points ouverts (Jon) : la PA de référence (decisions.md, urgent) bloque la 1re vente du pack FE ET l'outil de facturation récurrente des abonnés ; plateforme de formation de référence à choisir (Format B) ; gabarit d'autorisation droit à l'image à faire valider par l'avocat ; nom d'agence à trancher avant d'envoyer la séquence de prospection (signature des messages).

## 2026-08-23 — web — site vitrine complet de l'agence

- Livrables sous `agence/site/` — statique portable (HTML/CSS/JS, zéro build, zéro
  backend), déployable tel quel sur un dépôt GitHub Pages dédié :
  - `index.html` — promesse (un interlocuteur, 974), cycle 4 temps, références
    Yoga Doula + Croc Parc (prestations seulement, aucun chiffre inventé),
    aperçu des 6 offres avec prix, CTA diagnostic, bandeau échéance facture électronique
  - `offres.html` — 5 packs détaillés (livrables, prix, délais depuis `agence/offre/`),
    passerelle pack→abonnement écrite dans chaque fiche, comparatif des 3 niveaux
    d'abonnement (cartes + tableau), conditions et avantages abonnés, étage 3 sur mesure
  - `facture-electronique.html` — coin d'entrée : compte à rebours J−N vers le
    01/09/2026 (bascule seul en « Obligation en vigueur » après), la loi sans jargon,
    Solo 690 € / Équipe 1 290 €, FAQ reprise des objections, urgence sans catastrophisme
  - `contact.html` — coordonnées en placeholders `[À COMPLÉTER PAR JON]`, formulaire
    **mailto** (aucun serveur), liens tel:/wa.me prêts en commentaires HTML
  - `mentions-legales.html` — squelette complet avec placeholders, en `noindex`
    tant que non complété
  - `assets/` : `tokens.css` (copie de `agence/design/tokens.css`), `site.css`
    (mobile-first, clair+sombre via tokens, focus visibles, tableau scrollable),
    `site.js` (optionnel : année, J−N, composition mailto)
  - `README.md` — modifier, changer le nom de marque (rechercher-remplacer documenté),
    resynchroniser les tokens, déployer sur GitHub Pages + domaine
- Choix notables : identité recommandée « Otonom Digital » incarnée (baseline
  « Installé. Formé. Otonom. »), nom en dur dans le HTML pour le SEO + procédure de
  renommage en 3 chaînes dans le README ; nav sans hamburger (fonctionne sans JS) ;
  une seule touche Braise par écran (règle identite.md) ; JSON-LD LocalBusiness/Service
  avec placeholders ; vendu au résultat — « IA » n'apparaît que dans le nom officiel
  du pack « Diagnostic Digital & IA », jamais en argument de vente ;
  pas de sitemap/robots tant que l'URL définitive n'existe pas ; site 2CV racine intact.
- En attente de Jon : nom définitif (site prêt à renommer), coordonnées (tél/WhatsApp,
  email — y compris `data-mailto` du formulaire), mentions légales (SIREN, statut, TVA,
  hébergeur), décision hébergement (dépôt dédié + domaine .re/.fr recommandés), URL
  définitive à reporter dans les JSON-LD, chiffres/citations clients pour de vraies
  études de cas.

## 2026-08-23 — video — supports formation & vidéo (Temps 2 + moteur commercial)

- Livrables sous `agence/formation/` :
  - `atelier-ia-tpe.md` — micro-atelier commercial « l'IA pour ta TPE » (45 min) : déroulé minuté, 3 démos ancrées 974 (devis artisan, publications commerce, avis Google), plan de 10 slides, script de transition vers le Diagnostic sans forcing (sortie honorable explicite), matériel + plan B hors ligne
  - `trame-formation-outil.md` — trame générique du « Temps 2 : Former » (1–2 h sur poste) : boucle en 4 temps par geste (je montre → tu fais guidé → tu fais seul → validé), variables entre crochets, séquence « erreur volontaire », fiche mémo 1 page, critère d'autonomie mesurable écrit AVANT la session et validé par le dirigeant
  - `formation-croc-parc-modele.md` — déclinaison parc de loisirs (modèle Croc Parc) : sessions courtes 1 h/outil, pédagogie « surveiller et rattraper » pour les automatisations, kit nouvel arrivant (turnover saisonnier) ; inventaire réel des outils = [À DEMANDER À JON] partout où le cerveau ne documente pas les faits
  - `script-video-vitrine.md` — script vidéo 60–90 s (8 blocs : accroche, cycle 4 temps, preuve locale, CTA Diagnostic) + plan de tournage 3 séances et liste de 10 plans de coupe ; tourné en 9:16 + 16:9, sous-titres obligatoires
- Choix notables : le mot « IA » n'est jamais l'argument (une seule occurrence dans le script vidéo) ; hors Qualiopi rappelé en tête de chaque support ; jamais de données/écrans d'un client sans accord écrit (démos = contenus fictifs préparés) ; le critère d'autonomie daté matérialise le passage au Temps 3
- Points ouverts (Jon) : inventaire précis des outils Croc Parc + état des formations déjà faites ; accords écrits Croc Parc / Yoga Doula pour citation et tournage + un chiffre ou une citation défendable (bloc preuve) ; tutoiement ou vouvoiement de la vidéo ; nom de marque (bloque l'écran de fin et les incrustations, pas le tournage)

## 2026-08-23 — juridique — socle documentaire de l'agence

- Livrables sous `agence/juridique/` (tous en-têtés « trame à faire valider par un avocat / expert-comptable ») :
  - `contrat-prestation-cadre.md` — contrat cadre packs one-shot (devis signé > cadre > CGV ; PI cédée après paiement complet ; clause IA ; plafond de responsabilité)
  - `contrat-abonnement.md` — abonnement Pilotage digital 3 niveaux (150/350/750 €, alignés sur l'offre strategie), sans engagement, préavis 1 mois symétrique, pause saisonnière, réversibilité totale en fin de contrat
  - `cgv.md` — CGV B2B ; art. 9 « préparation documentaire » (périmètre du droit, loi 1971) ; alerte rétractation L221-3 (TPE ≤ 5 salariés démarchées hors établissement)
  - `onboarding-client.md` — questionnaire d'entrée (identité, existant, accès, contenus, bloc 5 = déclencheur de l'annexe RGPD)
  - `rgpd.md` — registre art. 30 (volets responsable + sous-traitant) et annexe de sous-traitance art. 28 avec clause IA (no-training, minimisation, supervision humaine)
  - `checklist-lancement.md` — démarches de Jon, vérifiées par WebSearch et sourcées (INPI guichet unique, exonération DOM, RC Pro+cyber, mentions légales, facturation électronique : réception 01/09/2026, émission TPE 01/09/2027)
- Points de vigilance majeurs : inscription plateforme agréée avant le 01/09/2026 (imminent) ; droit de rétractation L221-3 possible sur nos ventes terrain ; taux de cotisations BNC et durée d'exonération DOM à confirmer (sources divergentes) ; plafonds de responsabilité à faire valider
- Points ouverts ajoutés à decisions.md (avocat partenaire, plateforme agréée, RC Pro, paramètres contractuels)

## 2026-08-23 — strategie (+ redaction) — offre commerciale complète

- Livrables sous `agence/offre/` : `pack-diagnostic.md` (590 € déductibles),
  `pack-presence.md` (2 400 €), `pack-facture-electronique.md` (Solo 690 € /
  Équipe 1 290 € — coin d'entrée), `pack-automatisation.md` (1 900 €, suivant
  1 200 €), `pack-video-formation.md` (vidéo dès 900 €, formation dès 2 500 €),
  `abonnement-pilotage.md` (Essentiel 150 / Croissance 350 / Partenaire 750 €/mois,
  sans engagement préavis 1 mois, périmètres inclus/exclus écrits),
  `grille-tarifaire.md` (récap prospect), `argumentaire-general.md` (pitch cycle
  4 temps + 5 objections).
- Choix structurants : prix fermes (fin des fourchettes floues), base ~600 €/jour
  homme réel IA comprise, gamme abonnement en ×2 (150/350/750), mix cible
  5+4+2 abonnés = 3 650 € MRR, avantages abonnés (sur-mesure réservé,
  Automatisation −700 €, Vidéo −10 %), prérequis abonnement = un pack réalisé.
- `cerveau/offre.md` réécrit en synthèse pointant vers les fiches.
- Points ouverts pour Jon : régime TVA/TTC selon statut, validation paiement 3×
  sans frais, chiffres + citations Yoga Doula et Croc Parc, périmètre exact
  Partenaire Croc Parc.

## 2026-08-23 — design — nom de marque + système de design de référence

- 3 directions de nom vérifiées (WebSearch + DNS) : « Zarboutan » (grillée : SAS homonyme
  en conseil/formation à Saint-Paul, zarboutan.re et .fr pris), « L'artisan et son outil »
  (Atelier Digital déjà pris, Comptoir générique, Zoutil ambigu vs Zot Zoutils),
  « Otonom » (apparemment libre : otonom.re ne résout pas, aucun homonyme 974 ;
  marque INPI Innothera limitée à l'orthopédie)
- **Recommandation : « Otonom Digital », usage court « Otonom », domaine otonom.re** —
  Jon tranche (decisions.md mis à jour)
- Système de design complet pour cette direction : palette matière (Sable/Basalte/Vert
  canne/Braise/Curcuma) clair + sombre, contrastes AA/AAA calculés et vérifiés,
  paire Fraunces + Work Sans (Google Fonts), ton visuel (fait / jamais)
- Livrables : `agence/design/noms-de-marque.md`, `agence/design/identite.md`,
  `agence/design/tokens.css` (prêt pour l'agent web, clair + sombre + data-theme)
- Points ouverts : choix du nom par Jon ; validation de l'identité ; avant dépôt du nom
  retenu → recherche d'antériorité INPI classes 35/41/42 + réservation domaine réelle

## 2026-08-23 — orchestrateur — création de l'agence

- Cerveau commun initialisé (`agence/cerveau/`) : contexte, offre, clients, marché, décisions, journal
- Agents définis dans `.claude/agents/` : strategie, redaction, web, design, juridique, automatisation, video, veille-marche
- Skill `/agence` créée (`.claude/skills/agence/`)
- Plan de référence publié en artifact (voir contexte.md)
- Points ouverts : voir decisions.md (nom de marque, statut, hébergement site vitrine)
