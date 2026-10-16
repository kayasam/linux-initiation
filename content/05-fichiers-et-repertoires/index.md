---
title: "05. Fichiers et répertoires"
---

# Chapitre 05 — Fichiers et répertoires

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="05-fichiers-et-repertoires" style="--resource-count:4"><div class="resource-buttons"><a class="resource-button resource-markdown" data-resource-kind="markdown" aria-label="Cours — Lire le cours en Markdown" href="https://kayasam.github.io/linux-initiation/05-fichiers-et-repertoires/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg></span><span class="resource-label">Cours<small>Lire le cours en Markdown</small></span></a><a class="resource-button resource-html" data-resource-kind="html" aria-label="HTML — Explorer le chapitre" href="https://kayasam.github.io/linux-initiation/05-fichiers-et-repertoires/html/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 28 32"><path d="M2 2h24l-2 25-10 3-10-3Z" fill="#e44d26"/><path d="M14 5v22l7-2 2-20Z" fill="#f16529"/><path d="M7 8h15l-.3 3H11l.3 3h10l-.8 9-6.5 2-6.5-2-.4-5h3l.2 2.6 3.7 1 3.7-1 .3-3.6H8Z" fill="#fff"/></svg></span><span class="resource-label">HTML<small>Explorer le chapitre</small></span></a><a class="resource-button resource-quiz" data-resource-kind="quiz" aria-label="Quiz — 20 questions" href="https://kayasam.github.io/linux-initiation/05-fichiers-et-repertoires/quiz/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="4" y="3" width="24" height="26" rx="6" fill="#7652ad"/><path d="M12 12a4 4 0 1 1 6 3.5c-1.5.8-2 1.4-2 3" fill="none" stroke="#fff" stroke-width="2.8" stroke-linecap="round"/><circle cx="16" cy="23" r="1.6" fill="#fff"/></svg></span><span class="resource-label">Quiz<small>20 questions</small></span></a><a class="resource-button resource-tp" data-resource-kind="tp" aria-label="TP — Mettre en pratique" href="https://kayasam.github.io/linux-initiation/05-fichiers-et-repertoires/tp"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg></span><span class="resource-label">TP<small>Mettre en pratique</small></span></a></div><div class="resource-actions"><a class="resource-download" href="https://kayasam.github.io/linux-initiation/telechargements/cours/05-fichiers-et-repertoires.md" download aria-label="Télécharger le cours en Markdown"><span aria-hidden="true">↓</span> Télécharger .md</a><a class="resource-download resource-pdf" href="https://kayasam.github.io/linux-initiation/telechargements/cours/05-fichiers-et-repertoires.pdf?v=10c481a0af71" download aria-label="Télécharger le cours en PDF"><span aria-hidden="true">↓</span> PDF</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>


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

---

[← Le terminal](https://kayasam.github.io/linux-initiation/04-le-terminal/) · [Chapitre suivant →](https://kayasam.github.io/linux-initiation/06-arborescence-linux/)
