# CRM léger de l'agence

> Structure du CRM. Version 2026-08-23 (agent automatisation).
> Principe : **l'outil le plus simple qui marche**. Une seule base, 3 tables, des vues.
> Outil recommandé : **Notion** (gratuit, Jon seul, bases liées, rappels) ; Airtable
> convient à l'identique (mêmes colonnes). Un Google Sheets à 3 onglets ferait
> l'affaire au tout début — ne pas monter d'usine.
> Le CRM est la source opérationnelle ; `agence/cerveau/clients.md` reste la fiche
> narrative (études de cas, citations) — voir règles de synchro en bas.

## Table 1 — PIPELINE PROSPECTS

Une ligne = une entreprise prospectée.

| Colonne | Type | Valeurs / règle |
|---|---|---|
| Entreprise | titre | nom commercial |
| Contact | texte | prénom, nom, rôle |
| Tél / WhatsApp | texte | |
| Email | texte | email pro générique de préférence (règle B2B) |
| Commune | sélection | utile pour grouper les tournées terrain |
| Secteur | sélection | artisan / commerce / tourisme / services / bien-être / autre |
| Source | sélection | terrain / recommandation / atelier CCI-CMA / séquence FE / site / autre |
| Statut | sélection | À contacter → Contacté → Échange en cours → RDV fixé → Devis envoyé → **Gagné** / **Perdu** / **Plus tard** / **Opposé (ne plus contacter)** |
| Pack visé | multi-sélection | Diagnostic / FE Solo / FE Équipe / Présence / Automatisation / Vidéo-Formation |
| Prochaine action | texte | TOUJOURS remplie tant que le statut n'est pas final (ex. « relance tél jeudi ») |
| Date prochaine action | date | alimente la vue « Aujourd'hui » |
| Dernier contact | date | |
| Séquence FE | sélection | — / msg1 envoyé / relance1 / relance2 / appel fait / sortie (voir `sequence-prospection-fe.md`) |
| Notes | texte | verbatims, objections entendues, saisonnalité |

**Vues :** « Aujourd'hui » (date prochaine action ≤ aujourd'hui, tri par date) — la seule vue ouverte chaque matin · « Pipeline » (kanban par statut) · « Séquence FE » (filtre séquence ≠ —) · « Par commune » (tournées).

## Table 2 — CLIENTS ACTIFS

Une ligne = un client (lié à sa ligne prospect d'origine).

| Colonne | Type | Valeurs / règle |
|---|---|---|
| Client | titre | |
| Packs réalisés | multi-sélection | + dates |
| Chantier en cours | texte | pack + étape du playbook (ex. « Présence — S2 recette ») |
| Échéances chantier | date | prochaine étape due (recette, formation, point J+30, relance J+45 diagnostic) |
| Abonnement | sélection | — / Essentiel / Croissance / Partenaire |
| Annexe RGPD | case + date | OBLIGATOIRE cochée si données confiées (bloc 5 onboarding) |
| Accès détenus | texte | renvoi vers le tableau d'accès de l'onboarding, jamais de mots de passe ici |
| Anniversaire hébergement | date | relance à M+10 (bascule abonnement ou renouvellement) |
| Idées d'optimisation | relation | vers table 3 |
| Satisfaction / signaux | texte | à chaud après chaque livraison ; signaux de churn (paie en retard, ne répond plus) |

**Vues :** « Chantiers en cours » (échéance croissante) · « Abonnés » (groupé par niveau) · « Sans abonnement » = la liste de développement commercial n°1 (clients pack sans abonnement).

## Table 3 — ABONNEMENTS & IDÉES D'OPTIMISATION

### 3a. Suivi d'abonnement (une ligne par abonné)

| Colonne | Type | Règle |
|---|---|---|
| Abonné | relation | table 2 |
| Niveau / prix | sélection + nombre | 150 / 350 / 750 (ou montant devis Partenaire) |
| Date de début | date | |
| Jour de facturation | nombre | facture mensuelle envoyée ce jour-là |
| Rapport mensuel | sélection | à générer → généré → relu Jon → envoyé (remis à zéro le 1er du mois) |
| Heures consommées ce mois | nombre | modifs site (1 h / 2 h incluses) — non reportables, rappel fiche |
| Pause saisonnière | dates | clause du contrat d'abonnement |
| Préavis reçu | date | si résiliation : dernier mois + entretien de sortie + réversibilité |
| Révision tarifaire | date | possible 1×/an, préavis 2 mois (contrat) |

### 3b. Idées d'optimisation par client (le carburant du cycle « revenir optimiser »)

| Colonne | Type | Règle |
|---|---|---|
| Client | relation | |
| Idée | titre | notée À CHAUD dès qu'elle apparaît (en formation, en rapport, en réunion) |
| Gain estimé | texte | h/mois ou € — même grossier |
| Type | sélection | optimisation incluse abonnement / pack à vendre / sur-mesure |
| Statut | sélection | idée → proposée (dans un rapport mensuel ou une réunion) → acceptée → faite |

Ces idées alimentent : la section « le mois prochain » du rapport mensuel, la réunion mensuelle Partenaire, et le pipeline de packs additionnels (Automatisation à 1 200 € pour abonnés).

## Règles de mise à jour (la discipline qui fait vivre le CRM)

1. **Tout contact = une trace le jour même** (2 min max). Un échange non noté n'a pas existé.
2. **Aucune ligne prospect sans « prochaine action » datée** — sinon statut Perdu, Plus tard (avec date de réveil) ou Opposé.
3. Statut « Opposé » = définitif : plus aucun message commercial, jamais (règle B2B, voir `sequence-prospection-fe.md` et `agence/juridique/rgpd.md`).
4. Vendredi routine hebdo (voir `routine-hebdo.md`) : passer la vue « Aujourd'hui » de la semaine suivante + la vue « Sans abonnement ».
5. Le 1er du mois : colonne « Rapport mensuel » de tous les abonnés remise à « à générer ».
6. Après chaque livraison de pack : échéances de suivi créées immédiatement (J+30 automatisation, J+45 diagnostic, M+10 hébergement, T1 2027 facture électronique).
7. Synchro cerveau : quand un prospect devient client, ou qu'un chiffre d'étude de cas apparaît → reporter dans `agence/cerveau/clients.md`. Le CRM porte l'opérationnel, le cerveau porte l'histoire.

## Automatisations du CRM (simples, avec reprise manuelle)

| Automatisation | Outil | Condition d'échec | Reprise manuelle |
|---|---|---|---|
| Rappel quotidien « prochaines actions du jour » | rappels natifs Notion/Airtable | notification ratée/désactivée | la vue « Aujourd'hui » reste LA référence : l'ouvrir chaque matin est dans la routine, le rappel n'est qu'une ceinture |
| Remise à zéro mensuelle « rapport à générer » | répétition de modèle Notion (ou à la main) | modèle non dupliqué le 1er | check-list du lundi de la routine hebdo : compter les abonnés vs rapports en cours |
| Alerte échéance (J+30, M+10, préavis) | champ date + vue filtrée | date jamais saisie à la livraison | check-list de fin de playbook (chaque playbook impose la saisie CRM comme dernière étape) |

Pas d'intégration lourde au lancement (pas de Zapier CRM↔facturation avant 5 abonnés) : à ce volume, la double saisie coûte moins cher que la maintenance d'un pont.

## RGPD — le CRM lui-même

Le CRM contient des données personnelles de prospects et de contacts clients : l'agence est **responsable de traitement** → à inscrire au registre (volet responsable, `agence/juridique/rgpd.md`), base légale intérêt légitime (prospection B2B), durée de conservation des prospects sans réponse : 3 ans après le dernier contact, puis suppression. La liste « Opposé » se conserve, elle, sans limite (c'est une liste de suppression, pas de prospection). Minimisation : pas de données perso superflues dans les notes.
