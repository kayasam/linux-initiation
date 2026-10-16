---
title: "TP 06"
---

# TP 06 — Préparer le ravitaillement d'Orion *(avancé)*

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="bash/06-sed-et-awk" style="--resource-count:4"><div class="resource-buttons"><a class="resource-button resource-markdown" data-resource-kind="markdown" aria-label="Cours — Lire le cours en Markdown" href="https://kayasam.github.io/linux-initiation/bash/06-sed-et-awk/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg></span><span class="resource-label">Cours<small>Lire le cours en Markdown</small></span></a><a class="resource-button resource-html" data-resource-kind="html" aria-label="HTML — Explorer le chapitre" href="https://kayasam.github.io/linux-initiation/bash/06-sed-et-awk/html/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 28 32"><path d="M2 2h24l-2 25-10 3-10-3Z" fill="#e44d26"/><path d="M14 5v22l7-2 2-20Z" fill="#f16529"/><path d="M7 8h15l-.3 3H11l.3 3h10l-.8 9-6.5 2-6.5-2-.4-5h3l.2 2.6 3.7 1 3.7-1 .3-3.6H8Z" fill="#fff"/></svg></span><span class="resource-label">HTML<small>Explorer le chapitre</small></span></a><a class="resource-button resource-quiz" data-resource-kind="quiz" aria-label="Quiz — 20 questions" href="https://kayasam.github.io/linux-initiation/bash/06-sed-et-awk/quiz/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="4" y="3" width="24" height="26" rx="6" fill="#7652ad"/><path d="M12 12a4 4 0 1 1 6 3.5c-1.5.8-2 1.4-2 3" fill="none" stroke="#fff" stroke-width="2.8" stroke-linecap="round"/><circle cx="16" cy="23" r="1.6" fill="#fff"/></svg></span><span class="resource-label">Quiz<small>20 questions</small></span></a><a class="resource-button resource-tp" data-resource-kind="tp" aria-label="TP — Mettre en pratique" href="https://kayasam.github.io/linux-initiation/bash/06-sed-et-awk/tp"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg></span><span class="resource-label">TP<small>Mettre en pratique</small></span></a></div><div class="resource-actions"><a class="resource-download" href="https://kayasam.github.io/linux-initiation/telechargements/bash/cours/06-sed-et-awk.md" download aria-label="Télécharger le cours en Markdown"><span aria-hidden="true">↓</span> Télécharger .md</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>

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

[← Parcours Bash](https://kayasam.github.io/linux-initiation/#bash)

<a href="https://kayasam.github.io/linux-initiation/telechargements/bash/tp/tp-06-sed-et-awk.md" download>Télécharger le TP en Markdown</a>
