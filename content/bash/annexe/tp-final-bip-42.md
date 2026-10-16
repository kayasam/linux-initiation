---
title: "TP final — BIP-42 a perdu son boulon"
aliases: ["bash/ateliers/tp-final-bip-42"]
---

<nav class="chapter-resources workshop-resources" aria-label="Ressources de l’atelier" data-workshop-key="bash/annexe/tp-final-bip-42"><div class="resource-buttons"><a class="resource-button" href="https://kayasam.github.io/linux-initiation/bash/annexe/tp-final-bip-42" aria-current="page"><span class="resource-icon"><svg class="resource-symbol" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/></svg></span><span class="resource-label">Énoncé</span></a><a class="resource-button" href="https://kayasam.github.io/linux-initiation/bash/annexe/tp-final-bip-42-corrigev2"><span class="resource-icon"><svg class="resource-symbol" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="m5 12 4 4L19 6"/></svg></span><span class="resource-label">Corrigé v2</span></a></div><div class="resource-actions"><a class="resource-download" href="https://kayasam.github.io/linux-initiation/telechargements/bash/tp/tp-final-bip-42.md" download aria-label="Télécharger ce support en Markdown">↓ Télécharger .md</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>

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

**A2.** Crée un fichier `robot.txt` contenant cette ligne :

```text
ROBOT : Qui ose toucher a mon chocolat ?
```

Utilise `echo` et `>`. Lis le fichier avec `cat`.

**A3.** Crée le script `jeu-v1.sh` avec nano. Ajoute le shebang Bash et un titre avec `echo`.

**À chaque version :** enregistre, lance `bash -n nom-du-script.sh`, puis `bash nom-du-script.sh`. Pour lancer directement le fichier avec `./`, ajoute le droit d'exécution avec `chmod +x`.

## Partie B — Un nombre, une réponse

**B1.** Dans `jeu-v1.sh`, définis `secret=6`. Demande une proposition avec `read -p`.

**B2.** Vérifie la saisie **avant le calcul ou la comparaison numérique**. Seul un chiffre de `1` à `9` est accepté. Le motif `[1-9]` dans `case` correspond à exactement un caractère dans cet intervalle : `6` convient, `06`, `10`, une saisie vide ou `banane` ne conviennent pas.

> Indice : un premier cas `[1-9])` accepte la saisie ; le cas `*)` affiche une erreur et termine avec le code 2. Si `read` échoue, affiche « Saisie interrompue » et termine aussi avec 2.

**B3.** Avec `if`, `elif` et `else`, compare la proposition à `secret` :

| Proposition | Réaction |
|---|---|
| Inférieure à 6 | `Trop petit !` |
| Supérieure à 6 | `Trop grand !` |
| Égale à 6 | `BINGO ! Le chocolat est libere.` |

Ajoute une phrase drôle après « Trop petit » et « Trop grand ».

**Point de contrôle :** lance trois fois le script avec `1`, `9` et `6`. Teste aussi `banane`. Pour cette première version, il n'y a qu'une proposition par lancement ; une saisie valide se termine avec 0, même si elle est incorrecte.

## Partie C — Une vraie partie

**C1.** Copie `jeu-v1.sh` vers `jeu-v2.sh`. Le secret reste fixé à 6.

**C2.** Ajoute `essais=0` et `maximum=5`. Place la question et les tests dans une boucle `while` qui continue tant que `essais` est inférieur à `maximum`.

**C3.** Une saisie invalide affiche une remarque puis utilise `continue` : **elle ne consomme aucun essai**. Une saisie valide augmente le compteur avec `$((essais + 1))`.

**C4.** Si le joueur trouve le secret, affiche son nombre d'essais et termine avec 0. Sinon, après cinq propositions valides, annonce la défaite, révèle le secret et termine avec 1.

**Point de contrôle :** `1`, `9`, `banane`, `6` doit donner une victoire en **3 essais**. Cinq fois `1` doit donner une défaite. Une fin de saisie (**Ctrl+D** sur une ligne vide) termine avec 2 et ne relance pas indéfiniment la question.

## Partie D — Personnaliser le robot

**D1.** Copie `jeu-v2.sh` vers `jeu.sh`. Accepte au maximum deux arguments : le prénom ou pseudo, puis le mode.

| Lancement | Comportement |
|---|---|
| `./jeu.sh` | Joueur `visiteur`, mode `normal` |
| `./jeu.sh "Mila Vega" entrainement` | Joueur Mila Vega, secret fixé à 6 |
| `./jeu.sh Noe normal` | Secret aléatoire entre 1 et 9 |

Utilise `${1:-visiteur}` et `${2:-normal}`. Un mode inconnu ou trop d'arguments doit afficher l'utilisation et terminer avec 2. Pour les scores, refuse aussi un pseudo contenant `;` ou un retour à la ligne : une partie occupera une seule ligne du fichier.

**D2.** Choisis le secret avec `case`. En mode normal :

```bash
secret=$((RANDOM % 9 + 1))
```

`RANDOM` fournit un entier pseudo-aléatoire de Bash. `% 9` donne un reste de 0 à 8 ; `+ 1` le ramène entre 1 et 9. Ce hasard suffit pour notre jeu.

**D3.** Affiche ton titre, le nom du joueur et les règles. Avec une boucle `for`, fais afficher un petit démarrage : `3`, `2`, `1`. Pas besoin de pause entre les nombres.

**D4.** Fais parler le robot à partir de `robot.txt`. Utilise `sed` pour remplacer `ROBOT` par `BIP-42` **à l'affichage**, sans modifier le fichier. Vérifie d'abord que le fichier est lisible ; sinon, termine avec 2.

**Point de contrôle :** le prénom composé reste entier ; le mode entraînement reste prévisible ; `robot.txt` contient toujours `ROBOT` après la partie.

> [!NOTE] Dossier de lancement
> Pour ce TP, lance le jeu depuis `~/atelier-bash/final-bip-42`. Les chemins `robot.txt` et `scores.csv` sont relatifs à ce dossier.

## Partie E — Le tableau des humains victorieux

**E1.** Ajoute l'enregistrement d'un score **seulement lors d'une victoire**. Si `scores.csv` n'existe pas, crée-le avec l'en-tête `joueur;essais;date`.

**E2.** Ajoute une ligne avec `printf`, le pseudo, le compteur et la date obtenue avec `date +%F`. Exemple :

```text
joueur;essais;date
Mila Vega;3;2026-10-14
Noe;1;2026-10-14
```

La date réelle sera celle du jour. Utilise `>>` pour conserver les victoires précédentes. Si l'écriture échoue, explique le problème et termine avec 1.

**E3.** Crée un second script, `statistiques.sh`. Vérifie que `scores.csv` est un fichier lisible, puis utilise `awk -F ';'` pour afficher :

- le nombre de victoires ;
- le plus petit nombre d'essais parmi ces victoires ;
- un message adapté si le fichier n'a encore que l'en-tête.

> Indice : ignore l'en-tête avec `NR > 1`. Incrémente un compteur. Pour le meilleur résultat, garde `$2` quand c'est la première victoire ou quand `$2` est plus petit que le minimum courant.

Les modes normal et entraînement alimentent ici **le même tableau** : c'est un historique pédagogique, pas une compétition équitable. Ne modifie pas le fichier de scores à la main pendant les tests.

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

**F2.** Avec `ls -l`, vérifie tes fichiers. Avec `cat scores.csv`, retrouve les victoires. Lance les statistiques.

**F3.** Avant de lancer une partie depuis un sous-shell `( ./jeu.sh Noe entrainement )`, prédis : le fichier de scores sera-t-il conservé après la fin du sous-shell ? Teste !

> [!TIP] Le piège de BIP-42
> Un sous-shell isole ses variables et son dossier courant. Il ne crée pas une copie du disque : les écritures dans un fichier restent présentes après sa fin.

## Bonus — BIP-42 devient animateur

Quand le jeu fonctionne, crée `arcade.sh` avec un menu `case` : `1` joue, `2` affiche les statistiques, `3` quitte. Une boucle permet de revenir au menu après une partie. Un choix inconnu doit afficher une remarque, sans fermer le menu.

Tu peux aussi créer une fonction `titre` pour éviter de répéter la bannière. Garde les règles et les scores identiques.

## Livraison — Défier un autre équipier

Montre une partie au formateur, puis laisse un camarade jouer en mode normal. Présente `jeu.sh`, `statistiques.sh` et tes scores. Explique où se trouvent une variable, une condition, une boucle, un argument, une redirection, le traitement `sed` et le calcul `awk`.

**Défi final :** en sachant que le code est entre 1 et 9, quelle première proposition évite de chercher trop longtemps ? Testez vos stratégies !

[Correction du TP](https://kayasam.github.io/linux-initiation/bash/annexe/tp-final-bip-42-corrigev2)

[← Parcours Bash](https://kayasam.github.io/linux-initiation/#bash)

<a href="https://kayasam.github.io/linux-initiation/telechargements/bash/tp/tp-final-bip-42.md" download>Télécharger le TP en Markdown</a>
