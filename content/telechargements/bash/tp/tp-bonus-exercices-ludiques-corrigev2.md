# TP bonus — Trois jeux dans le terminal — Corrigév2

> Essaie chaque question avant de cliquer sur **Afficher la correction**. Chaque réponse s’ouvre et se referme indépendamment.

## Mission

Tu as terminé le parcours ? Choisis un jeu et construis-le avec les outils déjà vus. Chaque jeu est indépendant. Les données restent dans ton atelier Debian.

```bash
mkdir -p ~/atelier-bash/bonus
cd ~/atelier-bash/bonus
```

## Jeu A — Le compte à rebours

**A1.** Crée `depart.sh` avec son shebang. Une boucle affiche `3`, `2`, `1`, puis `Decollage !`.

> [!success]- Afficher la correction — A1
> ```bash
> #!/usr/bin/env bash
> for nombre in 3 2 1; do
>     echo "$nombre"
> done
> echo 'Decollage !'
> ```
>
> Enregistre dans `depart.sh`. La liste du `for` donne trois passages, puis le message final est affiché après `done`.

**A2.** Vérifie sa syntaxe, puis lance-le. Pour les premiers essais, aucune pause n'est nécessaire.

> [!success]- Afficher la correction — A2
> ```bash
> bash -n depart.sh
> bash depart.sh
> ```
>
> Attendu : `3`, `2`, `1`, puis `Decollage !`. Aucune pause n’est nécessaire pour vérifier la sortie.

**A3.** Bonus : demande à Bash d'attendre une seconde entre deux nombres avec `sleep 1`. Cette commande met en pause le programme ; elle ne change pas le compteur.

> [!success]- Afficher la correction — A3
> ```bash
> for nombre in 3 2 1; do
>     echo "$nombre"
>     sleep 1
> done
> echo 'Decollage !'
> ```
>
> `sleep 1` attend une seconde à chaque passage. Il ne change ni la liste ni la valeur de `nombre`.

## Jeu B — Le quiz de la station

**B1.** Crée `quiz.sh`. Initialise `score=0`.

> [!success]- Afficher la correction — B1
> ```bash
> #!/usr/bin/env bash
> score=0
> ```
>
> Ce début va dans `quiz.sh`. Le score est réinitialisé à chaque lancement.

**B2.** Pose trois questions avec `read -p` :

1. Quel shell utilisons-nous ? Réponse : `Bash` ou `bash`.
2. Quel outil du cours calcule une somme par colonnes ? Réponse : `awk`.
3. Quel code indique généralement la réussite d'une commande ? Réponse : `0`.

> [!success]- Afficher la correction — B2
> ```bash
> if ! read -p 'Quel shell utilisons-nous ? ' reponse; then
>     echo 'Saisie interrompue' >&2
>     exit 2
> fi
> ```
>
> Pose les trois questions l’une après l’autre. La même variable peut être réutilisée : traite sa réponse avant de poser la question suivante.

**B3.** Utilise `case` ou `if` pour ajouter un point par bonne réponse. Affiche `Score : N/3`.

> [!success]- Afficher la correction — B3
> ```bash
> #!/usr/bin/env bash
> score=0
> if ! read -p 'Quel shell utilisons-nous ? ' reponse; then
>     echo 'Saisie interrompue' >&2
>     exit 2
> fi
> case "$reponse" in
>     Bash|bash) score=$((score + 1)) ;;
> esac
> if ! read -p 'Quel outil calcule par colonnes ? ' reponse; then
>     echo 'Saisie interrompue' >&2
>     exit 2
> fi
> if [[ "$reponse" == "awk" ]]; then
>     score=$((score + 1))
> fi
> if ! read -p 'Code de reussite ? ' reponse; then
>     echo 'Saisie interrompue' >&2
>     exit 2
> fi
> if [[ "$reponse" == "0" ]]; then
>     score=$((score + 1))
> fi
> echo "Score : $score/3"
> ```
>
> Voici `quiz.sh` complet. `case` accepte `Bash` ou `bash` pour la première réponse ; les deux autres comparaisons attendent `awk` et `0`. Le score augmente une seule fois par bonne réponse.

**B4.** Si la saisie est interrompue par une fin d'entrée (**Ctrl+D** sur une ligne vide), affiche `Saisie interrompue` et termine avec le code 2. Indice : `if ! read ...; then ... fi`.

> [!success]- Afficher la correction — B4
> Chaque `read` est placé dans `if ! read ...; then ... fi`. Si la fin d’entrée interrompt la saisie, le programme affiche **`Saisie interrompue`** sur la sortie d’erreur et termine avec **2**, sans continuer les questions.

**B5.** Teste trois bonnes réponses, puis trois mauvaises. Un score de 0 n'est pas une panne du programme : le quiz s'est bien déroulé et peut se terminer avec le code 0.

> [!success]- Afficher la correction — B5
> ```bash
> printf 'Bash\nawk\n0\n' | bash quiz.sh
> echo "Code : $?"
> printf 'faux\nfaux\nfaux\n' | bash quiz.sh
> echo "Code : $?"
> ```
>
> Les résultats sont **3/3**, puis **0/3**. Dans les deux cas, le quiz a été mené à son terme et le code vaut 0. Les tubes servent ici à reproduire les essais ; tu peux aussi répondre dans le terminal.

## Jeu C — Le trésor caché

**C1.** Crée `tresor.sh`. Pour pouvoir vérifier tes essais, fixe d'abord `secret=7` et `essais=0`.

> [!success]- Afficher la correction — C1
> ```bash
> #!/usr/bin/env bash
> secret=7
> essais=0
> ```
>
> Ce début va dans `tresor.sh`. La valeur fixe permet des tests reproductibles.

**C2.** Tant que le nombre d'essais valides est inférieur à 3, demande un chiffre de 0 à 9.

> [!success]- Afficher la correction — C2
> Place la lecture protégée dans `while [[ "$essais" -lt 3 ]]; do ... done`. On compte les **chiffres valides**, pas tous les tours de boucle. La version complète est donnée en C5.

**C3.** Vérifie la saisie avec `case` : le motif `[0-9]` accepte exactement un chiffre. Une autre saisie affiche un message puis passe au tour suivant avec `continue`, sans compter d'essai.

> [!success]- Afficher la correction — C3
> ```bash
> case "$choix" in
>     [0-9]) ;;
>     *) echo 'Saisis un seul chiffre'; continue ;;
> esac
> ```
>
> Ce bloc se place dans la boucle, après le `read` protégé et avant l’incrémentation. `chat`, le vide et `10` n’ajoutent aucun essai.

**C4.** Compte chaque chiffre valide. S'il égale le secret, affiche `Tresor trouve` et termine avec 0. Sinon, indique `Plus grand` ou `Plus petit`.

> [!success]- Afficher la correction — C4
> ```bash
> essais=$((essais + 1))
> if [[ "$choix" -eq "$secret" ]]; then
>     echo 'Tresor trouve'
>     exit 0
> elif [[ "$choix" -lt "$secret" ]]; then
>     echo 'Plus grand'
> else
>     echo 'Plus petit'
> fi
> ```
>
> La validation C3 précède ces comparaisons numériques. Un chiffre correct termine immédiatement le jeu avec 0.

**C5.** Après trois essais valides ratés, affiche le secret et termine avec 1. Une fin d'entrée doit terminer avec 2.

> [!success]- Afficher la correction — C5
> ```bash
> #!/usr/bin/env bash
> secret=7
> essais=0
> while [[ "$essais" -lt 3 ]]; do
>     if ! read -p 'Un chiffre de 0 a 9 : ' choix; then
>         echo 'Saisie interrompue' >&2
>         exit 2
>     fi
>     case "$choix" in
>         [0-9]) ;;
>         *) echo 'Saisis un seul chiffre'; continue ;;
>     esac
>     essais=$((essais + 1))
>     if [[ "$choix" -eq "$secret" ]]; then
>         echo 'Tresor trouve'
>         exit 0
>     elif [[ "$choix" -lt "$secret" ]]; then
>         echo 'Plus grand'
>     else
>         echo 'Plus petit'
>     fi
> done
> echo "Perdu : le secret etait $secret"
> exit 1
> ```
>
> Voici `tresor.sh` complet. La défaite se trouve **après `done`** : elle n’est atteinte qu’après trois chiffres valides ratés. Une fin de saisie est traitée à l’intérieur de la boucle et renvoie 2.

**C6.** Teste : réussite immédiate avec `7` ; réussite après `4` puis `7` ; défaite avec `1`, `2`, `3` ; saisie invalide `chat` suivie de `7`.

> [!success]- Afficher la correction — C6
> ```bash
> printf '7\n' | bash tresor.sh
> printf '4\n7\n' | bash tresor.sh
> printf '1\n2\n3\n' | bash tresor.sh
> printf 'chat\n7\n' | bash tresor.sh
> ```
>
> Résultats : victoire immédiate ; indice « Plus grand » puis victoire ; défaite avec code 1 ; remarque sur la saisie puis victoire. Pour lire un code, lance `echo "$?"` immédiatement après le test concerné.

**Défi supplémentaire :** une fois les tests réussis, remplace la valeur fixe par `$((RANDOM % 10))`. Bash fournit `RANDOM`, un entier pseudo-aléatoire ; le reste de la division par 10 fournit ici une valeur de 0 à 9. Garde la version fixe pour reproduire tes essais.

> [!success]- Afficher la correction — Défi supplémentaire
> ```bash
> secret=$((RANDOM % 10))
> ```
>
> Remplace seulement `secret=7` une fois les tests fixes réussis. Le reste de la division par 10 donne une valeur de **0 à 9** ; garde une copie de la version fixe pour reproduire les essais.

## Livraison

Montre ton jeu à un camarade. Il doit pouvoir comprendre les questions, essayer une mauvaise réponse et quitter proprement. Explique les cas testés, pas seulement la réussite.

[← Énoncé du TP](https://kayasam.github.io/linux-initiation/bash/annexe/tp-bonus-exercices-ludiques)
