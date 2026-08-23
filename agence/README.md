# Agence Couteau Suisse Digital 974

Espace de travail de l'activité de Jon : pilotage digital-IA des TPE réunionnaises.
Nom de travail — la marque définitive est une décision ouverte (`cerveau/decisions.md`).

## Arborescence

| Dossier | Contenu | Agent responsable |
|---|---|---|
| `cerveau/` | Mémoire commune : contexte, offre, clients, marché, décisions, journal | tous (protocole) |
| `offre/` | Fiches packs, argumentaires, grilles tarifaires | strategie, redaction |
| `contenu/` | Études de cas, posts, prospection | redaction |
| `site/` | Site vitrine de l'agence (statique portable) | web, design |
| `design/` | Identité visuelle, système de design | design |
| `juridique/` | Contrats types, CGV, RGPD, onboarding | juridique |
| `machine/` | Machine de production interne (CRM, rapports) | automatisation |
| `playbooks/` | Modes opératoires de livraison par pack | automatisation |
| `formation/` | Trames de mini-formations, scripts vidéo, ateliers | video |
| `veille/` | Recherches marché détaillées, listes prospects | veille-marche |

## Fonctionnement

1. Jon (ou l'orchestrateur via `/agence`) définit une mission.
2. L'agent concerné lit le cerveau, produit dans son dossier, met à jour le cerveau
   (journal + fichier concerné).
3. Commit + push sur la branche de travail après chaque mission.

Le plan de référence complet est publié en artifact — lien dans `cerveau/contexte.md`.
