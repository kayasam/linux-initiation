---
title: "05. Les boucles"
---

# Chapitre 05 — Les boucles

> [!TIP] Ressources du chapitre
> - [Version HTML](https://kayasam.github.io/linux-initiation/bash/cours/05-boucles-interactif.html)
> - <a href="https://kayasam.github.io/linux-initiation/telechargements/bash/cours/05-boucles.md" download>Télécharger le cours en Markdown</a>
> - [Passer au TP](https://kayasam.github.io/linux-initiation/bash/05-boucles/tp)


> [!NOTE] Objectif
> Répéter une action sur une liste ou un groupe de fichiers, sans recopier les mêmes commandes.

**À connaître :** `for`, `in`, `do`, `done`, `while`, `read`, `break`, `continue`.
---

## 1. Une action, plusieurs éléments

![La même action pour chaque fichier](https://kayasam.github.io/linux-initiation/bash/images/bash-05-boucle.svg)

Une boucle `for` prend les éléments **un par un**. À chaque passage, une variable contient l'élément courant.

```bash
for personne in Mila Noe Vega; do
    printf 'Bonjour %s\n' "$personne"
done
```

Résultat : trois lignes, une par personne. `do` ouvre le corps de la boucle ; `done` le ferme.

Un élément peut contenir des espaces :

```bash
for poste in "salle radio" "poste de pilotage"; do
    printf 'Controle : %s\n' "$poste"
done
```

Les guillemets conservent ici **deux éléments**, pas six mots.

## 2. Répéter avec un compteur

```bash
for numero in 1 2 3; do
    printf 'Test numero %s\n' "$numero"
done
```

Pour compter des passages :

```bash
compteur=0
for objet in radio casque batterie; do
    compteur=$((compteur + 1))
    printf '%s : %s\n' "$compteur" "$objet"
done
printf 'Objets controles : %s\n' "$compteur"
```

On initialise le compteur **avant** la boucle. On augmente sa valeur **dans** la boucle. Le résultat final est 3.

## 3. Parcourir des fichiers

Prépare quelques données :

```bash
mkdir -p ~/atelier-bash/boucles/messages
cd ~/atelier-bash/boucles
printf 'Bienvenue\n' > messages/accueil.txt
printf 'Radio active\n' > "messages/radio du jour.txt"
printf 'Image fictive\n' > messages/image.png
```

```bash
for fichier in messages/*.txt; do
    if [[ -f "$fichier" ]]; then
        printf 'Lecture de %s\n' "$fichier"
        cat "$fichier"
    fi
done
```

`*.txt` est un **motif de noms** : Bash le remplace par les noms qui correspondent. Le fichier `image.png` n'est pas sélectionné.

Le test `-f` évite de traiter un dossier. Il gère aussi le cas où aucun nom ne correspond : avec les réglages habituels de Bash, le motif reste alors un texte littéral, qui n'est pas un fichier.

> [!TIP] La bonne place des guillemets
> Écris `"$dossier"/*.txt` si le dossier vient d'une variable. La variable est protégée ; le `*` reste disponible pour la recherche. Ne fais pas une boucle sur le résultat de `ls` : les noms contenant des espaces seraient difficiles à traiter correctement.

## 4. Une boucle while répète tant que le test réussit

```bash
compteur=3
while [[ "$compteur" -gt 0 ]]; do
    printf 'Depart dans %s\n' "$compteur"
    compteur=$((compteur - 1))
done
printf 'Decollage\n'
```

La valeur descend de 3 à 1. Quand elle vaut 0, le test échoue et la boucle se termine. Si tu oublies la soustraction, la condition ne changera pas : **Ctrl+C** permet d'interrompre une boucle sans fin.

## 5. Lire un fichier ligne par ligne

```bash
printf 'Mila Vega\nNoe\n' > equipe.txt
while IFS= read -r personne; do
    printf 'Equipier : %s\n' "$personne"
done < equipe.txt
```

- `read` lit une ligne à chaque passage.
- `IFS=` évite de retirer les espaces de début et de fin.
- `-r` conserve les antislashs.
- `< equipe.txt` fournit le fichier comme entrée à la boucle.

Ici, les lignes se terminent toutes par un retour à la ligne, créé avec `\n`. Pour traiter aussi une dernière ligne sans ce retour, on peut compléter la condition ; ce cas est proposé en bonus du TP.

## 6. Passer un élément ou arrêter la boucle

`continue` passe directement à l'élément suivant. `break` quitte la boucle.

```bash
for message in INFO IGNORER ALERTE FIN; do
    if [[ "$message" == "IGNORER" ]]; then
        continue
    fi
    if [[ "$message" == "FIN" ]]; then
        break
    fi
    printf 'Message : %s\n' "$message"
done
```

Résultat : `INFO` puis `ALERTE`. Commence par une boucle simple ; ajoute ces instructions seulement si elles rendent le parcours plus clair.

## 7. Exemple complet : copier les messages

Dans le dossier `boucles`, crée `copier.sh` :

<!-- fichier: copier.sh -->
```bash
#!/usr/bin/env bash

if [[ "$#" -gt 1 ]]; then
    printf 'Usage : %s [dossier]\n' "$0" >&2
    exit 2
fi

source="${1:-messages}"
if [[ ! -d "$source" ]]; then
    printf 'Dossier absent : %s\n' "$source" >&2
    exit 2
fi

destination="$source/copies"
if ! mkdir -p -- "$destination"; then
    printf 'Impossible de creer la destination\n' >&2
    exit 1
fi

compteur=0
for fichier in "$source"/*.txt; do
    if [[ ! -f "$fichier" ]]; then
        continue
    fi
    if ! cp -- "$fichier" "$destination/"; then
        printf 'Copie impossible : %s\n' "$fichier" >&2
        exit 1
    fi
    compteur=$((compteur + 1))
done

printf 'Copies realisees : %s\n' "$compteur"
```

`--` marque la fin des options pour `mkdir` et `cp`. Un nom commençant par `-` ne sera donc pas pris pour une option. `cp` copie les fichiers sans supprimer les originaux.

```bash
bash -n copier.sh
bash copier.sh messages
ls messages/copies
```

Deux fichiers doivent être copiés. Ce petit outil remplace les copies de même nom lors d'un nouveau lancement : ce n'est pas un système de sauvegarde avec historique.

## Pour aller plus loin : une fonction

Une fonction donne un nom à un groupe de commandes. Tu peux l'appeler plusieurs fois :

```bash
saluer() {
    local personne="${1:-equipier}"
    printf 'Bienvenue %s\n' "$personne"
}
saluer Mila
saluer Vega
```

`local` réserve la variable à cette fonction. Les arguments de la fonction se lisent avec `$1`, `$2`, comme ceux d'un script.

## À retenir

- `for` parcourt des éléments ; `while` répète tant qu'une condition réussit.
- Protège les noms avec `"$variable"` et vérifie le type de fichier.
- Teste aussi une liste vide, un nom composé et un dossier absent.

[Passer au TP](https://kayasam.github.io/linux-initiation/bash/05-boucles/tp)

[← Parcours Bash](https://kayasam.github.io/linux-initiation/#bash) · [Tous les TP Bash](https://kayasam.github.io/linux-initiation/bash/tp/)
