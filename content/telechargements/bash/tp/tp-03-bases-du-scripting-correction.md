# TP 03 — Correction — Le robot d'accueil

> Énoncé : [TP 03](https://kayasam.github.io/linux-initiation/bash/03-bases-du-scripting/tp)

## Partie A — Construire le robot

**A1.**

```bash
mkdir -p ~/atelier-bash/03-robot
cd ~/atelier-bash/03-robot
```

**A2 à A4.** Contenu final de `robot.sh`, avec l'ajout demandé en C2 :

<!-- fichier: robot.sh -->
```bash
#!/usr/bin/env bash

# Accueillir un visiteur de la station.
prenom="${1:-visiteur}"
role="${2:-explorateur}"
echo "Bonjour $prenom, ton role sur Orion est $role."
echo "Arguments recus : $#"
```

## Partie B — Les essais du robot

**B1 à B4.**

```bash
bash -n robot.sh
bash robot.sh Mila pilote
chmod +x robot.sh
./robot.sh Mila pilote
./robot.sh
./robot.sh "Mila Vega" "responsable radio"
./robot.sh Mila pilote
code=$?
echo "Code : $code"
```

Attendus : `Mila/pilote`, `visiteur/explorateur`, puis `Mila Vega/responsable radio`. Le dernier code est `0`.

## Partie C — Comprendre le programme

**C1.**

```bash
bash -x robot.sh Mila pilote
```

**C2.** `$#` produit `0` sans argument, `2` avec un prénom et un rôle.

**C3.** `./` désigne le dossier courant. Les guillemets conservent chaque nom composé dans un seul argument.

## Bonus — Le journal des arrivées

Ajoute cette ligne à la fin du script, puis refais deux lancements :

<!-- ajouter: robot.sh -->
```bash
echo "$prenom ; $role" >> arrivees.txt
```

Cette ligne se place **dans `robot.sh`**, après les affectations. Le fichier dépend du dossier courant au lancement. `>>` conserve les arrivées précédentes.

[← Énoncé du TP](https://kayasam.github.io/linux-initiation/bash/03-bases-du-scripting/tp)
