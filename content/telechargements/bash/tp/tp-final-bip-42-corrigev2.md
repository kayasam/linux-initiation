# TP final — BIP-42 a perdu son boulon — Corrigév2

> Essaie chaque question avant de cliquer sur **Afficher la correction**. Chaque réponse s’ouvre et se referme indépendamment.

> Parcours associé : les six chapitres Bash. Travaille dans Bash sur la VM Debian, après ta connexion SSH.

## Mission — Libérer le chocolat

Le robot **BIP-42** a verrouillé le distributeur de chocolat d'Orion. Il affirme que seuls les humains « suffisamment logiques » méritent une tasse. Son code secret est un nombre entre **1 et 9**. Heureusement, il est incapable de garder ses commentaires pour lui.

Tu vas créer un vrai jeu « plus ou moins », puis lui ajouter des scores. **On construit une version qui fonctionne avant d'ajouter la suite.** Garde les versions précédentes pour observer tes progrès.

Voici la partie que tu dois pouvoir jouer à la fin, en mode entraînement :

```text
========================================
 BIP-42 : OPERATION CHOCOLAT
========================================
Mila Vega, trouve mon code entre 1 et 9.
Tu as 5 essais. Les fautes de frappe ne comptent pas.
Essai 1/5 - Ton nombre : 1
Trop petit ! Meme mon grille-pain vise plus haut.
Essai 2/5 - Ton nombre : 9
Trop grand ! Tu cherches un code, pas mon numero de serie.
Essai 3/5 - Ton nombre : banane
Une banane n'est pas un chiffre. Essaie de 1 a 9.
Essai 3/5 - Ton nombre : 6
BINGO ! Le chocolat est libere en 3 essais.
BIP-42 : Je te laisse gagner. Evidemment.
Score enregistre. BIP-42 prepare ta tasse.
```

> [!TIP] Règle du jeu
> « Trop petit » signifie que le nombre proposé est inférieur au secret. « Trop grand » signifie qu'il est supérieur. Pour commencer, le secret sera **toujours 6** : tu pourras vérifier ton programme sans dépendre du hasard.

## Partie A — Monter l'atelier

**A1.** Prépare ton dossier :

```bash
mkdir -p ~/atelier-bash/final-bip-42
cd ~/atelier-bash/final-bip-42
```

> [!success]- Afficher la correction — A1
> ```bash
> mkdir -p ~/atelier-bash/final-bip-42
> cd ~/atelier-bash/final-bip-42
> ```
>
> Reste dans cet atelier pour les lancements : les chemins `robot.txt` et `scores.csv` sont relatifs au dossier courant.

**A2.** Crée un fichier `robot.txt` contenant cette ligne :

```text
ROBOT : Qui ose toucher a mon chocolat ?
```

Utilise `echo` et `>`. Lis le fichier avec `cat`.

> [!success]- Afficher la correction — A2
> ```bash
> echo "ROBOT : Qui ose toucher a mon chocolat ?" > robot.txt
> cat robot.txt
> ```
>
> Le fichier doit contenir exactement la phrase de l’énoncé. `>` crée ou remplace ce fichier de l’atelier.

**A3.** Crée le script `jeu-v1.sh` avec nano. Ajoute le shebang Bash et un titre avec `echo`.

**À chaque version :** enregistre, lance `bash -n nom-du-script.sh`, puis `bash nom-du-script.sh`. Pour lancer directement le fichier avec `./`, ajoute le droit d'exécution avec `chmod +x`.

> [!success]- Afficher la correction — A3
> ```bash
> #!/usr/bin/env bash
> echo "BIP-42 : OPERATION CHOCOLAT"
> ```
>
> Enregistre ce début dans `jeu-v1.sh`. Après chaque étape, vérifie la syntaxe avec `bash -n jeu-v1.sh`.

## Partie B — Un nombre, une réponse

**B1.** Dans `jeu-v1.sh`, définis `secret=6`. Demande une proposition avec `read -p`.

> [!success]- Afficher la correction — B1
> ```bash
> secret=6
> if ! read -p 'Ton nombre de 1 a 9 : ' proposition; then
>     echo "Saisie interrompue" >&2
>     exit 2
> fi
> ```
>
> Ajoute ce bloc après le titre. La garde évite de continuer avec une saisie interrompue.

**B2.** Vérifie la saisie **avant le calcul ou la comparaison numérique**. Seul un chiffre de `1` à `9` est accepté. Le motif `[1-9]` dans `case` correspond à exactement un caractère dans cet intervalle : `6` convient, `06`, `10`, une saisie vide ou `banane` ne conviennent pas.

> Indice : un premier cas `[1-9])` accepte la saisie ; le cas `*)` affiche une erreur et termine avec le code 2. Si `read` échoue, affiche « Saisie interrompue » et termine aussi avec 2.

> [!success]- Afficher la correction — B2
> ```bash
> case "$proposition" in
>     [1-9]) ;;
>     *) echo "Une banane n'est pas un chiffre. Essaie de 1 a 9." >&2
>        exit 2 ;;
> esac
> ```
>
> `[1-9]` est ici un motif de `case`. Il accepte un seul caractère de 1 à 9 : `06`, `10`, le vide et `banane` sont refusés avant la comparaison numérique.

**B3.** Avec `if`, `elif` et `else`, compare la proposition à `secret` :

| Proposition | Réaction |
|---|---|
| Inférieure à 6 | `Trop petit !` |
| Supérieure à 6 | `Trop grand !` |
| Égale à 6 | `BINGO ! Le chocolat est libere.` |

Ajoute une phrase drôle après « Trop petit » et « Trop grand ».

**Point de contrôle :** lance trois fois le script avec `1`, `9` et `6`. Teste aussi `banane`. Pour cette première version, il n'y a qu'une proposition par lancement ; une saisie valide se termine avec 0, même si elle est incorrecte.

> [!success]- Afficher la correction — B3
> ```bash
> if [[ "$proposition" -lt "$secret" ]]; then
>     echo "Trop petit ! Meme mon grille-pain vise plus haut."
> elif [[ "$proposition" -gt "$secret" ]]; then
>     echo "Trop grand ! Tu cherches un code, pas mon numero de serie."
> else
>     echo "BINGO ! Le chocolat est libere."
> fi
> ```
>
> Avec `1` : trop petit ; avec `9` : trop grand ; avec `6` : victoire. Cette version ne propose qu’un essai. Une saisie valide finit avec 0, même si le secret n’a pas été trouvé ; une saisie invalide renvoie 2.

## Partie C — Une vraie partie

**C1.** Copie `jeu-v1.sh` vers `jeu-v2.sh`. Le secret reste fixé à 6.

> [!success]- Afficher la correction — C1
> ```bash
> cp jeu-v1.sh jeu-v2.sh
> ```
>
> Conserve la première version. Dans `jeu-v2.sh`, le secret reste **6** pour reproduire les tests.

**C2.** Ajoute `essais=0` et `maximum=5`. Place la question et les tests dans une boucle `while` qui continue tant que `essais` est inférieur à `maximum`.

> [!success]- Afficher la correction — C2
> ```bash
> essais=0
> maximum=5
> ```
>
> Ajoute ces variables avant la boucle. La question et les comparaisons se placent entre `while [[ "$essais" -lt "$maximum" ]]; do` et `done`. La version complète est donnée en C4.

**C3.** Une saisie invalide affiche une remarque puis utilise `continue` : **elle ne consomme aucun essai**. Une saisie valide augmente le compteur avec `$((essais + 1))`.

> [!success]- Afficher la correction — C3
> ```bash
> case "$proposition" in
>     [1-9]) ;;
>     *) echo "Une banane n'est pas un chiffre. Essaie de 1 a 9."
>        continue ;;
> esac
> essais=$((essais + 1))
> ```
>
> Ce bloc se place **dans la boucle**, après le `read` protégé. La saisie invalide atteint `continue` avant l’incrémentation : aucun essai n’est consommé.

**C4.** Si le joueur trouve le secret, affiche son nombre d'essais et termine avec 0. Sinon, après cinq propositions valides, annonce la défaite, révèle le secret et termine avec 1.

**Point de contrôle :** `1`, `9`, `banane`, `6` doit donner une victoire en **3 essais**. Cinq fois `1` doit donner une défaite. Une fin de saisie (**Ctrl+D** sur une ligne vide) termine avec 2 et ne relance pas indéfiniment la question.

> [!success]- Afficher la correction — C4
> ```bash
> #!/usr/bin/env bash
> secret=6
> essais=0
> maximum=5
> while [[ "$essais" -lt "$maximum" ]]; do
>     if ! read -p "Essai $((essais + 1))/$maximum - Ton nombre : " proposition; then
>         echo "Saisie interrompue" >&2
>         exit 2
>     fi
>     case "$proposition" in
>         [1-9]) ;;
>         *) echo "Une banane n'est pas un chiffre. Essaie de 1 a 9."
>            continue ;;
>     esac
>     essais=$((essais + 1))
>     if [[ "$proposition" -lt "$secret" ]]; then
>         echo "Trop petit ! Meme mon grille-pain vise plus haut."
>     elif [[ "$proposition" -gt "$secret" ]]; then
>         echo "Trop grand ! Tu cherches un code, pas mon numero de serie."
>     else
>         unite="essais"
>         if [[ "$essais" -eq 1 ]]; then
>             unite="essai"
>         fi
>         echo "BINGO ! Le chocolat est libere en $essais $unite."
>         exit 0
>     fi
> done
> echo "PERDU ! Le code etait $secret. BIP-42 boit ta tasse."
> exit 1
> ```
>
> Voici `jeu-v2.sh` complet. La victoire renvoie 0 immédiatement ; seule l’épuisement des cinq essais atteint la défaite, code 1. `1`, `9`, `banane`, `6` donne une victoire en **3 essais**. Une fin d’entrée renvoie 2.

## Partie D — Personnaliser le robot

**D1.** Copie `jeu-v2.sh` vers `jeu.sh`. Accepte au maximum deux arguments : le prénom ou pseudo, puis le mode.

| Lancement | Comportement |
|---|---|
| `./jeu.sh` | Joueur `visiteur`, mode `normal` |
| `./jeu.sh "Mila Vega" entrainement` | Joueur Mila Vega, secret fixé à 6 |
| `./jeu.sh Noe normal` | Secret aléatoire entre 1 et 9 |

Utilise `${1:-visiteur}` et `${2:-normal}`. Un mode inconnu ou trop d'arguments doit afficher l'utilisation et terminer avec 2. Pour les scores, refuse aussi un pseudo contenant `;` ou un retour à la ligne : une partie occupera une seule ligne du fichier.

> [!success]- Afficher la correction — D1
> ```bash
> cp jeu-v2.sh jeu.sh
> ```
>
> Remplace le début de `jeu.sh` par cette gestion des arguments, avant la sélection du secret :
>
> ```bash
> #!/usr/bin/env bash
> if [[ "$#" -gt 2 ]]; then
>     echo 'Usage : ./jeu.sh [pseudo] [normal|entrainement]' >&2
>     exit 2
> fi
> joueur="${1:-visiteur}"
> mode="${2:-normal}"
> # ; separe les champs ; les retours a la ligne separeraient les parties.
> if [[ "$joueur" == *';'* || "$joueur" == *$'\n'* || "$joueur" == *$'\r'* ]]; then
>     echo "Pseudo interdit : pas de point-virgule ni de retour a la ligne." >&2
>     exit 2
> fi
> ```
>
> Le pseudo composé reste un argument lorsqu’il est entre guillemets. Le garde refuse `;`, le retour à la ligne et le retour chariot pour préserver le format des scores.

**D2.** Choisis le secret avec `case`. En mode normal :

```bash
secret=$((RANDOM % 9 + 1))
```

`RANDOM` fournit un entier pseudo-aléatoire de Bash. `% 9` donne un reste de 0 à 8 ; `+ 1` le ramène entre 1 et 9. Ce hasard suffit pour notre jeu.

> [!success]- Afficher la correction — D2
> ```bash
> case "$mode" in
>     normal) secret=$((RANDOM % 9 + 1)) ;;
>     entrainement) secret=6 ;;
>     *) echo 'Usage : ./jeu.sh [pseudo] [normal|entrainement]' >&2
>        exit 2 ;;
> esac
> ```
>
> Le mode entraînement fixe **6**. Le mode normal choisit un entier de 1 à 9. Un mode inconnu affiche l’utilisation et renvoie 2.

**D3.** Affiche ton titre, le nom du joueur et les règles. Avec une boucle `for`, fais afficher un petit démarrage : `3`, `2`, `1`. Pas besoin de pause entre les nombres.

> [!success]- Afficher la correction — D3
> ```bash
> echo "========================================"
> echo " BIP-42 : OPERATION CHOCOLAT"
> echo "========================================"
> for numero in 3 2 1; do
>     echo "Demarrage : $numero"
> done
> echo "$joueur, trouve mon code entre 1 et 9."
> echo "Tu as 5 essais. Les fautes de frappe ne comptent pas."
> ```
>
> Place cet accueil avant la boucle de jeu. Une pause n’est pas nécessaire pour les tests.

**D4.** Fais parler le robot à partir de `robot.txt`. Utilise `sed` pour remplacer `ROBOT` par `BIP-42` **à l'affichage**, sans modifier le fichier. Vérifie d'abord que le fichier est lisible ; sinon, termine avec 2.

**Point de contrôle :** le prénom composé reste entier ; le mode entraînement reste prévisible ; `robot.txt` contient toujours `ROBOT` après la partie.

> [!NOTE] Dossier de lancement
> Pour ce TP, lance le jeu depuis `~/atelier-bash/final-bip-42`. Les chemins `robot.txt` et `scores.csv` sont relatifs à ce dossier.

> [!success]- Afficher la correction — D4
> ```bash
> if [[ ! -f robot.txt || ! -r robot.txt ]]; then
>     echo "Message du robot absent ou illisible" >&2
>     exit 2
> fi
> sed 's/ROBOT/BIP-42/' robot.txt
> ```
>
> `sed` transforme la sortie affichée. Sans option `-i` et sans redirection vers `robot.txt`, le fichier source conserve `ROBOT`.

## Partie E — Le tableau des humains victorieux

**E1.** Ajoute l'enregistrement d'un score **seulement lors d'une victoire**. Si `scores.csv` n'existe pas, crée-le avec l'en-tête `joueur;essais;date`.

> [!success]- Afficher la correction — E1
> ```bash
> if [[ ! -e scores.csv ]]; then
>             if ! echo 'joueur;essais;date' > scores.csv; then
>                 echo "Creation des scores impossible" >&2
>                 exit 1
>             fi
>         fi
>         if [[ ! -f scores.csv || ! -w scores.csv ]]; then
>             echo "Fichier de scores inutilisable" >&2
>             exit 1
>         fi
> ```
>
> Place ce bloc **dans la branche de victoire**, avant l’enregistrement et avant `exit 0`. Il crée l’en-tête une seule fois, puis vérifie que la destination est un fichier utilisable.

**E2.** Ajoute une ligne avec `printf`, le pseudo, le compteur et la date obtenue avec `date +%F`. Exemple :

```text
joueur;essais;date
Mila Vega;3;2026-10-14
Noe;1;2026-10-14
```

La date réelle sera celle du jour. Utilise `>>` pour conserver les victoires précédentes. Si l'écriture échoue, explique le problème et termine avec 1.

> [!success]- Afficher la correction — E2
> ```bash
> jour=$(date +%F)
> if ! printf '%s;%s;%s\n' "$joueur" "$essais" "$jour" >> scores.csv; then
>     echo "Ecriture du score impossible" >&2
>     exit 1
> fi
> ```
>
> `>>` conserve les victoires précédentes. La date réelle dépend du jour. Si l’écriture échoue, le script renvoie 1 même si le secret avait été trouvé.

**E3.** Crée un second script, `statistiques.sh`. Vérifie que `scores.csv` est un fichier lisible, puis utilise `awk -F ';'` pour afficher :

- le nombre de victoires ;
- le plus petit nombre d'essais parmi ces victoires ;
- un message adapté si le fichier n'a encore que l'en-tête.

> Indice : ignore l'en-tête avec `NR > 1`. Incrémente un compteur. Pour le meilleur résultat, garde `$2` quand c'est la première victoire ou quand `$2` est plus petit que le minimum courant.

Les modes normal et entraînement alimentent ici **le même tableau** : c'est un historique pédagogique, pas une compétition équitable. Ne modifie pas le fichier de scores à la main pendant les tests.

> [!success]- Afficher la correction — E3
> ```bash
> #!/usr/bin/env bash
> if [[ ! -f scores.csv || ! -r scores.csv ]]; then
>     echo "Pas encore de scores lisibles. Gagne une partie !" >&2
>     exit 2
> fi
> awk -F ';' '
> NR > 1 {
>     victoires++
>     if (victoires == 1 || $2 < meilleur) {
>         meilleur = $2
>     }
> }
> END {
>     if (victoires == 0) {
>         print "Aucune victoire : BIP-42 garde tout le chocolat."
>     } else {
>         print "Victoires :", victoires
>         print "Meilleur resultat :", meilleur, "essai(s)"
>     }
> }' scores.csv
> ```
>
> Enregistre ce script dans `statistiques.sh`. `NR > 1` ignore l’en-tête. Le minimum est initialisé par la première victoire. Un fichier avec le seul en-tête affiche le message « Aucune victoire ».

## Partie F — Faire passer le contrôle technique à BIP-42

**F1.** Vérifie les deux scripts avec `bash -n`. Joue ces cas en mode entraînement :

| Cas | Résultat attendu |
|---|---|
| `1`, `9`, `6` | Victoire en 3 essais, code 0 |
| `banane`, ligne vide, `10`, `6` | Victoire en 1 essai, code 0 |
| Cinq fois `1` | Défaite, code 1, aucun score ajouté |
| Ctrl+D sur une ligne vide | Saisie interrompue, code 2 |
| Mode `turbo` | Utilisation affichée, code 2 |
| Pseudo `Mila Vega` | Un seul joueur, nom conservé dans les scores |

Lis le code avec `echo "$?"` **immédiatement après** le lancement du script.

> [!success]- Afficher la correction — F1
> ```bash
> bash -n jeu.sh
> bash -n statistiques.sh
> ```
>
> Teste les cas du tableau et lis `$?` immédiatement après chaque lancement. Voici le **`jeu.sh` complet** réunissant les étapes D et E :
>
> ```bash
> #!/usr/bin/env bash
> if [[ "$#" -gt 2 ]]; then
>     echo 'Usage : ./jeu.sh [pseudo] [normal|entrainement]' >&2
>     exit 2
> fi
> joueur="${1:-visiteur}"
> mode="${2:-normal}"
> # ; separe les champs ; les retours a la ligne separeraient les parties.
> if [[ "$joueur" == *';'* || "$joueur" == *$'\n'* || "$joueur" == *$'\r'* ]]; then
>     echo "Pseudo interdit : pas de point-virgule ni de retour a la ligne." >&2
>     exit 2
> fi
> case "$mode" in
>     normal) secret=$((RANDOM % 9 + 1)) ;;
>     entrainement) secret=6 ;;
>     *) echo 'Usage : ./jeu.sh [pseudo] [normal|entrainement]' >&2
>        exit 2 ;;
> esac
> if [[ ! -f robot.txt || ! -r robot.txt ]]; then
>     echo "Message du robot absent ou illisible" >&2
>     exit 2
> fi
> echo "========================================"
> echo " BIP-42 : OPERATION CHOCOLAT"
> echo "========================================"
> sed 's/ROBOT/BIP-42/' robot.txt
> for numero in 3 2 1; do
>     echo "Demarrage : $numero"
> done
> echo "$joueur, trouve mon code entre 1 et 9."
> echo "Tu as 5 essais. Les fautes de frappe ne comptent pas."
> essais=0
> maximum=5
> while [[ "$essais" -lt "$maximum" ]]; do
>     if ! read -p "Essai $((essais + 1))/$maximum - Ton nombre : " proposition; then
>         echo "Saisie interrompue" >&2
>         exit 2
>     fi
>     case "$proposition" in
>         [1-9]) ;;
>         *) echo "Une banane n'est pas un chiffre. Essaie de 1 a 9."
>            continue ;;
>     esac
>     essais=$((essais + 1))
>     if [[ "$proposition" -lt "$secret" ]]; then
>         echo "Trop petit ! Meme mon grille-pain vise plus haut."
>     elif [[ "$proposition" -gt "$secret" ]]; then
>         echo "Trop grand ! Tu cherches un code, pas mon numero de serie."
>     else
>         unite="essais"
>         if [[ "$essais" -eq 1 ]]; then
>             unite="essai"
>         fi
>         echo "BINGO ! Le chocolat est libere en $essais $unite."
>         echo "BIP-42 : Je te laisse gagner. Evidemment."
>         if [[ ! -e scores.csv ]]; then
>             if ! echo 'joueur;essais;date' > scores.csv; then
>                 echo "Creation des scores impossible" >&2
>                 exit 1
>             fi
>         fi
>         if [[ ! -f scores.csv || ! -w scores.csv ]]; then
>             echo "Fichier de scores inutilisable" >&2
>             exit 1
>         fi
>         jour=$(date +%F)
>         if ! printf '%s;%s;%s\n' "$joueur" "$essais" "$jour" >> scores.csv; then
>             echo "Ecriture du score impossible" >&2
>             exit 1
>         fi
>         echo "Score enregistre. BIP-42 prepare ta tasse."
>         exit 0
>     fi
> done
> echo "PERDU ! Le code etait $secret. BIP-42 boit ta tasse."
> exit 1
> ```
>
> En mode entraînement : `1`, `9`, `6` gagne en 3 essais ; `banane`, vide, `10`, `6` gagne en 1 ; cinq fois `1` perd avec 1. Fin d’entrée, mode inconnu ou pseudo interdit donnent 2 et n’ajoutent pas de score.

**F2.** Avec `ls -l`, vérifie tes fichiers. Avec `cat scores.csv`, retrouve les victoires. Lance les statistiques.

> [!success]- Afficher la correction — F2
> ```bash
> ls -l
> cat scores.csv
> bash statistiques.sh
> ```
>
> Chaque victoire occupe une ligne après l’en-tête. Les défaites et les saisies interrompues n’ajoutent rien. Les statistiques dépendent des parties déjà gagnées dans ton atelier.

**F3.** Avant de lancer une partie depuis un sous-shell `( ./jeu.sh Noe entrainement )`, prédis : le fichier de scores sera-t-il conservé après la fin du sous-shell ? Teste !

> [!TIP] Le piège de BIP-42
> Un sous-shell isole ses variables et son dossier courant. Il ne crée pas une copie du disque : les écritures dans un fichier restent présentes après sa fin.

> [!success]- Afficher la correction — F3
> ```bash
> echo '6' | ( bash jeu.sh Noe entrainement )
> cat scores.csv
> bash statistiques.sh
> ```
>
> Le score reste présent après la fin du sous-shell : les variables sont isolées, mais le disque est partagé. Après cette victoire, le meilleur résultat peut descendre à **1 essai**.

## Bonus — BIP-42 devient animateur

Quand le jeu fonctionne, crée `arcade.sh` avec un menu `case` : `1` joue, `2` affiche les statistiques, `3` quitte. Une boucle permet de revenir au menu après une partie. Un choix inconnu doit afficher une remarque, sans fermer le menu.

Tu peux aussi créer une fonction `titre` pour éviter de répéter la bannière. Garde les règles et les scores identiques.

> [!success]- Afficher la correction — Bonus
> ```bash
> #!/usr/bin/env bash
> titre() {
>     echo "=== BIP-42 : LE CHOCOLAT SE MERITE ==="
> }
> while true; do
>     titre
>     echo "1. Jouer | 2. Statistiques | 3. Quitter"
>     if ! read -p 'Ton choix : ' choix; then
>         echo "Saisie interrompue" >&2
>         exit 2
>     fi
>     case "$choix" in
>         1) bash jeu.sh ;;
>         2) bash statistiques.sh ;;
>         3) echo "BIP-42 : Enfin seul avec le chocolat."; break ;;
>         *) echo "Ce bouton n'existe pas. Meme sur un robot." ;;
>     esac
> done
> ```
>
> Enregistre dans `arcade.sh`. Le menu revient après le jeu ou les statistiques. Un choix inconnu n’arrête pas le menu ; `3` quitte avec `break`. Une fin d’entrée renvoie 2. Vérifie avec `bash -n arcade.sh`, puis joue avec `bash arcade.sh`.

## Livraison — Défier un autre équipier

Montre une partie au formateur, puis laisse un camarade jouer en mode normal. Présente `jeu.sh`, `statistiques.sh` et tes scores. Explique où se trouvent une variable, une condition, une boucle, un argument, une redirection, le traitement `sed` et le calcul `awk`.

**Défi final :** en sachant que le code est entre 1 et 9, quelle première proposition évite de chercher trop longtemps ? Testez vos stratégies !

> [!success]- Afficher la correction — Défi final
> Proposer **5** coupe d’abord l’intervalle 1–9 en deux. À chaque réponse, coupe la zone restante : avec cette stratégie, quatre propositions suffisent au maximum. Garde le secret fixe pour comparer les essais avant de jouer en mode normal.

[← Énoncé du TP](https://kayasam.github.io/linux-initiation/bash/annexe/tp-final-bip-42)
