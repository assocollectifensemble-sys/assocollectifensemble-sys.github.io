# Routine hebdo — Jon seul avec 10 clients

> Version 2026-08-23 (agent automatisation).
> Hypothèse : le mix cible de l'offre — ~5 Essentiel + 4 Croissance + 2 Partenaire
> (≈ 3 650 € MRR) — soit ~40–45 h/mois de production d'abonnements (chiffrage
> `agence/offre/abonnement-pilotage.md`), ≈ **10–11 h/semaine**, laissant ~3 jours/semaine
> pour les chantiers de packs (le revenu one-shot) et la prospection.
> Principe fondateur (contexte.md) : **l'IA fait la production, Jon porte la relation.**

## La ligne rouge — jamais automatisé, par choix

- **Les rendez-vous** (vente, cadrage, restitution, réunion mensuelle Partenaire) — en face-à-face ou visio, préparés par IA, tenus par Jon.
- **Les formations** — sur poste, en personne : c'est le produit « autonomie », cœur de la valeur.
- **Les appels et le support à un client en difficulté** — quand un client appelle, un humain répond ou rappelle. Les accusés de réception peuvent être automatiques, la réponse est de Jon.
- **La relecture des rapports mensuels et de tout contenu publié** — rien ne part au nom d'un client ou de l'agence sans validation humaine.
- La décision commerciale (refuser un pack non rentable, choisir quoi proposer).

## La semaine type

### Tous les matins (30–40 min, avant les chantiers)
1. Boîte mail + WhatsApp : réponses courtes immédiates, le reste planifié. Délais contractuels : Partenaire 2 h ouvrées, Croissance 4 h, Essentiel 1 j — le tri se fait dans cet ordre.
2. Tableau de bord de surveillance (voir automatisations) : sites en ligne ? automatisations sans erreur ? Un voyant rouge = priorité de la matinée.
3. CRM vue « Aujourd'hui » : les prochaines actions datées du jour (relances séquence FE, échéances chantiers).

### Lundi — pilotage et production de contenu
- Revue de la semaine : chantiers en cours (CRM table 2), échéances, préparation des RDV posés.
- **Bloc contenu Croissance/Partenaire** (2–3 h) : les publications de la semaine des 6 abonnés concernés, générées par IA sur les calendriers validés, ajustées et programmées par Jon. Envoi en validation client quand c'est la règle du compte.
- Semaine 1 du mois : bloc **rapports mensuels** à la place (génération + relecture + envoi, voir `rapport-mensuel-modele.md`) — c'est la plus grosse échéance récurrente (½ à 1 jour).

### Mardi et jeudi — jours terrain (sanctuarisés)
- RDV clients et prospects, formations, tournages, audits sur site, réunions mensuelles Partenaire (2/mois, à caler ces jours-là).
- Groupés par commune autant que possible (vue CRM « par commune ») — l'île se traverse, les trajets se mutualisent.
- Pas de production planifiée ces jours-là : le terrain déborde toujours.

### Mercredi — jour chantier (production de packs)
- Bloc profond de 5–6 h sur LE chantier en cours (playbooks `agence/playbooks/`) : site, automatisation, montage, reprise de données.
- Règle de charge : **2 chantiers de packs actifs maximum en parallèle** avec 10 abonnés — au-delà, les délais vendus (fiches) ne tiennent plus, on décale la date de démarrage plutôt que la promesse.

### Vendredi — machine et commercial
- Matin : maintenance groupée Essentiel (mises à jour, vérif sauvegardes, petites modifs de la semaine — traiter en lot, pas au fil de l'eau), heures consommées saisies au CRM.
- Prospection (1–2 h) : séquence FE (`sequence-prospection-fe.md`) — messages du jour, appels de 2 min, mise à jour pipeline.
- Revue hebdo CRM (15 min, règle n°4) : prochaines actions de la semaine suivante, vue « Sans abonnement » (passerelles à activer), idées d'optimisation notées à chaud dans la semaine → table 3b.
- Facturation : devis en attente, factures à émettre (jour de facturation des abonnés), relances d'impayés.

## Quoi est automatisé / assisté / humain

| Tâche | Statut | Comment | Si ça casse (reprise manuelle) |
|---|---|---|---|
| Surveillance des sites (up/down) | **Automatisé** | service de monitoring simple → alerte WhatsApp/mail | pas d'alerte reçue ≠ tout va bien : contrôle visuel du tableau de bord chaque matin (30 s) |
| Sauvegardes des sites | **Automatisé** | sauvegarde planifiée hébergeur/CMS | vérif hebdo du vendredi : la dernière sauvegarde date de < 7 j, test de restauration 1×/trimestre |
| Surveillance des automatisations clients | **Automatisé** | chaque flux livré avec notification d'échec (règle playbook automatisation) | le client a aussi la doc de reprise manuelle ; Jon intervient selon le niveau d'abonnement |
| Alerte nouveaux avis Google | **Automatisé** | notifications Google Business | passage manuel hebdo sur les fiches (vendredi) |
| Brouillons de posts, textes, rapports | **Assisté IA** | générés par prompts des playbooks, TOUJOURS relus | l'IA en panne n'est jamais bloquante : tout peut s'écrire à la main, en plus lent |
| Relevés de chiffres mensuels | **Assisté** | exports/captures mensuels des outils | chiffre indisponible = dit honnêtement dans le rapport (règle du modèle) |
| Rappels d'échéances (J+30, M+10, relances) | **Automatisé** | dates CRM + vue « Aujourd'hui » | discipline de saisie en fin de playbook ; revue du vendredi rattrape les trous |
| Facturation récurrente des abonnés | **Semi-auto** | factures récurrentes de l'outil de facturation (la PA de référence) | échec de prélèvement/envoi → alerte outil → relance humaine sous 48 h |
| RDV, formations, appels, vente, réunions | **HUMAIN — jamais automatisé** | préparés par IA (ordre du jour, synthèses), tenus par Jon | — |
| Réponses de support | **Humain** | accusé de réception automatique possible hors horaires, réponse réelle par Jon dans le délai du niveau | — |

## Garde-fous de charge (les seuils qui protègent le modèle)

- **> 2 chantiers de packs en parallèle** → refuser ou décaler. Le délai promis est un argument de vente ; le rater coûte plus que décaler.
- **Support Essentiel qui dépasse 1 h/mois régulièrement chez un client** → signal : proposer le niveau supérieur, pas absorber en silence (l'heure incluse est contractuelle, `abonnement-pilotage.md`).
- **La routine déborde 3 semaines de suite** → avant d'embaucher ou de refuser des clients : chercher la tâche répétitive de Jon lui-même et l'automatiser (l'agence est son propre premier client du Pack Automatisation).
- **Vacances / pause** : prévenir les abonnés (clause de pause du contrat), monitoring et sauvegardes continuent seuls, un numéro d'urgence pour les Partenaires.

## RGPD

La routine touche des accès et données clients au quotidien : accès délégués uniquement (règle onboarding §3), mots de passe dans le gestionnaire — jamais WhatsApp/mail en clair, et toute nouvelle tâche récurrente touchant des données personnelles de clients finaux passe par la case annexe de sous-traitance (`agence/juridique/rgpd.md`).

## Critère d'une « bonne semaine »

> Les délais de réponse contractuels tenus, zéro voyant rouge non traité le jour même, les publications de la semaine parties validées, le CRM sans ligne orpheline (sans prochaine action), et — semaine 1 du mois — tous les rapports envoyés avant le 5. Si tout ça tient ET qu'il reste du temps de prospection le vendredi, la machine tourne.
