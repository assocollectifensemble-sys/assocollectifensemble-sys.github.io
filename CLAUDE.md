# Guide du dépôt

Ce dépôt contient deux choses distinctes :

## 1. Le site « Une 2CV, mille histoires » (racine)

Site GitHub Pages en production : `index.html`, `balades.html`, `mariage.html`,
`contact.html`, `faq.html`, etc., générés via `build.py`.
**Ne pas modifier ces fichiers dans le cadre des missions de l'agence.**

## 2. L'agence Couteau Suisse Digital 974 (`agence/` + `.claude/`)

Espace de travail de l'activité de Jon : accompagnement digital-IA des TPE
réunionnaises (interlocuteur unique — sites, réseaux, automatisation, agents IA,
apps, vidéo/formation).

- **Cerveau commun** : `agence/cerveau/` — contexte, offre, clients, marché,
  décisions, journal. Toute mission commence par sa lecture et finit par sa mise à jour.
- **Agents** : `.claude/agents/` — strategie, redaction, web, design, juridique,
  automatisation, video, veille-marche. Chaque agent porte son protocole dans son fichier.
- **Pilotage** : skill `/agence` (`.claude/skills/agence/SKILL.md`) — point,
  dispatch des agents, synchronisation du cerveau.
- **Branche de travail** : `claude/reunion-ai-business-ideas-ovs7xh`.

Règles transverses : décisions « ouvertes » de `agence/cerveau/decisions.md` = Jon
tranche ; aucune donnée client inventée ; livrables en français.
