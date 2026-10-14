# Chapitre 04 — Les tests et les conditions

> [!NOTE] Objectif
> Faire prendre une décision à ton script : continuer, choisir une action ou expliquer pourquoi il s'arrête.

**À connaître :** `if`, `then`, `else`, `elif`, `fi`, `[[ ... ]]`, `case`, `exit`.
---

## 1. Une question avec deux chemins

![Un test choisit entre deux actions](https://kayasam.github.io/linux-initiation/bash/images/bash-04-condition.svg)

Un test a un résultat : vrai ou faux. `if` exécute le premier bloc lorsque le test réussit ; sinon, il peut exécuter le bloc `else`.

```bash
energie=30
if [[ "$energie" -ge 20 ]]; then
    printf 'Depart autorise\n'
else
    printf 'Recharge necessaire\n'
fi
```

Résultat : `Depart autorise`. Avec `energie=10`, tu prendrais l'autre chemin.

Dans ce cours, nous utilisons `[[ ... ]]`, une syntaxe de **Bash**. Garde les espaces après `[[` et avant `]]`. `then` ouvre le bloc et `fi` ferme le `if`. L'indentation de quatre espaces rend les branches visibles.

## 2. Comparer du texte

```bash
destination="Orion"
if [[ "$destination" == "Orion" ]]; then
    printf 'Bonne destination\n'
else
    printf 'Verifier le billet\n'
fi
```

| Test | Question posée |
|---|---|
| `[[ "$nom" == "Mila" ]]` | La valeur est-elle exactement `Mila` ? |
| `[[ "$nom" != "Mila" ]]` | Est-elle différente de `Mila` ? |
| `[[ -z "$nom" ]]` | La chaîne est-elle vide ? |
| `[[ -n "$nom" ]]` | Contient-elle au moins un caractère ? |

Le signe `=` d'une affectation n'est pas un test. `nom="Mila"` change la variable ; le test vérifie sa valeur.

## 3. Comparer des entiers

| Opérateur | Signification |
|---|---|
| `-eq`, `-ne` | Égal, différent |
| `-lt`, `-le` | Inférieur, inférieur ou égal |
| `-gt`, `-ge` | Supérieur, supérieur ou égal |

On peut distinguer plusieurs situations avec `elif` :

```bash
energie=15
if [[ "$energie" -ge 50 ]]; then
    printf 'Grande mission\n'
elif [[ "$energie" -ge 20 ]]; then
    printf 'Petite mission\n'
else
    printf 'Recharge\n'
fi
```

Bash s'arrête à la première branche qui réussit. Ici, il affiche `Recharge`. Les valeurs de cet exemple sont des entiers fixés dans le programme ; une saisie utilisateur doit être vérifiée avant un test numérique.

## 4. Tester un fichier

```bash
mkdir -p ~/atelier-bash/conditions
cd ~/atelier-bash/conditions
printf 'ORION-OK\n' > billet.txt

if [[ -f "billet.txt" ]]; then
    printf 'Billet trouve\n'
else
    printf 'Billet absent\n'
fi
```

| Test | Vérification |
|---|---|
| `-e` | Le chemin existe |
| `-f` | C'est un fichier ordinaire |
| `-d` | C'est un dossier |
| `-r` | Le fichier est lisible pour le processus |
| `-s` | Le fichier existe et sa taille dépasse zéro |

Un dossier n'est pas un fichier ordinaire. Choisis le test adapté plutôt que de tout vérifier avec `-e`.

## 5. Réagir au résultat d'une commande

On peut placer une commande directement après `if` : son code de retour sert de test.

```bash
if grep -qx 'ORION-OK' billet.txt; then
    printf 'Billet accepte\n'
else
    printf 'Billet refuse\n'
fi
```

`grep -q` n'affiche pas les lignes trouvées. `-x` exige une correspondance sur une ligne entière. Le code `0` de `grep` sélectionne le premier bloc.

Cet exemple vérifie qu'au moins une ligne est exactement `ORION-OK`. Ce n'est pas une vérification de signature ni un vrai système d'accès.

## 6. Vérifier les arguments avant de les utiliser

Contenu de `controle.sh` :

<!-- fichier: controle.sh -->
```bash
#!/usr/bin/env bash

if [[ "$#" -ne 1 ]]; then
    printf 'Usage : %s fichier\n' "$0" >&2
    exit 2
fi

fichier="$1"
if [[ ! -f "$fichier" ]]; then
    printf 'Fichier absent : %s\n' "$fichier" >&2
    exit 2
fi

printf 'Fichier disponible : %s\n' "$fichier"
exit 0
```

- `$#` vérifie le nombre d'arguments **avant** la lecture de `$1`.
- `!` inverse un test.
- `>&2` dirige un message vers la sortie d'erreur.
- `exit` termine ce script avec le code choisi.

```bash
bash -n controle.sh
bash controle.sh billet.txt
bash controle.sh introuvable.txt
printf 'Code du dernier essai : %s\n' "$?"
```

Le premier essai réussit. Le second affiche une erreur et le code **2**. Ces valeurs sont une convention choisie pour ce programme ; d'autres commandes peuvent en utiliser d'autres.

## 7. Choisir parmi plusieurs mots avec case

```bash
choix="radio"
case "$choix" in
    radio)
        printf 'Canal radio ouvert\n'
        ;;
    reserve)
        printf 'Reserve disponible\n'
        ;;
    *)
        printf 'Choix inconnu\n'
        ;;
esac
```

Chaque choix se termine par `)`. `;;` termine sa branche. `*` récupère les autres cas. `esac` ferme la structure.

## 8. Combiner deux vérifications

```bash
if [[ -f "billet.txt" && -r "billet.txt" ]]; then
    printf 'Le billet est un fichier lisible\n'
fi
```

`&&` signifie « et ». `||` signifie « ou ». Commence par des tests courts ; si la condition devient difficile à lire, sépare les vérifications et explique chaque erreur.

## À retenir

- Un test choisit un chemin ; il ne modifie pas la valeur testée.
- Vérifie les arguments et les fichiers avant leur utilisation.
- Prévois aussi un message et un code de retour pour les cas invalides.

**À toi :** quel test différencie un dossier d'un fichier ? Quelle branche exécute `case` pour un mot inconnu ?

[Passer au TP](https://kayasam.github.io/linux-initiation/bash/04-tests-et-conditions/tp)
