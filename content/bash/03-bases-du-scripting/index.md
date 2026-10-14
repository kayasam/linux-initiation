---
title: "03. Bases du scripting"
---

# Chapitre 03 — Bases du scripting

> [!TIP] Ressources du chapitre
> - [Version HTML interactive](https://kayasam.github.io/linux-initiation/bash/cours/03-bases-du-scripting-interactif.html)
> - <a href="https://kayasam.github.io/linux-initiation/telechargements/bash/cours/03-bases-du-scripting.md" download>Télécharger le cours en Markdown</a>
> - [Passer au TP](https://kayasam.github.io/linux-initiation/bash/tp/tp-03-bases-du-scripting)


---

## 1. Qu'est-ce qu'un script ?

[Formatux](https://www.formatux.fr/formatux-bash/develop/module-010-niveau1/index.html) :

> Les scripts en shell ont l'avantage d'être réalisables **rapidement** et de manière **fiable**, **sans compilation** ni installation de commandes supplémentaires. Un script shell n'est qu'un fichier texte sans enluminures.
>
> Pour écrire un script shell, il suffit de réunir dans un même fichier texte toutes les commandes nécessaires. En rendant ce fichier exécutable, le shell le lira **séquentiellement** et exécutera une à une les commandes le comportant.

Un bon script est :
- **Fiable** : son fonctionnement est irréprochable même en cas de mauvaise utilisation
- **Commenté** : son code est annoté pour faciliter la relecture et les évolutions
- **Lisible** : le code est indenté, les commandes sont aérées
- **Portable** : le code fonctionne sur tout système Linux

---

<iframe width="560" height="315" src="https://www.youtube.com/embed/XGxtbcAzk-g?si=YZyolW6VCyvwFE7I" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## 2. Structure d'un script

Un script bash est un fichier texte qui contient des commandes. Il s'exécute **ligne par ligne, du début à la fin**.

```bash
#!/usr/bin/env bash        ← ligne 1 obligatoire : le shebang

# Ceci est un commentaire  ← tout ce qui suit # est ignoré

echo "Bonjour !"           ← commandes, une par ligne
date +%Y-%m-%d
```

Les quatre éléments d'un script :

| Élément | Rôle |
|---------|------|
| **Shebang** (ligne 1) | Indique à l'OS quel interpréteur utiliser |
| **Commentaires** (`#`) | Annotations ignorées à l'exécution |
| **Commandes** | Le contenu du script, une par ligne |
| **Indentation** | Non obligatoire, mais indispensable pour la lisibilité |

---

## 3. Le shebang

https://abs.traduc.org/abs-fr/ch02.html#magnumref :

> Le *sha-bang* (`#!`) en tête de fichier indique à votre système que ce fichier est un ensemble de commandes pour l'interpréteur indiqué. Tout de suite après le *sha-bang* se trouve le chemin vers le programme qui interprète les commandes de ce script.

```bash
#!/usr/bin/env bash    ← recommandé (compatible tous les systèmes)
#!/bin/bash            ← fonctionne aussi mais moins portable
#!/usr/bin/sh          ← interpréteur POSIX minimal (pas de fonctions bash)
```

> [!TIP]
> Toujours utiliser `#!/usr/bin/env bash` plutôt que `#!/bin/bash`. `env` cherche bash dans le `PATH` et le trouve quel que soit son emplacement sur le système.
> [!NOTE]
> Le shebang n'est lu que si le script est exécuté directement (`./script.sh`). Si on passe le script en argument à bash (`bash script.sh`), le shebang est ignoré.
---

## 4. Exécution d'un script

https://learning.lpi.org/fr/learning-materials/102-500/105/105.2/105.2_01/

Il existe deux façons d'exécuter un script :

### Méthode 1 — passer le script à bash

```bash
bash monscript.sh
```

Simple, ne nécessite pas de droits d'exécution sur le fichier.

### Méthode 2 — rendre le script exécutable

```bash
chmod +x monscript.sh    # donner le droit d'exécution (une seule fois)
./monscript.sh           # exécuter
```

> [!WARNING]
> Le `./` devant le nom du script est obligatoire si le dossier courant n'est pas dans le `PATH`. Sans lui, bash cherche la commande dans les dossiers du `PATH` et ne trouve pas le script.
### Environnement d'exécution

Quand un script est exécuté, il tourne dans un **sous-shell** — un processus enfant du shell courant. Conséquences :
- Les variables locales du shell courant ne sont **pas** disponibles dans le script (sauf si exportées)
- Les modifications faites dans le script (variables, `cd`…) n'affectent **pas** le shell courant
- Le script ne charge **pas** `.bashrc` — il n'a pas d'environnement interactif

---

## 5. Options de shell — sécuriser un script

Par défaut, bash continue l'exécution même si une commande échoue. C'est dangereux dans un script. On active des options de sécurité en début de script avec `set` :

```bash
#!/usr/bin/env bash

set -e              # arrête le script si une commande échoue
set -u              # arrête le script si une variable non définie est utilisée
set -o pipefail     # arrête si une commande dans un tube échoue
set -x              # affiche chaque commande avant de l'exécuter (debug)
```

Version condensée — les trois premières ensemble :

```bash
set -euo pipefail
```

| Option | Signification | Utilité |
|--------|--------------|---------|
| `-e` | *errexit* | Arrête immédiatement si une commande renvoie une erreur |
| `-u` | *nounset* | Traite les variables non définies comme des erreurs |
| `-o pipefail` | — | Propage les erreurs dans les tubes (`\|`) |
| `-x` | *xtrace* | Affiche les commandes au moment de leur exécution (debug) |

> [!TIP]
> **Bonne pratique** : commencer tout script avec `set -euo pipefail`. Cela transforme les erreurs silencieuses en arrêts explicites, ce qui rend les bugs bien plus faciles à trouver.
> [!WARNING]
> `set -x` est très utile pour déboguer mais produit beaucoup de sortie. L'activer uniquement pendant la mise au point, pas en production.
Pour désactiver une option ponctuellement :

```bash
set +e   # désactive -e
commande_qui_peut_echouer
set -e   # réactive -e
```

---

## 6. Code retour d'une commande

Toute commande Linux retourne un **code de retour** à la fin de son exécution :
- `0` → succès
- Toute autre valeur (1 à 255) → échec ou erreur

Ce code est accessible immédiatement après l'exécution via `$?` :

```bash
ls /etc
echo $?    # 0  ← succès

ls /dossier-inexistant
echo $?    # 2  ← échec (dossier introuvable)
```

> [!WARNING]
> `$?` ne contient que le code de la **dernière** commande exécutée. Si tu exécutes une autre commande entre les deux, tu perds la valeur.
C'est ce code que `set -e` surveille : dès qu'une commande renvoie autre chose que 0, le script s'arrête.

---

## 7. Variables spéciales et paramètres positionnels

https://learning.lpi.org/fr/learning-materials/102-500/105/105.2/105.2_01/#:~:text=variables%20sp%C3%A9ciales

Ces variables sont définies automatiquement par bash. On ne peut que les lire, pas les modifier.

| Variable | Contenu |
|----------|---------|
| `$0` | Nom du script |
| `$1`, `$2`… `$9` | Arguments passés au script (1er, 2e… 9e) |
| `${10}`, `${11}`… | Arguments au-delà du 9e (accolades obligatoires) |
| `$#` | Nombre d'arguments passés au script |
| `$@` | Tous les arguments (chacun entre guillemets si `"$@"`) |
| `$*` | Tous les arguments (un seul mot si `"$*"`) |
| `$?` | Code de retour de la dernière commande |
| `$$` | PID du shell courant |
| `$!` | PID du dernier processus lancé en arrière-plan |

> Différence entre `$@` et `$*` : https://unix.stackexchange.com/questions/129072/whats-the-difference-between-and

### Exemple concret

`salutation.sh` :
```bash
#!/usr/bin/env bash

set -euo pipefail

echo "Nom du script  : $0"
echo "1er argument   : $1"
echo "Nb d'arguments : $#"
echo "Tous les args  : $@"
```

```bash
./salutation.sh Alice Bob Charlie
# Nom du script  : ./salutation.sh
# 1er argument   : Alice
# Nb d'arguments : 3
# Tous les args  : Alice Bob Charlie
```

---

## 8. Micro-TP — Premier script

Créer un script `d.sh` dans le répertoire `~/scripting` qui affiche la date au format `AAAA-MM-JJ`.

```bash
mkdir -p ~/scripting
nano ~/scripting/d.sh
```

Contenu du script :
```bash
#!/usr/bin/env bash

set -euo pipefail

date +%F
```

Exécution :
```bash
chmod +x ~/scripting/d.sh
~/scripting/d.sh
# 2026-04-27
```

> [!NOTE]
> `date +%F` est équivalent à `date +%Y-%m-%d`. Le format `%F` est un raccourci ISO 8601.
---

## Récapitulatif des commandes

| Commande | Description |
|----------|-------------|
| `bash script.sh` | Exécute un script sans droit d'exécution |
| `chmod +x script.sh` | Donne le droit d'exécution à un script |
| `./script.sh` | Exécute un script dans le répertoire courant |
| `set -e` | Arrête le script si une commande échoue |
| `set -u` | Arrête si une variable non définie est utilisée |
| `set -o pipefail` | Propage les erreurs dans les tubes |
| `set -x` | Mode debug : affiche chaque commande avant exécution |
| `set -euo pipefail` | Les trois options de sécurité en une ligne |
| `set +e` | Désactive l'option `-e` |
| `echo $?` | Affiche le code de retour de la dernière commande |
| `$0` | Nom du script |
| `$1` … `$9` | Arguments positionnels (1er au 9e) |
| `$#` | Nombre d'arguments passés au script |
| `$@` | Tous les arguments |
| `$$` | PID du shell courant |
| `type -t commande` | Indique si une commande est interne ou externe |
| `date +%F` | Affiche la date au format AAAA-MM-JJ |
| `date +%Y-%m-%d` | Idem, format explicite |

---

> [!NOTE]
> ### À retenir
> 
> - Un script bash est un fichier texte exécuté **ligne par ligne, du début à la fin**.
> - La **première ligne** est toujours le shebang : `#!/usr/bin/env bash`.
> - Deux façons d'exécuter : `bash script.sh` (sans droit d'exécution) ou `chmod +x` + `./script.sh`.
> - Le `./` est obligatoire — bash ne cherche pas dans le dossier courant par défaut.
> - Commencer tout script avec `set -euo pipefail` : arrêt immédiat sur erreur, variable non définie ou échec dans un tube.
> - `$?` contient le code de retour de la dernière commande : `0` = succès, autre = erreur.
> - Les **variables spéciales** : `$0` nom du script, `$1`…`$9` arguments, `$#` nombre d'arguments, `$@` tous les arguments.
> - Un script s'exécute dans un **sous-shell** — il ne modifie pas le shell courant et ne charge pas `.bashrc`.
---

> [!TIP]
> **TP associé** → `tp-03-bases-du-scripting.md`

[← Parcours Bash](https://kayasam.github.io/linux-initiation/#bash) · [Tous les TP Bash](https://kayasam.github.io/linux-initiation/bash/tp/)
