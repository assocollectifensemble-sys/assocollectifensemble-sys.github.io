# État des lieux SEO/GEO yoga-doula.eu — 7 août 2026

Vérifié via Search Console, connecteur WordPress et analyse du code source en direct.
Ce document remplace les parties périmées du BRIEF et de la PASSATION du 15 juillet.

---

## Ce que le brief disait, et qui est faux aujourd'hui

| Le brief dit | Réalité au 7 août |
|---|---|
| 🔴 Le sitemap est en 404, problème n°1 | ✅ **Réglé.** `sitemap_index.xml` répond 200, généré par Rank Math, soumis le 15/07, retéléchargé par Google le 4 août, 0 erreur, 48 URLs |
| ⚠️ Doublon possible de la page PYM | ✅ **Pas de doublon.** L'ancienne URL redirige en 301 vers `/formation-yoga-maternite/`. Canonique tranchée |
| La page PYM est à optimiser (titre, méta) | ✅ **Déjà fait**, et bien fait. Je n'y ai pas touché |
| Installer WPCode pour le snippet | ❌ Inutile — **Code Snippets** est déjà installé et actif |
| 4 brouillons existants | ❌ Il y en a **7**, tous du 15/07 |
| Deadline mi-août | ⚠️ **Il reste 8 jours.** Le plan en 9 étapes du brief ne tient pas dans ce délai |

**Toujours vrai :** les champs Rank Math ne sont pas écrivables via l'API (retesté le 7/08 sur l'article 12052 — seuls `_acf_changed`, `footnotes` et les 5 champs Elementor sont exposés).

---

## La donnée Search Console (12 mois glissants)

### Le paradoxe « doula »

| | Impressions | Position | Clics |
|---|---|---|---|
| requête « doula » | **68 868** | 2,0 | **18** (CTR 0,0 %) |
| page `/qu-est-ce-qu-une-doula/` | **86 646** | 4,3 | 91 (CTR 0,1 %) |

86 000 affichages pour 91 clics : ce n'est pas un lien bleu, c'est une citation en AI Overview / People Also Ask. Le brief avait raison de dire de ne pas pleurer cet « acquis ».

**La chute de mai n'est pas résorbée.** 90 derniers jours vs 90 précédents :
- « doula » : **17 090 → 3 658 impressions (−79 %)**, position 2,0 → 3,6
- aucune requête ne récupère

### Les fruits mûrs, par rentabilité

| Requête | Impr./an | Position | Page qui remonte |
|---|---|---|---|
| **formation yoga prénatal** | 1 649 | **31,9** | PYM — la cible n°1 de la campagne d'octobre |
| formation doula | 1 828 | 21,0 | page formation YD |
| doula formation | 1 790 | 14,4 | page formation YD |
| doula def / definition / signification | ~6 300 cumulé | ~11 | article 5751 |
| formation doula en ligne | 723 | 27,7 | aucune page dédiée |
| formation yoga pré et post natal | 482 | 40,7 | PYM |
| mantra accouchement | 1 079 | 8,2 | article 9450 ✅ 465 clics/an |
| yoga prénatal + [ville] | ~2 500 cumulé | 7–16 | annuaire cours yoga ✅ |

### Les deux trous béants

1. **« yoga prénatal » seul (2 900/mois) n'apparaît nulle part** dans le top 150. Le site ne capte que les variantes par ville via l'annuaire. → traité par l'article 12200.
2. **« yoga femme enceinte » (880/mois) : aucune page.** L'ancienne page « Maternité & yoga » (ID 691) est passée en privé. → traité en mot-clé secondaire de 12200, pour éviter la cannibalisation.

---

## Les défauts techniques trouvés dans le code source

| Défaut | Où | Gravité |
|---|---|---|
| **4 schemas `FAQPage` concurrents** (16 Q/R) | page PYM | 🔴 aucune FAQ ne remonte |
| **Aucun schema `Course`** ; la page est typée `Article` | page PYM | 🔴 invisible pour les IA sur « quelle formation » |
| **9 balises H1** | page d'accueil | 🟠 signal dilué |
| **8 balises H1** | page Formation Yoga Doula | 🟠 idem |
| « plus de 15 ans » | page Formation Yoga Doula | 🟠 sous-vend GJK (19 ans d'école, 46 ans de pratique) |
| 3 articles publiés en « Uncategorized » | 5751, 9450, 10032 | ⚪ |

*(Note : la page Formation Yoga Doula émet bien `Course` + `EducationalOrganization`. C'est la page PYM, celle de la campagne, qui est la moins bien balisée.)*

---

## Inventaire du blog au 7 août 2026

### Publiés (non touchés)
| ID | Titre | Note |
|---|---|---|
| 5751 | Qu'est-ce qu'une doula | 86 646 impr./an, refonte en cours ailleurs, auteur = Fabien Sayer |
| 9450 | Mantras pendant l'accouchement | 465 clics/an — le meilleur article du site |
| 10032 | Formation IVG médicamenteuse | |

### Brouillons retravaillés aujourd'hui (7 + 3 nouveaux)
| ID | Titre | Cluster |
|---|---|---|
| 12049 | Le métier de doula est-il reconnu en France ? | Doula |
| 12051 | Comment devenir doula en France *(pilier)* | Doula |
| 12054 | Combien gagne une doula en France ? | Doula |
| 12055 | Doula et enseignante de yoga prénatal | Doula ↔ Yoga |
| 12058 | Devenir doula sans diplôme | Doula |
| 12059 | Devenir doula salariée | Doula |
| 12060 | Doula de fin de vie | Doula |
| **12200** | **Yoga prénatal *(pilier, nouveau)*** | Yoga |
| **12201** | **Yoga postnatal *(nouveau)*** | Yoga |
| **12202** | **Devenir prof de yoga prénatal *(nouveau)*** | Yoga → PYM |

### À jeter
| ID | Titre | Pourquoi |
|---|---|---|
| 9043 | Fêtes de fin d'année (2023) | 531 Ko de résidus Word, 85 % copié-collé d'un autre article |
| 12052 | [V2 – test Claude] | article de test, sert de bac à sable pour le snippet |

---

## Ce qui a été fait aujourd'hui (via API, sans intervention humaine)

1. **Les 7 brouillons réattribués à Gurujagat Ronen (ID 2)** — ils étaient tous signés Jonathan (ID 5), ce qui annulait l'avantage E-E-A-T.
2. **Erreurs factuelles corrigées** : « 275 heures » → 261 h · « plus de 500 personnes formées » (invérifiable) supprimé · « depuis plus de quinze ans » → depuis 2007 · « prochaine session janvier 2027 » → session 2027-2028.
3. **Phrase corrompue réparée** dans l'article 12059 (« au prix, il est vrai, de la ée » — texte cassé au milieu d'un paragraphe).
4. **Maillage interne** : chaque article passe de 1-3 liens à 5-8 liens internes, avec un bloc « Aller plus loin » standardisé.
5. **Conformité YMYL** : chaque article se termine par un renvoi explicite vers la sage-femme ou le médecin, et par la signature E-E-A-T de GJK (École 2007, yoga doula depuis 1980).
6. **FAQ ajoutée** à l'article 12055, qui n'en avait pas.
7. **Catégorie « Yoga périnatal » créée** (ID 27) — le cluster A n'existait pas.
8. **3 articles piliers du cluster Yoga écrits** (12200, 12201, 12202), en brouillon, signés GJK, avec 3 emplacements `[GJK]` à compléter par elle.

## Ce qui reste bloqué côté humain

Voir `04-a-faire-jonathan.md`. Dans l'ordre : Bing Webmaster Tools → snippet Rank Math → Elementor (FAQ + H1) → validation GJK.
