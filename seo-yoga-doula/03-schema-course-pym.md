# Schema `Course` pour la page Programme Yoga Maternité

**Page concernée :** `https://yoga-doula.eu/formation-yoga-maternite/` (ID 7018)

## Le constat (vérifié dans le code source le 7 août 2026)

La page émet actuellement 5 blocs de données structurées :

| Type détecté | Nombre | Verdict |
|---|---|---|
| `FAQPage` | **4 blocs, 16 questions** | 🔴 **problème** — quatre FAQ concurrentes sur une même page |
| `Article` | 1 | ⚠️ type inadapté pour une page de formation |
| `Organization`, `WebSite`, `WebPage`, `Person`, `BreadcrumbList`, `ImageObject` | 1 chacun | ✅ normal, généré par Rank Math |
| **`Course`** | **0** | 🔴 **absent** |

À titre de comparaison, la page *Formation Yoga Doula* émet bien `Course` + `EducationalOrganization`.
**La page commerciale de la campagne d'octobre est donc la moins bien balisée des deux.**

## Pourquoi ça compte

Le schema `Course` est ce qui permet à Google — et surtout aux IA type ChatGPT ou Perplexity — de comprendre que cette page décrit *une formation*, avec une durée, un prix, un format et des dates. Sans lui, la page est vue comme un simple article de blog. C'est exactement le balisage qui décide si l'École apparaît quand quelqu'un demande « quelle formation pour enseigner le yoga prénatal en France ? ».

---

## Méthode recommandée : le générateur intégré de Rank Math

**Ne colle pas de JSON-LD à la main.** Rank Math sait générer ce schema proprement, et il évite les doublons.

1. Ouvre la page **Programme Yoga Maternité** dans WordPress.
2. En bas de l'éditeur → onglet **Rank Math** → **Schéma** → **Générateur de schéma**.
3. Si un schéma **Article** est actif : **supprime-le**.
4. Choisis **Course** et remplis :

| Champ Rank Math | Valeur à saisir |
|---|---|
| Course Name | `Programme Yoga Maternité` |
| Description | `Formation à l'enseignement du yoga prénatal et postnatal. 84 heures en format hybride (en ligne et présentiel), session d'octobre 2026 à juin 2027.` |
| Course Provider | `École Internationale Yoga Doula` |
| Provider URL | `https://yoga-doula.eu/` |
| Course Mode | `Blended` (hybride) |
| Workload / durée | `84 heures` |
| Date de début | `2026-10-01` *(à corriger avec la date exacte du calendrier)* |
| Date de fin | `2027-06-30` *(idem)* |
| Prix | `1050` |
| Devise | `EUR` |
| Langue | `fr` |

5. **Enregistre**, puis vérifie sur <https://search.google.com/test/rich-results> en collant l'URL de la page.

---

## Le vrai chantier : les 4 `FAQPage` concurrents

C'est plus important que le `Course`. Quatre FAQ déclarées sur une même page, Google n'en retient aucune — et on perd les 16 questions/réponses qui pourraient remonter en résultats enrichis.

**Origine probable :** les widgets « Accordéon / FAQ » d'Elementor et d'ElementsKit émettent chacun leur propre schema FAQ, en plus de celui de Rank Math.

**Ce qu'il faut faire (dans Elementor, donc côté toi ou Fabien) :**

1. Ouvre la page avec Elementor.
2. Repère chaque widget FAQ / Accordéon / Toggle.
3. Dans les réglages de chaque widget, cherche une option du type **« Schema FAQ »**, **« FAQ Schema »** ou **« Structured data »** → **désactive-la sur tous les widgets sauf un**.
4. Si l'option n'existe pas sur ces widgets : désactive plutôt le **module FAQ de Rank Math** pour cette page (Rank Math → Schéma → retirer le bloc FAQPage), et ne garde que celui d'Elementor.
5. **Publie** (dans Elementor, « Enregistrer » ne suffit pas — il faut « Publier »).
6. Redonne-moi signe : je revérifie le code source en 30 secondes et je te confirme qu'il ne reste qu'un seul `FAQPage`.

**Règle simple à retenir :** un seul bloc FAQ déclaré par page. Deux, c'est déjà pire que zéro.

---

## Bonus : les H1 multiples

| Page | Nombre de H1 | Devrait être |
|---|---|---|
| Accueil | **9** | 1 |
| Formation Yoga Doula | **8** | 1 |
| Programme Yoga Maternité | 1 ✅ | — |

Quentin l'avait déjà signalé en mars 2023. C'est un réglage de widget Elementor : dans chaque widget « Titre », il y a un menu déroulant **HTML Tag** — il faut passer les titres secondaires de `H1` à `H2`, et n'en garder qu'un seul en `H1` par page.

Sur la page Formation Yoga Doula, le H1 unique devrait être : **« Formation de doula & yoga périnatal »** (aujourd'hui c'est « Deviens DOULA », qui ne contient pas le mot-clé « formation doula » sur lequel la page est en position 21 avec 1 828 impressions par an).
