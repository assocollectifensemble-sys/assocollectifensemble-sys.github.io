# Playbook — Pack Conformité Facture Électronique (Solo 690 € / Équipe 1 290 €)

> Mode opératoire de livraison du **coin d'entrée commercial**. Version 2026-08-23 (agent automatisation).
> Fiche vendue : `agence/offre/pack-facture-electronique.md`. Délai vendu : 10 jours (Solo urgence : 5 j).
> Prérequis agence : Jon lui-même inscrit sur une plateforme agréée (PA) et une PA de
> référence choisie — décision OUVERTE dans `cerveau/decisions.md`, **bloquante avant la 1re vente**.

## Temps cible

| | Temps homme réel | Délai calendaire |
|---|---|---|
| Solo — 1re livraison | **2 jours** | 10 j (5 j urgence) |
| Solo — suivantes | **1 jour** (÷2 — chiffrage fiche) | 10 j |
| Équipe — 1re livraison | **3,5 jours** | 10 j |
| Équipe — suivantes | **2 jours** (÷2 — chiffrage fiche) | 10 j |

Le ÷2 vient de : la PA de référence maîtrisée par cœur (paramétrage devenu mécanique), le gabarit de reprise de données (tableur type), le mémo pas-à-pas générique personnalisé en 30 min, et la check-list 2027 réutilisée telle quelle.

## Déroulé jour par jour

| Jour | Étape | Solo | Équipe |
|---|---|---|---|
| J1 | **État des lieux (30 min, visio ou sur site)** : comment il facture aujourd'hui, volume, outil actuel, expert-comptable, qui facture. Onboarding §0–2 + bloc 5 (les fiches clients = données perso → annexe RGPD à signer AVANT la reprise) | ✅ | ✅ |
| J1–J2 | **Choix argumenté de la PA** : grille de décision (volume, budget, compatibilité expert-comptable, simplicité). Par défaut la PA de référence de l'agence ; si l'outil actuel du client est déjà compatible, on le garde — honnêteté commerciale de la fiche | ✅ | ✅ |
| J2–J3 | Ouverture du compte **au nom du client**, paramétrage : identité, mentions légales, numérotation (continuité avec l'existant !), TVA, **raccordement réception opérationnel** | ✅ | ✅ |
| J3–J5 | **Reprise des données** : export de l'existant (Excel, ancien logiciel) → gabarit → import. Solo : jusqu'à 50 fiches. Équipe : volume complet + articles/tarifs | ✅ | ✅ |
| J5–J6 | **Test grandeur nature** : réception d'une facture réelle via la PA + émission d'une facture test réelle (ou d'un brouillon validé si l'émission attend 2027). Preuve conservée (capture) et remise au client | ✅ | ✅ |
| J6–J7 | Équipe : **coordination expert-comptable** — appel ou mail, transmission des accès en lecture, format d'export convenu, compte rendu écrit en 5 lignes | — | ✅ |
| J8–J9 | **Formation sur poste** : Solo 1 h (le dirigeant fait une facture lui-même) ; Équipe 2 h jusqu'à 4 personnes + **mémo pas-à-pas** personnalisé (captures de LEUR compte) | ✅ | ✅ |
| J9 | Remise de la **check-list émission 2027** + proposition Essentiel 150 €/mois (veille conformité incluse — argument de la fiche : « en 2027, ce sera déjà fait ») | ✅ | ✅ |
| J10 | CRM : statut « conforme réception », relance programmée **T1 2027** (préparer l'émission), niveau d'abonnement proposé/réponse | ✅ | ✅ |

Variante urgence 5 jours (Solo) : J1 état des lieux + choix PA le même jour, reprise limitée aux 20 clients actifs (le reste après), formation à J5.

## Checklist de livraison

- [ ] État des lieux fait, volume et outil actuel notés
- [ ] Annexe RGPD signée AVANT tout accès au fichier clients (`agence/juridique/rgpd.md`)
- [ ] Choix de PA argumenté par écrit (3 lignes suffisent : pourquoi celle-là)
- [ ] Compte PA au nom du client, Jon en accès délégué (jamais le compte principal)
- [ ] Mentions légales et numérotation vérifiées (continuité de séquence avec l'ancien système)
- [ ] Fiches clients reprises (Solo ≤ 50 / Équipe complet), échantillon contrôlé à la main (10 fiches)
- [ ] **Réception testée avec une vraie facture** — capture de preuve remise
- [ ] Émission testée (facture réelle ou brouillon complet)
- [ ] Expert-comptable dans la boucle (Équipe) : accès transmis, format d'export convenu, trace écrite
- [ ] Formation faite — chaque personne formée a produit une facture elle-même
- [ ] Mémo pas-à-pas remis (Équipe) ; check-list émission 2027 remise (les deux versions)
- [ ] Export des données remis au client (réversibilité) + fichiers de travail intermédiaires supprimés chez Jon
- [ ] CRM : relance T1 2027 programmée, proposition Essentiel notée

## Outils

- La **PA de référence de l'agence** `[à trancher — decisions.md]` + l'outil du client s'il est déjà compatible (Tiime, Qonto, Pennylane…).
- Tableur (gabarit de reprise : colonnes normalisées clients/articles) — le plus simple qui marche.
- IA pour : nettoyage/normalisation du fichier de reprise (SIREN manquants, doublons, casse), rédaction du mémo. **Le fichier clients ne passe dans un outil IA que si l'annexe RGPD l'autorise et avec option no-training** ; sinon nettoyage local au tableur.
- Annuaire SIRENE (sirene.fr) pour vérifier les SIREN clients.

## Prompts types réutilisables

**Prompt 1 — normalisation du fichier de reprise** (uniquement si couvert par l'annexe RGPD, sinon travail local) :
```
Voici un export clients à normaliser pour import dans [PLATEFORME]. Colonnes
attendues : raison sociale, SIREN, adresse, CP, ville, email de facturation,
conditions de paiement. Sans inventer aucune donnée : signale les doublons
probables, les SIREN absents ou invalides (9 chiffres), les emails mal formés.
Rends deux tableaux : « prêts à importer » et « à vérifier avec le client ».
```

**Prompt 2 — mémo pas-à-pas personnalisé :**
```
Rédige un mémo « faire une facture dans [PLATEFORME] » pour une TPE ([ACTIVITE]),
utilisateurs non techniques. Étapes numérotées, une action par étape, à partir de
ce déroulé constaté : [NOTES_DE_PARAMETRAGE]. Ajoute : « que faire si » (avoir,
facture reçue à valider, client introuvable) et « qui appeler » ([CONTACT_JON]).
3 pages max, français simple.
```

**Prompt 3 — mail de coordination expert-comptable :**
```
Écris un email professionnel court à l'expert-comptable de [CLIENT] : nous avons
installé [PLATEFORME] pour la conformité facturation électronique (réception
opérationnelle), voici l'accès lecture / le format d'export [FORMAT], question :
ce format vous convient-il ou préférez-vous [ALTERNATIVE] ? Ton confraternel :
je travaille AVEC lui, pas à sa place.
```

## Livrables types

Compte PA opérationnel (réception testée, preuve) · fichier clients repris + export de réversibilité · mémo pas-à-pas (Équipe) · check-list émission 2027 · trace de coordination expert-comptable (Équipe) · formation faite.

## Pièges connus

- **Vendre avant d'avoir sa propre PA maîtrisée.** On ne livre bien que ce qu'on utilise soi-même. Blocage à lever en premier (decisions.md — urgent).
- **Casser la numérotation de factures.** La séquence doit continuer l'existant ; une rupture = problème comptable et fiscal. Vérifier le dernier numéro émis AVANT paramétrage.
- **Reprise de données sale.** 50 fiches avec 15 doublons détruisent la confiance. Contrôle manuel d'un échantillon, toujours.
- **Court-circuiter l'expert-comptable.** S'il découvre l'outil après coup, il torpille. L'appeler pendant la mission est un argument de vente (« appelez-le devant moi »).
- **Promettre l'émission « conforme 2027 » alors que le périmètre exact peut évoluer** : la check-list 2027 dit ce qu'on sait à date et renvoie vers la veille conformité de l'abonnement — c'est la passerelle, pas un défaut.
- **Garder le fichier clients du client après la mission** : violation de la minimisation. Export remis, copies de travail supprimées, fait noté.

## RGPD / données personnelles — POINT CRITIQUE DU PACK

La reprise de données EST un traitement de données personnelles pour le compte du client (noms, emails, historique de facturation). Donc systématiquement : bloc 5 de l'onboarding coché → **annexe de sous-traitance signée avec le devis** (`agence/juridique/rgpd.md`) → minimisation (uniquement les champs utiles à la facturation) → suppression des copies de travail en fin de mission → mention au registre sous-traitant de l'agence.

## Critère de « fini »

> Le client a REÇU une vraie facture électronique sur sa plateforme (preuve datée remise), ses fiches clients y sont propres, chaque personne formée a émis une facture de ses propres mains, l'expert-comptable est au courant (Équipe), la check-list 2027 est remise et la relance T1 2027 est dans le CRM. « Le compte est ouvert » n'est pas fini — **testé et prouvé** est la promesse de la fiche.
