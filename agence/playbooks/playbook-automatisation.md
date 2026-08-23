# Playbook — Pack Automatisation (1 900 € / processus suivant 1 200 €)

> Mode opératoire de livraison. Version 2026-08-23 (agent automatisation).
> Fiche vendue : `agence/offre/pack-automatisation.md`. Délai vendu : 2–3 semaines + point à 30 jours.
> Règle d'honnêteté (fiche) : si le gain ne rembourse pas le pack en < 6 mois, on refuse et on le dit à l'atelier.

## Temps cible

| | Temps homme réel | Délai calendaire |
|---|---|---|
| 1re livraison | **6 jours** (bibliothèque de scénarios types à construire) | 3 semaines + J30 |
| Livraisons suivantes | **3 jours** (÷2 — chiffrage fiche : ~3 j) | 2–3 semaines + J30 |
| Processus supplémentaire même client (1 200 €) | **2 jours** (cartographie et accès déjà faits) | 2 semaines |

Le ÷2 vient de : la **bibliothèque de scénarios types** (relances impayés, accusé de réception WhatsApp/FB, confirmation de réservation, devis type, ressaisie vers tableur), le gabarit de documentation 3 pages, et le gabarit de fiche de garde-fous.

## Déroulé jour par jour

### Semaine 1 — cartographier et chiffrer AVANT de construire

| Jour | Étape | Durée |
|---|---|---|
| J1 | **Atelier de cartographie (1 h 30, sur site)** avec ceux qui FONT la tâche (pas seulement le dirigeant) : qui fait quoi, outils, volumes, cas particuliers, heures/semaine. **Le gain visé est chiffré et écrit séance tenante** (h/sem × taux chargé → mois de remboursement). Si > 6 mois : on arrête là, honnêteté vendue | 0,5 j |
| J2 | Schéma du flux cible (1 page : déclencheur → étapes → règles → humain) + **fiche garde-fous** : ce qui part automatiquement / ce qui attend validation humaine. Validation écrite du client sur les deux | 2 h |
| J2 | Bloc 5 onboarding : le flux touche-t-il des messages ou fichiers clients ? Presque toujours oui → **annexe RGPD signée avant de brancher quoi que ce soit** | 30 min |
| J3 | Accès : outils du client (délégués), création des comptes nécessaires **au nom du client** (règle de transférabilité : le client doit pouvoir partir avec) | 2 h |

### Semaine 2 — construire et tester

| Jour | Étape | Durée |
|---|---|---|
| J8–J10 | Construction du scénario à partir de la bibliothèque : déclencheurs, messages types (rédigés par IA, **validés mot à mot par le client** — c'est son image), rangement des données au bon endroit | 1,5 j |
| J10–J11 | **Tests à blanc** : jeux d'essai internes, puis 3–5 cas réels supervisés (chaque envoi vérifié à la main). Tests des cas d'échec : outil en panne, message inattendu, donnée manquante | 0,5 j |
| J11 | **Documentation en français clair (1–3 pages)** : comment ça marche, comment vérifier que ça tourne, quoi faire si ça s'arrête (procédure de reprise manuelle), qui prévenir. Gabarit ci-dessous | 2 h |

### Semaine 3 — mise en production et autonomie

| Jour | Étape | Durée |
|---|---|---|
| J15 | Mise en production réelle, surveillance rapprochée 48 h (notification d'erreur → téléphone de Jon) | 0,5 j |
| J17–J18 | **Formation sur poste (2 h)** : l'équipe surveille, corrige, ajuste ; exercice réel : provoquer une erreur et la traiter ensemble avec la doc | 0,5 j |
| J18 | Compteur de gain posé (le plus simple : le scénario logge chaque exécution dans un tableur) — c'est lui qui alimentera le point à 30 j et le rapport mensuel si abonnement | 1 h |
| J45 env. | **Point de contrôle J+30 (offert)** : heures réellement gagnées vs chiffre promis, ajustements fins, et proposition abonnement Croissance 350 € (surveillance incluse jusqu'à 2 processus) ou Partenaire | 0,5 j |

## Checklist de livraison

- [ ] Gain chiffré à l'atelier, ÉCRIT dans le devis (h/semaine, €/mois, mois de remboursement)
- [ ] Refus documenté si remboursement > 6 mois (mail au client — cette honnêteté est un actif commercial)
- [ ] Schéma du flux 1 page validé par le client
- [ ] Fiche garde-fous signée : automatique vs validation humaine — rien qui engage l'image ne part sans règle
- [ ] Annexe RGPD signée si messages/fichiers clients traversent le flux (quasi systématique)
- [ ] Comptes des outils au nom du client, Jon en délégué
- [ ] Messages sortants validés mot à mot par le client
- [ ] Testé : cas nominal, 3 cas particuliers, ET 2 cas d'échec (panne, donnée manquante)
- [ ] Notification d'échec en place (le client ET Jon sont prévenus quand ça casse)
- [ ] Documentation 1–3 pages remise, **avec procédure de reprise manuelle** (« revenez à votre méthode d'avant, voici comment »)
- [ ] Formation 2 h : l'équipe a traité une erreur simulée elle-même
- [ ] Compteur de gain actif ; point J+30 dans l'agenda ET le CRM

## Outils

- **Make** (Make.com) en plateforme par défaut — visuel, montrable au client, transférable ; **n8n** si le client veut l'auto-hébergement ou du volume. Un seul des deux par client, jamais une plateforme de plus si les outils natifs du client suffisent (rappel du standard : un tableau + une automatisation avant une plateforme).
- Outils natifs d'abord : réponses enregistrées WhatsApp Business, modèles d'email, règles de boîte mail, Zapier/Make seulement quand il faut relier deux mondes.
- Google Sheets comme pivot de données et de log (le client sait l'ouvrir).
- Claude/API IA pour la génération de réponses SEULEMENT derrière les garde-fous validés et l'annexe RGPD (option no-training).

## Prompts types réutilisables

**Prompt 1 — analyse de cartographie :**
```
Voici la cartographie d'une tâche répétitive dans une TPE ([SECTEUR], La Réunion) :
[NOTES_ATELIER_ANONYMISÉES]. Propose le flux automatisé le plus SIMPLE possible :
déclencheur, étapes, où l'humain valide, outils déjà possédés par le client à
privilégier. Liste ensuite : les cas particuliers qui casseront le flux, les
conditions d'échec probables, et pour chacune la reprise manuelle. Ne propose une
plateforme d'automatisation que si les fonctions natives des outils ne suffisent pas.
```

**Prompt 2 — messages types du flux :**
```
Rédige les messages automatiques pour [PROCESSUS — ex. accusé de réception WhatsApp]
d'une entreprise : [ACTIVITE], ton : [TON], signature : [NOM_ENTREPRISE].
Contraintes : jamais prétendre être un humain, annoncer le délai de reprise humaine
réel ([DELAI]), proposer une issue de secours ([TELEPHONE]). Variantes : horaires
ouvrés / soir et week-end / période de fermeture [SAISON].
```

**Prompt 3 — documentation client :**
```
Transforme ces notes techniques en mode d'emploi de 1 à 3 pages pour une équipe non
technique : [NOTES]. Plan imposé : 1) ce que fait l'automatisation, en une phrase ;
2) comment vérifier chaque matin que ça tourne (30 secondes) ; 3) que faire si ça
s'arrête — étapes de reprise manuelle ; 4) qui prévenir et quand ([CONTACT_JON]).
Zéro jargon : pas de « webhook », pas de « scénario », des mots de tous les jours.
```

## Livrables types

Processus en production · schéma de flux 1 page · fiche garde-fous signée · documentation 1–3 pages avec reprise manuelle · formation faite · compteur de gain · compte rendu du point J+30.

## Pièges connus

- **Automatiser un processus bancal.** Si la méthode manuelle est incohérente, l'automatiser industrialise le chaos. L'atelier sert aussi à simplifier AVANT d'automatiser.
- **Le flux silencieusement mort.** Une automatisation qui échoue sans prévenir est pire que pas d'automatisation (le client croit que ses relances partent). Notification d'échec = livrable obligatoire, non négociable.
- **Messages qui se font passer pour un humain.** Interdit par les garde-fous : dégât d'image + terrain glissant réglementairement. « Machine polie qui annonce l'humain » est l'argument de la fiche.
- **Construire sur le compte perso de Jon** (API, plateforme). Le cycle « rendre autonome » exige que tout soit au nom du client — sinon la réversibilité promise est un mensonge.
- **Sous-estimer les cas particuliers.** 80 % du temps de construction est dans les 20 % de cas tordus ; c'est le travail humain que l'IA ne fait pas (dit dans la fiche). Les lister à l'atelier, pas en production.
- **Sauter le point J+30.** C'est là que le chiffre promis devient un chiffre prouvé — matière de l'étude de cas et du passage en abonnement.

## RGPD / données personnelles — quasi systématique ici

Messages clients, coordonnées, réservations, impayés : presque tout flux automatisé traite des données personnelles pour le compte du client → bloc 5 onboarding + **annexe de sous-traitance** (`agence/juridique/rgpd.md`), minimisation (le flux ne stocke que ce dont il a besoin), localisation des serveurs des outils notée dans l'annexe, option no-training activée sur tout outil IA. Données sensibles (santé…) : STOP, cadrage avocat avant tout (règle rgpd.md).

## Critère de « fini »

> Le processus tourne en production depuis au moins 48 h sans intervention, une erreur prévient automatiquement le client et Jon, l'équipe a traité une panne simulée seule avec la documentation, le compteur de gain enregistre, et le point J+30 est planifié. « Ça marche quand Jon regarde » n'est pas fini — fini, c'est **ça marche, ça se surveille, et ça sait tomber en panne proprement**.
