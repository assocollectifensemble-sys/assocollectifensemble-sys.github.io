# Séquence de prospection — « Facture électronique »

> Version 2026-08-23 (agent automatisation).
> Le coin d'entrée commercial (décision 2026-08-23) : vendre le Pack Conformité
> Facture Électronique (`agence/offre/pack-facture-electronique.md`), qui ouvre la relation.
> Cible : TPE/micro du 974 qui facturent d'autres entreprises (liste de 50 cibles — CRM table 1).
> Angle : l'obligation de **réception est déjà en vigueur** (01/09/2026) ; l'émission arrive en sept. 2027.
> Signature des messages : `[NOM_AGENCE — à trancher, decisions.md]`, Jon, [TEL], [SITE].

## Vue de la séquence

| Étape | Canal | Quand | Statut CRM (colonne « Séquence FE ») |
|---|---|---|---|
| Message initial | email (ou WhatsApp si numéro pro public et pas d'email) | J0 | msg1 envoyé |
| Relance 1 | même canal | **J+7** | relance1 |
| Relance 2 (la dernière) | même canal | **J+21** | relance2 |
| Appel de 2 min | téléphone | entre relance 1 et 2, ou après relance 2 | appel fait |
| Sortie | — | réponse, RDV, refus ou fin de séquence | sortie / Opposé |

**3 messages maximum + 1 appel. Après, silence = « Plus tard » (réveil dans 6 mois, à l'approche de l'échéance émission 2027) — jamais de harcèlement : on recroisera ces dirigeants au marché.**

## Message initial — email

Objet : `Factures électroniques — [ENTREPRISE] est-elle prête ?`

```
Bonjour [PRÉNOM],

Depuis le 1er septembre, toute entreprise — même une micro — doit pouvoir
RECEVOIR des factures électroniques via une plateforme agréée. Et en
septembre 2027, il faudra aussi les ÉMETTRE.

Beaucoup de patrons du secteur [SECTEUR/COMMUNE] ne sont pas encore raccordés,
et le risque est concret : des factures fournisseurs qui ne vous arrivent plus,
des litiges, des retards.

Je suis [PRÉNOM_JON], basé à [COMMUNE_JON]. Je mets les TPE réunionnaises en
règle en 10 jours : choix de la plateforme adaptée à VOTRE cas, installation,
reprise de vos fiches clients, test avec une vraie facture, et je vous forme.
Forfait ferme : 690 € (ou 1 290 € si plusieurs personnes facturent). Si un
simple logiciel à 20 €/mois vous suffit, je vous le dirai aussi — c'est déjà
arrivé.

15 minutes au téléphone cette semaine pour voir où vous en êtes ?
[PRÉNOM_JON] — [TEL]

—
[NOM_AGENCE], [ADRESSE], [SIREN].
Vous ne souhaitez plus recevoir de messages de ma part : répondez « STOP »
et je vous retire immédiatement de ma liste.
```

## Message initial — WhatsApp (numéro professionnel public uniquement)

```
Bonjour [PRÉNOM], ici [PRÉNOM_JON] de [NOM_AGENCE] ([COMMUNE_JON]). Je contacte
les patrons de [SECTEUR/COMMUNE] au sujet de la facturation électronique :
la réception est obligatoire depuis le 1er septembre, et beaucoup ne sont pas
raccordés. Je mets les TPE en règle en 10 jours, forfait ferme 690 €, testé
avec une vraie facture, formation comprise. Est-ce que 15 min au téléphone
cette semaine vous iraient pour faire le point ? (Si vous ne voulez pas être
recontacté, dites-le-moi simplement et je vous retire de ma liste.)
```

Règle WhatsApp : premier contact UNIQUEMENT vers un numéro affiché publiquement à titre professionnel (fiche Google, site, page FB pro). Message individuel, personnalisé, envoyé à la main — **jamais d'envoi en masse ni d'outil de diffusion automatique** (risque de blocage du numéro de Jon par WhatsApp + image dégradée). En cas de doute sur le numéro : email ou passage terrain.

## Relance 1 (J+7) — l'angle utile

Objet : `Re: Factures électroniques — le test en 2 minutes`

```
Bonjour [PRÉNOM],

Un test simple pour savoir si vous êtes concerné : demandez à votre
expert-comptable « sur quelle plateforme agréée est-ce que je reçois mes
factures ? ». S'il n'y a pas de réponse claire, c'est qu'il y a un trou.

Je peux faire ce point avec vous en 15 minutes, sans engagement. Et si vous
êtes déjà en règle, tant mieux — je vous le confirme et on en reste là.

[PRÉNOM_JON] — [TEL]
```

## Relance 2 (J+21) — la dernière, on l'annonce

Objet : `Re: Factures électroniques — dernier message`

```
Bonjour [PRÉNOM],

Dernier message de ma part sur ce sujet, promis. L'échéance suivante (émettre
ses factures en électronique) tombe en septembre 2027 : ceux qui s'y mettent
tôt choisissent leur plateforme tranquillement, les autres prendront ce qui
reste, dans l'urgence.

Ma porte reste ouverte : [TEL], ou répondez à ce message quand le sujet
remontera sur votre pile. Bonne continuation à [ENTREPRISE].

[PRÉNOM_JON]
```

## Script d'appel — 2 minutes montre en main

> À passer aux heures creuses du métier ciblé (artisans : 12 h–13 h 30 ou après 16 h 30 ;
> commerces : avant l'ouverture). Souriant, debout, droit au but.

1. **Ouverture (15 s)** — « Bonjour, [PRÉNOM_JON], de [NOM_AGENCE] à [COMMUNE_JON]. Je vous ai écrit au sujet de la facturation électronique — je vous dérange pas plus de deux minutes, c'est bon pour vous ? » *(Si non : « Quel moment vous arrange mieux ? » → noter et rappeler À CE MOMENT-LÀ.)*
2. **La question qui qualifie (30 s)** — « Question simple : aujourd'hui, vous savez sur quelle plateforme agréée vous recevez vos factures fournisseurs ? » *(90 % : non / c'est quoi.)*
3. **Le cadre (30 s)** — « C'est obligatoire depuis le 1er septembre pour tout le monde, même les micros. Et en 2027, il faudra aussi émettre comme ça. Concrètement, mal raccordé, ce sont des factures qui n'arrivent plus et des embrouilles avec les fournisseurs. »
4. **L'offre (30 s)** — « Ce que je fais : je regarde votre cas, je choisis la plateforme adaptée, j'installe, je reprends vos fiches clients, on teste avec une vraie facture et je vous forme. Dix jours, forfait ferme 690 €. Et si un logiciel simple suffit chez vous, je vous le dis et ça s'arrête là. »
5. **La clôture (15 s)** — « Le plus simple : je passe faire l'état des lieux, c'est 30 minutes chez vous. Plutôt mardi ou jeudi ? » *(Objection → réponses de la fiche pack, section objections. Refus net → « Compris, je vous retire de ma liste. Bonne journée. » → CRM : Opposé.)*

## Règles B2B (à respecter à la lettre)

1. **Cibles B2B uniquement**, sur coordonnées professionnelles, avec un message **en rapport avec la fonction** du destinataire (dirigeant → obligation de facturation de son entreprise : c'est le cas). C'est ce qui permet la prospection email B2B sans consentement préalable (régime opt-out).
2. **Identification claire** dans chaque message : qui écrit, pour quelle entreprise, coordonnées complètes (nom, adresse, SIREN en pied d'email).
3. **Moyen de désinscription simple dans CHAQUE message** (réponse « STOP » suffit — pas de lien compliqué). Toute demande = statut **« Opposé » dans le CRM le jour même, définitif, tous canaux**.
4. **3 messages + 1 appel maximum** par séquence. Réveil unique possible à ~6 mois (angle « émission 2027 ») sauf statut Opposé.
5. Constitution de la liste : sources publiques et professionnelles (annuaires pro, fiches Google, pages FB pro, réseau CCI/CMA). Noter la source dans le CRM (obligation d'information : en cas de question « d'où avez-vous mon contact ? », on répond précisément).
6. Numéros de téléphone : vérifier que l'entreprise démarchée n'exprime pas d'opposition au démarchage ; en cas de doute sur une ligne perso/pro mélangée (courant en TPE), privilégier l'email.
7. **Aucun envoi en masse automatisé au lancement** : les messages partent un par un, personnalisés ([SECTEUR/COMMUNE] réellement adaptés). À 50 cibles, la personnalisation EST la stratégie ; un outil d'emailing ne se justifie qu'au-delà, et avec les mêmes règles.

## Automatisation de la séquence (minimale, avec reprise manuelle)

| Quoi | Outil | Condition d'échec | Reprise manuelle |
|---|---|---|---|
| Génération des messages personnalisés | IA (prompt : « adapte le gabarit à [ENTREPRISE, SECTEUR, COMMUNE, source] ») puis relecture Jon avant CHAQUE envoi | personnalisation fausse (mauvais secteur) | jamais d'envoi sans lecture — l'erreur de personnalisation grille un prospect à vie |
| Rappels J+7 / J+21 | dates « prochaine action » du CRM (vue Aujourd'hui) | date non saisie à l'envoi | règle CRM n°2 : aucune ligne sans prochaine action datée |
| Suivi des réponses | boîte mail + CRM à la main | réponse ratée (spam, WhatsApp non lu) | passage boîte mail dans la routine quotidienne (matin) |

## RGPD

La liste de prospection contient des données personnelles (nom, contact de dirigeants) : traitement en responsabilité propre de l'agence → registre volet responsable de traitement (`agence/juridique/rgpd.md`), base légale intérêt légitime (prospection B2B ciblée et proportionnée), information à première demande, droit d'opposition respecté sans délai (liste Opposé), conservation 3 ans après dernier contact. Pas d'enrichissement par achat de fichiers au lancement.

## Mesure de la séquence (revue à la routine hebdo)

Taux de réponse au message 1, RDV obtenus / 10 séquences, packs signés / RDV. Si < 1 RDV pour 10 séquences complètes après les 20 premières : revoir l'angle (tester l'entrée « votre expert-comptable vous en a parlé ? ») plutôt qu'augmenter le volume.
