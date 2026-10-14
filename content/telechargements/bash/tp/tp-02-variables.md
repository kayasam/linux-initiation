# TP 02 — Les variables

> Chapitre associé : `02-variables.md`
> Durée estimée : 45 min

---

## Objectifs

- Créer et lire des variables locales et d'environnement
- Comprendre la différence de portée entre les deux types
- Utiliser la substitution de commande
- Manipuler les variables d'environnement importantes (`PATH`, `PS1`…)

---

## Partie A — Variables locales (10 min)

**A1.** Crée une variable `prenom` contenant ton prénom, et une variable `ville` contenant une ville de ton choix. Affiche-les avec `echo`.

**A2.** Crée une variable `phrase` contenant une phrase avec des espaces. Affiche-la avec et sans guillemets autour de la variable. Observe la différence.

**A3.** Crée une variable `unite` contenant `litre`. Affiche la phrase `"Cette bouteille fait 1 litre(s)"` en utilisant `${unite}` et en ajoutant le `s` directement dans la commande echo.

**A4.** Affiche toutes les variables et fonctions du shell courant. Retrouve dans la liste les variables que tu viens de créer.

**A5.** Supprime la variable `prenom` et vérifie qu'elle n'existe plus.

---

## Partie B — Variables locales vs d'environnement (10 min)

**B1.** Crée une variable locale `secret=local`. Ouvre un sous-shell avec la commande `bash`, essaie d'afficher `$secret`. Que se passe-t-il ? Quitte le sous-shell.

**B2.** Exporte maintenant `secret` en tant que variable d'environnement. Ouvre à nouveau un sous-shell et réessaie d'afficher `$secret`. Quelle différence ?

**B3.** Affiche la liste des variables d'environnement avec `env`, puis avec `printenv`. Retrouve ta variable `secret` dans la liste.

**B4.** Retransforme `secret` en variable locale avec `export -n`. Vérifie dans un nouveau sous-shell qu'elle n'est plus transmise.

---

## Partie C — Variables d'environnement importantes (10 min)

**C1.** Affiche les valeurs des variables suivantes : `HOME`, `USER`, `SHELL`, `LANG`, `PWD`.

**C2.** Génère et affiche trois nombres aléatoires en utilisant `$RANDOM`.

**C3.** Affiche le `PATH` actuel. Compte combien de dossiers il contient (utilise un tube avec `tr` et `wc`).

```bash
echo $PATH | tr ':' '\n' | wc -l
```

**C4.** Ajoute le dossier `/opt/scripts` à la fin de ton `PATH` pour la session courante. Vérifie le résultat.

**C5.** Modifie ton prompt (`PS1`) pour qu'il affiche `[cours-bash] $` à la place du prompt habituel. Recharge ton `.bashrc` pour revenir au prompt d'origine.

---

## Partie D — Substitution de commande (15 min)

**D1.** Stocke le résultat de `uname -o` dans une variable `os` et affiche-la.

**D2.** Stocke la date du jour au format `AAAA-MM-JJ` dans une variable `aujourd_hui` et affiche-la.
> Indice : `date +%Y-%m-%d`

**D3.** Stocke le nombre d'utilisateurs du système dans une variable `nb_users` (utilise `/etc/passwd` et `wc -l`). Affiche une phrase du type : `Il y a X utilisateurs sur ce système`.

**D4.** Stocke le nom du répertoire courant (juste le nom, pas le chemin complet) dans une variable `dossier`. Affiche-le.
> Indice : `basename $(pwd)`

**D5.** (Bonus) Affiche la longueur en caractères de la variable `os` créée en D1.

---

## Questions de vérification

- [ ] Quelle syntaxe permet de créer une variable ? Y a-t-il des espaces autour du `=` ?
- [ ] Quelle est la différence entre `$variable` et `${variable}` ?
- [ ] Comment rendre une variable accessible à un processus enfant (sous-shell) ?
- [ ] Quelle commande supprime une variable ?
- [ ] Quelle syntaxe permet de stocker le résultat d'une commande dans une variable ?
