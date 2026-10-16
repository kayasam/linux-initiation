---
title: "TP 05"
---

# TP 05 bis — Les boucles pas à pas

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="bash/05-boucles" style="--resource-count:4"><div class="resource-buttons"><a class="resource-button resource-markdown" data-resource-kind="markdown" aria-label="Cours — Lire le cours en Markdown" href="https://kayasam.github.io/linux-initiation/bash/05-boucles/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg></span><span class="resource-label">Cours<small>Lire le cours en Markdown</small></span></a><a class="resource-button resource-html" data-resource-kind="html" aria-label="HTML — Explorer le chapitre" href="https://kayasam.github.io/linux-initiation/bash/05-boucles/html/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 28 32"><path d="M2 2h24l-2 25-10 3-10-3Z" fill="#e44d26"/><path d="M14 5v22l7-2 2-20Z" fill="#f16529"/><path d="M7 8h15l-.3 3H11l.3 3h10l-.8 9-6.5 2-6.5-2-.4-5h3l.2 2.6 3.7 1 3.7-1 .3-3.6H8Z" fill="#fff"/></svg></span><span class="resource-label">HTML<small>Explorer le chapitre</small></span></a><a class="resource-button resource-quiz" data-resource-kind="quiz" aria-label="Quiz — 20 questions" href="https://kayasam.github.io/linux-initiation/bash/05-boucles/quiz/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="4" y="3" width="24" height="26" rx="6" fill="#7652ad"/><path d="M12 12a4 4 0 1 1 6 3.5c-1.5.8-2 1.4-2 3" fill="none" stroke="#fff" stroke-width="2.8" stroke-linecap="round"/><circle cx="16" cy="23" r="1.6" fill="#fff"/></svg></span><span class="resource-label">Quiz<small>20 questions</small></span></a><a class="resource-button resource-tp" data-resource-kind="tp" aria-label="TP — Mettre en pratique" href="https://kayasam.github.io/linux-initiation/bash/05-boucles/tp"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg></span><span class="resource-label">TP<small>Mettre en pratique</small></span></a></div><div class="resource-actions"><a class="resource-download" href="https://kayasam.github.io/linux-initiation/telechargements/bash/cours/05-boucles.md" download aria-label="Télécharger le cours en Markdown"><span aria-hidden="true">↓</span> Télécharger .md</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>

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

[← Parcours Bash](https://kayasam.github.io/linux-initiation/#bash)

<a href="https://kayasam.github.io/linux-initiation/telechargements/bash/tp/tp-05-boucles-2.md" download>Télécharger le TP en Markdown</a>
