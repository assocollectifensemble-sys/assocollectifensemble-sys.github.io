# Journal de l'agence

> Chaque agent ajoute une entrée À LA FIN de sa mission : date, agent, mission,
> livrables (chemins de fichiers), points ouverts. Ordre antichronologique.

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
