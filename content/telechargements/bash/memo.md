# Mémo Bash — Les repères du parcours

| Besoin | Repère |
|---|---|
| Savoir où je suis | `pwd` |
| Changer de dossier | `cd` |
| Lire un fichier | `cat` |
| Afficher une phrase simple | `echo "Bonjour"` |
| Formater une sortie | `printf '%s\n' "$nom"` |
| Identifier le shell actuel | `ps -p $$ -o comm=` |
| Grouper dans un sous-shell | `( commandes )` |
| Remplacer / ajouter dans un fichier | `>` / `>>` |
| Relier deux commandes | le tube `\|` |
| Affecter / lire une variable | `nom="Mila"` / `"$nom"` |
| Demander une réponse | `read -r` |
| Récupérer une sortie | `$(commande)` |
| Calculer avec des entiers | `$((calcul))` |
| Vérifier la syntaxe | `bash -n script.sh` |
| Exécuter directement | droit `+x`, puis `./script.sh` |
| Arguments | `$1`, `$2`, `$#`, `"$@"` |
| Dernier code de retour | `$?`, à lire immédiatement |
| Choisir | `if` / `case` |
| Répéter | `for` / `while` |
| Transformer du texte | `sed` |
| Travailler avec des champs | `awk` |

## Avant de rendre un script

1. Vérifier le dossier de travail et les fichiers utilisés.
2. Garder les variables de chemin entre guillemets.
3. Tester la syntaxe puis un cas normal.
4. Tester un argument absent, un nom composé et une donnée vide quand ils sont pertinents.
5. Vérifier les messages et les codes de retour.
6. Relire le résultat avant d’écrire dans un fichier existant.

[Revenir aux cours](https://kayasam.github.io/linux-initiation/#bash)
