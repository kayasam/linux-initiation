---
title: "06. Traiter du texte avec sed et awk"
---

# Chapitre 06 — Traiter du texte avec sed et awk

> [!TIP] Ressources du chapitre
> - [Version HTML](https://kayasam.github.io/linux-initiation/bash/cours/06-sed-et-awk-interactif.html)
> - <a href="https://kayasam.github.io/linux-initiation/telechargements/bash/cours/06-sed-et-awk.md" download>Télécharger le cours en Markdown</a>
> - [Faire le quiz — 20 questions](https://kayasam.github.io/linux-initiation/bash/cours/quiz/06-sed-et-awk.html)
> - [Passer au TP](https://kayasam.github.io/linux-initiation/bash/06-sed-et-awk/tp)


> [!NOTE] Objectif
> Transformer un fichier texte, sélectionner des colonnes et calculer un total, sans modifier l'original par erreur.

**À connaître :** `sed 's/.../.../g'`, `sed -n`, `awk -F`, `$1`, `NR`, `END`.
---

## 1. Choisir l'outil selon la tâche

| Besoin | Outil |
|---|---|
| Garder des lignes contenant un mot | `grep` |
| Remplacer un mot ou sélectionner des lignes | `sed` |
| Lire des champs et calculer | `awk` |

Les trois outils lisent le texte. **Par défaut, ils ne changent pas le fichier lu.** Ils envoient un résultat sur leur sortie standard.

## 2. Préparer un petit inventaire

Dans Bash sur Debian, colle le bloc complet jusqu'à `EOF` :

```bash
mkdir -p ~/atelier-bash/texte
cd ~/atelier-bash/texte
cat > stock.csv <<'EOF'
produit;categorie;quantite;prix
clavier;informatique;8;25
souris;informatique;12;15
cahier;papeterie;20;3
ecran;informatique;4;180
stylo;papeterie;30;2
EOF
```

`<<'EOF'` fournit les lignes suivantes à `cat`, sans interpréter leur contenu. `>` écrit le résultat dans `stock.csv`. La dernière ligne `EOF` doit être seule.

Ce fichier utilise `;` pour séparer quatre champs. La première ligne est un en-tête. C'est un format simple : aucun champ ne contient de point-virgule ni de saut de ligne. Le `awk` de ce cours ne remplace pas un lecteur CSV capable de traiter tous les cas de champs entre guillemets.

![Une ligne découpée en quatre champs](https://kayasam.github.io/linux-initiation/bash/images/bash-06-colonnes.svg)

## 3. Remplacer du texte avec sed

```bash
sed 's/informatique/materiel/g' stock.csv
```

Lis l'expression de gauche à droite :

| Partie | Rôle |
|---|---|
| `s` | Substitution |
| `informatique` | Texte recherché dans cet exemple |
| `materiel` | Texte de remplacement |
| `g` | Toutes les occurrences sur chaque ligne |

Les guillemets simples protègent l'expression du shell. La recherche de `sed` utilise des expressions régulières ; ici, nous cherchons un mot sans caractère spécial.

Pour conserver le résultat :

```bash
sed 's/informatique/materiel/g' stock.csv > stock-corrige.csv
cat stock-corrige.csv
cat stock.csv
```

Le nouveau fichier contient `materiel`. L'original contient toujours `informatique`.

> [!WARNING] Deux noms de fichiers différents
> N'écris jamais `sed ... stock.csv > stock.csv`. Le shell viderait le fichier de destination avant que `sed` puisse le lire.

## 4. Choisir ou retirer des lignes

```bash
sed -n '2,4p' stock.csv
```

`-n` coupe l'affichage automatique ; `2,4p` affiche les lignes 2 à 4 incluses. Tu obtiens clavier, souris et cahier.

```bash
sed '1d' stock.csv
```

`1d` retire la première ligne de la **sortie**. Le fichier n'est pas modifié.

```bash
sed '/papeterie/d' stock.csv
```

Ce dernier exemple retire de la sortie les lignes contenant `papeterie`.

## 5. Lire les champs avec awk

```bash
awk -F ';' 'NR > 1 { print $1, $3 }' stock.csv
```

- `-F ';'` fixe le séparateur de champs.
- `NR` est le numéro de la ligne en cours.
- `NR > 1` saute l'en-tête.
- `$1` est le produit, `$3` sa quantité.
- `{ print ... }` est l'action exécutée pour les lignes sélectionnées.

Résultat :

```text
clavier 8
souris 12
cahier 20
ecran 4
stylo 30
```

Les `$1` et `$3` appartiennent ici à **awk**, pas à Bash : les guillemets simples empêchent Bash de les remplacer.

## 6. Filtrer avec une condition

```bash
awk -F ';' 'NR > 1 && $3 < 10 { print $1, $3 }' stock.csv
```

La ligne doit être après l'en-tête **et** sa quantité doit être inférieure à 10. Résultat : `clavier 8`, puis `ecran 4`.

## 7. Calculer un total

```bash
awk -F ';' 'NR > 1 { total += $3 } END { print total }' stock.csv
```

À chaque produit, `total += $3` ajoute sa quantité. Après la dernière ligne, `END` affiche la somme. Résultat : **74 articles**.

Pour calculer la valeur de l'inventaire :

```bash
awk -F ';' 'NR > 1 { total += $3 * $4 } END { print total }' stock.csv
```

Chaque quantité est multipliée par son prix unitaire. Résultat : **1220**.

Le `END` de `awk` n'est pas le `done` d'une boucle Bash : nous utilisons deux langages différents, chacun avec sa syntaxe.

## 8. Relier deux outils

```bash
sed '1d' stock.csv | awk -F ';' '{ total += $3 } END { print total }'
```

`sed` retire l'en-tête, puis le tube transmet les produits à `awk`. On retrouve 74. C'est une autre façon de faire ; le `awk` précédent suffit quand il sait filtrer lui-même l'en-tête.

## Pour aller plus loin : modifier avec une sauvegarde

Travaille d'abord sur une copie :

```bash
cp stock.csv stock-test.csv
sed -i.bak 's/informatique/materiel/g' stock-test.csv
cat stock-test.csv
cat stock-test.csv.bak
```

Sur Debian, `-i.bak` modifie `stock-test.csv` et conserve l'ancienne version dans `stock-test.csv.bak`. Ce comportement est celui de GNU sed ; ne suppose pas que les options sont identiques sur tous les systèmes.

## À retenir

- `sed` transforme ou sélectionne du texte ; `awk` travaille bien avec des champs.
- Identifie le séparateur et l'en-tête avant de calculer.
- Regarde d'abord le résultat, puis écris dans un nouveau fichier.

**À toi :** que désigne `$4` dans notre inventaire ? Pourquoi utilisons-nous `NR > 1` ? Pourquoi des guillemets simples autour du programme `awk` ?

[Passer au TP](https://kayasam.github.io/linux-initiation/bash/06-sed-et-awk/tp)

[← Parcours Bash](https://kayasam.github.io/linux-initiation/#bash) · [Tous les TP Bash](https://kayasam.github.io/linux-initiation/bash/tp/)
