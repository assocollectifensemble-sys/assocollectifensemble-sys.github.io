# RGPD — Registre de traitements type + clause de sous-traitance de données

> **Trame de travail — à faire valider par un avocat / expert-comptable avant usage**
> (idéalement par un avocat ou un DPO externe pour la partie RGPD).
> Deux pièces dans ce document :
> **A.** le registre des traitements de l'agence elle-même (art. 30 RGPD) —
> volet « responsable de traitement » **et** volet « sous-traitant » ;
> **B.** la **clause/annexe de sous-traitance** (art. 28 RGPD) à signer avec le
> client dès qu'un agent IA ou une automatisation installée par l'agence touche
> aux données clients du client.
> La CNIL recommande une revue du registre **au moins une fois par an** ; les
> recommandations CNIL « IA et RGPD » (publiées en 2025) servent de référence
> pour les traitements impliquant des systèmes d'IA (cnil.fr).

---

## A. Registre des traitements de l'agence

### A.1 Identification

| Champ | Valeur |
|---|---|
| Responsable de traitement | `[Nom de Jon]`, EI micro-entrepreneur, SIREN `[…]`, `[adresse]`, La Réunion |
| Contact données personnelles | `[e-mail pro]` *(pas de DPO obligatoire à ce stade — activité à petite échelle, pas de suivi régulier et systématique à grande échelle ; à réévaluer chaque année)* |
| Dernière revue du registre | `[date]` |

### A.2 Volet responsable de traitement (art. 30.1) — traitements pour le compte de l'agence

**Traitement n° 1 — Gestion clients et facturation**

| Rubrique | Contenu |
|---|---|
| Finalité | Gestion commerciale, contrats, devis, facturation, comptabilité |
| Base légale | Exécution du contrat (art. 6.1.b) ; obligation légale pour la comptabilité (6.1.c) |
| Personnes concernées | Dirigeants et interlocuteurs des clients |
| Données | Identité, coordonnées pro, fonction, données de facturation, historique de prestations |
| Destinataires | Jon ; expert-comptable `[nom]` ; administration fiscale ; plateforme agréée de facturation électronique `[nom]` ; outil de facturation `[nom]` |
| Durées | Durée de la relation + 5 ans (prescription) ; pièces comptables : 10 ans |
| Transferts hors UE | `[oui/non — si outils US : encadrement (clauses contractuelles types / Data Privacy Framework), à documenter]` |
| Sécurité | Postes chiffrés, gestionnaire de mots de passe, MFA sur tous les comptes, sauvegardes `[modalité]` |

**Traitement n° 2 — Prospection et communication**

| Rubrique | Contenu |
|---|---|
| Finalité | Prospection B2B, newsletter, invitations aux micro-ateliers « l'IA pour ta TPE » |
| Base légale | Intérêt légitime (prospection B2B en lien avec la fonction du destinataire), avec information et droit d'opposition à chaque envoi |
| Données | Nom, fonction, e-mail pro, entreprise, source du contact |
| Durées | 3 ans après le dernier contact entrant |
| Destinataires | Jon ; outil d'e-mailing `[nom]` |

**Traitement n° 3 — Site vitrine de l'agence** *(à activer quand le site existera)*

| Rubrique | Contenu |
|---|---|
| Finalité | Formulaire de contact, mesure d'audience |
| Base légale | Mesures précontractuelles (6.1.b) ; consentement pour les cookies non essentiels |
| Durées | Demandes de contact : 3 ans ; cookies : selon CMP |
| Note | Bannière cookies uniquement si traceurs non exemptés ; privilégier une mesure d'audience exemptée de consentement (configuration conforme CNIL) |

**Traitement n° 4 — Sous-traitants de l'agence (pour mémoire)**
Liste tenue à jour des outils utilisés par l'agence elle-même (hébergeur, e-mail,
stockage cloud, outils IA, plateforme agréée) : `[tableau nom / finalité /
localisation / garanties]`.

### A.3 Volet sous-traitant (art. 30.2) — traitements pour le compte des clients

> À remplir **une ligne par client et par mission** dès que l'agence ou un agent
> IA qu'elle opère accède aux données clients du client. C'est le pendant interne
> de l'annexe B.

| Client (responsable de traitement) | Mission / système concerné | Catégories de traitements réalisés pour son compte | Catégories de données | Sous-traitants ultérieurs (outils, IA) et localisation | Transferts hors UE et garanties | Sécurité | Début / fin |
|---|---|---|---|---|---|---|---|
| *Ex. : Croc Parc* | *Agent IA de réponse / automatisation vente* | *Réponse automatisée aux demandes, relances, statistiques* | *Identité, coordonnées, contenus des demandes, réservations* | *`[plateforme IA]` (UE/US), `[automatisation]`* | *`[CCT / DPF]`* | *MFA, accès délégué, journalisation* | *`[dates]`* |
| *Ex. : École Yoga Doula* | *Site + préparation documentaire* | *Hébergement de formulaires, gestion des inscrits* | *Identité, coordonnées* | *`[hébergeur]`* | | | |

---

## B. Annexe de sous-traitance de données (art. 28 RGPD)

> **Quand la signer** : dès qu'une case « oui » apparaît au bloc 5 du questionnaire
> d'onboarding — c'est-à-dire dès que l'agence (ou un agent IA/automatisation
> qu'elle installe et opère) accède aux données personnelles des clients du client.
> **Rôles** : le client = **responsable de traitement** ; l'agence = **sous-traitant**.
> Les plateformes d'IA et outils SaaS utilisés = **sous-traitants ultérieurs**.
> Cette annexe se joint au contrat cadre ou au contrat d'abonnement.

### ANNEXE — TRAITEMENT DE DONNÉES PERSONNELLES POUR LE COMPTE DU CLIENT

**Annexe au contrat du `[date]` entre** `[Client]` (« le Responsable de
traitement ») **et** `[Prestataire]` (« le Sous-traitant »).

#### 1. Description du traitement

| Rubrique | À compléter |
|---|---|
| Objet et nature du traitement | `[ex. : exploitation d'un agent IA répondant aux demandes clients ; automatisation des relances ; publication assistée]` |
| Finalité(s) | `[ex. : relation client, vente, support]` |
| Durée | Durée du contrat principal |
| Catégories de personnes | `[clients, prospects, visiteurs…]` |
| Catégories de données | `[identité, coordonnées, contenu des messages, historique d'achat…]` — **aucune donnée sensible (art. 9) sauf accord écrit spécifique** |

#### 2. Instructions

Le Sous-traitant traite les données **uniquement sur instruction documentée** du
Responsable (le contrat, la présente annexe et toute instruction écrite
ultérieure). Il l'informe immédiatement si une instruction lui paraît contraire au
RGPD.

#### 3. Engagements spécifiques liés aux systèmes d'IA

> 💬 **Pourquoi cette clause** : c'est la clause différenciante de l'agence — elle
> traduit contractuellement les recommandations CNIL sur l'IA et rassure un
> dirigeant de TPE en langage clair.

Le Sous-traitant s'engage à :
1. **Ne jamais permettre l'entraînement** de modèles d'IA sur les données du
   Responsable : les options de type « n'utilisez pas mes données pour
   l'entraînement » sont activées sur chaque outil, et documentées ;
2. N'envoyer aux plateformes d'IA que les données **strictement nécessaires** à la
   fonction (minimisation), avec anonymisation ou pseudonymisation quand c'est
   possible ;
3. Maintenir une **liste des outils** utilisés (point 5) avec leur localisation et
   leurs garanties, tenue à disposition du Responsable ;
4. Conserver une **supervision humaine** : aucun message généré par IA engageant
   le Responsable (devis, promesse commerciale, réponse à réclamation) n'est
   envoyé sans règle de validation convenue avec lui ;
5. Configurer les agents IA pour qu'ils **n'inventent pas** de données
   personnelles et n'en divulguent pas d'un client à un autre ;
6. Se tenir informé des recommandations de la CNIL applicables aux systèmes d'IA
   et adapter la configuration en conséquence.

#### 4. Confidentialité et sécurité

Le Sous-traitant : garantit la confidentialité (lui-même et toute personne
autorisée) ; met en œuvre des mesures adaptées : authentification forte (MFA),
accès délégués nominatifs, chiffrement des postes et des échanges, gestionnaire de
mots de passe, journalisation des accès aux outils, sauvegardes `[modalités]` ;
notifie au Responsable **toute violation de données dans les meilleurs délais et
au plus tard 48 h** après en avoir eu connaissance, avec les informations
nécessaires à une éventuelle notification CNIL (le Responsable reste titulaire de
l'obligation de notifier sous 72 h).

#### 5. Sous-traitants ultérieurs

5.1. Le Responsable **autorise de manière générale** le recours aux sous-traitants
ultérieurs listés ci-dessous. Toute modification (ajout/remplacement) est notifiée
par écrit au moins `[15]` jours avant ; le Responsable peut s'y opposer pour motif
légitime — en cas de désaccord persistant, chacun peut résilier la prestation
concernée.

| Outil / plateforme | Rôle | Localisation des données | Garanties de transfert |
|---|---|---|---|
| `[Plateforme IA]` | `[génération / agent]` | `[UE / USA]` | `[CCT / Data Privacy Framework]` |
| `[Hébergeur]` | hébergement | | |
| `[Automatisation]` | orchestration | | |

5.2. Le Sous-traitant impose à chaque sous-traitant ultérieur des obligations
équivalentes à la présente annexe et reste pleinement responsable envers le
Responsable.

#### 6. Transferts hors Union européenne

Aucun transfert hors UE sans garanties appropriées (décision d'adéquation,
clauses contractuelles types, certification Data Privacy Framework pour les
prestataires américains) ; les garanties utilisées sont mentionnées au tableau
du point 5.

#### 7. Assistance au Responsable

Le Sous-traitant aide le Responsable, dans la mesure du possible : à répondre aux
demandes d'exercice des droits (accès, rectification, effacement, opposition…) —
toute demande reçue directement est transmise sans délai au Responsable, sans y
répondre lui-même ; à documenter la conformité et, le cas échéant, à réaliser une
analyse d'impact (AIPD).

#### 8. Sort des données en fin de contrat

Au choix du Responsable : **restitution** dans un format lisible puis suppression,
ou **suppression directe**, dans les `[30]` jours suivant la fin du contrat,
copies de sauvegarde comprises (à l'expiration de leur cycle), sauf obligation
légale de conservation. Suppression attestée par écrit.

#### 9. Documentation et audit

Le Sous-traitant met à disposition la documentation nécessaire pour démontrer le
respect de la présente annexe (registre art. 30.2, liste d'outils, mesures de
sécurité) et permet un audit du Responsable, au maximum `[une fois par an]`, avec
un préavis de `[15]` jours, à ses frais, sans accès aux données d'autres clients.

---

Fait à `[ville]`, le `[date]`.

| Le Responsable de traitement (Client) | Le Sous-traitant (Agence) |
|---|---|
| | |

---

## Points à faire arbitrer par l'avocat / DPO (mémo interne, à retirer)

1. Vérifier outil par outil (plateformes IA réellement utilisées) : localisation,
   base de transfert, option no-training — et remplir le tableau 5 avant toute signature.
2. Délai de notification de violation (48 h) : confirmer qu'il est tenable.
3. Cas Croc Parc : si des données de visiteurs mineurs ou des volumes importants
   apparaissent, évaluer la nécessité d'une AIPD côté client.
4. Réévaluation annuelle : besoin d'un DPO ? (non obligatoire a priori à cette échelle).
