---
title: "TP de synthèse — Le rapport de mission Orion"
aliases: ["bash/ateliers/tp-synthese"]
---

<nav class="chapter-resources workshop-resources" aria-label="Ressources de l’atelier" data-workshop-key="bash/annexe/tp-synthese"><div class="resource-buttons"><a class="resource-button" href="https://kayasam.github.io/linux-initiation/bash/annexe/tp-synthese" aria-current="page"><span class="resource-icon"><svg class="resource-symbol" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M8 3h8l4 4v14H4V3h4Z"/><path d="M14 3v5h6M8 12h8M8 16h6"/></svg></span><span class="resource-label">Énoncé</span></a><a class="resource-button" href="https://kayasam.github.io/linux-initiation/bash/annexe/tp-synthese-corrigev2"><span class="resource-icon"><svg class="resource-symbol" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="m5 12 4 4L19 6"/></svg></span><span class="resource-label">Afficher les corrections</span></a></div><div class="resource-actions"><a class="resource-download" href="https://kayasam.github.io/linux-initiation/telechargements/bash/tp/tp-synthese.md" download aria-label="Télécharger ce support en Markdown">↓ Télécharger .md</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>

## Mission

La relève arrive. Ton programme doit préparer un rapport avec l'équipage, l'inventaire et les stocks faibles. Tu vas réutiliser les six chapitres, sans commande d'administration ni accès à des fichiers système.

Travaille dans Bash sur Debian. Pour chaque étape : écris une petite partie, vérifie avec `bash -n`, puis teste le résultat.

## Partie A — Préparer les données

**A1.** Colle le bloc complet :

```bash
mkdir -p ~/atelier-bash/synthese/donnees
cd ~/atelier-bash/synthese
printf 'Mila Vega\nNoe\nSami\n' > donnees/equipe.txt
cat > donnees/stock.csv <<'EOF'
produit;categorie;quantite;prix
clavier;informatique;8;25
souris;informatique;12;15
cahier;papeterie;20;3
ecran;informatique;4;180
stylo;papeterie;30;2
EOF
```

**A2.** Vérifie les deux fichiers. Tu dois retrouver trois personnes et cinq produits, plus l'en-tête de l'inventaire.

## Partie B — Le début du programme

Crée `mission.sh` dans nano.

**B1.** Ajoute le shebang. Le script accepte zéro ou un argument : le nom de la mission, avec `Orion` par défaut. Refuse plus d'un argument avec un message d'utilisation et le code 2.

**B2.** Vérifie séparément que `donnees/equipe.txt` et `donnees/stock.csv` sont des fichiers lisibles. Si un fichier manque, explique lequel et termine avec le code 2.

**B3.** Crée le dossier `rapports`. Si la création échoue, termine avec le code 1.

**Point de contrôle :** vérifie la syntaxe. Ne produis pas encore le rapport tant que ces gardes ne sont pas en place.

## Partie C — Construire le rapport

Le rapport sera écrit dans `rapports/mission.txt`. Il remplace le rapport précédent ; les données d'entrée restent dans un autre dossier.

**C1.** Écris un titre contenant le nom de la mission et la date obtenue avec `date +%F`.

**C2.** Parcours l'équipage avec une boucle de lecture. Affiche une ligne par personne et compte les personnes. Ne découpe pas `Mila Vega`.

**C3.** Avec `awk`, calcule les quantités et la valeur totale de l'inventaire, sans l'en-tête.

**C4.** Ajoute les produits dont la quantité est inférieure à 10.

> Indice : tu peux regrouper plusieurs commandes entre `{` et `}` puis rediriger tout leur résultat. Dans le cours, tu as aussi vu comment initialiser avec `>` puis ajouter avec `>>` : cette solution est acceptée.

**C5.** En cas de réussite, affiche le chemin du rapport, puis son contenu.

## Partie D — La recette de livraison

**D1.** Lance le programme depuis `~/atelier-bash/synthese`, sans argument, puis avec `"Orion Nord"`.

**D2.** Vérifie dans le rapport :

| Information | Résultat attendu |
|---|---|
| Équipage | Mila Vega, Noe, Sami |
| Personnes | 3 |
| Articles | 74 |
| Valeur | 1220 |
| Stocks faibles | clavier 8 ; ecran 4 |

**D3.** Pour tester l'erreur de fichier, renomme temporairement **dans cet atelier** `donnees/equipe.txt` en `donnees/equipe-attente.txt`. Lance le script : il doit renvoyer 2. Remets immédiatement le nom initial, puis relance le cas valide.

**D4.** Vérifie que les deux fichiers de données contiennent toujours leur contenu original.

## Bonus — Éviter de répéter les titres

Crée une fonction `titre` qui affiche un titre de section. Réutilise-la pour l'équipage et l'inventaire. Le rapport final doit garder les mêmes informations.

## Livraison

Montre le script, le rapport et les essais au formateur. Explique une variable, une condition, une boucle et le programme `awk` de ton choix.

[Correction du TP](https://kayasam.github.io/linux-initiation/bash/annexe/tp-synthese-corrigev2)

[← Parcours Bash](https://kayasam.github.io/linux-initiation/#bash)

<a href="https://kayasam.github.io/linux-initiation/telechargements/bash/tp/tp-synthese.md" download>Télécharger le TP en Markdown</a>
