# TP 04 — Tests et conditions

> Chapitre associé : `04-tests-et-conditions.md`
> Durée estimée : 1h

---

## Objectifs

- Écrire des tests sur des fichiers, des chaînes et des nombres
- Utiliser `if/elif/else` dans un script
- Utiliser `case` pour gérer des choix multiples
- Combiner les acquis des chapitres précédents (arguments, variables, code retour)

---

## Partie A — Tests en ligne de commande (10 min)

Sans écrire de script, exécute les tests suivants directement dans le terminal et observe le code de retour avec `echo $?`.

**A1.** Teste si `/etc` est un dossier.

**A2.** Teste si `/etc/hosts` est un fichier ordinaire.

**A3.** Teste si `/etc/hosts` est non vide.

**A4.** Teste si tu as le droit d'écriture sur `/etc/hosts`.

**A5.** Teste si la chaîne `"bonjour"` est égale à `"Bonjour"`. Puis teste si elles sont différentes.

**A6.** Crée une variable `age=25`. Teste si elle est supérieure à 18, puis si elle est inférieure à 30.

---

## Partie B — if/elif/else (20 min)

**B1.** Écris un script `verif-argument.sh` qui :
- Vérifie qu'il reçoit exactement 1 argument
- Si non, affiche le message d'usage et quitte avec le code 1
- Si oui, affiche `Argument reçu : <valeur>`

**B2.** Écris un script `verif-fichier.sh` qui prend un chemin en argument et affiche :
- `<chemin> est un fichier` si c'est un fichier ordinaire
- `<chemin> est un dossier` si c'est un répertoire
- `<chemin> n'existe pas` sinon

**B3.** Écris un script `age.sh` qui prend un âge en argument et affiche :
- `Mineur` si l'âge est strictement inférieur à 18
- `Majeur` si l'âge est entre 18 et 64 (inclus)
- `Senior` si l'âge est supérieur ou égal à 65

**B4.** Améliore `verif-fichier.sh` pour qu'il affiche aussi si le fichier est lisible et exécutable.

---

## Partie C — case (20 min)

**C1.** Écris un script `extension.sh` qui prend un nom de fichier en argument et affiche son type selon son extension :
- `.sh` → Script bash
- `.txt` → Fichier texte
- `.log` → Fichier journal
- `.conf` ou `.cfg` → Fichier de configuration
- Autre → Extension inconnue

> Indice : utilise `case "$1" in` avec des motifs comme `*.sh)`

**C2.** Écris un script `menu.sh` qui affiche un menu avec 3 options et exécute l'action correspondante :
- `1` → afficher la date et l'heure
- `2` → afficher l'espace disque sur `/`
- `3` → afficher les 5 dernières lignes de `/var/log/syslog`
- Autre → afficher `Option invalide` et quitter avec le code 1

---

## Bonus

**B+1.** Modifie `menu.sh` pour qu'il accepte aussi les réponses en lettres : `d` pour date, `e` pour espace disque, `l` pour logs.

**B+2.** Écris un script `verif-commande.sh` qui prend un nom de commande en argument et affiche si elle est installée sur le système ou non.
> Indice : `command -v nom > /dev/null`

---

## Questions de vérification

- [ ] Quelle est la différence entre `[ ]` et `[[ ]]` ?
- [ ] Pourquoi faut-il mettre les variables entre guillemets dans un test ?
- [ ] Quelle valeur retourne un test vrai ? Un test faux ?
- [ ] Quel opérateur compare deux nombres pour savoir si le premier est supérieur ?
- [ ] Comment tester si un fichier existe et est non vide en une seule ligne ?
- [ ] Quel mot-clé termine un bloc `if` ? Un bloc `case` ?
