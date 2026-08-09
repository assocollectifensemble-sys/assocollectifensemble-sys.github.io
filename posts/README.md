# Publications programmées — Facebook & Instagram

Un fichier `.md` par publication dans ce dossier, les images dans `posts/media/`.
Un robot passe toutes les 15 minutes et publie ce qui est arrivé à échéance.

---

## 1. Écrire un post

Créez `posts/2026-08-20-balade-cilaos.md` :

```markdown
---
date: 2026-08-20 18:30
cibles: [facebook, instagram]
images:
  - media/balade-cilaos.jpg
---
Le soleil se couche sur Cilaos et Rosalie a encore volé la vedette 🌿

Une balade, deux heures, mille souvenirs.
Réservations par WhatsApp — lien dans la bio.

#2CV #LaReunion #SaintLeu #Cilaos
```

Tout ce qui suit le deuxième `---` est le texte publié. Poussez le fichier sur
`main` : il part tout seul à la date indiquée.

### Les clés disponibles

| Clé | Obligatoire | Détail |
|---|---|---|
| `date` | oui | `2026-08-20 18:30`, **heure de La Réunion**. Sans heure, 9 h par défaut. |
| `cibles` | non | `[facebook, instagram]` par défaut. Mettez `[facebook]` pour ne pas toucher Instagram. |
| `images` | selon | Chemins relatifs à `posts/`, ou URL complètes. 2 à 10 images = carrousel. |
| `image` | — | Synonyme de `images` quand il n'y en a qu'une. |
| `lien` | non | URL d'aperçu. **Facebook uniquement**, Instagram ne cliquerait pas dessus. |
| `brouillon` | non | `true` = le fichier est ignoré. Pour préparer sans risquer une publication. |

### Ce que le robot refuse

La validation tourne à chaque `push` et bloque avant publication si :
la date est illisible, une image est introuvable, un post Instagram n'a pas
d'image, la légende Instagram dépasse 2 200 caractères, il y a plus de
10 images, ou deux posts tombent exactement à la même seconde.

Pour vérifier depuis votre poste, sans rien envoyer :

```bash
pip install requests pyyaml
python scripts/publier_meta.py --valider
python scripts/publier_meta.py --simulation   # montre ce qui partirait
```

---

## 2. Les images

Elles sont servies par GitHub Pages : Meta va les chercher à l'adresse
`https://assocollectifensemble-sys.github.io/posts/media/...`. Deux conséquences :

- **Poussez l'image bien avant l'heure du post.** GitHub Pages met une à deux
  minutes à déployer ; si l'image n'est pas encore en ligne, Instagram échoue.
  En pratique : préparez la veille, pas cinq minutes avant.
- Instagram est exigeant : **JPEG**, ratio entre 4:5 (portrait) et 1,91:1
  (paysage), 8 Mo maximum. Une image carrée ou portrait passe toujours.

Les photos Google Drive utilisées par le site (`lh3.googleusercontent.com`)
peuvent être mises en URL complète dans `images`, mais Instagram les refuse
par moments — mieux vaut déposer le JPEG dans `posts/media/`.

---

## 3. Installation (une seule fois)

### a. Le compte Instagram

Il doit être un **compte professionnel** rattaché à la Page Facebook.
Instagram → Paramètres → Type de compte → passer en compte professionnel, puis
lier la Page depuis Meta Business Suite. Sans ça, l'API Instagram ne répond pas.

### b. Le jeton d'accès

Le plus simple et le plus durable : un **utilisateur système**, dont le jeton
n'expire jamais (un jeton personnel, lui, meurt au bout de 60 jours et les
publications s'arrêteraient sans prévenir).

1. [business.facebook.com](https://business.facebook.com) → **Paramètres d'entreprise**
2. **Utilisateurs → Utilisateurs système** → *Ajouter*, rôle **Administrateur**
3. **Ajouter des actifs** → la Page *Une 2CV, mille histoires* (contrôle total)
   et le compte Instagram
4. **Générer un nouveau jeton** → choisir l'application, expiration **Jamais**,
   et cocher :
   `pages_manage_posts`, `pages_read_engagement`,
   `instagram_basic`, `instagram_content_publish`, `business_management`
5. Copier le jeton — il n'est affiché qu'une fois.

### c. Trouver l'identifiant Instagram

La Page est déjà connue : `61586545132399`. Pour l'identifiant Instagram,
collez ceci dans un terminal avec votre jeton :

```bash
curl -s "https://graph.facebook.com/v23.0/61586545132399?fields=instagram_business_account&access_token=VOTRE_JETON"
```

La réponse contient `"instagram_business_account": {"id": "1784..."}` — c'est ce
nombre qu'il faut.

### d. Renseigner GitHub

Dépôt → **Settings → Secrets and variables → Actions**.

Onglet **Secrets** (valeurs cachées) :

| Nom | Valeur |
|---|---|
| `META_ACCESS_TOKEN` | le jeton de l'étape b |
| `META_PAGE_ID` | `61586545132399` |
| `META_IG_USER_ID` | l'identifiant de l'étape c |

Onglet **Variables** (facultatif) :

| Nom | Quand |
|---|---|
| `MEDIA_BASE_URL` | `https://une2cvmillehistoires.re` une fois le domaine branché sur Pages |
| `META_API_VERSION` | pour figer une version de l'API, `v23.0` par défaut |

---

## 4. Comment ça marche, et ce qu'il faut savoir

**Facebook** sait programmer : dès qu'un post est à plus de 15 minutes, le robot
le dépose chez Meta avec son heure de publication. Meta le publie à la seconde
près, même si GitHub est en panne ce jour-là. Le post apparaît immédiatement dans
le Planificateur de Business Suite — vous pouvez l'y relire, le modifier ou
l'annuler comme n'importe quel post programmé à la main.

**Instagram** ne sait pas programmer : l'API n'accepte que la publication
immédiate. C'est donc le cron qui publie, à l'heure dite. GitHub exécute ses
crons avec du retard — **comptez 5 à 20 minutes après l'heure indiquée**. Pour un
post à l'heure exacte sur Instagram, passez par le Planificateur de Business
Suite.

**Rien ne part deux fois.** Après chaque publication, le robot écrit dans
`posts/.etat.json` ce qui est parti, et commite ce fichier. Ne le modifiez pas à
la main : supprimer une ligne fait republier le post.

**Un post en retard de plus de 48 h est ignoré**, pour qu'ajouter un ancien
fichier ne déclenche pas une publication surprise. Pour le publier quand même :
onglet Actions → *Publier sur Facebook et Instagram* → *Run workflow* → cocher
*forcer*.

**Corriger un post déjà programmé sur Facebook** : modifier le `.md` ne change
rien, il est déjà chez Meta. Passez par le Planificateur de Business Suite.

**Si le dépôt reste 60 jours sans le moindre commit**, GitHub désactive les
workflows programmés et vous préviendra par mail — il suffit de les réactiver
dans l'onglet Actions.

---

## 5. En cas de pépin

Onglet **Actions** → *Publier sur Facebook et Instagram* → dernière exécution.

| Message | Cause |
|---|---|
| `secret(s) manquant(s)` | l'étape 3.d n'est pas faite |
| `Meta a refusé : ... code 190` | jeton expiré ou révoqué → en regénérer un (3.b) |
| `Meta a refusé : ... code 200` | permission manquante sur le jeton |
| `Instagram n'a pas pu préparer le média` | image inaccessible, mauvais format ou mauvais ratio |
| `image introuvable` | le chemin dans `images` ne correspond à aucun fichier |
