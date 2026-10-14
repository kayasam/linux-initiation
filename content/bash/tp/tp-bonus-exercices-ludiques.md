---
title: "Bash — TP Bonus — Exercices ludiques"
---

# TP Bonus — Exercices ludiques

> Durée estimée : selon l'inspiration 😄
> Dossier de travail : `~/scripting/fun/`

```bash
mkdir -p ~/scripting/fun
```

---

## Exercice 1 — L'horoscope du terminal 🔮

Écris un script `horoscope.sh` qui demande le signe astrologique de l'utilisateur et affiche un horoscope **totalement inventé** avec `case`.

Le script doit couvrir au moins 4 signes, et un cas par défaut pour les signes inconnus.

Exemple d'exécution :
```
Quel est ton signe astrologique ? bélier
♈ Bélier : Les astres s'alignent pour toi aujourd'hui.
Évite cependant de lancer des rm -rf avant 14h.
```

> Indice : `case` + `read -p` — et sois créatif dans les prédictions !

---

## Exercice 2 — La machine à compliments 🎉

Écris un script `compliment.sh` qui :
1. Demande le prénom de l'utilisateur
2. Affiche un compliment **choisi au hasard** parmi une liste

Pour le hasard, utilise `$RANDOM` et le modulo `%` :

```bash
compliments=("Tu codes comme un dieu" "Ton .bashrc est magnifique" "Même Linus Torvalds serait jaloux")
index=$(( RANDOM % ${#compliments[@]} ))
echo "${compliments[$index]}"
```

**Bonus** : affiche un compliment différent à chaque fois qu'on lance le script.

---

## Exercice 3 — Pierre, feuille, ciseaux ✂️

Écris un script `pfc.sh` qui joue à pierre-feuille-ciseaux contre l'ordinateur.

Le script doit :
1. Demander le choix du joueur (`pierre`, `feuille` ou `ciseaux`)
2. Tirer un choix aléatoire pour l'ordinateur parmi les trois
3. Comparer et annoncer le résultat (`Gagné !`, `Perdu !` ou `Égalité !`)

```bash
options=("pierre" "feuille" "ciseaux")
ordi="${options[$((RANDOM % 3))]}"
```

> Indice : `case` imbriqué ou plusieurs `if` — à toi de choisir.

---

## Exercice 4 — La barre de chargement fictive ⏳

Écris un script `chargement.sh` qui simule une barre de progression en affichant des `#` un par un, avec un petit délai entre chaque.

Résultat attendu :
```
Chargement en cours...
[##########          ] 50%
[####################] 100%
Terminé !
```

> Indice : boucle `for` de 1 à 20, `printf` pour afficher sur la même ligne avec `\r`, `sleep 0.1`.

```bash
printf "\r[%-20s] %d%%" "$barre" "$pourcent"
```

---

## Exercice 5 — Le générateur de mot de passe 🔐

Écris un script `motdepasse.sh` qui :
1. Demande la longueur souhaitée du mot de passe
2. Génère un mot de passe aléatoire de cette longueur

```bash
# Astuce : cette commande génère des caractères aléatoires
tr -dc 'A-Za-z0-9!@#%' < /dev/urandom | head -c "$longueur"
```

**Bonus** : affiche un avertissement si la longueur demandée est inférieure à 8.

---

## Exercice 6 — Le quiz Linux 🧠

Écris un script `quiz.sh` qui pose **3 questions** sur Linux, vérifie les réponses et affiche le score final.

Questions suggérées :
- Quelle commande affiche le répertoire courant ? → `pwd`
- Quel fichier contient la liste des utilisateurs ? → `/etc/passwd`
- Quelle option de `ls` affiche les fichiers cachés ? → `-a`

Le script doit :
- Compter les bonnes réponses
- Afficher le score à la fin (`2/3 — Pas mal !`)
- Être insensible à la casse (`PWD` accepté comme `pwd`)

> Indice : `read -p` + `[[ "${reponse,,}" == "pwd" ]]` (`,, `= tout en minuscules)

---

## Exercice 7 — La devinette améliorée 🎯

Reprends la devinette du TP 05 (deviner un nombre entre 1 et 100) et améliore-la :

- Le nombre secret est **tiré au hasard** : `secret=$(( RANDOM % 100 + 1 ))`
- Compte le **nombre de tentatives**
- Affiche à la fin : `Bravo ! Trouvé en 4 tentatives.`
- Si l'utilisateur tape `abandon`, il peut quitter avec le message `Le nombre était X.`

> [!WARNING]
> Avec `set -e`, utiliser `variable=$(( variable + 1 ))` pour incrémenter un compteur plutôt que `(( variable++ ))` — cette dernière forme peut faire quitter le script quand le compteur vaut 0.
---

## Exercice 8 — Le cowsay maison 🐄

Sans installer `cowsay`, écris un script `vache.sh` qui prend un message en argument et l'affiche avec une vache ASCII :

```
 ___________________
< Linux c'est la vie >
 -------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

> Indice : la longueur du message se récupère avec `${#message}` pour dessiner la bordure dynamiquement.

---

## Pour aller encore plus loin 🚀

- Combine les exercices : un **menu interactif** (avec `case`) qui propose de lancer l'horoscope, le quiz ou la devinette
- Ajoute des **couleurs** dans tes scripts avec les codes ANSI :
  ```bash
  echo -e "\e[32mTexte en vert\e[0m"
  echo -e "\e[31mTexte en rouge\e[0m"
  echo -e "\e[33mTexte en jaune\e[0m"
  ```
- Transforme le quiz en un fichier de questions externe que le script lit ligne par ligne

[← Parcours Bash](https://kayasam.github.io/linux-initiation/#bash)

<a href="https://kayasam.github.io/linux-initiation/telechargements/bash/tp/tp-bonus-exercices-ludiques.md" download>Télécharger le TP en Markdown</a>
