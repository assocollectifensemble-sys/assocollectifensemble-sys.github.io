# Playbook — Pack Diagnostic Digital & IA (590 €)

> Mode opératoire de livraison. Version 2026-08-23 (agent automatisation).
> Fiche vendue : `agence/offre/pack-diagnostic.md` — ce playbook livre exactement ce qu'elle promet.
> Onboarding : le questionnaire `agence/juridique/onboarding-client.md` sert de trame d'entretien.

## Temps cible

| | Temps homme réel | Délai calendaire |
|---|---|---|
| 1re livraison | **2 jours** (construction des gabarits en marchant) | 7 jours |
| Livraisons suivantes | **1 jour** (objectif ÷2 — c'est le chiffrage de la fiche) | 7 jours |

La division par deux vient de trois choses : le gabarit de plan d'action réutilisé, la grille d'audit de poste pré-remplie, et les prompts ci-dessous devenus routiniers.

## Déroulé jour par jour (délai vendu : 7 jours calendaires)

| Jour | Étape | Où | Durée |
|---|---|---|---|
| J0 | Vente conclue, date de J1 fixée, questionnaire d'onboarding §0–1 pré-rempli au téléphone | tél. | 15 min |
| J1 matin | **Entretien de cadrage (1 h)** avec le dirigeant + **audit sur place** dans la foulée (~1,5 h) : tour des postes, observation réelle, photos des écrans/outils (avec accord), point conformité FE | sur site | 3 h |
| J1 soir | Décharge à chaud : dicter les notes brutes dans un doc, lancer le prompt de structuration (voir prompts) | bureau | 30 min |
| J2–J3 | Audit de présence en ligne (grille ci-dessous) + vérification conformité FE (plateforme agréée ? réception opérationnelle ?) | bureau | 1,5 h |
| J3–J4 | Rédaction IA du plan d'action (prompt n°2), puis passe humaine de Jon : chiffrage local, priorisation ROI, coupes (5–8 actions MAX) | bureau | 2–3 h |
| J5 | Relecture à froid, mise en page du document remis, préparation de la page « et après ? » (passerelle abonnement, niveau recommandé) | bureau | 1 h |
| J6–J7 | **Restitution en face-à-face (1 h)** : dérouler le plan, remettre le document, poser la suite (pack ? les 590 € sont déduits sous 60 j) | sur site | 1 h + trajet |
| J7 | Mise à jour CRM (statut, pack pressenti, relance J+45 programmée) + fiche `cerveau/clients.md` | bureau | 15 min |

## Checklist de livraison

- [ ] Questionnaire d'onboarding rempli (au minimum §0, 1, 2, 5)
- [ ] Entretien de cadrage fait sur site (1 h)
- [ ] Chaque poste de travail passé en revue (grille : tâches, outils, temps/semaine, frictions)
- [ ] Audit présence en ligne : site, Google Business, FB/IG, WhatsApp, avis (captures datées)
- [ ] Verdict facturation électronique écrit : conforme / à migrer / urgent
- [ ] Plan d'action : 5–8 actions max, chacune avec quoi / pourquoi / coût / gain (€ ou h)
- [ ] Page « et après ? » : niveau d'abonnement recommandé + pack prioritaire
- [ ] Zéro jargon : relu à voix haute, compréhensible par un dirigeant pressé
- [ ] Restitution faite en face-à-face, document remis (PDF + papier)
- [ ] CRM à jour : pack pressenti, échéance de déduction (J+60), relance programmée
- [ ] Si données personnelles vues pendant l'audit (fichier clients à l'écran…) : rien copié, rien conservé — sinon voir `agence/juridique/rgpd.md`

## Outils

- Bloc-notes + dictaphone du téléphone (audit terrain) — le plus simple qui marche.
- Claude (ou équivalent) pour structuration et rédaction ; **jamais de données nominatives clients du client dans le prompt** (voir RGPD ci-dessous).
- Gabarit de plan d'action : `[à créer à la 1re livraison, puis stocké dans le dossier modèles]` — c'est LE réutilisable qui fait le ÷2.
- Grille d'audit de poste (tableau 5 colonnes : poste / tâches répétitives / outils / h par semaine / friction).
- PageSpeed Insights + recherche Google en navigation privée (« [métier] [ville] ») pour l'audit de présence.

## Prompts types réutilisables

**Prompt 1 — structuration des notes terrain (J1 soir) :**
```
Voici mes notes brutes d'audit d'une TPE réunionnaise ([SECTEUR], [NB_SALARIES]
salariés, à [VILLE]). Structure-les en : 1) activité et contexte, 2) tableau des
postes (tâches répétitives, outils, heures/semaine estimées, frictions),
3) existant digital, 4) signaux d'opportunité classés (gain de temps, visibilité,
conformité). Ne rien inventer : si une info manque, écris [À VÉRIFIER].
Notes : [NOTES_BRUTES_ANONYMISÉES]
```

**Prompt 2 — ossature du plan d'action (J3) :**
```
À partir de cette synthèse d'audit [COLLER SYNTHÈSE], propose 8 à 12 actions
candidates pour cette TPE. Pour chacune : quoi, pourquoi (problème constaté),
coût estimé (fourchette), gain attendu (heures/mois ou € — hypothèses écrites),
délai. Classe par retour sur investissement décroissant. Français courant,
zéro jargon technique, zéro mention d'IA côté client : parle de résultats.
Contexte local : La Réunion, clients qui cherchent via Google/Facebook/WhatsApp.
```
Puis Jon coupe à 5–8, corrige les chiffres avec les prix réels de la grille tarifaire (`agence/offre/grille-tarifaire.md`).

**Prompt 3 — contrôle qualité :**
```
Relis ce plan d'action comme un dirigeant de TPE pressé et méfiant : [PLAN].
Liste ce qui est flou, invérifiable, jargonneux, ou ressemble à de la vente
forcée. Vérifie que chaque action a un chiffre et que le total est réaliste.
```

## Livrables types

1. **Plan d'action chiffré** (6–10 pages max) : contexte, constat par poste, audit présence, verdict FE, 5–8 actions priorisées ROI, page « et après ? ».
2. Captures d'écran datées de l'existant en ligne (annexe).
3. Restitution orale 1 h.

## Pièges connus

- **Le rapport-fleuve.** 20 pages tuent la vente. 5–8 actions, pas une de plus — le reste va en annexe « pistes secondaires ».
- **Chiffrer trop optimiste.** Les gains d'heures se prennent sur les dires du dirigeant, divisés par deux par prudence, hypothèse écrite. Un chiffre invérifiable détruit la crédibilité de tout le document.
- **Auditer par questionnaire au lieu d'observer.** La fiche vend une observation réelle ; c'est là que se voient les 5 h/semaine de ressaisie que personne ne déclare.
- **Oublier la déduction J+60.** C'est le moteur commercial du pack : date écrite dans le document ET dans le CRM avec relance à J+45.
- **Copier des données clients du client** pour « analyser » : interdit sans annexe RGPD. Le diagnostic s'écrit avec des volumes et des constats, pas des fichiers nominatifs.

## RGPD / données personnelles

L'audit fait voir des écrans contenant des données clients : on observe, on ne copie pas, on ne photographie pas d'écran nominatif. Les notes envoyées à l'IA sont anonymisées (pas de noms de clients finaux). Si la mission suivante implique un accès aux données → bloc 5 de l'onboarding + `agence/juridique/rgpd.md`.

## Critère de « fini »

> Le dirigeant a reçu, en face-à-face, un document de 5–8 actions chiffrées qu'il peut montrer tel quel à son expert-comptable, il sait quel est le verdict facturation électronique de son entreprise, la date limite de déduction des 590 € est écrite noir sur blanc, et le CRM porte la relance. Tant qu'une de ces quatre choses manque, ce n'est pas fini.
