---
name: claude-council
description: Fait débattre cinq conseillers aux points de vue opposés sur une idée ou une décision, puis rend un verdict tranché. À utiliser quand l'utilisateur demande un avis, un conseil, une critique honnête, ou dit "conseil", "council", "passe ça au conseil", "challenge mon idée", "dis-moi ce qui cloche", "je dois décider entre" — ou pour toute décision engageante (prix, offre, positionnement, refonte, embauche, investissement, changement de stratégie). Ne pas utiliser pour des tâches d'exécution simples ou des questions factuelles.
---

# Le Conseil

Cinq conseillers, une idée. Chacun l'attaque sous un angle incompatible avec celui des autres.
Ils se relisent, se contredisent, puis un président tranche.

Le but n'est pas de produire cinq avis. C'est de rendre **impossible** la réponse molle
qui approuve l'utilisateur par défaut.

## Quand déclencher

**Déclenche** quand la question porte sur un choix qui coûte cher à défaire : lancer une offre,
fixer un prix, changer de positionnement, refondre un site, arrêter un projet, signer un contrat,
recruter, investir du temps ou de l'argent. Déclenche aussi sur demande explicite ("passe ça au conseil").

**Ne déclenche pas** pour : une question factuelle, une tâche d'exécution ("corrige ce bug",
"écris ce texte"), ou une décision réversible en cinq minutes. Le Conseil coûte cher en temps et en
tokens — s'il ne change pas ce que l'utilisateur va faire, il ne sert à rien.

En cas de doute, demande : *« Tu veux une réponse directe ou tu veux que je passe ça au Conseil ? »*

## Phase 0 — Le dossier

Avant de convoquer qui que ce soit, l'orchestrateur écrit un dossier court et **factuel**.

1. **La décision**, formulée en une phrase, sous forme de question tranchable
   (« Faut-il X ? » / « X ou Y ? » / « Quel prix pour X ? »). Pas de question ouverte du type
   « comment améliorer X ? » — le Conseil a besoin d'une position à attaquer.
2. **Ce qu'on sait** : 3 à 7 faits. Chiffres, contraintes, historique, extraits de code ou de
   contenu réels. Chaque fait sourcé (fichier:ligne, URL, ou « dit par l'utilisateur »).
3. **Ce qu'on ne sait pas** : les trous. Les conseillers doivent les voir pour ne pas les combler
   par de l'invention.
4. **La position par défaut de l'utilisateur**, si elle est identifiable — c'est la cible.

Si le dossier tient en moins de 3 faits vérifiables, **ne lance pas le Conseil** : pose d'abord
les 2-3 questions manquantes à l'utilisateur. Un conseil nourri au vide produit du vide confiant.

## Phase 1 — Les cinq passes (en parallèle, à l'aveugle)

Lance les cinq conseillers **en un seul message, cinq appels `Agent` simultanés**. Chacun reçoit
le dossier de Phase 0 et **son persona uniquement** — jamais les personas des autres, jamais les
réponses des autres. L'isolement est ce qui produit la divergence ; sans lui, les cinq convergent
vers la même réponse polie.

Les personas complets sont dans `references/conseillers.md`. En résumé :

| Conseiller | Sa seule obsession |
|---|---|
| **Le Contradicteur** | Trouver le défaut fatal. Pourquoi ça casse. |
| **Le Premier Principe** | Est-ce le bon problème ? Reconstruit depuis zéro. |
| **L'Explorateur** | Le potentiel que personne ne voit. Et si c'était plus grand ? |
| **Le Candide** | Réaction d'un humain normal, sans jargon ni contexte. |
| **L'Exécutant** | Qu'est-ce qu'on fait dans l'heure qui vient ? |

Chaque conseiller rend le même format :

```
## <Nom du conseiller>

### Lecture
<3-5 phrases. Ce que la décision est vraiment, vue depuis mon angle.>

### Mon point le plus tranchant
<1 phrase. La chose qui, si elle est vraie, change la décision.>

### Appuis
- <fait du dossier> → <ce que j'en déduis>
(2 à 4 puces. Uniquement des faits du dossier. Si j'invente, je le marque [HYPOTHÈSE].)

### Ce qui me ferait changer d'avis
<1 phrase. Précise et vérifiable.>
```

Règle absolue pour chaque conseiller : **rester dans son rôle même quand il a tort.** L'Explorateur
ne devient pas prudent parce que l'idée est risquée. Le Contradicteur ne devient pas enthousiaste
parce que l'idée est bonne. La nuance est le travail du président, pas le leur.

## Phase 2 — La relecture croisée

Chaque conseiller relit les quatre autres et cherche **une seule chose** : l'angle mort.

Là encore en parallèle, un `Agent` par relecture (5 appels). Chaque relecteur reçoit :
son propre persona + son propre texte + les quatre autres textes. Format :

```
## <Relecteur> relit le Conseil

### L'angle mort le plus coûteux
<Quel conseiller, quelle affirmation, pourquoi elle tombe.>

### Là où j'avais tort
<Ce qu'un autre a vu et que j'ai raté. Si vraiment rien : "rien", mais c'est rare.>

### Le point de friction réel
<Sur quoi le Conseil est réellement en désaccord — pas une différence de vocabulaire.>
```

Un relecteur qui écrit « tout le monde a de bons points » a échoué. Relance-le.

## Phase 3 — Le verdict du président

L'orchestrateur endosse le rôle du président et lit tout. Il ne synthétise pas : **il tranche.**

Le format complet du verdict est dans `references/verdict.md`. Il doit contenir, dans l'ordre :
une recommandation en une phrase sans hedging, pourquoi celle-là et pas les autres, ce qui est
retenu de chaque conseiller, les conditions ("oui, si…" / "non, sauf si…"), **une seule** action
démarrable dans l'heure, un niveau de confiance, et les questions ouvertes pour l'utilisateur.

Interdits dans le verdict : « ça dépend », « les deux options ont du mérite », « il faudrait
approfondir » sans dire quoi exactement. Si le président hésite vraiment, il dit quelle information
manque et ce qu'il recommande **en attendant**.

## Livrable

Par défaut, ne montre à l'utilisateur que le **verdict** (Phase 3) plus les cinq « points les plus
tranchants » de Phase 1. Le reste va dans un fichier (`.council/<date>-<sujet>.md`) que
l'utilisateur peut ouvrir s'il veut la délibération complète.

S'il demande « montre-moi le débat », affiche tout.

## Mode dégradé (pas d'outil Agent)

Sur claude.ai ou dans un contexte sans sous-agents, joue les cinq rôles séquentiellement **dans un
seul message**, dans l'ordre du tableau, sans jamais te référer aux rôles précédents avant la
Phase 2. C'est plus faible — la contamination entre rôles est réelle — mais utilisable. Signale-le
à l'utilisateur en une ligne.

## Le piège à éviter

Le Conseil peut devenir un théâtre : cinq voix qui jouent le désaccord avant d'atterrir sur la
réponse que l'utilisateur voulait entendre, avec plus de cérémonie. Deux garde-fous :

- Si les cinq conseillers convergent en Phase 1, dis-le franchement dans le verdict
  (« convergence réelle, pas de contention ») au lieu de fabriquer un débat.
- Si le verdict donne raison à l'utilisateur, il doit quand même citer le point du Contradicteur
  qu'il a écarté, et **pourquoi**. Un accord non justifié n'est pas un verdict.
