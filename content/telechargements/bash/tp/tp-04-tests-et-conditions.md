# TP 04 — Contrôler le sas de la station

> Chapitre associé : [04 — Tests et conditions](https://kayasam.github.io/linux-initiation/bash/04-tests-et-conditions/)

## Mission

Le sas d'Orion est une simulation locale. Ton programme lit un fichier billet et choisit d'accepter ou de refuser l'entrée. Il doit aussi expliquer les erreurs d'utilisation.

## Partie A — Préparer les billets

**A1.** Crée ton atelier et deux billets :

```bash
mkdir -p ~/atelier-bash/04-sas
cd ~/atelier-bash/04-sas
printf 'ORION-OK\n' > billet-valide.txt
printf 'AUTRE-STATION\n' > billet-refuse.txt
```

**A2.** Affiche leurs contenus et vérifie qu'ils sont différents.

## Partie B — Programmer le contrôleur

Crée `sas.sh` dans nano, avec son shebang.

**B1.** Le programme attend exactement un argument. Si `$#` ne vaut pas 1, affiche une ligne d'utilisation sur la sortie d'erreur et termine avec `exit 2`.

**B2.** Range le premier argument dans `billet`. Vérifie qu'il désigne un fichier ordinaire lisible. Sinon, affiche une erreur et termine avec le code 2.

**B3.** Cherche une ligne exactement égale à `ORION-OK` avec `grep -qx`.

- Si la recherche réussit : affiche `SAS OUVERT`, puis termine avec le code 0.
- Sinon : affiche `SAS FERME`, puis termine avec le code 1.

> Indice : une commande placée après `if` sert elle-même de test.

**B4.** Vérifie la syntaxe et ajoute le droit d'exécution.

## Partie C — La tournée des essais

**C1.** Teste les situations ci-dessous. Après **chaque** lancement, utilise immédiatement `printf 'Code : %s\n' "$?"`.

| Lancement | Résultat attendu | Code |
|---|---|---|
| `./sas.sh billet-valide.txt` | SAS ouvert | 0 |
| `./sas.sh billet-refuse.txt` | SAS fermé | 1 |
| `./sas.sh absent.txt` | Erreur de fichier | 2 |
| `./sas.sh` | Aide d'utilisation | 2 |
| `./sas.sh .` | Erreur de fichier : `.` est un dossier | 2 |

**C2.** Copie le billet valide vers un fichier nommé `billet equipe.txt`, puis teste ce nom composé. Il doit être accepté quand tu utilises les guillemets.

**C3.** Explique pourquoi le script vérifie le nombre d'arguments avant de lire `$1`.

## Bonus — Le menu de la station

Crée `menu.sh`. Il demande un choix avec `read -r -p`, puis utilise `case` :

- `1` affiche `Radio disponible`.
- `2` affiche `Reserve disponible`.
- Toute autre réponse affiche `Choix inconnu` et termine avec le code 2.

Ce menu fait un seul choix puis se termine. Une boucle pour le répéter sera vue au prochain chapitre.

## Mission accomplie si…

Les cinq cas du tableau donnent les résultats et codes attendus, et le billet au nom composé fonctionne.

[← Revenir au cours](https://kayasam.github.io/linux-initiation/bash/04-tests-et-conditions/)
