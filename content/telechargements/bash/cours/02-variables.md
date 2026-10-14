# Chapitre 02 — Les variables

> [!NOTE] Objectif
> Mémoriser une valeur, l'afficher dans une phrase et demander une réponse à l'utilisateur.

**À connaître :** `nom=valeur`, `"$nom"`, `read -r`, `$(commande)`, `$((calcul))`, `export`.
---

## 1. Une variable donne un nom à une valeur

```bash
prenom="Mila"
printf 'Bonjour %s\n' "$prenom"
```

Résultat : `Bonjour Mila`.

La première ligne **affecte** une valeur. La seconde **lit** cette valeur avec `$prenom`. Dans `printf`, `%s` est l'emplacement où sera inséré le texte fourni ensuite.

![Affecter une valeur puis la lire](https://kayasam.github.io/linux-initiation/bash/images/bash-02-variables.svg)

| Écriture | Ce qu'elle signifie |
|---|---|
| `prenom="Mila"` | Ranger `Mila` dans la variable `prenom` |
| `"$prenom"` | Utiliser sa valeur comme un seul argument |
| `"${prenom}"` | Même lecture, avec une limite explicite du nom |

**Aucun espace autour de `=`.** `prenom = Mila` demanderait à Bash de lancer une commande nommée `prenom`.

Choisis des noms lisibles : `prenom`, `nom_station`, `nombre_messages`. Un nom ne commence pas par un chiffre. `prenom` et `PRENOM` sont deux variables différentes.

## 2. Pourquoi mettre des guillemets ?

```bash
station="Orion Nord"
printf 'Destination : %s\n' "$station"
```

Les guillemets doubles gardent les mots ensemble, tout en laissant Bash lire la variable.

```bash
printf '%s\n' '$station'
printf '%s\n' "$station"
```

Résultats, dans cet ordre :

```text
$station
Orion Nord
```

- Les **guillemets simples** conservent le texte tel quel.
- Les **guillemets doubles** permettent la lecture de `$station`, en gardant sa valeur groupée.

> [!TIP] Habitude à prendre
> Quand tu utilises une variable comme argument, écris `"$variable"`. C'est particulièrement important pour les noms de fichiers contenant des espaces.

## 3. Réutiliser une valeur dans un nom

```bash
mission="orion"
fichier="${mission}_rapport.txt"
printf '%s\n' "$fichier"
```

Résultat : `orion_rapport.txt`. Les accolades montrent que le nom de variable s'arrête avant `_rapport.txt`.

## 4. Poser une question avec read

```bash
read -r -p 'Ton prenom : ' prenom
printf 'Bienvenue %s\n' "$prenom"
```

- `read` attend une ligne et la range dans `prenom`.
- `-r` conserve les antislashs au lieu de les interpréter comme des échappements.
- `-p` affiche la question dans le terminal.

Tape une réponse, puis appuie sur **Entrée**. Le nom après la question est celui de la variable : on écrit `prenom`, sans `$`.

Ces lignes s'exécutent dans ton terminal Bash. Le programme attend réellement ta saisie : ce n'est pas un blocage.

## 5. Garder le résultat d'une commande

```bash
machine=$(hostname)
jour=$(date +%F)
printf 'Machine : %s — date : %s\n' "$machine" "$jour"
```

`$(...)` exécute la commande et récupère sa sortie. Ici, Bash garde le nom de la machine et la date au format année-mois-jour. La valeur de la date dépend du jour où tu exécutes l'exemple.

Ne confonds pas : `"$machine"` lit une variable, `$(hostname)` lance une commande.

## 6. Calculer avec des nombres entiers

```bash
batteries=4
energie_par_batterie=25
energie_totale=$((batteries * energie_par_batterie))
printf 'Energie disponible : %s unites\n' "$energie_totale"
```

Résultat : `Energie disponible : 100 unites`.

Dans `$((...))`, Bash calcule avec des entiers. Il reconnaît ici les noms de variables sans `$`.

| Opérateur | Calcul |
|---|---|
| `+`, `-` | Addition, soustraction |
| `*` | Multiplication |
| `/` | Division entière : `7 / 2` donne `3` |
| `%` | Reste : `7 % 2` donne `1` |

Nous utilisons ici des valeurs fixées dans le cours. Avant de calculer avec une saisie libre, il faudra vérifier qu'elle contient bien un nombre : ce sera un défi du chapitre 04.

## 7. Une variable d'environnement

Certaines variables sont déjà définies :

```bash
printf 'Dossier personnel : %s\n' "$HOME"
printf 'Recherche des commandes : %s\n' "$PATH"
```

`HOME` désigne ton dossier personnel. `PATH` liste les dossiers où le shell recherche les commandes quand leur nom ne contient pas de `/`.

`export` rend une variable disponible pour les programmes lancés ensuite :

```bash
export NOM_STATION="Orion"
bash -c 'printf "Station recue : %s\n" "$NOM_STATION"'
```

Le second Bash reçoit `NOM_STATION`. Cet exemple ne modifie aucun fichier de configuration. Les variables disparaissent à la fin du processus qui les contient ; un nouveau script ne peut pas modifier les variables de ton shell parent.

## 8. Une valeur par défaut

```bash
surnom=""
printf 'Nom affiche : %s\n' "${surnom:-visiteur}"
```

Résultat : `Nom affiche : visiteur`. `${surnom:-visiteur}` fournit `visiteur` si `surnom` est vide ou absente. Cela ne remplit pas automatiquement la variable `surnom`.

## À retenir

- Affecter : `prenom="Mila"`. Lire : `"$prenom"`.
- `read` récupère une saisie ; `$(...)` récupère une sortie de commande.
- `$((...))` effectue un calcul entier.
- Les guillemets doubles protègent les valeurs contenant des espaces.

**À toi :** que produit `printf '%s\n' '$prenom'` ? Et si tu remplaces les guillemets simples par des doubles ?

[Passer au TP](https://kayasam.github.io/linux-initiation/bash/02-variables/tp)
