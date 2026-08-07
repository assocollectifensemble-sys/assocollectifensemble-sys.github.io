# Tutos complets — ce que tu peux faire depuis le téléphone, et le reste

**Réponse courte à tes deux questions :**
- **Bing sur mobile : oui, ça marche.** C'est même l'action la plus rentable et elle prend un quart d'heure. Tuto 1.
- **Le snippet sur mobile : techniquement possible, mais ne le fais pas.** Et surtout : **il n'est plus urgent du tout**, j'ai trouvé un contournement. Explication au Tuto 2.
- **Elementor sur mobile : non.** L'éditeur ne fonctionne pas correctement sur un écran de téléphone. Tuto 3, pour quand tu seras devant l'ordinateur.

---

# TUTO 1 — Créer Bing Webmaster Tools depuis ton téléphone

⏱️ 15 minutes · 📱 marche sur mobile · 🔴 **c'est l'action la plus importante de tout le chantier**

## Pourquoi c'est le truc à faire

ChatGPT ne cherche pas dans Google. Il cherche dans **Bing**. Aujourd'hui, le site n'est pas déclaré à Bing : quoi qu'on écrive, il ne peut pas apparaître dans les réponses de ChatGPT. C'est gratuit, ça prend un quart d'heure, et la quasi-totalité des concurrents ne le font pas.

Il faut compter 6 à 12 semaines avant que ça produise un effet. C'est pour ça que ça ne peut pas attendre.

## Les étapes

**1.** Ouvre ton navigateur mobile (Safari ou Chrome) et va sur :
👉 **bing.com/webmasters**

**2.** Appuie sur **« Se connecter »** (ou *Sign in*).
Tu as le choix entre plusieurs comptes. **Choisis « Google »** — c'est ce qui rend la suite automatique. Connecte-toi avec le compte Google qui a accès à la Search Console de yoga-doula.eu.

**3.** Une fois connecté, Bing te propose deux options :
- **« Importer depuis Google Search Console »** ← **choisis celle-là**
- « Ajouter un site manuellement »

**4.** Bing demande l'autorisation d'accéder à ta Search Console. Appuie sur **« Continuer »** puis **« Autoriser »** sur l'écran Google.

**5.** Bing affiche la liste de tes sites Search Console. Tu devrais voir **yoga-doula.eu**.
Coche-le, puis appuie sur **« Importer »**.

**6.** C'est fini. Bing récupère automatiquement la propriété vérifiée, le sitemap et l'historique.

## Vérifier que ça a marché (2 min)

Dans le menu (l'icône ☰ en haut à gauche) :
- **« Sitemaps »** → tu dois voir `https://yoga-doula.eu/sitemap_index.xml`
  → S'il n'y est pas : bouton **« Soumettre un sitemap »**, colle cette adresse exactement, valide.
- **« Site Explorer »** ou **« Pages indexées »** → au début ce sera vide ou presque, c'est normal. Bing met plusieurs jours à passer.

## Si ça coince

| Problème | Solution |
|---|---|
| L'import Google Search Console ne s'affiche pas | Ajoute le site manuellement : `https://yoga-doula.eu`. Bing proposera 3 méthodes de vérification. Prends **« Balise meta »** et envoie-moi le code, je te dirai où le mettre. |
| « Site déjà vérifié par un autre compte » | Quelqu'un l'a déjà fait (Fabien ?). Dis-le-moi, on cherchera qui. |
| L'interface est illisible sur le téléphone | Demande le **site en version ordinateur** dans le menu de ton navigateur (Safari : `ᴀA` en bas à gauche → « Site pour ordinateur »). |

**Quand c'est fait, dis-le-moi.** Je vérifierai que Bing voit bien le sitemap.

---

# TUTO 2 — Le snippet Rank Math : bonne nouvelle, tu peux l'oublier pour l'instant

⏱️ 10 minutes · 💻 ordinateur recommandé · 🟢 **plus urgent**

## Ce que j'ai découvert

J'ai analysé le code source de deux articles en ligne pour comprendre comment Rank Math est configuré sur ce site. Résultat :

- **Le titre SEO reprend exactement le titre de l'article.** (Vérifié : la balise `<title>` de l'article « Mantras pendant l'accouchement » est identique à son titre WordPress, sans suffixe.)
- **La méta description reprend l'extrait de l'article.**

Or **le titre et l'extrait, je peux les écrire par l'API.** Le snippet ne servait qu'à écrire les champs Rank Math directement — mais je peux atteindre le même résultat autrement.

## Ce que j'ai donc fait à la place

J'ai réécrit **les 10 titres et les 10 extraits** aux bonnes longueurs pour Google (titre ≤ 60 caractères, description ≈ 150). J'ai raccourci six titres qui débordaient, par exemple :

| Avant | Après |
|---|---|
| Doula et enseignante de yoga prénatal : la double compétence qui remplit votre agenda *(85 car.)* | Doula et prof de yoga prénatal : la double compétence *(53)* |
| Doula de fin de vie : rôle, formation et différence avec la doula de naissance *(78)* | Doula de fin de vie : rôle, formation et différences *(52)* |
| Devenir professeur·e de yoga prénatal : formation, débouchés et réalité du métier *(81)* | Devenir prof de yoga prénatal : formation et débouchés *(54)* |

**Tu n'as donc rien à copier-coller.** Le fichier `02-titres-seo-et-metas.md` devient une simple référence.

## Ce que le snippet apporterait encore (mineur)

Deux choses seulement, aucune urgente :
1. Écrire le **mot-clé principal** Rank Math — ça ne sert qu'au score /100 affiché dans l'admin, ça n'a **aucun effet sur Google**.
2. Pouvoir donner à un article un titre SEO **différent** de son titre affiché. Confortable, pas indispensable.

**Conclusion : installe-le tranquillement un jour où tu es devant l'ordinateur, ou jamais.** Ce n'est plus un blocage.

## Le tuto quand même, pour le jour où

1. **D'abord la sauvegarde.** WordPress → **UpdraftPlus** → onglet *Sauvegarder / Restaurer*. Tu dois voir une sauvegarde datée de moins d'une semaine. Sinon, bouton bleu **« Sauvegarder maintenant »**, coche base de données + fichiers, attends la fin.
2. Menu de gauche → **Snippets** (le plugin Code Snippets est déjà installé) → **Ajouter**.
3. **Titre :** `Rank Math REST — titres SEO et métas`
4. Dans le grand cadre de code, colle le contenu du fichier `01-snippet-rank-math-rest.php` **en enlevant la toute première ligne `<?php`**.
5. Plus bas, coche **« Run snippet everywhere »**.
6. Bouton **« Enregistrer les modifications et activer »**.
7. Préviens-moi : je teste immédiatement sur l'article 12052 (un brouillon de test, aucun risque) et je te confirme.

**Si quelque chose casse :** Snippets → décoche celui-là → tout revient instantanément à l'état d'avant. Le snippet n'écrit rien de lui-même, il ouvre juste une porte.

⚠️ **Ne le fais pas sur mobile.** Le champ de code utilise un éditeur qui gère mal le collage sur téléphone : il peut couper ou reformater le code sans prévenir.

---

# TUTO 3 — Les corrections Elementor (ordinateur uniquement)

⏱️ 45 minutes · 💻 **impossible sur mobile** — l'éditeur Elementor ne fonctionne pas sur un écran de téléphone

Trois chantiers, par ordre d'importance. **J'ai revu ma priorité depuis ce matin** : ce n'est pas la FAQ le plus urgent, c'est le schema `Course`.

## 3.1 — 🔴 Ajouter le schema `Course` à la page Programme Yoga Maternité

C'est **la** correction qui compte pour la campagne d'octobre. Sans elle, Google et les IA voient cette page comme un article de blog, pas comme une formation. C'est exactement ce qui décide si l'École sort quand quelqu'un demande à ChatGPT « quelle formation pour enseigner le yoga prénatal ? ».

Bonne nouvelle : **ça se fait dans Rank Math, pas dans Elementor.** Pas besoin de toucher au constructeur visuel.

1. WordPress → **Pages** → ouvre **Programme Yoga Maternité**.
2. Descends tout en bas de l'éditeur → onglet **Rank Math**.
3. Clique sur **Schéma** (l'icône en forme de code).
4. Si un schéma **Article** est actif : clique dessus → **Supprimer**.
5. **Ajouter un schéma** → choisis **Course**.
6. Remplis :

| Champ | Valeur |
|---|---|
| Course Name | `Programme Yoga Maternité` |
| Description | `Formation à l'enseignement du yoga prénatal et postnatal. 84 heures en format hybride (en ligne et présentiel), session d'octobre 2026 à juin 2027.` |
| Course Provider | `École Internationale Yoga Doula` |
| Provider URL | `https://yoga-doula.eu/` |
| Course Mode | `Blended` |
| Durée / Workload | `84 heures` |
| Date de début | la date exacte de ton calendrier (≈ `2026-10-01`) |
| Date de fin | la date exacte (≈ `2027-06-30`) |
| Prix | `1050` |
| Devise | `EUR` |
| Langue | `fr` |

7. **Mettre à jour** la page.
8. Teste sur **search.google.com/test/rich-results** en collant l'adresse de la page. Tu dois voir « Course » détecté, sans erreur.

## 3.2 — 🟠 Ramener les H1 à un seul par page

| Page | H1 actuels | Cible |
|---|---|---|
| Accueil | **9** | 1 |
| Formation Yoga Doula | **8** | 1 |
| Programme Yoga Maternité | 1 ✅ | — |

Un H1, c'est le titre principal de la page — celui qui dit à Google de quoi elle parle. Neuf H1, c'est comme crier neuf choses en même temps : plus rien ne ressort. Quentin l'avait déjà signalé en mars 2023.

**Comment faire :**
1. Ouvre la page avec **Modifier avec Elementor**.
2. Clique sur chaque gros titre de la page.
3. Dans le panneau de gauche, onglet **Contenu**, cherche la ligne **« Balise HTML »** (ou *HTML Tag*).
4. Passe-les tous en **H2**, sauf **un seul** qui reste en **H1**.
5. Bouton vert **PUBLIER** (⚠️ « Enregistrer le brouillon » ne suffit pas — seul « Publier » met la modification en ligne).

**Quel H1 garder :**
- Page d'accueil → `Deviens DOULA` (c'est déjà le premier, garde-le)
- Page Formation Yoga Doula → remplace `Deviens DOULA` par **`Formation de doula & yoga périnatal`**
  *Pourquoi : cette page est en position 21 sur « formation doula » avec 1 828 affichages par an, et le mot « formation » n'apparaît nulle part dans son H1.*

## 3.3 — 🟡 Les 4 FAQ en double sur la page PYM

**Moins urgent que je ne l'ai dit ce matin, et je te dois la correction :** depuis 2023, Google n'affiche plus les résultats enrichis FAQ sauf pour les sites gouvernementaux et de santé publique. Ces 16 questions n'auraient donc pas remonté de toute façon. Ça reste une incohérence à nettoyer (les IA lisent ce balisage), mais ce n'est pas prioritaire.

**Ce qui se passe :** la section « Foire aux questions » de la page PYM est composée de **4 widgets accordéon séparés**, et chacun déclare sa propre FAQ. Ils sont repérables par leur première question :
1. « Je n'ai jamais suivi de formation de yoga… »
2. « Quand commence et quand se termine le programme… »
3. « Quels sont les frais annexes… »
4. « Comment obtenir mon certificat d'accomplissement ? »

**Comment faire :** ouvre la page dans Elementor, clique sur chacun de ces 4 accordéons, et dans le panneau de gauche cherche une option **« Schema FAQ »** / *« FAQ Schema »* / *« Données structurées »* → **désactive-la sur 3 d'entre eux, garde-la sur un seul**. Puis **PUBLIER**.

Si l'option n'existe sur aucun widget, dis-le-moi : on prendra l'autre chemin (regrouper les 4 accordéons en un seul).

**Quand tu auras publié, préviens-moi** — je relis le code source en 30 secondes et je te confirme le résultat.

---

# TUTO 4 — Publier les articles depuis ton téléphone

⏱️ 2 min par article · 📱 **marche très bien sur mobile**

Une fois que Gurujagat a validé, la publication, elle, se fait parfaitement depuis le téléphone.

**Option A — l'application WordPress** (la plus confortable)
Installe *WordPress* (Automattic) sur ton téléphone, connecte-toi à yoga-doula.eu, onglet **Articles → Brouillons**. Tu ouvres, tu lis, tu appuies sur **Publier**.

**Option B — le navigateur**
Va sur ton adresse d'administration (le site utilise *WPS Hide Login*, donc ce n'est pas `/wp-admin` — c'est l'adresse que tu as en favori). Puis **Articles → Brouillons**.

## ⚠️ L'ordre de publication compte

Les articles se citent les uns les autres. Si tu publies un article qui pointe vers un autre encore en brouillon, le lien tombe sur une page 404.

**Publie dans cet ordre :**

| Vague | Articles | Pourquoi |
|---|---|---|
| **1** | `12051` Comment devenir doula · `12200` Yoga prénatal | Les deux piliers. Tous les autres pointent vers eux. |
| **2** *(le lendemain)* | `12049` Métier reconnu · `12201` Yoga postnatal · `12202` Devenir prof de yoga prénatal | |
| **3** *(le surlendemain)* | `12054` Combien gagne · `12055` Double compétence | |
| **4** | `12058` Sans diplôme · `12059` Salariée · `12060` Fin de vie | |

**Pourquoi étaler sur 4 jours et pas tout d'un coup :** on est dans un domaine santé. Dix articles publiés dans la même heure, ça ressemble à du contenu produit en masse, et Google le sanctionne. Deux à trois par jour, c'est un rythme d'école qui écrit. C'est le seul point du brief sur lequel je ne transigerais pas.

---

# ⚠️ Un point de coordination important

Tu m'as dit qu'une autre conversation écrit sur le site via **Cowork**. C'est le risque n°1 en ce moment : on peut très facilement créer des doublons ou s'écraser mutuellement — c'est déjà arrivé le 15 juillet avec 3 brouillons créés en 4 minutes depuis deux conversations.

**Message à coller dans la conversation Cowork :**

> Ne touche pas aux articles WordPress **12049, 12051, 12054, 12055, 12058, 12059, 12060, 12200, 12201, 12202** — ils sont en cours de finalisation ailleurs. Ne crée pas de nouvel article de blog sans me le demander. Tu peux travailler sur les **pages** (Elementor, Rank Math, formulaires) sans risque.

Le partage naturel : **Cowork = les pages et la technique. Moi = les articles de blog et le SEO éditorial.**
