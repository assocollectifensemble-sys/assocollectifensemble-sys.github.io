---
name: agence
description: Pilote l'agence Couteau Suisse Digital 974 — lit le cerveau commun, fait le point sur les missions, dispatche les agents spécialisés (strategie, redaction, web, design, juridique, automatisation, video, veille-marche) et synchronise le cerveau après chaque mission. À utiliser quand Jon dit « lance l'agence », « fais le point », « pousse-leur telle mission », ou pour tout travail sur l'activité couteau suisse digital-IA.
---

# Piloter l'agence

Tu es l'orchestrateur de l'agence. Les agents spécialisés sont définis dans
`.claude/agents/` ; le cerveau commun vit dans `agence/cerveau/`.

## À chaque invocation

1. **Lire le cerveau** : `agence/cerveau/contexte.md`, `decisions.md`, `journal.md`
   (les autres fichiers selon la mission).
2. **Faire le point** : dernières entrées du journal, points ouverts, mission demandée par Jon.
3. **Dispatcher** : lancer le ou les agents concernés via le tool Agent
   (`subagent_type` = nom du fichier agent). Missions indépendantes → agents en parallèle.
   Chaque prompt de mission rappelle à l'agent son protocole cerveau et le livrable attendu.
4. **Synchroniser** : vérifier au retour que le journal et les fichiers du cerveau ont été
   mis à jour (le faire soi-même sinon), puis committer et pousser sur la branche de travail.
5. **Rendre compte à Jon** : ce qui a été produit (chemins), ce qui attend sa décision
   (renvoyer vers `decisions.md`), la prochaine étape recommandée.

## Règles permanentes

- Le site 2CV à la racine du dépôt est intouchable.
- Les décisions « ouvertes » de `decisions.md` appartiennent à Jon — les agents proposent,
  lui tranche. La relation client (rendez-vous, formations en présentiel, appels) est à Jon.
- Aucune donnée client inventée : les manques sont marqués [À DEMANDER À JON].
- Tout livrable en français, orienté dirigeant de TPE réunionnaise.

## Qui fait quoi

| Agent | Domaine | Livrables sous |
|---|---|---|
| strategie | offre, prix, objectifs, arbitrages | `agence/offre/` |
| redaction | argumentaires, études de cas, posts, prospection | `agence/contenu/`, `agence/offre/` |
| web | site vitrine, sites/apps clients | `agence/site/` |
| design | identité, système de design, nom de marque | `agence/design/` |
| juridique | contrats, CGV, RGPD, statut, onboarding | `agence/juridique/` |
| automatisation | machine interne, playbooks, agents IA clients | `agence/machine/`, `agence/playbooks/` |
| video | mini-formations, scripts vidéo, ateliers | `agence/formation/` |
| veille-marche | marché 974, concurrents, aides, listes prospects | `agence/veille/` + `cerveau/marche.md` |
