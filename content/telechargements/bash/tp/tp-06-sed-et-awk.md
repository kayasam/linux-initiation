# TP 06 — La boutique du terminal : sed et awk

> Chapitre associé : [06 — sed et awk](https://kayasam.github.io/linux-initiation/bash/06-sed-et-awk/)

---

## Mission

Une boutique te confie son inventaire. Tu dois corriger des libellés, filtrer les produits et calculer les stocks avec `sed` et `awk`. Toutes les commandes s'exécutent dans Bash sur ta VM Debian.

## Partie A — Préparer les données

**A1.** Crée ton espace de travail et colle tout ce bloc :

```bash
mkdir -p ~/scripting/tp06
cd ~/scripting/tp06
cat > stock.csv <<'EOF'
produit;categorie;quantite;prix
clavier;informatique;8;25
souris;informatique;12;15
cahier;papeterie;20;3
ecran;informatique;4;180
stylo;papeterie;30;2
EOF
```

**A2.** Affiche le fichier et identifie le séparateur, l'en-tête et les quatre colonnes. Combien y a-t-il de produits ?

## Partie B — Transformer avec sed

**B1.** Affiche l'inventaire en remplaçant toutes les occurrences de `informatique` par `materiel`. Le fichier original doit rester intact.

> Indice : `sed 's/ancien/nouveau/g' fichier`

**B2.** Sauvegarde ce résultat dans un nouveau fichier `stock-corrige.csv`. Vérifie les deux fichiers pour prouver que l'original n'a pas changé.

**B3.** Avec `sed`, affiche uniquement les lignes 2 à 4 de `stock.csv`.

> Indice : `-n` masque l'affichage automatique ; `2,4p` affiche la plage demandée.

## Partie C — Analyser avec awk

**C1.** Affiche le nom et la quantité de chaque produit, sans l'en-tête.

> Indices : `-F ';'` choisit le séparateur, `NR > 1` ignore l'en-tête, `$1` désigne la première colonne.

**C2.** Affiche uniquement les produits dont la quantité est strictement inférieure à 10.

**C3.** Calcule le nombre total d'articles en additionnant les quantités. Attendu : **74**.

> Indice : accumule avec `total += $3`, puis affiche dans `END`.

**C4.** Calcule la valeur totale du stock : somme de `quantité × prix`. Attendu : **1220**.

## Bonus — Le rapport du responsable

Produis un fichier `rapport.txt` contenant le nom et la valeur du stock pour chaque produit, puis une dernière ligne donnant le total. Utilise `awk` et une redirection.

## Contrôle de mission

- Explique la différence entre afficher une transformation et modifier le fichier d'origine.
- Montre le filtre des stocks faibles et les deux totaux.
- Explique le rôle de `-F`, `NR`, `$3` et `END`.

Tu peux conserver les fichiers de cet exercice dans `~/scripting/tp06`.

[← Revenir au cours](https://kayasam.github.io/linux-initiation/bash/06-sed-et-awk/)
