# Chapitre 02 — Les variables

---

## 1. Qu'est-ce qu'une variable ?

**Une variable représente l'enregistrement d'une valeur** : une chaîne de caractères sert de clé (le nom), à laquelle est associé un contenu.

```
nom_variable = valeur
```

C'est le mécanisme de base pour stocker et réutiliser une information dans un script ou dans le shell.

---

## 2. Types de variables : locale vs d'environnement

Il existe deux types de variables :

| Type | Aussi appelée | Portée |
|------|--------------|--------|
| **Variable locale** | Variable du shell | Existe uniquement dans le shell courant — non transmise aux processus enfants |
| **Variable d'environnement** | Variable globale | Transmise au shell courant **et** à tous les processus enfants |

On commence par voir comment créer et utiliser une variable, avant de revenir sur la distinction locale/environnement.

---

## 3. Affectation et référencement

### Créer une variable (affectation)

L'affectation se fait avec le signe `=`, **sans espace avant ni après** :

```bash
ma_variable=Bonjour
ville="Paris"
nombre=42
```

> [!DANGER]
> Un espace autour du `=` provoque une erreur — bash interprète alors le nom comme une commande.
> 
> ```bash
> ma_variable = Bonjour   # ERREUR : bash cherche une commande appelée "ma_variable"
> ```
### Lire une variable (référencement)

Pour accéder au contenu d'une variable, on place `$` devant son nom :

```bash
echo $ma_variable
# Bonjour

echo $ville
# Paris
```

### Désambiguation avec les accolades `${}`

Quand le nom de la variable est ambigu (accolé à d'autres caractères), on utilise `${}` pour délimiter clairement le nom :

```bash
unite=gramme
echo "cette pomme pèse 2 $unite"      # cette pomme pèse 2 gramme
echo "cette pomme pèse 2 $unites"     # cette pomme pèse 2   ← variable vide !
echo "cette pomme pèse 2 ${unite}s"   # cette pomme pèse 2 grammes ✓
```

> [!TIP]
> Bonne pratique : utiliser `${}` dès que la variable est suivie d'autres caractères.
---

## 4. Guillemets simples et doubles

Le comportement de `$` dépend du type de guillemets utilisés.

```bash
nom=Samuel

echo "Bonjour $nom"    # Bonjour Samuel  ← guillemets doubles : $ est interprété
echo 'Bonjour $nom'    # Bonjour $nom    ← guillemets simples : $ est littéral
```

> [!WARNING]
> **Toujours mettre les variables entre guillemets doubles** quand leur valeur peut contenir des espaces. Sans guillemets, bash découpe la valeur en plusieurs mots.
> 
> ```bash
> fichier="mon fichier.txt"
> ls $fichier     # ERREUR : bash voit deux arguments "mon" et "fichier.txt"
> ls "$fichier"   # CORRECT : bash voit un seul argument
> ```
---

## 5. Nom de variable — règles

Un nom de variable obéit à ces règles :

- Lettres minuscules `a-z`, majuscules `A-Z`, chiffres `0-9`, et tiret bas `_`
- **Ne peut pas commencer par un chiffre**
- **Pas de tiret `-`** dans le nom

```bash
# Valides
ma_variable=ok
_variable=ok
var1=ok

# Invalides
1test=erreur        # commence par un chiffre → command not found
test-1=erreur       # tiret interdit → command not found
```

**Par convention : minuscules pour les variables locales, MAJUSCULES pour les variables d'environnement.**

---

## 6. Variables d'environnement

### Différence avec une variable locale

Une variable locale n'est **pas transmise** aux sous-shells (processus enfants) :

```bash
ma_variable=local
echo $ma_variable   # local
bash                # on ouvre un sous-shell
echo $ma_variable   # ← vide ! la variable n'existe pas ici
exit
```

Pour qu'une variable soit transmise aux processus enfants, on l'**exporte** :

```bash
export MA_VARIABLE="environnement"
bash
echo $MA_VARIABLE   # environnement ✓
exit
```

On peut aussi combiner déclaration et export en une seule ligne :

```bash
export MA_VARIABLE="valeur"
```

Pour retransformer une variable d'environnement en variable locale :

```bash
export -n MA_VARIABLE
```

Références :
- https://learning.lpi.org/fr/learning-materials/101-500/103/103.1/103.1_02/
- https://learning.lpi.org/fr/learning-materials/102-500/105/105.1/105.1_02/

### Lister les variables d'environnement

```bash
env         # toutes les variables d'environnement (format NOM=valeur)
printenv    # identique à env
export -p   # format declare -x NOM="valeur"
declare -x  # équivalent à export -p
```

`printenv` peut aussi afficher la valeur d'une variable précise (sans le `$`) :

```bash
printenv PATH
printenv HOME USER
```

### Supprimer une variable

```bash
unset ma_variable    # sans le symbole $
```

```bash
var=test
echo $var    # test
unset var
echo $var    # ← vide
```

---

## 7. Variables d'environnement importantes

Le contenu de ces variables système a une incidence directe sur le comportement du shell et des commandes.

| Variable | Contenu |
|----------|---------|
| `HOME` | Répertoire personnel de l'utilisateur (`~`) |
| `USER` | Nom de l'utilisateur courant |
| `SHELL` | Chemin du shell en cours d'exécution |
| `PATH` | Liste des répertoires où bash cherche les exécutables (séparés par `:`) |
| `PS1` | Définition du prompt affiché dans le terminal |
| `LANG` | Langue et jeu de caractères utilisés |
| `PWD` | Répertoire courant |
| `OLDPWD` | Répertoire précédent (utilisé par `cd -`) |
| `HISTFILE` | Fichier où est stocké l'historique des commandes |
| `HISTSIZE` | Nombre de commandes conservées dans l'historique |
| `RANDOM` | Génère un nombre aléatoire entre 0 et 32767 à chaque lecture |

```bash
echo $HOME
echo $USER
echo $PATH
echo $RANDOM   # différent à chaque fois
```

### Modifier le PATH

`PATH` est la liste des dossiers où bash cherche les exécutables. Si tu places un script dans un dossier absent du `PATH`, bash ne pourra pas le trouver par son nom seul.

```bash
# Afficher le PATH actuel
echo $PATH
# /usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games

# Ajouter un dossier à la fin du PATH (pour la session courante)
export PATH="$PATH:/opt/mon-outil/bin"

# Ajouter un dossier dans ~/.bashrc pour le rendre permanent
echo 'export PATH="$PATH:/opt/mon-outil/bin"' >> ~/.bashrc
source ~/.bashrc
```

> [!WARNING]
> Ne jamais **remplacer** le PATH entier. Toujours **ajouter** avec `$PATH:` au début ou à la fin, sinon les commandes système deviennent introuvables.
---

## 8. Substitution de commande

On peut stocker le résultat d'une commande dans une variable avec `$(commande)` :

https://learning.lpi.org/fr/learning-materials/102-500/105/105.2/105.2_01/#:~:text=backtick%20notation

```bash
os=$(uname -o)
echo $os
# GNU/Linux

date_du_jour=$(date +%Y-%m-%d)
echo $date_du_jour
# 2026-04-27

nb_utilisateurs=$(wc -l < /etc/passwd)
echo "Il y a $nb_utilisateurs utilisateurs sur ce système"
```

> [!NOTE]
> Tu peux rencontrer l'ancienne notation avec des guillemets inversés (*backticks*) : `` os=`uname -o` ``. Cette syntaxe est **obsolète** — préférer toujours `$()`.
---

## 9. Longueur d'une variable

https://learning.lpi.org/fr/learning-materials/102-500/105/105.2/105.2_01/#:~:text=La%20longueur%20d%E2%80%99une%20variable

La longueur (nombre de caractères) d'une variable s'obtient avec `${#variable}` :

```bash
os=$(uname -o)
echo $os        # GNU/Linux
echo ${#os}     # 9
```

---

## 10. Remplacement conditionnel

Les accolades permettent de définir une valeur de substitution selon qu'une variable existe ou non. Syntaxe : `${variable:opérateur valeur}`

| Syntaxe | Comportement |
|---------|-------------|
| `${x:-texte}` | Si `x` est vide ou inexistante → utilise `texte`, sinon la valeur de `x` |
| `${x:=texte}` | Idem, mais **affecte aussi** `texte` à `x` |
| `${x:+texte}` | Si `x` est définie et non vide → utilise `texte`, sinon rien |
| `${x:?texte}` | Si `x` est vide ou inexistante → affiche `texte` et quitte avec erreur |

```bash
echo $nom                            # (vide)
echo ${nom:-Camille}                 # Camille
echo $nom                            # (toujours vide, :- ne modifie pas)

echo ${nom:=Camille}                 # Camille
echo $nom                            # Camille  ← := a affecté la valeur

echo ${nom:+"Valeur définie"}        # Valeur définie

unset nom
echo ${nom:?Variable non définie}    # erreur + message → arrêt du script
```

> [!TIP]
> `${x:-valeur_par_defaut}` est très utilisé dans les scripts pour gérer le cas où un argument n'est pas passé.
---

## Récapitulatif des commandes

| Commande | Description |
|----------|-------------|
| `variable=valeur` | Crée une variable locale |
| `echo $variable` | Affiche la valeur d'une variable |
| `echo ${variable}` | Idem, avec délimitation explicite du nom |
| `export VARIABLE=valeur` | Crée une variable d'environnement (transmise aux enfants) |
| `export -n VARIABLE` | Repasse une variable d'environnement en locale |
| `unset variable` | Supprime une variable |
| `env` | Liste toutes les variables d'environnement |
| `printenv` | Idem (peut aussi afficher une variable précise) |
| `export -p` | Liste les variables d'environnement (format `declare -x`) |
| `set \| less` | Affiche toutes les variables et fonctions du shell |
| `$(commande)` | Substitution de commande — stocke le résultat dans une variable |
| `${#variable}` | Retourne la longueur de la variable |
| `${variable:-défaut}` | Retourne la valeur ou un défaut si vide/inexistante |
| `${variable:=défaut}` | Idem et affecte le défaut si vide/inexistante |
| `${variable:?message}` | Quitte avec erreur si la variable est vide/inexistante |
| `LANG=C commande` | Exécute une commande avec une variable d'environnement modifiée ponctuellement |

---

> [!NOTE]
> ### À retenir
> 
> - Une variable s'affecte avec `=` **sans espace** autour du signe : `variable=valeur`.
> - On lit une variable avec `$variable` ou `${variable}` — les accolades sont obligatoires si le nom est suivi d'autres caractères.
> - Guillemets **doubles** `"..."` : le `$` est interprété. Guillemets **simples** `'...'` : tout est littéral.
> - Toujours mettre les variables entre guillemets doubles quand leur valeur peut contenir des espaces.
> - Une **variable locale** n'est pas transmise aux sous-shells ; `export` la rend globale.
> - `unset variable` supprime une variable ; `env` ou `printenv` liste les variables d'environnement.
> - `PATH` : liste des dossiers où bash cherche les exécutables — toujours ajouter, jamais remplacer.
> - `$(commande)` stocke le résultat d'une commande dans une variable (substitution).
> - `${#variable}` retourne la longueur ; `${variable:-défaut}` retourne une valeur par défaut si vide.
---

> [!TIP]
> **TP associé** → [tp-02-variables.md](https://kayasam.github.io/linux-initiation/bash/02-variables/tp)
