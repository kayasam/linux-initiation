# TP 06 — Préparer le ravitaillement d'Orion

> Chapitre associé : [06 — sed et awk](https://kayasam.github.io/linux-initiation/bash/06-sed-et-awk/)

## Mission

Le cargo de ravitaillement arrive. Corrige l'inventaire, repère les stocks faibles et annonce sa valeur totale. Les données sont fictives et tous les calculs utilisent des entiers.

## Partie A — Recevoir l'inventaire

**A1.** Colle le bloc complet :

```bash
mkdir -p ~/atelier-bash/06-stock
cd ~/atelier-bash/06-stock
cat > stock.csv <<'EOF'
produit;categorie;quantite;prix
clavier;informatique;8;25
souris;informatique;12;15
cahier;papeterie;20;3
ecran;informatique;4;180
stylo;papeterie;30;2
EOF
```

**A2.** Affiche le fichier. Repère le séparateur, l'en-tête et les cinq produits. Quel champ contient le prix ?

## Partie B — Corriger les étiquettes

**B1.** Avec `sed`, affiche une version où `informatique` devient `materiel`.

**B2.** Conserve ce résultat dans `stock-corrige.csv`. Vérifie que `stock.csv` contient encore `informatique`.

**B3.** Affiche uniquement les lignes 2 à 4 avec `sed`. Attendu : clavier, souris, cahier.

> Indice : option `-n`, expression `2,4p`.

## Partie C — Faire les comptes

**C1.** Avec `awk`, affiche le nom et la quantité des produits, sans l'en-tête.

**C2.** Garde seulement les quantités inférieures à 10. Attendu : **clavier 8** et **ecran 4**.

**C3.** Calcule le nombre d'articles. Attendu : **74**.

**C4.** Calcule la valeur totale : somme de `quantité × prix`. Attendu : **1220**.

> Indices : `-F ';'` pour les champs, `NR > 1` pour les produits, une variable de total, puis `END`.

## Bonus — Le rapport du responsable

Crée `rapport.txt` avec une ligne par produit donnant son nom et la valeur de son stock. Ajoute une dernière ligne `TOTAL 1220`. Tu peux tout produire avec un seul programme `awk` et une redirection.

**Défi supplémentaire :** sur une copie nommée `stock-test.csv`, utilise `sed -i.bak`. Montre la version corrigée et sa sauvegarde, sans toucher à l'original.

## Mission accomplie si…

Les totaux sont exacts, les deux stocks faibles sont identifiés et l'inventaire original est conservé. Explique le rôle de `NR` et de `END` avec tes mots.

[← Revenir au cours](https://kayasam.github.io/linux-initiation/bash/06-sed-et-awk/)
