# Playbook — Pack Présence (2 400 €)

> Mode opératoire de livraison. Version 2026-08-23 (agent automatisation).
> Fiche vendue : `agence/offre/pack-presence.md`. Délai vendu : 3 semaines.
> Onboarding : `agence/juridique/onboarding-client.md` (les blocs 2, 3 et 4 sont vitaux ici).

## Temps cible

| | Temps homme réel | Délai calendaire |
|---|---|---|
| 1re livraison | **8 jours** (le thème de base, les gabarits de pages et les checklists se construisent ici) | 3 semaines |
| Livraisons suivantes | **4 jours** (objectif ÷2 — c'est le chiffrage de la fiche : ~4 j à 600 €/j) | 3 semaines |

Ce qui fait le ÷2 : un **site-mère réutilisable** (thème + 7 gabarits de pages TPE), la checklist contenus client standardisée, et les prompts de rédaction ci-dessous. Le délai calendaire ne bouge pas : il est dicté par les allers-retours client, pas par la production.

## Déroulé semaine par semaine

### Semaine 1 — cadrage et collecte (le goulot, à verrouiller d'entrée)

| Jour | Étape | Durée |
|---|---|---|
| J1 | **Réunion de lancement sur site** : onboarding complet, choix du nom de domaine, ton (créole/français), remise de la **checklist contenus** (photos, textes, tarifs, logo — à fournir sous 7 jours, écrit noir sur blanc) | 2 h |
| J1 | Achat domaine + hébergement **au nom du client** (règle : les comptes restent au client, Jon en accès délégué), création email pro | 1 h |
| J2 | Régularisation des accès existants : domaine chez un tiers, page FB d'un ancien prestataire, Google Business non revendiqué → tout récupérer AVANT de construire (voir pièges) | 0,5–2 h |
| J3–J5 | Structure du site + textes v1 générés (prompts ci-dessous) pendant que le client rassemble ses contenus ; relance douce à J5 si rien reçu | 0,5 j |

### Semaine 2 — production

| Jour | Étape | Durée |
|---|---|---|
| J8 | Séance photos/contenus chez le client si les siennes sont inutilisables (prévu dans le prix : 1 j terrain, fiche) | 0,5 j |
| J8–J10 | Montage du site (5–7 pages) sur le gabarit : vraies photos, vrais mots, mobile d'abord, formulaire testé (email de réception vérifié), bouton WhatsApp | 1,5 j |
| J10 | Fiche Google Business : création/revendication, catégories, horaires, zone, photos, 1er jeu de posts | 0,5 j |
| J11 | FB/IG : visuels profil + bannière, section infos, lien WhatsApp Business, 5 posts prêts (prompt n°3) | 0,5 j |
| J12 | Statistiques de visite installées (outil simple, sans bandeau cookies si possible — voir RGPD), envoi du lien de recette au client : **7 jours pour valider** | 1 h |

### Semaine 3 — recette, formation, clôture

| Jour | Étape | Durée |
|---|---|---|
| J15–J17 | Intégration des retours (1 tour de corrections inclus — le 2e se négocie, sinon dérive) | 0,5 j |
| J18 | Mise en ligne définitive, tests croisés (mobile, formulaire, WhatsApp, vitesse) | 2 h |
| J19–J21 | **Formation sur poste (2 h)** : modifier le site, publier un post, répondre à un avis. Mémo remis. Puis les **deux options écrites** : autonomie complète ou abonnement Essentiel 150 €/mois (hébergement année 2 inclus dans l'abonnement) | 0,5 j |
| J21 | CRM : date anniversaire hébergement (relance M+10), niveau d'abonnement proposé, réponse | 15 min |

## Checklist de livraison

- [ ] Domaine + hébergement au nom du client, année 1 payée, accès délégués notés (tableau accès de l'onboarding §3)
- [ ] Site 5–7 pages en ligne : accueil, prestations, à propos, contact, avis — lisible sur téléphone (testé sur un vrai)
- [ ] Formulaire de contact testé de bout en bout (le mail ARRIVE chez le client, pas en spam)
- [ ] Email pro créé et configuré sur le téléphone du client
- [ ] Bouton WhatsApp fonctionnel (numéro Business vérifié)
- [ ] Fiche Google Business revendiquée, complète, 1er jeu de posts publié
- [ ] FB/IG : profils propres, infos complètes, 5 posts prêts validés par le client
- [ ] Statistiques installées ET montrées au client
- [ ] Formation 2 h faite, mémo remis, le client a modifié une page LUI-MÊME devant Jon
- [ ] Mentions légales + politique de confidentialité posées sur le site (trames `agence/juridique/`)
- [ ] Options écrites autonomie / Essentiel remises ; CRM à jour (anniversaire hébergement M+10)

## Outils

- CMS habituel de Jon (WordPress ou équivalent) avec **un thème/gabarit unique réutilisé** pour tous les packs — l'outil le plus simple qui marche, pas un builder nouveau par client.
- Registrar/hébergeur unique de référence (compte client, carte client).
- Google Business Profile, Meta Business Suite, WhatsApp Business.
- Canva (visuels profil/bannière, gabarits dupliqués par client).
- Statistiques : outil léger sans cookies de préférence (sinon bandeau requis).
- Checklist contenus client (1 page, remise à J1 — réutilisable telle quelle).

## Prompts types réutilisables

**Prompt 1 — architecture + textes du site :**
```
Tu écris le site vitrine d'une TPE réunionnaise. Activité : [ACTIVITE_EN_UNE_PHRASE].
Clients : [CIBLE]. Zone : [VILLE/ZONE, La Réunion]. Ton : [TON — ex. chaleureux,
vouvoiement, français avec expressions locales sobres]. Différence clé : [DIFFERENCIATEUR].
Produis pour chaque page (accueil, prestations, à propos, contact, avis) : titre,
sous-titre, sections avec textes courts, appel à l'action. Interdits : superlatifs
creux, jargon, promesses invérifiables. Les textes seront relus et incarnés avec
les vrais mots du client recueillis en réunion : [VERBATIMS_CLIENT].
```

**Prompt 2 — fiche Google Business :**
```
Rédige pour une fiche Google Business : description (750 car. max) + 4 posts de
lancement pour [ACTIVITE] à [VILLE], La Réunion. Catégorie principale : [CATEGORIE].
Mots que tapent les clients : [REQUETES — ex. « plombier Saint-Pierre »]. Ton direct,
concret, sans emoji excessif. Chaque post : 1 info utile + 1 appel à l'action.
```

**Prompt 3 — les 5 premiers posts réseaux :**
```
Écris 5 posts Facebook/Instagram de lancement pour [ACTIVITE] ([VILLE], 974).
Trame : 1 présentation, 1 coulisses, 1 avant/après ou réalisation, 1 question à
la communauté, 1 offre/appel. Ton : [TON]. Longueur : 3–6 lignes + hashtags
locaux sobres. Le client validera chaque post avant publication.
```

## Livrables types

Site en ligne · fiche Google Business active · profils sociaux d'équerre + 5 posts · email pro · mesure installée · mémo de formation (2–4 pages) · tableau des accès remis au client.

## Pièges connus

- **La collecte de contenus qui traîne** — LE tueur de délai. Parade : checklist remise à J1 avec date butoir écrite, séance photos de secours prévue S2, et clause « le délai de 3 semaines court à réception des contenus » (déjà dans la fiche).
- **Construire sur un existant non maîtrisé** : domaine au nom d'un ancien prestataire, page FB dont personne n'a le mot de passe. Régulariser à J2 ou acter par écrit qu'on repart de zéro.
- **Le 3e tour de corrections.** Un tour inclus, écrit à J1. Au-delà : petites retouches offertes si < 30 min, sinon devis ou bascule abonnement (« c'est exactement ce que couvre l'heure mensuelle d'Essentiel »).
- **Livrer un site sans que le formulaire arrive** (SPF/DKIM, spam). Test réel obligatoire depuis un téléphone externe.
- **Faire la formation en dernier jour sans matière** : garder 2–3 modifications réelles À FAIRE PAR le client pendant la formation — c'est le critère d'autonomie.
- **Oublier mentions légales / confidentialité** : le site engage l'image ET la conformité du client.

## RGPD / données personnelles

Le formulaire de contact et les statistiques collectent des données personnelles **pour le compte du client** : mentions d'information sur le formulaire, politique de confidentialité, outil de mesure léger (ou bandeau de consentement). Si Jon gère ensuite la boîte mail ou les messages du client (abonnement), c'est un traitement en sous-traitance → annexe `agence/juridique/rgpd.md`.

## Critère de « fini »

> Le site est en ligne sur le domaine du client, le formulaire et le WhatsApp aboutissent réellement, la fiche Google et les réseaux sont actifs, ET le client a fait une modification lui-même devant Jon pendant la formation. Les deux options écrites (autonomie / Essentiel) sont remises. Un site en ligne avec un client qui ne sait pas le toucher n'est PAS fini — l'autonomie est dans la promesse.
