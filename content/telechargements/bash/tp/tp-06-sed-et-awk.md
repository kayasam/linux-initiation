# TP 06 — Préparer le ravitaillement d'Orion *(avancé)*

> Chapitre associé : [06 — sed et awk](https://kayasam.github.io/linux-initiation/bash/06-sed-et-awk/)
>
> **Prérequis :** le [TP 06 bis — sed et awk pas à pas](https://kayasam.github.io/linux-initiation/bash/06-sed-et-awk/tp/tp-06-sed-et-awk-2). Ce TP-ci suppose acquis `-F`, `$1`, `NR`, `END` et le couple `-n` / `p`.

## Mission

Le cargo de ravitaillement arrive. Corrige l'inventaire, repère les stocks faibles, produis un rapport lisible et annonce la valeur totale. Les données sont fictives et tous les calculs utilisent des entiers.

Ici, les indices sont rares : à toi de retrouver les options.

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

**B3.** Affiche uniquement les lignes 2 à 4. Attendu : clavier, souris, cahier.

**B4.** Le dépôt a déménagé. Crée ce fichier de chemins :

```bash
printf 'deb /etc/apt/sources.list principal\nlog /etc/apt/sources.list archive\n' > chemins.txt
```

Remplace `/etc/apt/` par `/srv/miroir/`. Écris-le **deux fois** : une version avec le délimiteur `/` habituel (en échappant chaque slash du motif), puis une version avec un autre délimiteur. Laquelle relirais-tu dans six mois ?

> Indice : le caractère qui suit le `s` **est** le délimiteur. `s,…,…,` et `s#…#…#` fonctionnent aussi.

## Partie C — Sélectionner avec un motif

**C1.** Affiche la ligne qui **commence** par `clavier`.

**C2.** Affiche la ligne qui **se termine** par `;2`. Attendu : le stylo uniquement.

**C3.** Affiche les lignes dont le produit commence par `c` **ou** par `s`. Attendu : quatre lignes.

**C4.** Refais C1 avec `awk`, en testant la **colonne 1** plutôt que la ligne entière. Explique la différence de comportement entre les deux approches.

> Indices : `^` début de ligne, `$` fin de ligne, `[cs]` l'un de ces caractères, `~` l'opérateur de correspondance d'`awk`.

## Partie D — Faire les comptes

**D1.** Affiche le nom et la quantité des produits, sans l'en-tête.

**D2.** Garde seulement les quantités inférieures à 10. Attendu : **clavier 8** et **ecran 4**.

**D3.** Garde les produits dont le prix unitaire atteint 100 ou plus.

**D4.** Calcule le nombre total d'articles. Attendu : **74**.

**D5.** Calcule la valeur totale du stock : somme de `quantité × prix`. Attendu : **1220**.

**D6.** Combien de champs par ligne ? Fais-le dire à `awk` plutôt que de les compter à l'œil.

> Indice : `NF`.

## Partie E — Produire un rapport lisible

**E1.** Affiche le nom et la valeur de stock de chaque produit, **alignés en colonnes** : le nom cadré à gauche sur 10 caractères, la valeur cadrée à droite sur 6.

> Indice : `printf "%-10s %6d\n", …` — attention, `printf` n'ajoute pas de retour à la ligne tout seul.

**E2.** Calcule la quantité totale **par catégorie**. Attendu : `informatique 24` et `papeterie 50`.

> Indice : un tableau indexé par le nom de la catégorie, puis une boucle `for (cle in tableau)` dans le bloc `END`.

**E3.** L'ordre d'affichage de E2 est-il garanti ? Relance plusieurs fois. Que faudrait-il ajouter pour obtenir un ordre stable ?

## Partie F — Le rapport final et la modification sur place

**F1.** Crée `rapport.txt` avec une ligne par produit (nom et valeur de stock), puis une dernière ligne `TOTAL 1220`. Un seul programme `awk` et une redirection suffisent.

**F2.** Sur une copie nommée `stock-test.csv`, utilise `sed -i.bak` pour appliquer le renommage de B1 **dans le fichier**. Montre la version modifiée et sa sauvegarde, sans jamais toucher à `stock.csv`.

**F3.** Démontre le danger de l'en-tête. Fabrique une copie dont la première ligne est `annee;categorie;2024;prix`, puis compare le total des quantités **avec** et **sans** `NR > 1`. Conclus.

> Indice pour fabriquer la copie : `sed '1s/.*/.../'`.

## Mission accomplie si…

Les totaux sont exacts, les deux stocks faibles sont identifiés, le rapport est aligné, l'inventaire original est conservé — et tu sais expliquer avec tes mots le rôle de `NR`, de `NF`, de `END` et le choix du délimiteur de `sed`.

[← Revenir au cours](https://kayasam.github.io/linux-initiation/bash/06-sed-et-awk/)
