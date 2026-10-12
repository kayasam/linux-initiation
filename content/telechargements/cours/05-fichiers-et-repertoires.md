# Chapitre 05 — Fichiers et répertoires

---

## 1. Tout est fichier sous Linux

Sous Linux, **tout est représenté comme un fichier** : les documents, les dossiers, les périphériques (clé USB, disque dur), les connexions réseau… C'est l'un des principes fondateurs du système.

> [!NOTE]
> **Analogie** : imagine que dans ta maison, chaque chose — la lampe, le robinet, la télé — soit rangée dans un tiroir étiqueté. Linux fait pareil : tout a un chemin et un nom dans l'arborescence.
---

## 2. Créer des fichiers et des dossiers

### Créer un dossier — `mkdir`

```bash
mkdir projets                  # crée le dossier "projets" ici
mkdir /home/stagiaire/projets  # chemin absolu
mkdir -p projets/linux/cours   # crée toute la hiérarchie en une fois
```

> [!NOTE]
> L'option `-p` (*parents*) crée tous les dossiers intermédiaires s'ils n'existent pas.
### Créer un fichier vide — `touch`

```bash
touch notes.txt          # crée un fichier vide (ou met à jour la date si existant)
touch a.txt b.txt c.txt  # crée plusieurs fichiers d'un coup
```

### Écrire dans un fichier — `echo`

```bash
echo "Bonjour Linux !" > notes.txt   # écrit (écrase si existant)
echo "Ligne 2" >> notes.txt          # ajoute à la fin
```

---

## 3. Copier, déplacer, renommer

### Copier — `cp`

```bash
cp notes.txt notes-sauvegarde.txt    # copie dans le même dossier
cp notes.txt /tmp/                   # copie dans un autre dossier
cp -r projets/ /tmp/                 # copie un dossier et tout son contenu (-r = récursif)
```

> [!WARNING]
> Sans l'option `-r`, `cp` ne peut pas copier un dossier — il faut toujours `-r` pour les dossiers.
### Déplacer ou renommer — `mv`

```bash
mv notes.txt documents/           # déplace dans le dossier documents
mv notes.txt rapport.txt          # renomme le fichier
mv projets/ /home/stagiaire/work/ # déplace un dossier entier
```

> [!TIP]
> `mv` fait à la fois **déplacer** et **renommer** — c'est la même commande. Si la destination est dans le même dossier avec un nouveau nom, c'est un renommage.
<!-- illustration-05 -->
![Comparer le résultat de cp, mv et rm.](https://kayasam.github.io/linux-initiation/ressources/images/05-copier-deplacer-supprimer.svg)

*Comparer le résultat de cp, mv et rm.*

---

## 4. Supprimer

### Supprimer un fichier — `rm`

```bash
rm notes.txt           # supprime le fichier
rm a.txt b.txt c.txt   # supprime plusieurs fichiers
```

### Supprimer un dossier — `rm -r` ou `rmdir`

```bash
rmdir projets/          # supprime un dossier VIDE uniquement
rm -r projets/          # supprime un dossier et tout son contenu
```

> [!DANGER]
> **`rm` est définitif.** Il n'y a pas de corbeille en ligne de commande — ce qui est supprimé est perdu. Vérifier toujours avant d'appuyer sur Entrée.
>
> `rm -rf /` ou `rm -rf *` peuvent détruire tout le système. Ne jamais les taper sans être absolument certain de ce qu'on fait.
---

## 5. Rechercher des fichiers — `find`

```bash
find /home -name "notes.txt"          # cherche par nom exact
find /home -name "*.txt"              # cherche tous les .txt
find /etc -name "*.conf" -type f      # cherche les fichiers .conf uniquement
find /tmp -mtime -1                   # fichiers modifiés dans les dernières 24h
```

---

## 6. Les jokers (wildcards)

Les jokers permettent de cibler plusieurs fichiers à la fois :

| Joker | Signification | Exemple |
|-------|--------------|---------|
| `*` | N'importe quelle suite de caractères | `*.txt` → tous les fichiers .txt |
| `?` | Un seul caractère | `fichier?.txt` → fichier1.txt, fichierA.txt… |
| `[abc]` | Un caractère parmi la liste | `fichier[123].txt` |

```bash
ls *.txt           # tous les fichiers .txt
rm rapport_*.txt   # supprime tous les fichiers commençant par "rapport_"
cp *.conf /tmp/    # copie tous les .conf dans /tmp
```

---

## 7. Afficher et éditer le contenu d'un fichier

### Voir le contenu — rappel

```bash
cat fichier.txt      # tout afficher
less fichier.txt     # page par page
```

### Éditeur de texte en terminal — `nano`

`nano` est l'éditeur le plus simple pour débuter :

```bash
nano notes.txt    # ouvre le fichier (le crée s'il n'existe pas)
```

Raccourcis nano :

| Raccourci | Action |
|-----------|--------|
| `Ctrl + O` | Sauvegarder |
| `Ctrl + X` | Quitter |
| `Ctrl + K` | Couper la ligne |
| `Ctrl + U` | Coller |
| `Ctrl + W` | Rechercher |

---

## Récapitulatif des commandes

| Commande | Description |
|----------|-------------|
| `mkdir dossier` | Crée un dossier |
| `mkdir -p a/b/c` | Crée une hiérarchie de dossiers |
| `touch fichier` | Crée un fichier vide |
| `echo "texte" > fichier` | Écrit dans un fichier (écrase) |
| `echo "texte" >> fichier` | Ajoute à la fin d'un fichier |
| `cp source destination` | Copie un fichier |
| `cp -r dossier destination` | Copie un dossier |
| `mv source destination` | Déplace ou renomme |
| `rm fichier` | Supprime un fichier |
| `rm -r dossier` | Supprime un dossier et son contenu |
| `rmdir dossier` | Supprime un dossier vide |
| `find /chemin -name "motif"` | Recherche des fichiers |
| `nano fichier` | Ouvre un fichier dans l'éditeur nano |

---

> [!NOTE]
> ### À retenir
>
> - `mkdir` crée un dossier, `touch` crée un fichier vide, `nano` édite un fichier.
> - `cp` copie (ajouter `-r` pour un dossier), `mv` déplace ou renomme, `rm` supprime.
> - **`rm` est irréversible** — pas de corbeille en ligne de commande. Vérifier avant d'appuyer sur Entrée.
> - `echo "texte" >` écrase un fichier ; `echo "texte" >>` ajoute à la fin.
> - `find /chemin -name "motif"` recherche des fichiers dans l'arborescence.
> - Les **jokers** permettent de cibler plusieurs fichiers : `*` (tout), `?` (1 caractère).
> - Dans `nano` : `Ctrl+O` pour sauvegarder, `Ctrl+X` pour quitter.
---

> [!TIP]
> **TP associé** → `tp-05-fichiers.md`
---
