# TP 05 bis — Les boucles pas à pas

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

**A3.** Refais la même boucle avec **tes propres** éléments : trois outils, trois planètes, ce que tu veux. Vérifie que tu obtiens bien une ligne par élément.

**A4.** Dans la boucle de A2, remplace `echo "Controle : $objet"` par `echo "Controle : objet"` (sans le `$`). Relance. Qu'affiche la boucle, et pourquoi ?

**A5.** Un élément peut contenir un espace, à condition de le protéger :

```bash
for poste in "salle radio" "poste de pilotage" soute; do
    echo "Inspection : $poste"
done
```

Combien de lignes obtiens-tu ? Refais l'essai **sans** les guillemets et compte à nouveau.

---

## Partie B — Compter les passages

**B1.** Une liste peut contenir des nombres :

```bash
for numero in 1 2 3; do
    echo "Capteur $numero teste"
done
```

**B2.** Au-delà de quelques valeurs, utilise une plage :

```bash
for numero in {1..6}; do
    echo "Capteur $numero teste"
done
```

Tu dois obtenir six lignes.

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

**B4.** Déplace la ligne `compteur=0` **après** le `done`, puis relance. Que vaut le total ? Remets ensuite la ligne à sa place.

> [!NOTE] Les trois temps d'un compteur
> On l'initialise **avant** la boucle, on l'augmente **dans** la boucle, on le lit **après**. Oublier l'un des trois est l'erreur la plus fréquente.

---

## Partie C — Boucler sur des fichiers

**C1.** Crée de quoi travailler :

```bash
echo 'Poste ouvert' > accueil.txt
echo 'Canal 7' > journal.txt
echo 'Reserve complete' > reserve.txt
echo 'Image fictive' > photo.png
ls
```

**C2.** Affiche le nom de chaque fichier `.txt` :

```bash
for fichier in *.txt; do
    echo "Trouve : $fichier"
done
```

Trois lignes. `photo.png` n'apparaît pas : le motif `*.txt` ne l'a pas sélectionné.

**C3.** Affiche aussi leur contenu, en ajoutant `cat "$fichier"` dans la boucle, juste après le `echo`.

**C4.** Essaie un motif qui ne correspond à rien :

```bash
for fichier in *.csv; do
    echo "Trouve : $fichier"
done
```

Note ce qui s'affiche. Ce n'est pas un fichier : c'est le motif lui-même, que Bash n'a pas pu remplacer.

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

## Partie D — Ton premier script à boucle

**D1.** Crée `inventaire.sh` dans nano, avec son shebang. Il doit :

1. Initialiser un compteur à 0.
2. Parcourir `*.txt`.
3. Ignorer ce qui n'est pas un fichier ordinaire (test `-f`).
4. Afficher une ligne `Fichier : <nom>` pour chaque fichier retenu.
5. Augmenter le compteur.
6. Après la boucle, afficher `Total : N`.

**D2.** Vérifie la syntaxe avec `bash -n inventaire.sh`, puis rends le script exécutable.

**D3.** Lance-le. Attendu : trois lignes `Fichier :` et `Total : 3`.

**D4.** Crée un quatrième fichier texte (`echo 'Test' > annexe.txt`) et relance **sans modifier le script**. Le total passe à 4 tout seul : c'est tout l'intérêt du motif.

**D5.** Crée un fichier dont le nom contient un espace :

```bash
echo 'Canal 9' > "journal du soir.txt"
./inventaire.sh
```

Si ton script affiche une ligne bizarre ou coupée en deux, c'est qu'il manque des guillemets autour de `"$fichier"`. Corrige-le.

---

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

**E2.** Dans la boucle, retire la ligne `compteur=$((compteur - 1))`, puis relance. La boucle ne s'arrête plus : le test reste vrai pour toujours. **Interromps avec Ctrl+C**, puis remets la ligne.

> [!WARNING] La règle du `while`
> Une des commandes de la boucle doit **faire évoluer le test**. Sans elle, la boucle tourne sans fin.

---

## Bonus — Lire un fichier ligne par ligne

**F1.** Crée la liste de l'équipage :

```bash
printf 'Mila Vega\nNoe\nOrion Base\n' > equipe.txt
cat equipe.txt
```

**F2.** Parcours-la :

```bash
while IFS= read -r personne; do
    echo "Bienvenue $personne"
done < equipe.txt
```

Trois lignes d'accueil. Retiens ce bloc **tel quel** : `IFS= read -r` est la façon correcte de lire un fichier, et `< equipe.txt` fournit le fichier à la boucle.

**F3.** Compte les lignes au passage : ajoute un compteur comme en B3 et affiche `Equipiers : 3` après le `done`.

---

## Mission accomplie si…

- Tu sais écrire une boucle `for` sur une liste, sur une plage et sur un motif de fichiers.
- Ton script `inventaire.sh` affiche le bon total, y compris avec un nom contenant un espace.
- Tu sais expliquer à quoi sert le test `-f` dans une boucle sur des fichiers.
- Tu sais pourquoi une boucle `while` peut tourner sans fin.

> Tu es à l'aise ? Enchaîne avec le [TP 05 — Le robot copieur](https://kayasam.github.io/linux-initiation/bash/05-boucles/tp/tp-05-boucles), qui ajoute la copie de fichiers et la gestion des erreurs.

[← Revenir au cours](https://kayasam.github.io/linux-initiation/bash/05-boucles/)

[Correction du TP](https://kayasam.github.io/linux-initiation/bash/05-boucles/tp/tp-05-boucles-2-corrigev2)
