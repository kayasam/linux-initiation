---
title: "04. Le terminal"
---

# Chapitre 04 — Le terminal

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="04-le-terminal" style="--resource-count:4"><div class="chapter-resources-heading"><span class="chapter-resources-title">Ressources du chapitre</span><a class="resource-download" href="https://kayasam.github.io/linux-initiation/telechargements/cours/04-le-terminal.md" download><span aria-hidden="true">↓</span> Télécharger le .md</a></div><div class="resource-buttons"><a class="resource-button resource-markdown" data-resource-kind="markdown" href="https://kayasam.github.io/linux-initiation/04-le-terminal/"><span class="resource-icon" aria-hidden="true"><img src="https://kayasam.github.io/linux-initiation/assets/resource-icons/markdown.svg" alt="" /></span><span class="resource-label">Markdown<small>Lire le cours</small></span></a><a class="resource-button resource-html" data-resource-kind="html" href="https://kayasam.github.io/linux-initiation/04-le-terminal/html/"><span class="resource-icon" aria-hidden="true"><img src="https://kayasam.github.io/linux-initiation/assets/resource-icons/html.svg" alt="" /></span><span class="resource-label">HTML<small>Explorer le chapitre</small></span></a><a class="resource-button resource-quiz" data-resource-kind="quiz" href="https://kayasam.github.io/linux-initiation/04-le-terminal/quiz/"><span class="resource-icon" aria-hidden="true"><img src="https://kayasam.github.io/linux-initiation/assets/resource-icons/quiz.svg" alt="" /></span><span class="resource-label">Quiz<small>20 questions</small></span></a><a class="resource-button resource-tp" data-resource-kind="tp" href="https://kayasam.github.io/linux-initiation/04-le-terminal/tp"><span class="resource-icon" aria-hidden="true"><img src="https://kayasam.github.io/linux-initiation/assets/resource-icons/tp.svg" alt="" /></span><span class="resource-label">TP<small>Mettre en pratique</small></span></a></div></nav>


---

## 1. Pourquoi utiliser le terminal ?

L'interface graphique est pratique pour un usage quotidien. Mais le terminal permet de faire des choses **impossibles ou très lentes** avec une souris :

- Automatiser des tâches répétitives
- Administrer un serveur distant (sans interface graphique)
- Exécuter des opérations sur des centaines de fichiers en une seule commande
- Diagnostiquer des problèmes système

> [!NOTE]
> **Analogie** : l'interface graphique, c'est comme cuisiner avec des plats préparés — pratique et rapide. Le terminal, c'est cuisiner soi-même — plus de temps au départ, mais tu peux faire exactement ce que tu veux.
---

## 2. Le prompt

Quand tu ouvres le terminal, tu vois une ligne qui ressemble à ça :

```
stagiaire@debian:~$
```

Ce **prompt** t'indique que le terminal est prêt. Il affiche :

| Partie | Signification |
|--------|--------------|
| `stagiaire` | Ton nom d'utilisateur |
| `@` | "at" (chez) |
| `debian` | Le nom de la machine |
| `:` | Séparateur |
| `~` | Le répertoire courant (`~` = ton dossier personnel) |
| `$` | Tu es un utilisateur normal |
| `#` | Tu es root (administrateur) — attention ! |

---

## 3. Structure d'une commande

Toute commande Linux suit la même structure :

```
commande [options] [arguments]
```

| Partie | Rôle | Exemple |
|--------|------|---------|
| `commande` | Ce qu'on veut faire | `ls` |
| `options` | Comment le faire (commence par `-`) | `-l`, `-a`, `--help` |
| `arguments` | Sur quoi agir | `/home`, `fichier.txt` |

Exemple complet :
```bash
ls -l /home
```
→ lister (`ls`) en détail (`-l`) le contenu de `/home`

> [!WARNING]
> Linux est **sensible à la casse** — `ls` et `LS` sont deux choses différentes. Toujours écrire les commandes en minuscules.
---

## 4. Se repérer dans le système

### `pwd` — Où suis-je ?

```bash
pwd
# /home/stagiaire
```

`pwd` (*Print Working Directory*) affiche le chemin complet du dossier où tu te trouves.

### `ls` — Qu'y a-t-il ici ?

```bash
ls             # liste simple
ls -l          # liste détaillée (permissions, taille, date)
ls -a          # affiche aussi les fichiers cachés (commençant par .)
ls -lh         # liste détaillée avec tailles lisibles (Ko, Mo…)
ls /etc        # liste le contenu d'un autre dossier
```

### `cd` — Se déplacer

```bash
cd /etc            # aller dans /etc
cd ..              # remonter d'un dossier
cd                 # revenir dans son dossier personnel (~)
cd ~/Documents     # aller dans Documents (~ = dossier personnel)
cd -               # retourner dans le dossier précédent
```

> [!TIP]
> **Astuce** : appuyer sur **Tab** complète automatiquement le nom d'un fichier ou dossier. Si plusieurs choix sont possibles, appuyer deux fois sur Tab affiche les possibilités.
---

## 5. Chemins absolus et relatifs

Il existe deux façons d'indiquer un emplacement :

| Type | Description | Exemple |
|------|-------------|---------|
| **Absolu** | Part toujours de la racine `/` | `/home/stagiaire/Documents` |
| **Relatif** | Part du dossier courant | `Documents` ou `../autres` |

```bash
# Si je suis dans /home/stagiaire :
cd Documents          # chemin relatif → va dans /home/stagiaire/Documents
cd /home/stagiaire/Documents   # chemin absolu → même résultat
```


<!-- illustration-04 -->
![Deux chemins différents peuvent mener au même dossier.](https://kayasam.github.io/linux-initiation/ressources/images/04-chemins-absolus-et-relatifs.svg)

*Deux chemins différents peuvent mener au même dossier.*

---

## 6. Lire des fichiers

```bash
cat fichier.txt        # affiche tout le contenu d'un coup
less fichier.txt       # affiche page par page (q pour quitter, flèches pour naviguer)
head fichier.txt       # affiche les 10 premières lignes
tail fichier.txt       # affiche les 10 dernières lignes
tail -f /var/log/syslog  # affiche les nouvelles lignes en temps réel
```

---

## 7. Obtenir de l'aide

```bash
man ls          # manuel complet de la commande ls (q pour quitter)
ls --help       # aide résumée directement dans le terminal
```

> [!NOTE]
> `man` (*manual*) est le manuel intégré de Linux. Chaque commande y est documentée. C'est la référence officielle.
---

## 8. Raccourcis indispensables du terminal

| Raccourci | Action |
|-----------|--------|
| `Tab` | Complétion automatique du nom |
| `↑` / `↓` | Naviguer dans l'historique des commandes |
| `Ctrl + C` | Interrompre une commande en cours |
| `Ctrl + L` | Effacer l'écran (équivalent de `clear`) |
| `Ctrl + A` | Aller au début de la ligne |
| `Ctrl + E` | Aller à la fin de la ligne |
| `history` | Afficher l'historique des commandes |

---

## Récapitulatif des commandes

| Commande | Description |
|----------|-------------|
| `pwd` | Affiche le répertoire courant |
| `ls` | Liste le contenu d'un répertoire |
| `ls -l` | Liste détaillée (permissions, taille, date) |
| `ls -a` | Affiche aussi les fichiers cachés |
| `ls -lh` | Liste détaillée avec tailles lisibles |
| `cd /chemin` | Va dans le dossier spécifié |
| `cd ..` | Remonte d'un niveau |
| `cd` | Retourne dans le dossier personnel |
| `cd -` | Retourne dans le dossier précédent |
| `cat fichier` | Affiche le contenu d'un fichier |
| `less fichier` | Affiche un fichier page par page |
| `head fichier` | Affiche les 10 premières lignes |
| `tail fichier` | Affiche les 10 dernières lignes |
| `man commande` | Affiche le manuel de la commande |
| `commande --help` | Affiche l'aide résumée |
| `clear` | Efface l'écran |
| `history` | Affiche l'historique des commandes |

---

> [!NOTE]
> ### À retenir
>
> - La structure d'une commande est : `commande [options] [arguments]`.
> - Linux est **sensible à la casse** — toujours écrire les commandes en minuscules.
> - On navigue avec `pwd` (où suis-je ?), `ls` (qu'y a-t-il ici ?), `cd` (je me déplace).
> - Un chemin **absolu** part de `/` ; un chemin **relatif** part du dossier courant.
> - On lit les fichiers avec `cat`, `less`, `head`, `tail`.
> - L'aide est toujours disponible : `man commande` ou `commande --help`.
> - **Tab** complète automatiquement — à utiliser sans modération.
---

> [!TIP]
> **TP associé** → `tp-04-terminal.md`
---

---

[← L'interface graphique](https://kayasam.github.io/linux-initiation/03-interface-graphique/) · [Chapitre suivant →](https://kayasam.github.io/linux-initiation/05-fichiers-et-repertoires/)
