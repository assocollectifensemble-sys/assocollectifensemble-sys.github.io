# Modèle — Rapport mensuel d'abonné

> Version 2026-08-23 (agent automatisation).
> Engagement contractuel : chaque abonné (Essentiel/Croissance/Partenaire) reçoit un
> rapport mensuel « généré par nos outils, relu et signé par Jon — jamais un robot en
> autopilote » (`agence/offre/abonnement-pilotage.md`). Ce fichier est le gabarit + le
> processus de génération.
> Format d'envoi : PDF d'1 à 2 pages (3 max pour Partenaire), joint à un email court
> personnel de Jon. Envoi entre le 1er et le 5 du mois.

## Ton

- Français direct, phrases courtes, **zéro jargon** (« votre site a été vu 340 fois », pas « 340 sessions organiques »).
- On parle résultats et heures gagnées, jamais de technique ni « d'IA » (règle commerciale de l'offre).
- Honnête : un mois creux se dit (« mois calme sur Google, normal en [saison] ») — la confiance vaut plus qu'une courbe flatteuse.
- Chaque rapport se termine par une phrase de Jon écrite à la main : c'est la signature humaine du modèle.

## Structure (sections dans l'ordre)

### 1. L'essentiel en 3 lignes
Le mois résumé : 1 chiffre marquant, 1 chose faite, 1 chose à venir. C'est la seule section que certains liront — elle doit suffire.

### 2. Ce qui a été fait ce mois-ci
Liste à puces datées, tirée du journal d'interventions. Inclure l'invisible payé par l'abonnement : sauvegardes OK, mises à jour, surveillance. Croissance/Partenaire : les publications du mois (liens) et **l'optimisation concrète du mois** (engagement contractuel Croissance — la nommer explicitement).

### 3. Vos chiffres du mois
Tableau 3 colonnes : indicateur / ce mois / mois précédent. Une ligne de lecture humaine sous le tableau (« en clair : … »).

| Niveau | Indicateurs à injecter |
|---|---|
| Essentiel | visites du site, appels/clics depuis la fiche Google, nouveaux avis (+ note), disponibilité du site (« en ligne sans interruption »), heures de modifications consommées / incluses |
| Croissance (en plus) | portée des 4 publications, meilleure publication du mois, messages/contacts reçus, **heures gagnées par les automatisations suivies** (compteur posé au pack) |
| Partenaire (en plus) | tableau des automatisations : nom / exécutions / incidents / heures gagnées ; avancement de la feuille de route de la réunion mensuelle |

### 4. Ce qu'on a vu (et notre conseil)
1 à 3 observations avec recommandation. C'est ici que les **idées d'optimisation du CRM** (table 3b) deviennent des propositions : optimisation incluse dans l'abonnement, ou pack à envisager (avec le tarif abonné : Automatisation 1 200 €, Vidéo −10 %). Une proposition max par rapport — pas un catalogue.

### 5. Le mois prochain
Ce qui est prévu (publications, optimisation, échéances de conformité — ex. préparation émission facture électronique 2027).

### 6. Le mot de Jon
2–3 phrases personnelles, écrites par Jon, jamais générées. + rappel discret : « une question, un souci : WhatsApp direct, réponse sous [délai du niveau] ».

## Données à injecter (à collecter AVANT la génération)

| Donnée | Source | Automatisable ? |
|---|---|---|
| Interventions du mois | journal d'interventions tenu au fil de l'eau (CRM / carnet) | non — discipline de saisie |
| Visites du site | outil de statistiques installé au Pack Présence | oui (export/capture mensuel) |
| Fiche Google (vues, appels, avis) | Google Business Profile | oui (relevé mensuel) |
| Publications et portée | Meta Business Suite | oui (relevé mensuel) |
| Heures gagnées automatisations | compteur posé au pack (log tableur) | oui |
| Heures de modifs consommées | CRM table 3a | non (saisie à l'acte) |
| Idées d'optimisation | CRM table 3b | non |
| Contexte local (saison, événement) | tête de Jon | non |

## Processus de génération (par abonné : cible 20 min Essentiel, 30–40 min Croissance/Partenaire)

1. Le 1er du mois : CRM passe tous les abonnés à « rapport à générer » (règle CRM).
2. Collecte des chiffres (relevés ci-dessus) dans le tableau de collecte.
3. Génération IA — prompt type :

```
Rédige le rapport mensuel [MOIS] pour [CLIENT], abonné [NIVEAU] ([ACTIVITE],
La Réunion). Structure imposée : 1. L'essentiel en 3 lignes / 2. Ce qui a été
fait / 3. Vos chiffres (tableau ce mois vs mois dernier + une ligne « en
clair ») / 4. Ce qu'on a vu et notre conseil (1 seule proposition, choisie
parmi : [IDEES_CRM]) / 5. Le mois prochain. Ton : direct, chaleureux, zéro
jargon, zéro mention d'IA ou d'outils techniques, honnête si un chiffre baisse
(contexte : [CONTEXTE_SAISON]). Données : interventions = [LISTE] ; chiffres =
[TABLEAU] ; prévu = [PREVU]. N'invente AUCUN chiffre : si une donnée manque,
écris [MANQUANT]. 1 à 2 pages.
```

4. **Relecture de Jon — obligatoire, jamais sautée** : chiffres vérifiés un à un, aucun `[MANQUANT]` restant, la proposition §4 est pertinente ce mois-ci, puis il écrit le « mot de Jon ».
5. Export PDF, email d'envoi court (2 lignes personnelles, jamais un modèle visible), CRM → « envoyé ».

## Conditions d'échec et reprise manuelle

| Échec | Symptôme | Reprise |
|---|---|---|
| Statistiques indisponibles (outil en panne, accès expiré) | trou dans le tableau | le dire dans le rapport (« relevé indisponible ce mois-ci, corrigé pour le prochain ») plutôt que retarder l'envoi ou inventer |
| Chiffre IA halluciné | un nombre absent des données injectées | c'est LE risque du modèle → la relecture de Jon compare chaque chiffre du rapport au tableau de collecte, ligne à ligne |
| Retard de génération | des rapports « à générer » après le 5 | envoyer une version courte (sections 1, 2, 6) plutôt que rien ; le rapport est un rituel de confiance, la régularité prime sur l'exhaustivité |
| Mois sans matière (client en pause saisonnière) | rien à dire | rapport allégé prévu par la clause de pause : surveillance + veille conformité uniquement |

## RGPD

Le rapport contient des données d'activité du client, pas de données de SES clients finaux : ne jamais citer de client final nommément (ex. avis Google cité → anonymiser sauf avis public). Les relevés (statistiques, Meta) transitent par les accès délégués déclarés dans l'annexe de sous-traitance quand elle existe — voir `agence/juridique/rgpd.md`.

## Critère de « fini » (chaque mois)

> Tous les abonnés ont reçu leur rapport entre le 1er et le 5, chaque chiffre a été vérifié par Jon contre la source, chaque rapport contient une section « mot de Jon » écrite à la main, et le CRM est passé à « envoyé ». Un rapport en retard se rattrape en version courte — un rapport faux ne se rattrape pas.
