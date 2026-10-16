# TP 05 bis — Les boucles pas à pas — Corrigév2

> Essaie chaque question avant de cliquer sur **Afficher la correction**. Chaque réponse s’ouvre et se referme indépendamment.

> Chapitre associé : [05 — Les boucles](https://kayasam.github.io/linux-initiation/bash/05-boucles/)

## Mission

Tu équipes la station Orion d'un inventaire automatique. On avance **une notion à la fois** : d'abord des boucles tapées directement dans le terminal, ensuite un petit script.

> [!TIP] Comment travailler ce TP
> Chaque étape tient en quelques lignes et affiche un résultat attendu. **Compare ta sortie avec celle indiquée avant de passer à la suite.** Si elle diffère, relis ta frappe : c'est presque toujours une faute de ponctuation (`;`, `do`, `done`).

---

## Partie A — Boucler sur une liste

Tu travailles directement dans le terminal, sans créer de fichier.

**A1.** Prépare ton atelier :

```bash
mkdir -p ~/atelier-bash/05bis
cd ~/atelier-bash/05bis
```

> [!success]- Afficher la correction — A1
> ```bash
> mkdir -p ~/atelier-bash/05bis
> cd ~/atelier-bash/05bis
> ```
>
> `~` est ton dossier personnel ; `-p` crée les parents manquants et accepte un dossier déjà présent.

**A2.** Tape cette boucle. Les trois lignes se tapent l'une après l'autre : tant que la boucle n'est pas fermée par `done`, le shell affiche une invite `>` et attend la suite.

```bash
for objet in radio casque batterie; do
    echo "Controle : $objet"
done
```

Résultat attendu :

```text
Controle : radio
Controle : casque
Controle : batterie
```

> [!success]- Afficher la correction — A2
> ```bash
> for objet in radio casque batterie; do
>     echo "Controle : $objet"
> done
> ```
>
> Trois passages : `Controle : radio`, `Controle : casque`, puis `Controle : batterie`. Chaque élément de la liste devient la valeur de `objet`. Les éléments sont séparés par des espaces, pas des virgules.

**A3.** Refais la même boucle avec **tes propres** éléments : trois outils, trois planètes, ce que tu veux. Vérifie que tu obtiens bien une ligne par élément.

> [!success]- Afficher la correction — A3
> ```bash
> for outil in tournevis pince marteau; do
>     echo "Outil : $outil"
> done
> ```
>
> C’est un exemple : tes propres éléments conviennent aussi. Vérifie une ligne par élément.

**A4.** Dans la boucle de A2, remplace `echo "Controle : $objet"` par `echo "Controle : objet"` (sans le `$`). Relance. Qu'affiche la boucle, et pourquoi ?

> [!success]- Afficher la correction — A4
> La boucle affiche **trois fois** `Controle : objet`. Sans `$`, `objet` est du texte littéral : sa valeur n’est pas remplacée. La boucle effectue toujours trois passages, car sa liste contient trois éléments.

**A5.** Un élément peut contenir un espace, à condition de le protéger :

```bash
for poste in "salle radio" "poste de pilotage" soute; do
    echo "Inspection : $poste"
done
```

Combien de lignes obtiens-tu ? Refais l'essai **sans** les guillemets et compte à nouveau.

---

> [!success]- Afficher la correction — A5
> Avec les guillemets : **3 lignes**, pour `salle radio`, `poste de pilotage` et `soute`. Sans eux : **6 lignes**, pour `salle`, `radio`, `poste`, `de`, `pilotage` et `soute`. Les guillemets regroupent les mots en un seul élément.

## Partie B — Compter les passages

**B1.** Une liste peut contenir des nombres :

```bash
for numero in 1 2 3; do
    echo "Capteur $numero teste"
done
```

> [!success]- Afficher la correction — B1
> ```bash
> for numero in 1 2 3; do
>     echo "Capteur $numero teste"
> done
> ```
>
> Trois lignes, numérotées 1, 2 et 3.

**B2.** Au-delà de quelques valeurs, utilise une plage :

```bash
for numero in {1..6}; do
    echo "Capteur $numero teste"
done
```

Tu dois obtenir six lignes.

> [!success]- Afficher la correction — B2
> ```bash
> for numero in {1..6}; do
>     echo "Capteur $numero teste"
> done
> ```
>
> Six lignes. Bash développe `{1..6}` avant d’exécuter la boucle. Avec une borne variable, `{1..$max}` ne fonctionne pas de cette façon : utilise une boucle `while`.

**B3.** Un compteur est une variable qu'on augmente à chaque tour. Recopie ce bloc :

```bash
compteur=0
for objet in radio casque batterie; do
    compteur=$((compteur + 1))
    echo "$compteur : $objet"
done
echo "Total : $compteur"
```

Résultat attendu :

```text
1 : radio
2 : casque
3 : batterie
Total : 3
```

> [!success]- Afficher la correction — B3
> ```bash
> compteur=0
> for objet in radio casque batterie; do
>     compteur=$((compteur + 1))
>     echo "$compteur : $objet"
> done
> echo "Total : $compteur"
> ```
>
> Attendu : `1 : radio`, `2 : casque`, `3 : batterie`, puis `Total : 3`. Initialisation avant la boucle, augmentation dans la boucle, lecture après.

**B4.** Déplace la ligne `compteur=0` **après** le `done`, puis relance. Que vaut le total ? Remets ensuite la ligne à sa place.

> [!NOTE] Les trois temps d'un compteur
> On l'initialise **avant** la boucle, on l'augmente **dans** la boucle, on le lit **après**. Oublier l'un des trois est l'erreur la plus fréquente.

---

> [!success]- Afficher la correction — B4
> Le total affiché devient **0** : l’affectation placée après `done` remet le compteur à zéro juste avant son affichage. Replace `compteur=0` **avant** la boucle. Une remise à zéro à chaque tour empêcherait également de cumuler les passages.

## Partie C — Boucler sur des fichiers

**C1.** Crée de quoi travailler :

```bash
echo 'Poste ouvert' > accueil.txt
echo 'Canal 7' > journal.txt
echo 'Reserve complete' > reserve.txt
echo 'Image fictive' > photo.png
ls
```

> [!success]- Afficher la correction — C1
> ```bash
> echo 'Poste ouvert' > accueil.txt
> echo 'Canal 7' > journal.txt
> echo 'Reserve complete' > reserve.txt
> echo 'Image fictive' > photo.png
> ls
> ```
>
> Dans cet atelier neuf, tu retrouves trois fichiers `.txt` et un fichier `.png`.

**C2.** Affiche le nom de chaque fichier `.txt` :

```bash
for fichier in *.txt; do
    echo "Trouve : $fichier"
done
```

Trois lignes. `photo.png` n'apparaît pas : le motif `*.txt` ne l'a pas sélectionné.

> [!success]- Afficher la correction — C2
> ```bash
> for fichier in *.txt; do
>     echo "Trouve : $fichier"
> done
> ```
>
> La boucle affiche `accueil.txt`, `journal.txt` et `reserve.txt`. Bash remplace le motif par les noms correspondants avant les passages ; `photo.png` n’est pas sélectionné.

**C3.** Affiche aussi leur contenu, en ajoutant `cat "$fichier"` dans la boucle, juste après le `echo`.

> [!success]- Afficher la correction — C3
> ```bash
> for fichier in *.txt; do
>     echo "Trouve : $fichier"
>     cat "$fichier"
> done
> ```
>
> Après chaque nom, `cat` affiche le contenu du fichier. Les guillemets autour de la variable protègent les noms composés.

**C4.** Essaie un motif qui ne correspond à rien :

```bash
for fichier in *.csv; do
    echo "Trouve : $fichier"
done
```

Note ce qui s'affiche. Ce n'est pas un fichier : c'est le motif lui-même, que Bash n'a pas pu remplacer.

> [!success]- Afficher la correction — C4
> Avec les réglages habituels de Bash et aucun fichier CSV, le résultat est **`Trouve : *.csv`**, une seule fois. Le motif n’a pas été remplacé : la variable contient littéralement `*.csv`.

**C5.** Protège-toi de ce cas avec un test `-f`, vu au chapitre 04 :

```bash
for fichier in *.csv; do
    if [[ -f "$fichier" ]]; then
        echo "Trouve : $fichier"
    fi
done
```

Cette fois, aucune ligne. Relance la même boucle avec `*.txt` : les trois lignes reviennent.

---

> [!success]- Afficher la correction — C5
> ```bash
> for fichier in *.csv; do
>     if [[ -f "$fichier" ]]; then
>         echo "Trouve : $fichier"
>     fi
> done
> ```
>
> Aucune ligne : le texte `*.csv` ne désigne pas un fichier ordinaire existant. Avec `*.txt`, les trois fichiers sont affichés. Le test écarte aussi les dossiers dont le nom finit par `.txt`.

## Partie D — Ton premier script à boucle

**D1.** Crée `inventaire.sh` dans nano, avec son shebang. Il doit :

1. Initialiser un compteur à 0.
2. Parcourir `*.txt`.
3. Ignorer ce qui n'est pas un fichier ordinaire (test `-f`).
4. Afficher une ligne `Fichier : <nom>` pour chaque fichier retenu.
5. Augmenter le compteur.
6. Après la boucle, afficher `Total : N`.

> [!success]- Afficher la correction — D1
> ```bash
> #!/usr/bin/env bash
>
> compteur=0
> for fichier in *.txt; do
>     if [[ ! -f "$fichier" ]]; then
>         continue
>     fi
>     echo "Fichier : $fichier"
>     compteur=$((compteur + 1))
> done
> echo "Total : $compteur"
> ```
>
> Enregistre ce contenu dans `inventaire.sh`. Seuls les fichiers ordinaires sont affichés et comptés. Une variante qui place le traitement dans `if [[ -f "$fichier" ]]` convient aussi.

**D2.** Vérifie la syntaxe avec `bash -n inventaire.sh`, puis rends le script exécutable.

> [!success]- Afficher la correction — D2
> ```bash
> bash -n inventaire.sh
> chmod +x inventaire.sh
> ```
>
> `bash -n` vérifie la syntaxe sans exécuter ; `chmod +x` permet le lancement direct.

**D3.** Lance-le. Attendu : trois lignes `Fichier :` et `Total : 3`.

> [!success]- Afficher la correction — D3
> ```bash
> ./inventaire.sh
> ```
>
> Attendu : les trois lignes `Fichier : accueil.txt`, `Fichier : journal.txt` et `Fichier : reserve.txt`, puis **`Total : 3`**.

**D4.** Crée un quatrième fichier texte (`echo 'Test' > annexe.txt`) et relance **sans modifier le script**. Le total passe à 4 tout seul : c'est tout l'intérêt du motif.

> [!success]- Afficher la correction — D4
> ```bash
> echo 'Test' > annexe.txt
> ./inventaire.sh
> ```
>
> Le total passe à **4**. Le motif retrouve les fichiers présents à chaque lancement : il n’est pas nécessaire de modifier le script.

**D5.** Crée un fichier dont le nom contient un espace :

```bash
echo 'Canal 9' > "journal du soir.txt"
./inventaire.sh
```

Si ton script affiche une ligne bizarre ou coupée en deux, c'est qu'il manque des guillemets autour de `"$fichier"`. Corrige-le.

---

> [!success]- Afficher la correction — D5
> ```bash
> echo 'Canal 9' > "journal du soir.txt"
> ./inventaire.sh
> ```
>
> Le nom `journal du soir.txt` apparaît en entier et le total vaut **5**. Garde `"$fichier"` entre guillemets dans les commandes. Précision : dans `[[ ... ]]`, Bash ne découpe pas une variable en arguments ; ce test ne rejette donc pas automatiquement un nom composé si l’on retire ses guillemets. Les guillemets restent une bonne habitude, particulièrement pour `cat` ou `cp`.

## Partie E — Une boucle while

`for` parcourt une liste connue d'avance. `while` répète **tant qu'un test réussit**.

**E1.** Tape ce décompte :

```bash
compteur=3
while [[ "$compteur" -gt 0 ]]; do
    echo "Depart dans $compteur"
    compteur=$((compteur - 1))
done
echo 'Decollage'
```

> [!success]- Afficher la correction — E1
> ```bash
> compteur=3
> while [[ "$compteur" -gt 0 ]]; do
>     echo "Depart dans $compteur"
>     compteur=$((compteur - 1))
> done
> echo 'Decollage'
> ```
>
> La sortie indique `Depart dans 3`, `Depart dans 2`, `Depart dans 1`, puis `Decollage`. La décrémentation finit par rendre le test faux.

**E2.** Dans la boucle, retire la ligne `compteur=$((compteur - 1))`, puis relance. La boucle ne s'arrête plus : le test reste vrai pour toujours. **Interromps avec Ctrl+C**, puis remets la ligne.

> [!WARNING] La règle du `while`
> Une des commandes de la boucle doit **faire évoluer le test**. Sans elle, la boucle tourne sans fin.

---

> [!success]- Afficher la correction — E2
> Sans la décrémentation, `compteur` reste à **3** et la boucle affiche `Depart dans 3` sans fin. **Ctrl+C** interrompt la commande en cours. Remets ensuite la décrémentation pour que le test évolue.

## Bonus — Lire un fichier ligne par ligne

**F1.** Crée la liste de l'équipage :

```bash
printf 'Mila Vega\nNoe\nOrion Base\n' > equipe.txt
cat equipe.txt
```

> [!success]- Afficher la correction — F1
> ```bash
> printf 'Mila Vega\nNoe\nOrion Base\n' > equipe.txt
> cat equipe.txt
> ```
>
> Le fichier contient trois lignes, chacune terminée par un retour à la ligne.

**F2.** Parcours-la :

```bash
while IFS= read -r personne; do
    echo "Bienvenue $personne"
done < equipe.txt
```

Trois lignes d'accueil. Retiens ce bloc **tel quel** : `IFS= read -r` est la façon correcte de lire un fichier, et `< equipe.txt` fournit le fichier à la boucle.

> [!success]- Afficher la correction — F2
> ```bash
> while IFS= read -r personne; do
>     echo "Bienvenue $personne"
> done < equipe.txt
> ```
>
> Trois lignes d’accueil : `Mila Vega`, `Noe`, `Orion Base`. `IFS=` conserve les espaces de début et de fin ; `-r` conserve les antislashs. `< equipe.txt` fournit le fichier à `read`.

**F3.** Compte les lignes au passage : ajoute un compteur comme en B3 et affiche `Equipiers : 3` après le `done`.

---

> [!success]- Afficher la correction — F3
> ```bash
> compteur=0
> while IFS= read -r personne; do
>     echo "Bienvenue $personne"
>     compteur=$((compteur + 1))
> done < equipe.txt
> echo "Equipiers : $compteur"
> ```
>
> Après les trois accueils, le résultat est **`Equipiers : 3`**. La redirection après `done` alimente la boucle entière ; le compteur reste disponible après celle-ci.

## Mission accomplie si…

- Tu sais écrire une boucle `for` sur une liste, sur une plage et sur un motif de fichiers.
- Ton script `inventaire.sh` affiche le bon total, y compris avec un nom contenant un espace.
- Tu sais expliquer à quoi sert le test `-f` dans une boucle sur des fichiers.
- Tu sais pourquoi une boucle `while` peut tourner sans fin.

> Tu es à l'aise ? Enchaîne avec le [TP 05 — Le robot copieur](https://kayasam.github.io/linux-initiation/bash/05-boucles/tp/tp-05-boucles), qui ajoute la copie de fichiers et la gestion des erreurs.

[← Énoncé du TP](https://kayasam.github.io/linux-initiation/bash/05-boucles/tp/tp-05-boucles-2)
