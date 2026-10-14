# Chapitre 04 — Tests et conditions

---

## 1. Les tests

La commande `test` permet d'effectuer des tests logiques dans un script. Elle retourne un **code de retour** :
- `0` → le test est **vrai**
- `1` → le test est **faux**

> [!WARNING]
> En bash, le `0` signifie VRAI et tout autre valeur signifie FAUX — c'est l'inverse de ce qu'on trouve dans la plupart des langages de programmation.
### Les trois syntaxes

```bash
test -d /etc          # syntaxe longue
[ -d /etc ]           # syntaxe courte — équivalente à test
[[ -d /etc ]]         # syntaxe bash étendue — recommandée
```

```bash
[ -d /etc ] ; echo $?    # 0 ← vrai, /etc est bien un dossier
[ -f /etc ] ; echo $?    # 1 ← faux, /etc n'est pas un fichier
```

---

> [!TIP]
> **Bonne pratique** : utiliser `[[ ]]` dans les scripts bash. Réserver `[ ]` pour les scripts POSIX portables (`sh`).
---

## 2. Tests sur les chaînes

```bash
[ -z "$chaine" ]     # vrai si la chaîne est vide (zero)
[ -n "$chaine" ]     # vrai si la chaîne n'est pas vide (non-zero)
[ "$a" = "$b" ]      # vrai si les deux chaînes sont identiques
[ "$a" != "$b" ]     # vrai si les deux chaînes sont différentes
```

> [!DANGER]
> Toujours mettre les variables entre guillemets doubles dans les tests. Sans guillemets, si la variable est vide, bash génère une erreur de syntaxe.
> 
> ```bash
> a=
> [ $a = "test" ]     # ERREUR : bash voit [ = "test" ] → opérateur manquant
> [ "$a" = "test" ]   # CORRECT
> ```
Exemples :

```bash
a=
[ -z "$a" ] ; echo $?    # 0 ← vrai, a est vide

a=Jules
[ -n "$a" ] ; echo $?    # 0 ← vrai, a n'est pas vide
[ "$a" = "Jules" ] ; echo $?   # 0 ← vrai
[ "$a" = "alice" ] ; echo $?   # 1 ← faux
```

---

## 3. Tests sur les valeurs numériques

Pour les comparaisons numériques on utilise des opérateurs dédiés (les `=` et `<` de chaînes ne fonctionnent pas pour les nombres) :

| Opérateur | Signification | Exemple |
|-----------|--------------|---------|
| `-eq` | égal (*equal*) | `[ "$a" -eq "$b" ]` |
| `-ne` | différent (*not equal*) | `[ "$a" -ne "$b" ]` |
| `-lt` | inférieur (*less than*) | `[ "$a" -lt "$b" ]` |
| `-gt` | supérieur (*greater than*) | `[ "$a" -gt "$b" ]` |
| `-le` | inférieur ou égal (*less or equal*) | `[ "$a" -le "$b" ]` |
| `-ge` | supérieur ou égal (*greater or equal*) | `[ "$a" -ge "$b" ]` |

```bash
a=10
b=20

[ "$a" -ne "$b" ] ; echo $?    # 0 ← vrai, 10 ≠ 20
[ "$a" -ge "$b" ] ; echo $?    # 1 ← faux, 10 n'est pas ≥ 20
[ "$a" -lt "$b" ] ; echo $?    # 0 ← vrai, 10 < 20
```

---

## 4. Tests sur les fichiers

| Opérateur | Vrai si… |
|-----------|---------|
| `-e fichier` | le fichier ou dossier **existe** |
| `-f fichier` | c'est un **fichier** ordinaire |
| `-d fichier` | c'est un **dossier** (*directory*) |
| `-r fichier` | le fichier est **lisible** |
| `-w fichier` | le fichier est **modifiable** (*writable*) |
| `-x fichier` | le fichier est **exécutable** |
| `-s fichier` | le fichier est **non vide** (*size > 0*) |
| `-L fichier` | c'est un **lien symbolique** |

```bash
[ -f /etc/hosts ] ; echo $?    # 0 ← c'est bien un fichier
[ -d /etc ]       ; echo $?    # 0 ← c'est bien un dossier
[ -d /etc/hosts ] ; echo $?    # 1 ← /etc/hosts n'est pas un dossier
[ -x /bin/bash ]  ; echo $?    # 0 ← bash est exécutable
[ -s /etc/hosts ] ; echo $?    # 0 ← le fichier n'est pas vide
```

---

## 5. Tests combinés — opérateurs logiques

On peut combiner plusieurs tests avec des opérateurs logiques.

Dans `[[ ]]` (recommandé) :

| Opérateur | Signification |
|-----------|--------------|
| `&&` | ET logique — les deux tests doivent être vrais |
| `\|\|` | OU logique — au moins un test doit être vrai |
| `!` | NON logique — inverse le résultat |

```bash
# Vrai si le dossier existe ET est accessible en écriture
[[ -d "$rep" && -w "$rep" ]] && echo "$rep : dossier, droit en écriture"

# Vrai si le fichier n'existe pas
[[ ! -e "$fichier" ]] && echo "le fichier n'existe pas"
```

Dans `[ ]` (POSIX) on utilise à la place `-a` (ET) et `-o` (OU) :

```bash
[ -d "$rep" -a -w "$rep" ] && echo "$rep : dossier, droit en écriture"
```

---

## 6. La condition if

https://learning.lpi.org/fr/learning-materials/102-500/105/105.2/105.2_01/#:~:text=commande%20interne%20if

La commande `if` exécute des commandes uniquement si une condition est vraie (code retour = 0).

### Syntaxe

```bash
if commande_ou_test ; then
    # commandes si vrai
elif autre_test ; then
    # commandes si le premier était faux mais celui-ci est vrai
else
    # commandes si tout était faux
fi
```

### Exemple — tester l'existence d'un dossier

`verif-dossier.sh` :
```bash
#!/usr/bin/env bash

set -euo pipefail

repertoire="$1"

if [[ -d "$repertoire" ]] ; then
    echo "Le dossier $repertoire existe."
else
    echo "Le dossier $repertoire n'existe pas."
fi
```

```bash
./verif-dossier.sh /etc       # Le dossier /etc existe.
./verif-dossier.sh /inexistant # Le dossier /inexistant n'existe pas.
```

### Exemple — tester le nombre d'arguments

```bash
#!/usr/bin/env bash

set -euo pipefail

if [[ $# -ne 1 ]] ; then
    echo "Usage : $0 <nom>"
    exit 1
fi

echo "Bonjour, $1 !"
```

### Exemple — tester si une commande est disponible

https://unix.stackexchange.com/questions/85249/why-not-use-which-what-to-use-then/85250#85250

```bash
if command -v curl > /dev/null ; then
    echo "curl est installé"
else
    echo "curl n'est pas installé"
fi
```

Voir aussi https://www.it-connect.fr/script-bash-utiliser-conditions-if-else-et-elif/

---

## 7. La structure case

`case` est utilisé pour simplifier les conditions à choix multiples — équivalent d'une série de `if/elif` sur la même variable.

https://ftp.traduc.org/doc-vf/guides/Bash-Beginners-Guide/Bash-Beginners-Guide.html#sect_07_03

### Syntaxe

```bash
case "$variable" in
    motif1)
        commandes
        ;;
    motif2 | motif3)      # plusieurs motifs séparés par |
        commandes
        ;;
    *)                    # cas par défaut (optionnel)
        commandes
        ;;
esac
```

Détails :
- `;;` termine chaque bloc — obligatoire
- `|` sépare les motifs alternatifs pour un même bloc
- `*` correspond à tout ce qui n'a pas été capturé avant (cas par défaut)
- Les motifs peuvent contenir des jokers (`*`, `?`)

### Exemple — format de paquets selon la distribution

```bash
#!/usr/bin/env bash

set -euo pipefail

distro="$1"

case "$distro" in
    debian | ubuntu | mint)
        echo "$distro utilise le format DEB"
        ;;
    centos | fedora | opensuse)
        echo "$distro utilise le format RPM"
        ;;
    *)
        echo "Distribution $distro inconnue"
        ;;
esac
```

### Exemple — menu interactif

```bash
#!/usr/bin/env bash

set -euo pipefail

echo "Que voulez-vous faire ?"
echo "  1) Afficher la date"
echo "  2) Afficher l'espace disque"
echo "  3) Quitter"
read -p "Votre choix : " choix

case "$choix" in
    1)
        date
        ;;
    2)
        df -h /
        ;;
    3)
        echo "Au revoir !"
        exit 0
        ;;
    *)
        echo "Choix invalide : $choix"
        exit 1
        ;;
esac
```

### Insensibilité à la casse avec nocasematch

```bash
shopt -s nocasematch    # active la correspondance insensible à la casse

case "$reponse" in
    oui | o | yes | y)
        echo "Vous avez répondu oui"
        ;;
    non | n | no)
        echo "Vous avez répondu non"
        ;;
esac

shopt -u nocasematch    # désactive
```

---

## 8. Exercices — conditions

**Exercice 1** : écrire un script `verif-fichier.sh` qui prend un chemin en argument et affiche si c'est :
- un fichier ordinaire
- un dossier
- ni l'un ni l'autre (ou inexistant)

> [!TIP]
> **Solution**
> 
> ```bash
> #!/usr/bin/env bash
> 
> set -euo pipefail
> 
> cible="$1"
> 
> if [[ -f "$cible" ]] ; then
>     echo "$cible est un fichier ordinaire"
> elif [[ -d "$cible" ]] ; then
>     echo "$cible est un dossier"
> else
>     echo "$cible n'existe pas ou n'est ni un fichier ni un dossier"
> fi
> ```
**Exercice 2** : écrire un script `comparaison.sh` qui prend deux nombres en argument et affiche si le premier est supérieur, inférieur ou égal au second.

> [!TIP]
> **Solution**
> 
> ```bash
> #!/usr/bin/env bash
> 
> set -euo pipefail
> 
> a="$1"
> b="$2"
> 
> if [[ "$a" -gt "$b" ]] ; then
>     echo "$a est supérieur à $b"
> elif [[ "$a" -lt "$b" ]] ; then
>     echo "$a est inférieur à $b"
> else
>     echo "$a est égal à $b"
> fi
> ```
---

## Récapitulatif des commandes

| Commande / Syntaxe | Description |
|-------------------|-------------|
| `test expression` | Évalue un test (retourne 0 si vrai, 1 si faux) |
| `[ expression ]` | Équivalent à `test` — syntaxe POSIX |
| `[[ expression ]]` | Test bash étendu — recommandé |
| `echo $?` | Affiche le résultat du dernier test |
| `-z "$var"` | Vrai si la variable est vide |
| `-n "$var"` | Vrai si la variable n'est pas vide |
| `"$a" = "$b"` | Vrai si les deux chaînes sont égales |
| `"$a" != "$b"` | Vrai si les deux chaînes sont différentes |
| `-eq`, `-ne` | Égal / différent (numérique) |
| `-lt`, `-gt` | Inférieur / supérieur (numérique) |
| `-le`, `-ge` | Inférieur ou égal / supérieur ou égal (numérique) |
| `-e fichier` | Vrai si le fichier ou dossier existe |
| `-f fichier` | Vrai si c'est un fichier ordinaire |
| `-d fichier` | Vrai si c'est un dossier |
| `-r / -w / -x` | Vrai si lisible / modifiable / exécutable |
| `-s fichier` | Vrai si le fichier est non vide |
| `&&` | ET logique (dans `[[ ]]`) |
| `\|\|` | OU logique (dans `[[ ]]`) |
| `!` | NON logique |
| `if ... ; then ... fi` | Condition simple |
| `if ... ; then ... elif ... ; then ... else ... fi` | Condition avec alternatives |
| `case "$var" in ... esac` | Choix multiples |
| `command -v nom` | Vérifie si une commande est disponible |
| `shopt -s nocasematch` | Active la correspondance insensible à la casse |
| `exit 1` | Quitte le script avec un code d'erreur |

---

> [!NOTE]
> ### À retenir
> 
> - Un test retourne `0` si **vrai**, `1` si **faux** — l'inverse de la plupart des langages.
> - Préférer `[[ ]]` à `[ ]` dans les scripts bash : plus sûr, supporte `&&`, `||` et les motifs.
> - Toujours mettre les variables entre guillemets doubles dans les tests pour éviter les erreurs sur variable vide.
> - Tests chaînes : `-z` (vide), `-n` (non vide), `=` (égal), `!=` (différent).
> - Tests numériques : `-eq`, `-ne`, `-lt`, `-gt`, `-le`, `-ge`.
> - Tests fichiers : `-e` (existe), `-f` (fichier), `-d` (dossier), `-r/-w/-x` (droits), `-s` (non vide).
> - `if ... ; then ... elif ... ; then ... else ... fi` — se termine toujours par `fi`.
> - `case "$var" in motif) ... ;; esac` — plus lisible qu'une série de `if/elif` sur la même variable.
> - `command -v nom` vérifie si une commande est disponible sur le système.
---

> [!TIP]
> **TP associé** → `tp-04-tests-et-conditions.md`
