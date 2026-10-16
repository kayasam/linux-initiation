---
title: "TP de synthèse — Le rapport de mission Orion — Corrigév2"
aliases: ["bash/ateliers/tp-synthese-corrigev2"]
---

<nav class="chapter-resources workshop-resources" aria-label="Ressources de l’atelier" data-workshop-key="bash/annexe/tp-synthese"><div class="resource-buttons"><a class="resource-button" href="https://kayasam.github.io/linux-initiation/bash/annexe/tp-synthese"><span class="resource-icon"><svg class="resource-symbol" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M8 3h8l4 4v14H4V3h4Z"/><path d="M14 3v5h6M8 12h8M8 16h6"/></svg></span><span class="resource-label">Énoncé</span></a><a class="resource-button" href="https://kayasam.github.io/linux-initiation/bash/annexe/tp-synthese-corrigev2" aria-current="page"><span class="resource-icon"><svg class="resource-symbol" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="m5 12 4 4L19 6"/></svg></span><span class="resource-label">Corrigé v2</span></a></div><div class="resource-actions"><a class="resource-download" href="https://kayasam.github.io/linux-initiation/telechargements/bash/tp/tp-synthese-corrigev2.md" download aria-label="Télécharger ce support en Markdown">↓ Télécharger .md</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>

> Essaie chaque question avant de cliquer sur **Afficher la correction**. Chaque réponse s’ouvre et se referme indépendamment.

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

> [!success]- Afficher la correction — A1
> Colle tout le bloc de l’énoncé. Le marqueur `EOF` doit être seul sur sa ligne. Tu obtiens `donnees/equipe.txt` et `donnees/stock.csv`, sans modifier de fichier système.

**A2.** Vérifie les deux fichiers. Tu dois retrouver trois personnes et cinq produits, plus l'en-tête de l'inventaire.

> [!success]- Afficher la correction — A2
> ```bash
> cat donnees/equipe.txt
> cat donnees/stock.csv
> ```
>
> L’équipage contient **3 personnes**, dont `Mila Vega` sur une seule ligne. L’inventaire contient **5 produits**, plus son en-tête.

## Partie B — Le début du programme

Crée `mission.sh` dans nano.

**B1.** Ajoute le shebang. Le script accepte zéro ou un argument : le nom de la mission, avec `Orion` par défaut. Refuse plus d'un argument avec un message d'utilisation et le code 2.

> [!success]- Afficher la correction — B1
> ```bash
> #!/usr/bin/env bash
> if [[ "$#" -gt 1 ]]; then
>     echo "Usage : $0 [nom-mission]" >&2
>     exit 2
> fi
> mission="${1:-Orion}"
> ```
>
> Place ce début dans `mission.sh`. Les guillemets conservent un nom de mission composé.

**B2.** Vérifie séparément que `donnees/equipe.txt` et `donnees/stock.csv` sont des fichiers lisibles. Si un fichier manque, explique lequel et termine avec le code 2.

> [!success]- Afficher la correction — B2
> ```bash
> if [[ ! -f donnees/equipe.txt || ! -r donnees/equipe.txt ]]; then
>     echo 'Equipage absent ou illisible' >&2
>     exit 2
> fi
> if [[ ! -f donnees/stock.csv || ! -r donnees/stock.csv ]]; then
>     echo 'Inventaire absent ou illisible' >&2
>     exit 2
> fi
> ```
>
> Ajoute ces deux gardes avant la lecture des données. Chaque message indique précisément le fichier en cause.

**B3.** Crée le dossier `rapports`. Si la création échoue, termine avec le code 1.

**Point de contrôle :** vérifie la syntaxe. Ne produis pas encore le rapport tant que ces gardes ne sont pas en place.

> [!success]- Afficher la correction — B3
> ```bash
> if ! mkdir -p rapports; then
>     echo 'Creation du dossier rapports impossible' >&2
>     exit 1
> fi
> ```
>
> Le code 1 signale un échec de création. Vérifie ensuite la syntaxe avec `bash -n mission.sh`.

## Partie C — Construire le rapport

Le rapport sera écrit dans `rapports/mission.txt`. Il remplace le rapport précédent ; les données d'entrée restent dans un autre dossier.

**C1.** Écris un titre contenant le nom de la mission et la date obtenue avec `date +%F`.

> [!success]- Afficher la correction — C1
> ```bash
> printf 'MISSION %s — %s\n' "$mission" "$(date +%F)" > rapports/mission.txt
> ```
>
> `>` initialise le rapport ; il sera remplacé au prochain lancement. Dans la version complète C5, cette sortie est regroupée avec les suivantes dans un seul bloc redirigé.

**C2.** Parcours l'équipage avec une boucle de lecture. Affiche une ligne par personne et compte les personnes. Ne découpe pas `Mila Vega`.

> [!success]- Afficher la correction — C2
> ```bash
> {
>     printf '\nEQUIPAGE\n'
>     personnes=0
>     while IFS= read -r personne || [[ -n "$personne" ]]; do
>         printf -- '- %s\n' "$personne"
>         personnes=$((personnes + 1))
>     done < donnees/equipe.txt
>     printf 'Personnes : %s\n' "$personnes"
> } >> rapports/mission.txt
> ```
>
> `IFS= read -r` conserve les lignes et les noms composés. Le second test conserve aussi une dernière ligne sans retour final. `>>` ajoute ce bloc au titre existant.

**C3.** Avec `awk`, calcule les quantités et la valeur totale de l'inventaire, sans l'en-tête.

> [!success]- Afficher la correction — C3
> ```bash
> {
>     printf '\nINVENTAIRE\n'
>     awk -F ';' 'NR > 1 { articles += $3; valeur += $3 * $4 } END { print "Articles :", articles; print "Valeur :", valeur }' donnees/stock.csv
> } >> rapports/mission.txt
> ```
>
> `NR > 1` ignore l’en-tête. `$3` contient la quantité et `$4` le prix. Résultats : **74 articles**, **1220** de valeur.

**C4.** Ajoute les produits dont la quantité est inférieure à 10.

> Indice : tu peux regrouper plusieurs commandes entre `{` et `}` puis rediriger tout leur résultat. Dans le cours, tu as aussi vu comment initialiser avec `>` puis ajouter avec `>>` : cette solution est acceptée.

> [!success]- Afficher la correction — C4
> ```bash
> {
>     printf '\nSTOCKS FAIBLES\n'
>     awk -F ';' 'NR > 1 && $3 < 10 { print $1, $3 }' donnees/stock.csv
> } >> rapports/mission.txt
> ```
>
> Les lignes retenues sont **`clavier 8`** et **`ecran 4`**.

**C5.** En cas de réussite, affiche le chemin du rapport, puis son contenu.

> [!success]- Afficher la correction — C5
> ```bash
> echo 'Rapport cree : rapports/mission.txt'
> cat rapports/mission.txt
> ```
>
> Ces commandes montrent le résultat après une écriture réussie. Voici une **version complète de `mission.sh`** qui regroupe C1 à C4 et vérifie la redirection du rapport :
>
> ```bash
> #!/usr/bin/env bash
>
> if [[ "$#" -gt 1 ]]; then
>     echo "Usage : $0 [nom-mission]" >&2
>     exit 2
> fi
> mission="${1:-Orion}"
>
> if [[ ! -f donnees/equipe.txt || ! -r donnees/equipe.txt ]]; then
>     echo 'Equipage absent ou illisible' >&2
>     exit 2
> fi
> if [[ ! -f donnees/stock.csv || ! -r donnees/stock.csv ]]; then
>     echo 'Inventaire absent ou illisible' >&2
>     exit 2
> fi
> if ! mkdir -p rapports; then
>     echo 'Creation du dossier rapports impossible' >&2
>     exit 1
> fi
>
> if {
>     printf 'MISSION %s — %s\n' "$mission" "$(date +%F)"
>     printf '\nEQUIPAGE\n'
>     personnes=0
>     while IFS= read -r personne || [[ -n "$personne" ]]; do
>         printf -- '- %s\n' "$personne"
>         personnes=$((personnes + 1))
>     done < donnees/equipe.txt
>     printf 'Personnes : %s\n' "$personnes"
>     printf '\nINVENTAIRE\n'
>     awk -F ';' 'NR > 1 { articles += $3; valeur += $3 * $4 } END { print "Articles :", articles; print "Valeur :", valeur }' donnees/stock.csv
>     printf '\nSTOCKS FAIBLES\n'
>     awk -F ';' 'NR > 1 && $3 < 10 { print $1, $3 }' donnees/stock.csv
> } > rapports/mission.txt; then
>     echo 'Rapport cree : rapports/mission.txt'
>     cat rapports/mission.txt
> else
>     echo 'Ecriture du rapport impossible' >&2
>     exit 1
> fi
> ```
>
> Les variantes avec `>` puis `>>` sont acceptées. Les entrées restent séparées du rapport et ne sont pas écrasées.

## Partie D — La recette de livraison

**D1.** Lance le programme depuis `~/atelier-bash/synthese`, sans argument, puis avec `"Orion Nord"`.

> [!success]- Afficher la correction — D1
> ```bash
> bash -n mission.sh
> chmod +x mission.sh
> ./mission.sh
> ./mission.sh "Orion Nord"
> ```
>
> Sans argument, le titre utilise `Orion`. Le second lancement conserve le nom composé `Orion Nord`. La date est celle de ton système.

**D2.** Vérifie dans le rapport :

| Information | Résultat attendu |
|---|---|
| Équipage | Mila Vega, Noe, Sami |
| Personnes | 3 |
| Articles | 74 |
| Valeur | 1220 |
| Stocks faibles | clavier 8 ; ecran 4 |

> [!success]- Afficher la correction — D2
> Le rapport contient `Mila Vega`, `Noe`, `Sami`, **3 personnes**, **74 articles**, une valeur de **1220**, puis les stocks faibles `clavier 8` et `ecran 4`.

**D3.** Pour tester l'erreur de fichier, renomme temporairement **dans cet atelier** `donnees/equipe.txt` en `donnees/equipe-attente.txt`. Lance le script : il doit renvoyer 2. Remets immédiatement le nom initial, puis relance le cas valide.

> [!success]- Afficher la correction — D3
> ```bash
> mv donnees/equipe.txt donnees/equipe-attente.txt
> ./mission.sh
> echo "Code sans equipage : $?"
> mv donnees/equipe-attente.txt donnees/equipe.txt
> ./mission.sh
> ```
>
> Le lancement sans fichier renvoie **2**, puis le cas valide fonctionne à nouveau. Ces renommages ne concernent que les données fictives de cet atelier.

**D4.** Vérifie que les deux fichiers de données contiennent toujours leur contenu original.

> [!success]- Afficher la correction — D4
> ```bash
> cat donnees/equipe.txt
> cat donnees/stock.csv
> ```
>
> Les trois personnes et les cinq produits sont toujours présents. Le programme lit ces fichiers ; seule la sortie `rapports/mission.txt` est remplacée.

## Bonus — Éviter de répéter les titres

Crée une fonction `titre` qui affiche un titre de section. Réutilise-la pour l'équipage et l'inventaire. Le rapport final doit garder les mêmes informations.

> [!success]- Afficher la correction — Bonus
> ```bash
> titre() {
>     printf '\n%s\n' "$1"
> }
> ```
>
> Définis la fonction **avant** le bloc du rapport. Remplace ensuite `printf '\nEQUIPAGE\n'` par `titre EQUIPAGE`, et fais de même avec `titre INVENTAIRE`. Les informations du rapport restent identiques.

## Livraison

Montre le script, le rapport et les essais au formateur. Explique une variable, une condition, une boucle et le programme `awk` de ton choix.

[← Énoncé du TP](https://kayasam.github.io/linux-initiation/bash/annexe/tp-synthese)
