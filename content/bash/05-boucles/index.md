---
title: "Bash 05 — Les boucles"
---

# Chapitre 05 — Les boucles

> [!TIP] Ressources du chapitre
> - [Version HTML interactive](https://kayasam.github.io/linux-initiation/bash/cours/05-boucles-interactif.html)
> - <a href="https://kayasam.github.io/linux-initiation/telechargements/bash/cours/05-boucles.md" download>Télécharger le cours en Markdown</a>
> - [Passer au TP](https://kayasam.github.io/linux-initiation/bash/tp/tp-05-boucles)


---

## 1. La boucle for

La boucle `for` exécute une série de commandes **pour chaque élément d'une liste**. C'est la boucle la plus utilisée en bash, y compris directement en ligne de commande.

En français, ça se lit comme ça :

```
POUR chaque "jour" DANS la liste [lundi, mardi, mercredi, jeudi, vendredi]
    afficher "Aujourd'hui : jour"
FIN POUR
```

Ce qui donne en bash :

```bash
for jour in lundi mardi mercredi jeudi vendredi ; do
    echo "Aujourd'hui : $jour"
done
```

La boucle tourne 5 fois. À chaque tour, la variable `$jour` prend la valeur suivante de la liste : d'abord `lundi`, puis `mardi`, etc.

### Syntaxe

```bash
for variable in élément1 élément2 élément3 ; do
    commandes utilisant $variable
done
```

| Mot-clé | Rôle |
|---------|------|
| `for` | "pour chaque" |
| `variable` | nom qu'on donne à l'élément courant (au choix) |
| `in liste` | la liste à parcourir |
| `do` | "faire" — début du bloc à répéter |
| `done` | fin du bloc |

### Liste statique

```bash
for jour in lundi mardi mercredi jeudi vendredi ; do
    echo "Aujourd'hui : $jour"
done
```

### Plage de nombres avec `{debut..fin}`

```bash
for i in {1..5} ; do
    echo "Itération $i"
done

# Plage avec pas : {debut..fin..pas}
for i in {0..10..2} ; do
    echo "$i"    # 0 2 4 6 8 10
done

# Compte à rebours
for i in {5..1} ; do
    echo "$i"
    sleep 1
done
echo "Décollage !"
```

### Résultat d'une commande

```bash
# Itérer sur les fichiers .txt du répertoire courant
for fichier in $(ls *.txt) ; do
    echo "Traitement de $fichier"
done

# Itérer sur les utilisateurs du système
for user in $(cut -d: -f1 /etc/passwd) ; do
    echo "$user"
done
```

> [!TIP]
> Pour itérer sur des fichiers, préférer le glob directement plutôt que `$(ls ...)` :
> 
> ```bash
> for fichier in *.txt ; do
>     echo "Traitement de $fichier"
> done
> ```
> 
> Le glob est plus sûr : `$(ls)` peut poser des problèmes si les noms de fichiers contiennent des espaces.
### For sur une ligne (utile en ligne de commande)

```bash
for i in {1..3} ; do echo "ligne $i" ; done
```

---

## 2. La boucle for — style C

Bash supporte aussi une syntaxe proche du C avec `(( ))`, utile quand on a besoin d'un compteur avec un pas précis :

```bash
for (( i=0 ; i<5 ; i++ )) ; do
    echo "$i"
done
# 0 1 2 3 4

# Compte à rebours
for (( i=5 ; i>=1 ; i-- )) ; do
    echo "$i"
    sleep 1
done
echo "Décollage !"
```

---

## 3. Expressions arithmétiques

Avant d'aborder `while`, il faut connaître la syntaxe pour faire des calculs en bash.

https://learning.lpi.org/fr/learning-materials/102-500/105/105.2/105.2_01/#sec.105.2_01-AE

Bash utilise `$(( expression ))` pour évaluer des expressions arithmétiques :

```bash
a=10
b=3

echo $(( a + b ))    # 13
echo $(( a - b ))    # 7
echo $(( a * b ))    # 30
echo $(( a / b ))    # 3  (division entière uniquement)
echo $(( a % b ))    # 1  (modulo — reste de la division)
```

Pour modifier une variable :

```bash
compteur=0
compteur=$(( compteur + 1 ))    # incrémenter
compteur=$(( compteur - 1 ))    # décrémenter

# Raccourcis
(( compteur++ ))    # équivalent à compteur=$(( compteur + 1 ))
(( compteur-- ))
(( compteur += 5 ))
```

> [!WARNING]
> Bash ne gère que les **entiers**. Pour des calculs avec des décimaux, utiliser `bc` :
> 
> ```bash
> echo "scale=2; 10 / 3" | bc    # 3.33
> ```
---

## 4. La boucle while

`while` exécute des commandes **tant qu'une condition est vraie**. À utiliser quand on ne connaît pas à l'avance le nombre d'itérations.

https://www.it-connect.fr/script-bash-utiliser-boucles-while-exemples-linux/

En français :

```
TANT QUE le compteur est inférieur à 5
    afficher le compteur
    ajouter 1 au compteur
FIN TANT QUE
```

Ce qui donne en bash :

```bash
compteur=0

while [[ "$compteur" -lt 5 ]] ; do
    echo "Compteur : $compteur"
    (( compteur++ ))
done
```

La boucle vérifie la condition **avant chaque tour**. Dès qu'elle devient fausse, on sort.

### Syntaxe

```bash
while [[ condition ]] ; do
    commandes
done
```

| Mot-clé | Rôle |
|---------|------|
| `while` | "tant que" |
| `[[ condition ]]` | la condition vérifiée avant chaque tour |
| `do` | "faire" — début du bloc à répéter |
| `done` | fin du bloc |

### Exemple — compteur

```bash
compteur=0

while [[ "$compteur" -lt 5 ]] ; do
    echo "Compteur : $compteur"
    (( compteur++ ))
done
```

> [!DANGER]
> Oublier d'incrémenter le compteur crée une **boucle infinie**. Pour en sortir : `Ctrl+C`.
> 
> ```bash
> compteur=0
> while [[ "$compteur" -lt 5 ]] ; do
>     echo "$compteur"
>     # (( compteur++ ))  ← oublié → boucle infinie !
> done
> ```
### Exemple — saisie utilisateur jusqu'à réponse valide

```bash
reponse=""

while [[ "$reponse" != "oui" && "$reponse" != "non" ]] ; do
    read -p "Voulez-vous continuer ? (oui/non) : " reponse
done

echo "Vous avez répondu : $reponse"
```

### Lire un fichier ligne par ligne

`while` avec `read` est le moyen idiomatique de traiter un fichier ligne par ligne :

```bash
while read -r ligne ; do
    echo "Ligne : $ligne"
done < /etc/hosts
```

> [!NOTE]
> L'option `-r` de `read` empêche l'interprétation des antislashs dans la ligne lue. Toujours utiliser `read -r` pour lire des fichiers.
---

## 5. La boucle until

`until` est l'inverse de `while` : elle s'exécute **tant que la condition est fausse**, et s'arrête dès qu'elle devient vraie.

En français :

```
JUSQU'À CE QUE le fichier existe
    afficher "En attente..."
    attendre 2 secondes
FIN JUSQU'À
```

Ce qui donne en bash :

```bash
until [[ -f "/tmp/signal.txt" ]] ; do
    echo "En attente du fichier..."
    sleep 2
done
echo "Fichier détecté !"
```

La boucle vérifie la condition **avant chaque tour**. Elle tourne tant que la condition est **fausse**, et s'arrête dès qu'elle devient vraie — l'inverse exact de `while`.

### Syntaxe

```bash
until [[ condition ]] ; do
    commandes
done
```

| Mot-clé | Rôle |
|---------|------|
| `until` | "jusqu'à ce que" |
| `[[ condition ]]` | la condition vérifiée avant chaque tour |
| `do` | "faire" — début du bloc à répéter |
| `done` | fin du bloc |

| Structure | Continue tant que… | S'arrête quand… |
|-----------|-------------------|-----------------|
| `while` | la condition est **vraie** | la condition devient **fausse** |
| `until` | la condition est **fausse** | la condition devient **vraie** |

```bash
# Attendre qu'un fichier existe
until [[ -f "/tmp/signal.txt" ]] ; do
    echo "En attente du fichier..."
    sleep 2
done
echo "Fichier détecté !"
```

---

## 6. La commande read

https://learning.lpi.org/fr/learning-materials/102-500/105/105.2/105.2_01/#:~:text=La%20commande%20read

`read` permet de **lire une saisie au clavier** (ou une ligne depuis un fichier) et de la stocker dans une variable. Elle est indispensable dès qu'un script doit interagir avec l'utilisateur ou traiter un fichier ligne par ligne.

### Syntaxe de base

```bash
read variable
```

La commande attend que l'utilisateur tape quelque chose et appuie sur Entrée. La valeur saisie est stockée dans `variable`.

```bash
read prenom
# l'utilisateur tape : Samuel
echo "Bonjour $prenom !"
# Bonjour Samuel !
```

Si aucune variable n'est fournie, la valeur est stockée dans la variable spéciale `$REPLY` :

```bash
read
echo $REPLY
```

### Options principales

| Option | Rôle |
|--------|------|
| `-p "message"` | Affiche un message avant d'attendre la saisie |
| `-s` | Mode silencieux — n'affiche pas ce que l'utilisateur tape (mots de passe) |
| `-r` | Mode brut — ne pas interpréter les antislashs (toujours utiliser pour lire un fichier) |

### Exemples

```bash
# Afficher une invite avec -p
read -p "Entrez votre prénom : " prenom
echo "Bonjour, $prenom !"

# Saisie de mot de passe avec -s
read -s -p "Mot de passe : " mdp
echo ""    # saut de ligne car -s n'en affiche pas
echo "Mot de passe enregistré."

# Lire plusieurs variables d'un coup (séparées par des espaces)
read -p "Entrez votre prénom et votre nom : " prenom nom
echo "Prénom : $prenom — Nom : $nom"
```

> [!NOTE]
> Avec plusieurs variables, chaque mot séparé par un espace est assigné à la variable suivante. Si l'utilisateur entre plus de mots que de variables, le surplus va dans la dernière variable.
### Utilisation avec while pour lire un fichier

C'est la combinaison la plus courante en scripting :

```bash
while read -r ligne ; do
    echo "$ligne"
done < /etc/hosts
```

> [!WARNING]
> Toujours utiliser `read -r` pour lire un fichier. Sans `-r`, bash interprète les `\n`, `\t` etc. présents dans le fichier comme des caractères spéciaux, ce qui peut corrompre la valeur lue.
---

## 7. Contrôle de flux : break et continue

### break — sortir d'une boucle

`break` interrompt immédiatement la boucle courante :

```bash
for i in {1..10} ; do
    if [[ "$i" -eq 5 ]] ; then
        echo "Arrêt à $i"
        break
    fi
    echo "$i"
done
# Affiche 1 2 3 4 puis "Arrêt à 5"
```

### continue — passer à l'itération suivante

`continue` saute le reste du bloc courant et passe directement à l'itération suivante :

```bash
for i in {1..6} ; do
    if [[ $(( i % 2 )) -eq 0 ]] ; then
        continue    # on saute les nombres pairs
    fi
    echo "$i"
done
# Affiche 1 3 5
```

---

## 7. Exercices intégrés

### Exercice 1 — Compte à rebours

Écrire un script `decollage.sh` qui compte à rebours de 5 à 1 (avec une seconde entre chaque), puis affiche `Décollage !`.

> [!TIP]
> **Solution avec for :**
> 
> ```bash
> #!/usr/bin/env bash
> 
> set -euo pipefail
> 
> for i in {5..1} ; do
>     echo "$i"
>     sleep 1
> done
> echo "Décollage !"
> ```
> 
> **Solution avec while :**
> 
> ```bash
> #!/usr/bin/env bash
> 
> set -euo pipefail
> 
> compteur=5
> 
> while [[ "$compteur" -gt 0 ]] ; do
>     echo "$compteur"
>     (( compteur-- ))
>     sleep 1
> done
> echo "Décollage !"
> ```
### Exercice 2 — Créer des fichiers en série

Écrire un script `creer-fichiers.sh` qui prend un dossier en argument et crée dedans 5 fichiers nommés `fichier1.txt` à `fichier5.txt`.

> [!TIP]
> **Solution :**
> 
> ```bash
> #!/usr/bin/env bash
> 
> set -euo pipefail
> 
> dossier="$1"
> 
> if [[ ! -d "$dossier" ]] ; then
>     echo "Erreur : $dossier n'est pas un dossier valide"
>     exit 1
> fi
> 
> for i in {1..5} ; do
>     touch "$dossier/fichier${i}.txt"
>     echo "Créé : $dossier/fichier${i}.txt"
> done
> ```
### Exercice 3 — Lire un fichier et afficher les utilisateurs bash

Écrire un script qui lit `/etc/passwd` ligne par ligne et affiche uniquement les utilisateurs qui ont `/bin/bash` comme shell.

> [!TIP]
> **Solution :**
> 
> ```bash
> #!/usr/bin/env bash
> 
> set -euo pipefail
> 
> while read -r ligne ; do
>     if [[ "$ligne" == *"/bin/bash" ]] ; then
>         echo "$ligne" | cut -d: -f1
>     fi
> done < /etc/passwd
> ```
---

## Récapitulatif des commandes

| Commande / Syntaxe | Description |
|-------------------|-------------|
| `for var in liste ; do ... done` | Boucle sur une liste d'éléments |
| `for var in {1..10} ; do ... done` | Boucle sur une plage de nombres |
| `for var in {0..10..2} ; do ... done` | Boucle sur une plage avec un pas |
| `for var in $(commande) ; do ... done` | Boucle sur le résultat d'une commande |
| `for var in *.ext ; do ... done` | Boucle sur des fichiers par glob |
| `for (( i=0; i<n; i++ )) ; do ... done` | Boucle style C avec compteur |
| `while [[ condition ]] ; do ... done` | Boucle tant que la condition est vraie |
| `until [[ condition ]] ; do ... done` | Boucle jusqu'à ce que la condition soit vraie |
| `while read -r ligne ; do ... done < fichier` | Lire un fichier ligne par ligne |
| `read variable` | Lit une saisie clavier et la stocke dans la variable |
| `read -p "msg" variable` | Idem avec une invite affichée avant la saisie |
| `read -s variable` | Saisie silencieuse (mot de passe) |
| `read -r variable` | Lecture brute — ne pas interpréter les antislashs |
| `$REPLY` | Variable par défaut de `read` si aucune variable n'est précisée |
| `break` | Interrompt la boucle courante |
| `continue` | Passe à l'itération suivante |
| `$(( a + b ))` | Calcul arithmétique entier |
| `(( compteur++ ))` | Incrémentation |
| `(( compteur-- ))` | Décrémentation |
| `(( compteur += n ))` | Addition et affectation |
| `echo "scale=2; a/b" \| bc` | Calcul avec décimaux |
| `sleep n` | Pause de n secondes |

---

> [!NOTE]
> ### À retenir
> 
> - `for var in liste ; do ... done` : boucle sur chaque élément d'une liste — **POUR chaque ... FAIRE**.
> - `{1..10}` génère une plage, `{0..10..2}` ajoute un pas, `{10..1}` fait un compte à rebours.
> - `for (( i=0; i<n; i++ ))` : boucle style C, utile pour un compteur avec pas précis.
> - `while [[ condition ]] ; do ... done` : **TANT QUE** la condition est vraie — toujours incrémenter le compteur !
> - `until [[ condition ]] ; do ... done` : **JUSQU'À CE QUE** la condition soit vraie — inverse du `while`.
> - `while read -r ligne ; do ... done < fichier` : lire un fichier ligne par ligne — toujours utiliser `-r`.
> - `read -p "message"` affiche une invite ; `read -s` masque la saisie (mots de passe).
> - `$(( expression ))` fait du calcul entier ; `(( compteur++ ))` incrémente.
> - `break` sort de la boucle ; `continue` passe à l'itération suivante.
---

> [!TIP]
> **TP associé** → `tp-05-boucles.md`

[← Parcours Bash](https://kayasam.github.io/linux-initiation/#bash) · [Tous les TP Bash](https://kayasam.github.io/linux-initiation/bash/tp/)
