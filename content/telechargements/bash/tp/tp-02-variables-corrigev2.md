# TP 02 — Fabriquer ton badge d'équipage — Corrigév2

> Essaie chaque question avant de cliquer sur **Afficher la correction**. Chaque réponse s’ouvre et se referme indépendamment.

> Chapitre associé : [02 — Les variables](https://kayasam.github.io/linux-initiation/bash/02-variables/)

## Mission

La station Orion attend son nouvel équipage. Prépare un badge personnalisé et calcule l'énergie du poste. Tout se fait dans le terminal Bash Debian.

## Partie A — Les informations du badge

**A1.** Prépare ton atelier :

```bash
mkdir -p ~/atelier-bash/02-badge
cd ~/atelier-bash/02-badge
```

> [!success]- Afficher la correction — A1
> ```bash
> mkdir -p ~/atelier-bash/02-badge
> cd ~/atelier-bash/02-badge
> ```
>
> Tu travailles maintenant dans l’atelier du badge.

**A2.** Crée les variables `station`, contenant `Orion Nord`, et `role`, contenant `pilote`.

> [!success]- Afficher la correction — A2
> ```bash
> station="Orion Nord"
> role="pilote"
> ```
>
> Pas d’espaces autour de `=`. Les guillemets conservent les espaces dans la valeur de `station`.

**A3.** Demande le prénom avec `read -p`. Range-le dans `prenom`.

> [!success]- Afficher la correction — A3
> ```bash
> read -p 'Ton prenom : ' prenom
> ```
>
> `prenom` est le nom de la variable qui reçoit la saisie : on ne met pas de `$` à cet endroit.

**A4.** Affiche une phrase construite avec les trois variables. Si tu réponds `Mila`, elle doit donner :

```text
Mila rejoint Orion Nord comme pilote.
```

> Indice : utilise `echo` et une phrase entre guillemets doubles contenant tes trois variables.

> [!success]- Afficher la correction — A4
> ```bash
> echo "$prenom rejoint $station comme $role."
> ```
>
> Avec `Mila` comme saisie : `Mila rejoint Orion Nord comme pilote.` Les guillemets doubles permettent le remplacement des variables.

## Partie B — Conserver le badge

**B1.** Range le résultat de `hostname` dans `machine` et celui de `date +%F` dans `jour`.

> [!success]- Afficher la correction — B1
> ```bash
> machine=$(hostname)
> jour=$(date +%F)
> ```
>
> `$(...)` exécute la commande et récupère sa sortie. La date et le nom de machine dépendent de ta VM.

**B2.** Crée `badge.txt` avec le prénom, le rôle, la station, la machine et la date. Une information par ligne suffit. Utilise `>` pour la première ligne, puis `>>`.

> [!success]- Afficher la correction — B2
> ```bash
> echo "Prenom : $prenom" > badge.txt
> echo "Role : $role" >> badge.txt
> echo "Station : $station" >> badge.txt
> echo "Machine : $machine" >> badge.txt
> echo "Date : $jour" >> badge.txt
> ```
>
> Le premier `>` initialise le fichier. Les `>>` ajoutent les autres informations sans effacer les précédentes.

**B3.** Lis ton badge avec `cat`. Vérifie que `Orion Nord` apparaît sur une seule ligne.

> [!success]- Afficher la correction — B3
> ```bash
> cat badge.txt
> ```
>
> La ligne `Station : Orion Nord` doit apparaître en entier : le nom de station ne se découpe pas sur plusieurs lignes.

## Partie C — Charger les batteries

**C1.** Définis `batteries=4` et `energie_par_batterie=25`. Calcule `energie_totale` avec une expansion arithmétique.

> [!success]- Afficher la correction — C1
> ```bash
> batteries=4
> energie_par_batterie=25
> energie_totale=$((batteries * energie_par_batterie))
> echo "$energie_totale"
> ```
>
> Résultat : `100`. `$((...))` effectue le calcul arithmétique.

**C2.** La radio consomme 15 unités. Calcule l'énergie restante et ajoute-la au badge.

**Points de contrôle :** énergie totale **100**, énergie restante **85**.

> [!success]- Afficher la correction — C2
> ```bash
> energie_restante=$((energie_totale - 15))
> echo "Energie restante : $energie_restante" >> badge.txt
> ```
>
> Résultat ajouté au badge : `Energie restante : 85`.

**C3.** Affiche une fois le texte littéral `$station`, puis une fois sa valeur. Quels guillemets changes-tu ?

> [!success]- Afficher la correction — C3
> ```bash
> echo '$station'
> echo "$station"
> ```
>
> Les guillemets simples affichent le texte littéral `$station`. Les guillemets doubles permettent son remplacement par `Orion Nord`.

## Bonus — Envoyer le nom de la station

Exporte `NOM_STATION="Orion Nord"`. Lance un second Bash avec `bash -c` et affiche cette variable dedans. Explique le rôle de `export`.

> [!success]- Afficher la correction — Bonus
> ```bash
> export NOM_STATION="Orion Nord"
> bash -c 'echo "Station recue : $NOM_STATION"'
> ```
>
> `export` transmet la variable aux processus enfants, ici le second Bash. Les guillemets simples autour de la commande retardent son expansion jusqu’à ce Bash enfant. Ce réglage n’est pas permanent.

## Mission accomplie si…

- Ton badge contient tes cinq informations et une énergie restante de 85.
- Tu expliques la différence entre `prenom`, `"$prenom"` et `$(hostname)`.
- Tu sais pourquoi les valeurs contenant des espaces restent entre guillemets.

[← Énoncé du TP](https://kayasam.github.io/linux-initiation/bash/02-variables/tp)
