# Skills design installés

Trois skills de design front-end, vendorisés au niveau projet (`.claude/skills/`)
pour qu'ils soient disponibles pour toute personne qui ouvre ce dépôt avec Claude Code.

| Dossier | Skill | Source | Commit | Licence |
|---|---|---|---|---|
| `design-taste-frontend/` | Donne une opinion esthétique — anti-templates, vrais systèmes de design, audit avant redesign | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) (`skills/taste-skill`) | `e988add` (2026-07-23) | voir `LICENSE` |
| `animate/` | Construit les animations : faut-il animer, quelle propriété, quelle courbe, quelle durée, interruption et sortie | [emilkowalski/skills](https://github.com/emilkowalski/skills) (`skills/animate`) | `de33dbe` (2026-08-05) | voir `LICENSE` |
| `impeccable/` | Système de design complet, ~23 commandes `/impeccable <verbe>` dont `polish`, `typeset`, `colorize`, `layout`, `audit` | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) v4.0.4 | `aee6ce9` (2026-08-06) | Apache 2.0 |

Les agents `impeccable-*` associés sont dans `.claude/agents/`.

## Utilisation

Les skills se déclenchent automatiquement sur une demande de design, ou explicitement :

```
/impeccable polish index.html      # passe finale avant mise en ligne
/impeccable typeset tarifs.html    # typographie
/impeccable layout balades.html    # espacement, rythme visuel
```

`design-taste-frontend` et `animate` n'ont pas de commande dédiée : ils s'activent
quand on demande une refonte, une page, ou l'ajout de motion.

## Ce qui n'a pas été installé

Impeccable propose aussi des hooks (`PostToolUse` + `Stop`) qui lancent son détecteur
d'anti-patterns après chaque édition de fichier UI. Ils ne sont pas activés ici — ils
modifient le comportement de chaque session. Pour les ajouter, reprendre le bloc `hooks`
de `.claude/settings.json` du dépôt upstream (nécessite Node 22+, présent ici).

## Mise à jour

```bash
npx impeccable update                                                    # impeccable
npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"
```

Ou recopier à la main depuis les dépôts sources aux chemins indiqués ci-dessus.

## Skills voisins non installés

`emilkowalski/skills` contient aussi `review-animations`, `improve-animations`,
`find-animation-opportunities`, `emil-design-eng`, `apple-design`, `prototype`.
`Leonxlnx/taste-skill` contient aussi `redesign-skill`, `brutalist-skill`,
`minimalist-skill`, `soft-skill`, `brandkit`.
