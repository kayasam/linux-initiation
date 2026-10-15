---
title: "03. Écrire son premier script"
---

# Chapitre 03 — Écrire son premier script

> [!TIP] Ressources du chapitre
> - [Version HTML](https://kayasam.github.io/linux-initiation/bash/cours/03-bases-du-scripting-interactif.html)
> - <a href="https://kayasam.github.io/linux-initiation/telechargements/bash/cours/03-bases-du-scripting.md" download>Télécharger le cours en Markdown</a>
> - [Faire le quiz — 20 questions](https://kayasam.github.io/linux-initiation/bash/cours/quiz/03-bases-du-scripting.html)
> - [Passer au TP](https://kayasam.github.io/linux-initiation/bash/03-bases-du-scripting/tp)


> [!NOTE] Objectif
> Transformer quelques commandes en un programme que tu peux relancer, lire et vérifier.

**À connaître :** shebang, `nano`, `bash`, `chmod +x`, `./`, `$1`, `$#`, `"$@"`, `$?`.
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

printf 'Bienvenue %s sur %s.\n' "$prenom" "$station"
```

| Ligne | Rôle |
|---|---|
| `#!/usr/bin/env bash` | Demande d'utiliser Bash pour l'exécution directe |
| `# Un nom…` | Commentaire destiné à la personne qui lit le fichier |
| `prenom=...` | Prépare une valeur |
| `printf ...` | Produit le message |

Dans nano : **Ctrl+O**, puis **Entrée** pour enregistrer ; **Ctrl+X** pour quitter. Les indications `^O` et `^X` de nano signifient « Ctrl+O » et « Ctrl+X ».

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
printf 'Nombre : %s\n' "$#"
printf 'Argument : %s\n' "$@"
```

```bash
bash arguments.sh "Mila Vega" pilote
```

Tu obtiens un nombre de **2**, puis une ligne par argument. `"$@"` ne recoupe pas `Mila Vega` en deux mots.

## 6. Le code de retour

Une commande fournit un **code de retour**. `0` signifie qu'elle a réussi selon ses propres règles. Une valeur différente de zéro indique un autre résultat : erreur, absence de correspondance pour `grep`, etc.

```bash
bash accueil.sh Mila
code=$?
printf 'Code : %s\n' "$code"
```

`$?` donne le code de la **dernière commande**. Ici, le script réussit et le code est `0`. Il faut le lire tout de suite, avant qu'une autre commande le remplace.

Observe un échec sans créer de fichier :

```bash
ls dossier-inexistant-orion 2>/dev/null
code=$?
printf 'Code apres echec : %s\n' "$code"
```

Le code est différent de zéro. `2>/dev/null` masque le message d'erreur ; il ne transforme pas l'échec en réussite. Nous verrons comment réagir au résultat dans le chapitre suivant.

## 7. Comprendre un comportement inattendu

```bash
bash -x accueil.sh Mila
```

`-x` affiche les commandes après les expansions. Cela aide à comprendre les valeurs réellement utilisées. Les lignes de trace et le résultat normal peuvent apparaître ensemble.

> [!WARNING] Trace et données personnelles
> Une trace peut afficher les valeurs des variables. Utilise les données fictives du cours avant de partager une capture.

Si tu crées un fichier sous Windows et vois une erreur liée à `bash\r`, vérifie les fins de ligne : le script doit être enregistré en **LF**, sans retours Windows CRLF. En travaillant avec nano dans Debian, tu évites ce problème.

## À retenir

- Le shebang choisit l'interpréteur lors de l'exécution directe.
- `bash -n` vérifie la syntaxe ; les essais vérifient le comportement.
- Protège les arguments avec des guillemets.
- Un script n'a pas besoin de `sudo` pour travailler dans ton dossier personnel.

**À toi :** combien d'arguments reçoit `bash arguments.sh "poste radio" Orion` ? Pourquoi `chmod +x` ne suffit-il pas à lancer un fichier ?

[Passer au TP](https://kayasam.github.io/linux-initiation/bash/03-bases-du-scripting/tp)

[← Parcours Bash](https://kayasam.github.io/linux-initiation/#bash) · [Tous les TP Bash](https://kayasam.github.io/linux-initiation/bash/tp/)
