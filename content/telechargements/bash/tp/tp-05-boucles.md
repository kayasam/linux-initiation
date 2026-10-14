# TP 05 — Les boucles

> Chapitre associé : `05-boucles.md`
> Durée estimée : 1h

---

## Objectifs

- Utiliser `for` pour itérer sur une liste, une plage, des fichiers
- Utiliser `while` avec un compteur et pour lire un fichier
- Combiner boucles, tests et variables dans un script complet
- Utiliser `break` et `continue`

---

## Partie A — Boucle for (20 min)

**A1.** Écris une boucle `for` qui affiche les jours de la semaine (du lundi au vendredi), un par ligne.

**A2.** Écris une boucle `for` qui affiche les nombres de 1 à 10.

**A3.** Écris une boucle `for` qui affiche uniquement les nombres pairs entre 2 et 20.
> Indice : utiliser `{2..20..2}`

**A4.** Écris un script `creer-fichiers.sh` qui prend un dossier en argument et crée à l'intérieur 5 fichiers nommés `fichier1.txt` à `fichier5.txt`. Le script doit vérifier que le dossier existe avant de commencer.

**A5.** Écris un script qui affiche pour chaque fichier `.sh` dans `~/scripting` :
- Son nom
- S'il est exécutable ou non

---

## Partie B — Arithmétique et while (20 min)

**B1.** Écris un script `decollage.sh` qui compte à rebours de 10 à 1 avec une seconde d'attente entre chaque nombre, puis affiche `Décollage !`.

**B2.** Écris un script `somme.sh` qui calcule et affiche la somme des nombres de 1 à 100 en utilisant une boucle `while`.

**B3.** Écris un script qui affiche la table de multiplication du nombre passé en argument (de 1 à 10).
Exemple pour `./table.sh 7` :
```
7 x 1 = 7
7 x 2 = 14
...
7 x 10 = 70
```

**B4.** Écris un script qui demande à l'utilisateur de deviner un nombre entre 1 et 10 (fixé à l'avance dans une variable). La boucle continue jusqu'à ce qu'il trouve la bonne réponse. Afficher si la tentative est trop haute, trop basse ou correcte.

---

## Partie C — Lire des fichiers et break/continue (20 min)

**C1.** Écris un script qui lit `/etc/passwd` ligne par ligne et affiche uniquement le nom d'utilisateur (premier champ, séparateur `:`) pour chaque ligne.

**C2.** Améliore le script précédent pour n'afficher que les utilisateurs dont le shell est `/bin/bash`.

**C3.** Écris un script qui affiche les nombres de 1 à 20 mais :
- Saute (ignore) les multiples de 3 avec `continue`
- S'arrête complètement si le nombre est supérieur à 15 avec `break`

**C4.** Écris un script `chercher.sh` qui parcourt tous les fichiers `.log` dans `/var/log` et affiche ceux qui contiennent le mot `error` (insensible à la casse).

---

## Questions de vérification

- [ ] Quelle syntaxe permet d'itérer sur une plage de nombres avec un pas de 2 ?
- [ ] Quelle est la différence entre `while` et `until` ?
- [ ] Comment lire un fichier ligne par ligne en bash ?
- [ ] Que fait `break` dans une boucle ? Et `continue` ?
- [ ] Comment calculer `5 * 3` en bash ?
- [ ] Pourquoi faut-il utiliser `read -r` et pas juste `read` pour lire un fichier ?

[← Revenir au cours](https://kayasam.github.io/linux-initiation/bash/05-boucles/)
