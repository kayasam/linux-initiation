# TP 03 — Programmer le robot d'accueil

> Chapitre associé : [03 — Écrire son premier script](https://kayasam.github.io/linux-initiation/bash/03-bases-du-scripting/)

## Mission

Le robot Orion doit accueillir les visiteurs avec leur nom et leur rôle. Crée un programme que tout l'équipage pourra relancer.

## Partie A — Construire le robot

**A1.** Prépare son atelier :

```bash
mkdir -p ~/atelier-bash/03-robot
cd ~/atelier-bash/03-robot
```

**A2.** Ouvre `robot.sh` avec nano. Ajoute le shebang Bash en première ligne, puis un commentaire décrivant le rôle du programme.

**A3.** Crée deux variables : `prenom`, qui lit le premier argument ou utilise `visiteur`, et `role`, qui lit le deuxième argument ou utilise `explorateur`.

> Indice : `${1:-visiteur}` ; adapte cette écriture au deuxième argument.

**A4.** Affiche une ligne de cette forme :

```text
Bonjour Mila, ton role sur Orion est pilote.
```

Utilise `printf` et tes deux variables. Enregistre et quitte nano.

## Partie B — Les essais du robot

**B1.** Vérifie la syntaxe avec `bash -n`, puis lance le script avec Bash et les arguments `Mila pilote`.

**B2.** Ajoute le droit d'exécution, puis refais le test avec `./robot.sh`.

**B3.** Teste ensuite ces deux cas :

```bash
./robot.sh
./robot.sh "Mila Vega" "responsable radio"
```

**Points de contrôle :** le premier utilise les valeurs par défaut ; le second conserve les noms composés.

**B4.** Relance le cas `Mila pilote`, récupère immédiatement son code de retour et affiche-le. Attendu : **0**.

## Partie C — Comprendre le programme

**C1.** Lance `bash -x robot.sh Mila pilote`. Repère les affectations des deux variables.

**C2.** Ajoute une ligne qui affiche le nombre d'arguments reçus, puis refais les essais sans argument et avec deux arguments.

**C3.** Explique pourquoi on écrit `./robot.sh` et pourquoi on entoure `Mila Vega` de guillemets.

## Bonus — Le journal des arrivées

Ajoute au programme une ligne qui enregistre le prénom et le rôle dans `arrivees.txt`, avec `>>`. Lance le robot deux fois et lis le journal : les deux arrivées doivent être présentes.

Le journal est créé dans le dossier **depuis lequel tu lances le script**. Pour ce TP, reste dans `03-robot`.

## Mission accomplie si…

- La syntaxe est correcte.
- Les trois essais produisent les bons noms et rôles.
- Le programme indique 0 argument ou 2 arguments selon l'essai.
- Le bonus ajoute des lignes sans remplacer les arrivées précédentes.

[← Revenir au cours](https://kayasam.github.io/linux-initiation/bash/03-bases-du-scripting/)
