---
title: "Orion Académie — Le jeu"
---

# Orion Académie — Apprendre Bash en sauvant une station

La station Orion est en panne. Son robot, **BIP-42**, prétend avoir la situation sous contrôle. Il a mangé le manuel et verrouillé le chocolat.

Une aventure gratuite dans le terminal : **48 missions, huit secteurs, huit badges**, de vraies commandes Bash et un jeu à construire pour la finale. Après téléchargement, tout fonctionne **hors ligne**.

```text
          *             .---.                  .
                    .--'     '--.
           *      _/   ORION     \_     *
              ===[=== ACADEMIE ===]===
                  \_           _/
                    '--.   .--'
                        '-'
       UNE STATION A SAUVER. UN ROBOT A SUPPORTER.

       .-----.
       | o o |   BIP-42 : Je supervise.
       |  ^  |            Tu travailles.
      /|-----|\           Accord parfait.
        /   \
```

## Télécharger et jouer sur Debian

Depuis ton terminal Debian, après ta connexion SSH, colle les commandes **une par une** :

```bash
mkdir -p ~/jeux-bash
cd ~/jeux-bash
curl -fLO https://kayasam.github.io/linux-initiation/telechargements/bash/orion-academie.tar.gz
tar -xzf orion-academie.tar.gz
bash orion-academie/jouer.sh
```

- `mkdir -p` prépare le dossier des téléchargements.
- `curl -fLO` télécharge le fichier : `-f` signale les erreurs HTTP, `-L` suit les redirections, `-O` conserve son nom.
- `tar -xzf` extrait l’archive compressée : `-x` extrait, `-z` décompresse gzip, `-f` désigne le fichier.
- `bash .../jouer.sh` lance l’aventure. Aucun compte administrateur n’est nécessaire.

Si `curl` manque, télécharge l’archive depuis le site sur Windows, puis envoie-la avec PowerShell :

```powershell
scp "$HOME\Downloads\orion-academie.tar.gz" stagiaire@192.168.84.10:
```

Sur Debian : `cd ~`, puis `tar -xzf orion-academie.tar.gz` et `bash orion-academie/jouer.sh`. Adapte le dossier Windows si ton navigateur utilise un autre emplacement.

**Prérequis :** Debian avec Python 3.9 ou plus, Bash, nano et les commandes usuelles `sed`, `awk`, `grep`, `tar`, `cp`, `chmod`, `ls`, `cat`, `readlink`, `ps`. Pas de module Python à installer, pas de réseau pendant la partie.

## Comment jouer ?

Chaque mission raconte un problème et donne un objectif. Tu tapes tes commandes au prompt `ORION 01>`. **Ce sont de vraies commandes Bash**, exécutées avec ton compte dans un atelier créé pour ta partie. L’atelier est annoncé au démarrage ; reste dedans pour les exercices.

Le jeu vérifie le résultat après chaque commande. Il accepte différentes solutions correctes. Les erreurs ne retirent pas de points. Les tests de scripts travaillent sur une copie de l’atelier : ils ne remplissent pas ton vrai tableau de scores.

```text
ORION 01> cd "$ORION_ATELIER/capsule"

[ MISSION ACCOMPLIE ] +100 XP
Un chemin absolu fonctionne quel que soit ton dossier de départ.
BIP-42 : Atterrissage réussi. Le stationnement, nous verrons plus tard.
Tape :suivant pour poursuivre, ou continue tes essais ici.
```

Les commandes du jeu commencent par `:` :

| Commande | Utilité |
|---|---|
| `:mission` | Relire l’objectif |
| `:indice` | Recevoir deux indices successifs |
| `:solution` | Voir une solution complète, à exécuter soi-même |
| `:test` | Vérifier après une modification de fichier |
| `:suivant` | Continuer après une mission réussie |
| `:carte` | Voir les huit secteurs, les XP et la progression |
| `:badges` | Voir tes titres d’explorateur |
| `:journal` | Revoir tes quinze dernières commandes de cette session |
| `:editer atelier/bonjour.sh` | Écrire un script avec nano |
| `:bloc` | Entrer plusieurs lignes ; terminer par `:fin` seul sur sa ligne |
| `:aide` | Relire les commandes du jeu |
| `:quitter` | Sauvegarder et quitter |

Un script de plusieurs lignes peut être écrit avec nano : **Ctrl+O**, **Entrée** pour enregistrer, **Ctrl+X** pour revenir au jeu. `:bloc` permet aussi de coller un bloc complet, notamment les solutions avec `cat <<'BASH'`.

Une mission vaut **100 XP** sans indice, **80** avec le premier, **60** avec les deux, **40** avec la solution. Une mission déjà gagnée conserve ses points. Chercher, se tromper et recommencer reste gratuit.

## Les huit secteurs

| Secteur | Ce que tu apprends |
|---|---|
| 1. Capsule de secours | Chemins, guillemets, Bash et sh, sous-shells |
| 2. Radio et boîte noire | Fichiers, redirections, tubes, grep, printf |
| 3. Réservoir des variables | Affectation, guillemets, calculs, read, export |
| 4. Atelier des robots | Scripts, shebang, syntaxe, exécution, arguments, codes, diagnostic |
| 5. Sas des conditions | Tests de fichiers, seuils numériques, case, validation des saisies |
| 6. Hangar des boucles | for, glob, compteur, while, lecture par lignes, copies |
| 7. Observatoire des données | sed, champs awk, filtres, totaux, rapport de mission |
| 8. Le code chocolat | Construire un « plus ou moins », le hasard, les scores et un menu |

À la fin, tu gardes tous tes scripts. Ton arcade se joue aussi sans Orion Académie : depuis ton atelier, lance `bash finale/arcade.sh`.

## Quitter et reprendre

La progression et les fichiers sont conservés sous `~/orion-academie/`. Relancer la même commande reprend la dernière partie :

```bash
bash ~/jeux-bash/orion-academie/jouer.sh
```

Le jeu restaure le dossier courant de l’atelier et les variables utilisées par les missions. Les alias, fonctions et autres réglages libres du shell sont propres à la session : recrée-les après une reprise si nécessaire. Les fichiers sont toujours conservés.

Pour commencer une **autre partie**, sans supprimer l’ancien atelier :

```bash
bash ~/jeux-bash/orion-academie/jouer.sh --nouvelle
```

La nouvelle partie devient celle reprise par défaut. Chaque ancien atelier garde aussi `.orion-sauvegarde.json` avec son état. Pour deux joueurs indépendants, utilise des dossiers distincts :

```bash
bash ~/jeux-bash/orion-academie/jouer.sh --dossier ~/orion-mila
```

Pour un terminal sans couleurs : ajoute `--sans-couleur`. **Ctrl+C** interrompt une commande ; au prompt du jeu, **Ctrl+D** quitte avec sauvegarde. Si tu tapes `exit` dans Bash, BIP-42 rouvre un shell et conserve les fichiers et la progression.

## Vérifier le téléchargement — facultatif

Dans le dossier contenant l’archive :

```bash
curl -fLO https://kayasam.github.io/linux-initiation/telechargements/bash/orion-academie.tar.gz.sha256
sha256sum -c orion-academie.tar.gz.sha256
```

Le résultat attendu est `orion-academie.tar.gz: OK`.

## Pour le formateur

Les missions suivent les six chapitres Bash du parcours. L’élève écrit de vraies commandes et peut consulter une aide graduée. Les solutions intégrées sont accessibles volontairement avec `:solution` ; les corrections privées des TP ne sont pas distribuées.

Faire expliquer le résultat avant `:suivant` permet de vérifier la compréhension. La progression et les XP encouragent la pratique ; ils ne constituent pas un examen sécurisé. Les commandes tournent avec les droits du joueur : l’atelier est un espace d’exercice, pas un mécanisme d’isolation de sécurité.

Le moteur est en Python standard, pour afficher le jeu et vérifier les missions. Les exercices et le jeu final utilisent Bash. Les sources `orion.py` et `missions.json` sont incluses dans le téléchargement.


[Télécharger Orion Académie](https://kayasam.github.io/linux-initiation/telechargements/bash/orion-academie.tar.gz) · [← Parcours Bash](https://kayasam.github.io/linux-initiation/#bash)
