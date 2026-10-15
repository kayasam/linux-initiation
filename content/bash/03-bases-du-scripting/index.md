---
title: "03. Écrire son premier script"
---

# Chapitre 03 — Écrire son premier script

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="bash/03-bases-du-scripting" style="--resource-count:4"><div class="chapter-resources-heading"><span class="chapter-resources-title">Ressources du chapitre</span><a class="resource-download" href="https://kayasam.github.io/linux-initiation/telechargements/bash/cours/03-bases-du-scripting.md" download><span aria-hidden="true">↓</span> Télécharger le .md</a></div><div class="resource-buttons"><a class="resource-button resource-markdown" data-resource-kind="markdown" href="https://kayasam.github.io/linux-initiation/bash/03-bases-du-scripting/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg></span><span class="resource-label">Markdown<small>Lire le cours</small></span></a><a class="resource-button resource-html" data-resource-kind="html" href="https://kayasam.github.io/linux-initiation/bash/03-bases-du-scripting/html/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 28 32"><path d="M2 2h24l-2 25-10 3-10-3Z" fill="#e44d26"/><path d="M14 5v22l7-2 2-20Z" fill="#f16529"/><path d="M7 8h15l-.3 3H11l.3 3h10l-.8 9-6.5 2-6.5-2-.4-5h3l.2 2.6 3.7 1 3.7-1 .3-3.6H8Z" fill="#fff"/></svg></span><span class="resource-label">HTML<small>Explorer le chapitre</small></span></a><a class="resource-button resource-quiz" data-resource-kind="quiz" href="https://kayasam.github.io/linux-initiation/bash/03-bases-du-scripting/quiz/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="4" y="3" width="24" height="26" rx="6" fill="#7652ad"/><path d="M12 12a4 4 0 1 1 6 3.5c-1.5.8-2 1.4-2 3" fill="none" stroke="#fff" stroke-width="2.8" stroke-linecap="round"/><circle cx="16" cy="23" r="1.6" fill="#fff"/></svg></span><span class="resource-label">Quiz<small>20 questions</small></span></a><a class="resource-button resource-tp" data-resource-kind="tp" href="https://kayasam.github.io/linux-initiation/bash/03-bases-du-scripting/tp"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg></span><span class="resource-label">TP<small>Mettre en pratique</small></span></a></div></nav>
<div class="support-toolbar markdown-course-toolbar"><span>Cours Markdown</span><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div>


> [!NOTE] Objectif
> Transformer quelques commandes en un programme que tu peux relancer, lire et vérifier.
---

## 1. Un script est un fichier texte

Un script Bash contient les commandes que tu aurais pu taper dans le terminal. Bash les lit dans l'ordre. Tu peux ainsi refaire la même tâche sans recopier les commandes.

![Écrire, vérifier puis exécuter](https://kayasam.github.io/linux-initiation/bash/images/bash-03-script.svg)

Commence dans un dossier de travail :

```bash
mkdir -p ~/atelier-bash/scripts
cd ~/atelier-bash/scripts
```

## 2. Créer le fichier avec nano

Ouvre l'éditeur :

<!-- interactif: editeur -->
```bash
nano accueil.sh
```

Dans l'éditeur, saisis le contenu suivant. Ne recopie pas les marques de bloc de code.

<!-- fichier: accueil.sh -->
```bash
#!/usr/bin/env bash

# Un nom peut etre fourni au lancement.
prenom="${1:-visiteur}"
station="Orion"

echo "Bienvenue $prenom sur $station."
```

| Ligne | Rôle |
|---|---|
| `#!/usr/bin/env bash` | Demande d'utiliser Bash pour l'exécution directe |
| `# Un nom…` | Commentaire : Bash l'ignore, il s'adresse à qui lit le fichier |
| `prenom="${1:-visiteur}"` | Prend le premier argument fourni au script, ou `visiteur` s'il n'y en a pas |
| `station="Orion"` | Range une valeur fixe |
| `echo ...` | Produit le message |

La troisième ligne est la plus chargée : `$1` désigne le premier argument et `${1:-visiteur}` fournit une valeur de secours, comme le `${nom:-defaut}` du chapitre 02. Le §5 y revient en détail — pour l'instant, recopie-la telle quelle.

La première ligne s'appelle le **shebang**. Nous écrivons `#!/usr/bin/env bash` plutôt que `#!/bin/bash` : `env` va chercher Bash là où il est réellement installé, ce qui rend le script utilisable sur des systèmes où le chemin diffère.

Dans nano : **Ctrl+O**, puis **Entrée** pour enregistrer ; **Ctrl+X** pour quitter. Les indications `^O` et `^X` de nano signifient « Ctrl+O » et « Ctrl+X ».

> [!WARNING] Fichier créé sous Windows
> Si tu vois une erreur mentionnant `bash\r`, le fichier a été enregistré avec des fins de ligne Windows (CRLF). Un script Linux doit être enregistré en **LF**. En travaillant avec nano dans Debian, tu évites ce problème.

## 3. Vérifier avant de lancer

```bash
bash -n accueil.sh
```

`-n` vérifie la syntaxe **sans exécuter** les commandes. Si rien ne s'affiche et que la commande réussit, Bash n'a pas trouvé d'erreur de syntaxe. Cela ne garantit pas que le programme fait ce que tu souhaites : il faut aussi le tester.

Lance-le ensuite en indiquant l'interpréteur :

```bash
bash accueil.sh Mila
```

Résultat : `Bienvenue Mila sur Orion.`. Dans ce mode, le fichier n'a pas besoin d'être exécutable.

## 4. Exécuter directement le script

```bash
chmod +x accueil.sh
./accueil.sh Mila
```

- `chmod +x` ajoute le droit d'exécution.
- `./accueil.sh` désigne le fichier dans le dossier courant.
- `Mila` est un argument transmis au script.

Le `./` n'est pas décoratif : le dossier courant n'est généralement pas dans `PATH`. Pour un script stocké ailleurs, indique son chemin.

Noter aussi ce qui **n'est pas** nécessaire : aucun `sudo` ici. Tu es propriétaire de ton dossier personnel, donc tu peux y créer un fichier, le rendre exécutable et le lancer sans droits administrateur. Un script qui réclame `sudo` pour travailler dans `~` est le signe qu'il se trompe de dossier.

## 5. Les arguments : des valeurs fournies au départ

Dans le script, `$1` est le premier argument. `${1:-visiteur}` donne une valeur par défaut si ce premier argument est absent ou vide.

```bash
./accueil.sh
./accueil.sh "Mila Vega"
```

Résultats :

```text
Bienvenue visiteur sur Orion.
Bienvenue Mila Vega sur Orion.
```

Les guillemets autour de `Mila Vega` conservent un seul argument.

| Variable spéciale | Signification |
|---|---|
| `$0` | Nom utilisé pour lancer le script |
| `$1`, `$2` | Premier et deuxième arguments |
| `$#` | Nombre d'arguments |
| `"$@"` | Tous les arguments, en conservant leurs limites |

Pour observer les arguments, crée un second fichier :

<!-- fichier: arguments.sh -->
```bash
#!/usr/bin/env bash
echo "Nombre : $#"
printf 'Argument : %s\n' "$@"
```

```bash
bash arguments.sh "Mila Vega" pilote
```

```text
Nombre : 2
Argument : Mila Vega
Argument : pilote
```

`"$@"` ne recoupe pas `Mila Vega` en deux mots : c'est bien un seul argument.

Une ligne de format, deux lignes affichées : `printf` **réapplique son format tant qu'il reste des arguments à consommer**. C'est le seul endroit de ce chapitre où `printf` rend un service qu'`echo` ne sait pas rendre — `echo "Argument : $@"` n'afficherait qu'une seule ligne, avec les deux valeurs à la suite. Partout ailleurs, `echo` suffit.

## 6. Le code de retour

Une commande fournit un **code de retour**. `0` signifie qu'elle a réussi selon ses propres règles. Une valeur différente de zéro indique un autre résultat : erreur, absence de correspondance pour `grep`, etc.

```bash
bash accueil.sh Mila
code=$?
echo "Code : $code"
```

`$?` donne le code de la **dernière commande**. Ici, le script réussit et le code est `0`. Il faut le lire tout de suite, avant qu'une autre commande le remplace.

Observe un échec sans créer de fichier :

```bash
ls dossier-inexistant-orion 2>/dev/null
code=$?
echo "Code apres echec : $code"
```

Le code est différent de zéro. `2>/dev/null` masque le message d'erreur ; il ne transforme pas l'échec en réussite. Nous verrons comment réagir au résultat dans le chapitre suivant.

## 7. Comprendre un comportement inattendu

```bash
bash -x accueil.sh Mila
```

`-x` affiche les commandes après les expansions. Cela aide à comprendre les valeurs réellement utilisées. Les lignes de trace et le résultat normal peuvent apparaître ensemble.

> [!WARNING] Trace et données personnelles
> Une trace peut afficher les valeurs des variables. Utilise les données fictives du cours avant de partager une capture.

## À retenir

- Le shebang choisit l'interpréteur lors de l'exécution directe ; nous utilisons `#!/usr/bin/env bash`.
- `bash -n` vérifie la syntaxe ; les essais vérifient le comportement ; `bash -x` montre les valeurs réellement utilisées.
- `chmod +x` donne le droit d'exécution, `./` indique le fichier du dossier courant : les deux sont nécessaires.
- Les arguments se lisent avec `$1`, `$#` et `"$@"` ; `${1:-defaut}` prévoit le cas où l'argument est absent.
- Protège les arguments avec des guillemets.
- `$?` donne le code de retour de la dernière commande : `0` pour une réussite, autre chose sinon. Lis-le tout de suite.
- Un script n'a pas besoin de `sudo` pour travailler dans ton dossier personnel.

**À toi :** combien d'arguments reçoit `bash arguments.sh "poste radio" Orion` ? Pourquoi `chmod +x` ne suffit-il pas à lancer un fichier ? Que vaut `$?` juste après une commande qui a échoué ?

[Passer au TP](https://kayasam.github.io/linux-initiation/bash/03-bases-du-scripting/tp)

[← Parcours Bash](https://kayasam.github.io/linux-initiation/#bash) · [Tous les TP Bash](https://kayasam.github.io/linux-initiation/bash/tp/)
