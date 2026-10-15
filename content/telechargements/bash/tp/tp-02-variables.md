# TP 02 — Fabriquer ton badge d'équipage

> Chapitre associé : [02 — Les variables](https://kayasam.github.io/linux-initiation/bash/02-variables/)

## Mission

La station Orion attend son nouvel équipage. Prépare un badge personnalisé et calcule l'énergie du poste. Tout se fait dans le terminal Bash Debian.

## Partie A — Les informations du badge

**A1.** Prépare ton atelier :

```bash
mkdir -p ~/atelier-bash/02-badge
cd ~/atelier-bash/02-badge
```

**A2.** Crée les variables `station`, contenant `Orion Nord`, et `role`, contenant `pilote`.

**A3.** Demande le prénom avec `read -p`. Range-le dans `prenom`.

**A4.** Affiche une phrase construite avec les trois variables. Si tu réponds `Mila`, elle doit donner :

```text
Mila rejoint Orion Nord comme pilote.
```

> Indice : utilise `echo` et une phrase entre guillemets doubles contenant tes trois variables.

## Partie B — Conserver le badge

**B1.** Range le résultat de `hostname` dans `machine` et celui de `date +%F` dans `jour`.

**B2.** Crée `badge.txt` avec le prénom, le rôle, la station, la machine et la date. Une information par ligne suffit. Utilise `>` pour la première ligne, puis `>>`.

**B3.** Lis ton badge avec `cat`. Vérifie que `Orion Nord` apparaît sur une seule ligne.

## Partie C — Charger les batteries

**C1.** Définis `batteries=4` et `energie_par_batterie=25`. Calcule `energie_totale` avec une expansion arithmétique.

**C2.** La radio consomme 15 unités. Calcule l'énergie restante et ajoute-la au badge.

**Points de contrôle :** énergie totale **100**, énergie restante **85**.

**C3.** Affiche une fois le texte littéral `$station`, puis une fois sa valeur. Quels guillemets changes-tu ?

## Bonus — Envoyer le nom de la station

Exporte `NOM_STATION="Orion Nord"`. Lance un second Bash avec `bash -c` et affiche cette variable dedans. Explique le rôle de `export`.

## Mission accomplie si…

- Ton badge contient tes cinq informations et une énergie restante de 85.
- Tu expliques la différence entre `prenom`, `"$prenom"` et `$(hostname)`.
- Tu sais pourquoi les valeurs contenant des espaces restent entre guillemets.

[← Revenir au cours](https://kayasam.github.io/linux-initiation/bash/02-variables/)
