# TP 02 — Correction — Fabriquer ton badge

> Énoncé : [TP 02](https://kayasam.github.io/linux-initiation/bash/02-variables/tp)

## Partie A — Les informations du badge

**A1 à A4.**

```bash
mkdir -p ~/atelier-bash/02-badge
cd ~/atelier-bash/02-badge
station="Orion Nord"
role="pilote"
read -p 'Ton prenom : ' prenom
echo "$prenom rejoint $station comme $role."
```

Avec la saisie `Mila`, on retrouve la phrase de l'énoncé. Le nom à la fin de `read` est une destination, donc il n'a pas de `$`.

## Partie B — Conserver le badge

**B1 à B3.**

```bash
machine=$(hostname)
jour=$(date +%F)
echo "Prenom : $prenom" > badge.txt
echo "Role : $role" >> badge.txt
echo "Station : $station" >> badge.txt
echo "Machine : $machine" >> badge.txt
echo "Date : $jour" >> badge.txt
cat badge.txt
```

La date et le nom de machine dépendent de la VM au moment du TP. Les autres champs correspondent aux variables choisies.

## Partie C — Charger les batteries

**C1 à C3.**

```bash
batteries=4
energie_par_batterie=25
energie_totale=$((batteries * energie_par_batterie))
energie_restante=$((energie_totale - 15))
echo "Energie restante : $energie_restante" >> badge.txt
echo "Total : $energie_totale ; reste : $energie_restante"
echo '$station'
echo "$station"
```

Résultats : 100, 85, puis le texte `$station` et la valeur `Orion Nord`.

## Bonus — Envoyer le nom de la station

```bash
export NOM_STATION="Orion Nord"
bash -c 'echo "Station recue : $NOM_STATION"'
```

L'export transmet la variable au processus enfant. Il n'écrit pas de réglage permanent.

[← Énoncé du TP](https://kayasam.github.io/linux-initiation/bash/02-variables/tp)
