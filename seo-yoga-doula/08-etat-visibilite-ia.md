# État de la visibilité côté IA — vérifié le 7 août 2026

Vérifications faites après que Bing Webmaster Tools a été configuré.

## Ce qui est en place ✅

| | État |
|---|---|
| Sitemap XML | ✅ répond 200, 48 URLs, retéléchargé par Google le 4 août |
| Sitemap déclaré dans robots.txt | ✅ ligne présente |
| Bing Webmaster Tools | ✅ fait le 7 août — **c'était le vrai verrou pour ChatGPT** |
| Robots d'IA autorisés à crawler | ✅ voir ci-dessous |
| Schema `Course` sur la formation de doula | ✅ présent, avec `EducationalOrganization` |

## Les robots d'IA : autorisés, mais par défaut

Contenu réel du `robots.txt` au 7 août :

```
User-agent: *
Disallow: /wp-admin/
Allow: /wp-admin/admin-ajax.php
Disallow: /wp-content/uploads/wpforms/
Disallow: /wp-content/uploads/wpo/wpo-plugins-tables-list.json
Sitemap: https://yoga-doula.eu/sitemap_index.xml
```

**Aucun robot d'IA n'est nommé** — ni GPTBot, ni OAI-SearchBot, ni ClaudeBot, ni PerplexityBot, ni Google-Extended.

C'est une bonne nouvelle : la règle `User-agent: *` les autorise tous implicitement. Rien ne bloque. Il n'y a **rien à ajouter** — un `Allow` explicite ne changerait strictement rien.

**Le seul angle mort :** certains hébergeurs et Cloudflare bloquent les robots d'IA au niveau du pare-feu, sans que ça apparaisse dans robots.txt. Si dans deux mois rien ne bouge côté ChatGPT alors que Bing indexe bien, c'est la première piste à creuser avec Fabien (dans Cloudflare : Security → Bots → « Block AI Scrapers and Crawlers » doit être **désactivé**).

## Ce qui manque encore

### 1. 🟠 Pas de `llms.txt` — vérifié, renvoie 404

`https://yoga-doula.eu/llms.txt` → **404**.

Si `robots.txt` dit aux robots ce qu'ils ont le droit de lire, `llms.txt` leur dit **ce qu'il faut retenir** : un résumé en texte brut de ce qu'est le site, ce qu'il propose, quelles pages comptent — sans avoir à déchiffrer le HTML d'Elementor.

Ce n'est pas encore un standard officiel, et Google ne s'en sert pas. Mais sur le terrain précis de la recommandation par les IA, c'est un des rares leviers directs disponibles, et presque personne ne l'a mis en place.

**Le fichier est écrit et prêt** : `07-snippet-llms-txt.php`. Il contient déjà tout — les deux formations avec leurs vrais volumes horaires, tarifs et dates, la bio de Gurujagat, les précisions factuelles sur le métier de doula (non réglementé, pas de CPF), les annuaires par ville. À coller dans Code Snippets quand tu es à l'ordinateur.

À mettre à jour une fois les 10 articles publiés.

### 2. 🔴 Schema `Course` absent sur la page Programme Yoga Maternité

Toujours le point n°1 pour la campagne d'octobre. C'est exactement ce balisage qui permet à une IA de répondre « le Programme Yoga Maternité de l'École Yoga Doula, 84 h, hybride, 1 050 € » plutôt que de ne rien dire.
Mode d'emploi dans `05-tutos-mobile.md`, section 3.1. Ça se fait dans Rank Math, sans ouvrir Elementor.

### 3. 🟡 Double balise `<meta name="description">` sur les articles

Découvert en analysant le code source de l'article « Mantras pendant l'accouchement ». La page contient **deux** balises de description :

1. `Quels sont les effets des mantras pendant la grossesse…` ← celle de Rank Math (la bonne)
2. `Cet article explore les bienfaits des mantras…` ← l'extrait de l'article, injecté par autre chose

La seconde est insérée tard dans le `<head>`, juste après Site Kit — c'est le **thème** qui l'ajoute, pas un plugin SEO. Les pages (PYM, accueil) n'ont qu'une seule balise : le problème est spécifique aux **articles**.

**Conséquence réelle : faible.** Google lit la première et ignore la seconde. Mais c'est une incohérence, et pour un modèle d'IA qui parse le `<head>`, deux descriptions contradictoires, c'est du bruit.

**C'est une tâche pour Fabien** : identifier la ligne du thème (probablement dans `header.php` ou une fonction accrochée à `wp_head`) qui émet cette seconde balise, et la retirer. Cinq minutes pour quelqu'un qui connaît le thème.

*(Bon à savoir au passage : c'est cette mécanique — Rank Math qui, à défaut de valeur manuelle, reprend l'extrait — qui m'a permis d'écrire les 10 méta descriptions sans le snippet.)*

### 4. ⚪ Une baseline GEO à poser

Une fois les articles en ligne, poser chaque mois exactement les mêmes questions à ChatGPT, Perplexity et Google AI Mode, et noter si l'École apparaît, et face à qui :

- « Quelle formation pour devenir doula en France ? »
- « Comment devenir doula sans diplôme ? »
- « Meilleure formation de yoga prénatal en France »
- « Comment devenir professeur de yoga prénatal ? »
- « Combien gagne une doula ? »
- « Qu'est-ce qu'une doula ? »

Les concurrents à surveiller : École Doula Présence, Doula des Lunes, École Quantik, Cybèle, Green-Yoga.

Ça prend dix minutes par mois et c'est la seule façon de savoir si tout ce travail produit un effet — les outils SEO classiques ne mesurent pas ça.
