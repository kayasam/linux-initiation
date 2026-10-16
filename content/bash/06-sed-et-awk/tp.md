---
title: "TP 06"
---

# TP 06 — Préparer le ravitaillement d'Orion

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="bash/06-sed-et-awk" style="--resource-count:4"><div class="resource-buttons"><a class="resource-button resource-markdown" data-resource-kind="markdown" aria-label="Cours — Lire le cours en Markdown" href="https://kayasam.github.io/linux-initiation/bash/06-sed-et-awk/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg></span><span class="resource-label">Cours<small>Lire le cours en Markdown</small></span></a><a class="resource-button resource-html" data-resource-kind="html" aria-label="HTML — Explorer le chapitre" href="https://kayasam.github.io/linux-initiation/bash/06-sed-et-awk/html/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 28 32"><path d="M2 2h24l-2 25-10 3-10-3Z" fill="#e44d26"/><path d="M14 5v22l7-2 2-20Z" fill="#f16529"/><path d="M7 8h15l-.3 3H11l.3 3h10l-.8 9-6.5 2-6.5-2-.4-5h3l.2 2.6 3.7 1 3.7-1 .3-3.6H8Z" fill="#fff"/></svg></span><span class="resource-label">HTML<small>Explorer le chapitre</small></span></a><a class="resource-button resource-quiz" data-resource-kind="quiz" aria-label="Quiz — 20 questions" href="https://kayasam.github.io/linux-initiation/bash/06-sed-et-awk/quiz/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="4" y="3" width="24" height="26" rx="6" fill="#7652ad"/><path d="M12 12a4 4 0 1 1 6 3.5c-1.5.8-2 1.4-2 3" fill="none" stroke="#fff" stroke-width="2.8" stroke-linecap="round"/><circle cx="16" cy="23" r="1.6" fill="#fff"/></svg></span><span class="resource-label">Quiz<small>20 questions</small></span></a><a class="resource-button resource-tp" data-resource-kind="tp" aria-label="TP — Mettre en pratique" href="https://kayasam.github.io/linux-initiation/bash/06-sed-et-awk/tp"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg></span><span class="resource-label">TP<small>Mettre en pratique</small></span></a></div><div class="resource-actions"><a class="resource-download" href="https://kayasam.github.io/linux-initiation/telechargements/bash/cours/06-sed-et-awk.md" download aria-label="Télécharger le cours en Markdown"><span aria-hidden="true">↓</span> Télécharger .md</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>

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

[← Parcours Bash](https://kayasam.github.io/linux-initiation/#bash)

<a href="https://kayasam.github.io/linux-initiation/telechargements/bash/tp/tp-06-sed-et-awk.md" download>Télécharger le TP en Markdown</a>
