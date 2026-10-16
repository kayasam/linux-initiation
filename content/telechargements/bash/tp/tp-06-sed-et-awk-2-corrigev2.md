# TP 06 bis — sed et awk pas à pas — Corrigév2

> Essaie chaque question avant de cliquer sur **Afficher la correction**. Les réponses s’ouvrent et se referment indépendamment.

> Chapitre associé : [06 — sed et awk](https://kayasam.github.io/linux-initiation/bash/06-sed-et-awk/)

## Mission

Tu apprends à lire et transformer un fichier de données. On avance **une commande à la fois**, en observant le résultat à chaque étape. Aucun script à écrire : tout se tape dans le terminal.

> [!TIP] Comment travailler ce TP
> Chaque étape affiche son **résultat attendu**. Compare avec ton écran avant de continuer. Si ça diffère, c'est presque toujours une apostrophe ou un point-virgule mal placé.

> [!NOTE] Rassure-toi tout de suite
> `sed` et `awk` **ne modifient jamais le fichier** qu'ils lisent. Ils affichent un résultat, c'est tout. Tu peux te tromper autant que tu veux : `stock.csv` sera toujours intact. Une seule exception, vue tout à la fin du TP avancé.

---

## Partie A — Regarder les données

**A1.** Crée ton atelier et le fichier de travail. Colle le bloc **entier**, jusqu'au `EOF` final :

```bash
mkdir -p ~/atelier-bash/06bis
cd ~/atelier-bash/06bis
cat > stock.csv <<'EOF'
produit;categorie;quantite;prix
clavier;informatique;8;25
souris;informatique;12;15
cahier;papeterie;20;3
ecran;informatique;4;180
stylo;papeterie;30;2
EOF
```

> [!success]- Afficher la correction — A1
> Colle le bloc complet de l’énoncé, jusqu’au `EOF` seul sur sa ligne. Tu obtiens `stock.csv` avec un en-tête et cinq produits dans ton atelier.

**A2.** Affiche-le :

```bash
cat stock.csv
```

> [!success]- Afficher la correction — A2
> ```bash
> cat stock.csv
> ```
>
> Tu retrouves les six lignes du bloc de départ, sans changement.

**A3.** Réponds par écrit, en regardant l'affichage :

- Quel caractère sépare les colonnes ?
- Combien y a-t-il de colonnes ?
- Combien y a-t-il de lignes en tout ? Et combien de **produits** ?
- Dans la ligne `clavier;informatique;8;25`, que représente le `25` ?

> [!success]- Afficher la correction — A3
> Le séparateur est le point-virgule `;`. Il y a **4 colonnes**, **6 lignes**, dont **1 en-tête et 5 produits**. `25` est le prix **unitaire** d’un clavier ; la valeur du stock de claviers est 8 × 25 = 200.

**A4.** Compte les lignes pour vérifier ta réponse :

```bash
wc -l stock.csv
```

> [!success]- Afficher la correction — A4
> ```bash
> wc -l stock.csv
> ```
>
> Résultat : **6 stock.csv**. `wc -l` compte les retours à la ligne ; le bloc de départ en ajoute un à chaque ligne, y compris la dernière.

---

## Partie B — sed : remplacer du texte

**B1.** Remplace un mot :

```bash
sed 's/informatique/materiel/' stock.csv
```

Attendu : les trois lignes `informatique` affichent maintenant `materiel`.

> [!success]- Afficher la correction — B1
> ```bash
> sed 's/informatique/materiel/' stock.csv
> ```
>
> Les trois occurrences, chacune sur une ligne différente, deviennent `materiel` dans l’affichage.

**B2.** Vérifie que le fichier n'a pas bougé :

```bash
cat stock.csv
```

`informatique` est toujours là. **`sed` a affiché un résultat, il n'a rien écrit.**

> [!success]- Afficher la correction — B2
> ```bash
> cat stock.csv
> ```
>
> Le mot `informatique` est toujours présent trois fois. Sans modification sur place, `sed` écrit son résultat sur la sortie standard.

**B3.** Maintenant, observe la différence que fait le `g`. Travaille sur une seule ligne :

```bash
echo 'stylo;papeterie;30;2' | sed 's/;/ - /'
echo 'stylo;papeterie;30;2' | sed 's/;/ - /g'
```

Attendu :

```text
stylo - papeterie;30;2
stylo - papeterie - 30 - 2
```

Note la règle avec tes mots : sans `g`, `sed` remplace ……… par ligne ; avec `g`, il remplace ……… .

> [!success]- Afficher la correction — B3
> ```bash
> echo 'stylo;papeterie;30;2' | sed 's/;/ - /'
> echo 'stylo;papeterie;30;2' | sed 's/;/ - /g'
> ```
>
> Sans `g` : **première occurrence par ligne**, soit `stylo - papeterie;30;2`. Avec `g` : **toutes les occurrences par ligne**, soit `stylo - papeterie - 30 - 2`.

**B4.** Pour garder un résultat, redirige-le vers un **autre** fichier :

```bash
sed 's/informatique/materiel/g' stock.csv > stock-corrige.csv
cat stock-corrige.csv
cat stock.csv
```

Deux fichiers différents : le corrigé et l'original.

> [!WARNING] Jamais le même nom des deux côtés
> `sed 's/.../.../' stock.csv > stock.csv` **vide** le fichier. Le shell prépare la destination avant que `sed` ait pu lire. Utilise toujours un nom différent.

> [!success]- Afficher la correction — B4
> ```bash
> sed 's/informatique/materiel/g' stock.csv > stock-corrige.csv
> cat stock-corrige.csv
> cat stock.csv
> ```
>
> Le résultat est conservé dans **un autre fichier**. `stock.csv` contient toujours trois occurrences d’`informatique`.
>
> Ne redirige jamais cette lecture vers `stock.csv` lui-même : le shell viderait la destination avant que `sed` la lise.

---

## Partie C — sed : choisir des lignes

**C1.** Affiche une ligne précise :

```bash
sed -n '2p' stock.csv
```

Attendu : uniquement `clavier;informatique;8;25`.

> [!success]- Afficher la correction — C1
> ```bash
> sed -n '2p' stock.csv
> ```
>
> Seule la ligne `clavier;informatique;8;25` est affichée.

**C2.** Retire l'option `-n` et relance :

```bash
sed '2p' stock.csv
```

La ligne 2 apparaît **deux fois**. Pourquoi ? Par défaut `sed` affiche chaque ligne qu'il lit ; `p` en demande une de plus. L'option `-n` coupe l'affichage automatique, et il ne reste que ce que `p` demande.

> [!success]- Afficher la correction — C2
> ```bash
> sed '2p' stock.csv
> ```
>
> Tu obtiens **7 lignes affichées** : les 6 lignes automatiquement affichées, plus une seconde copie de la ligne du clavier demandée par `p`. `-n` supprime l’affichage automatique.

**C3.** Affiche une plage de lignes :

```bash
sed -n '2,4p' stock.csv
```

Attendu : clavier, souris, cahier.

> [!success]- Afficher la correction — C3
> ```bash
> sed -n '2,4p' stock.csv
> ```
>
> La plage inclut les lignes 2 et 4 : clavier, souris, cahier. `-n` désactive l’affichage automatique ; `p` affiche la sélection.

**C4.** Retire l'en-tête :

```bash
sed '1d' stock.csv
```

Attendu : les cinq produits, sans la ligne `produit;categorie;quantite;prix`.

> [!success]- Afficher la correction — C4
> ```bash
> sed '1d' stock.csv
> ```
>
> L’affichage contient les cinq produits, sans en-tête. `d` supprime cette ligne du flux affiché ; le fichier source reste intact.

**C5.** Retire les lignes qui contiennent un mot :

```bash
sed '/papeterie/d' stock.csv
```

Attendu : l'en-tête et les trois produits informatiques.

> [!NOTE] Les trois actions de base
> `p` affiche (avec `-n`), `d` supprime de l'affichage, `s///` remplace. Devant chacune, on peut mettre un **numéro de ligne** (`1d`), une **plage** (`2,4p`) ou un **motif entre slashs** (`/papeterie/d`).

> [!success]- Afficher la correction — C5
> ```bash
> sed '/papeterie/d' stock.csv
> ```
>
> Il reste l’en-tête, clavier, souris et ecran : **4 lignes**. Le motif retire de l’affichage les lignes contenant `papeterie`.

---

## Partie D — awk : découvrir les colonnes

`awk` ne travaille pas sur du texte en vrac : il découpe chaque ligne en **champs numérotés**.

**D1.** Première commande, sans rien de compliqué :

```bash
awk -F ';' '{ print $1 }' stock.csv
```

Attendu :

```text
produit
clavier
souris
cahier
ecran
stylo
```

`-F ';'` dit : « les colonnes sont séparées par des `;` ». `$1` est la première colonne. Le bloc entre `{ }` est exécuté **une fois par ligne**.

> [!success]- Afficher la correction — D1
> ```bash
> awk -F ';' '{ print $1 }' stock.csv
> ```
>
> Résultat : produit, clavier, souris, cahier, ecran, stylo, un par ligne. `-F` choisit le séparateur ; `$1` désigne le premier champ. L’en-tête est encore traité.

**D2.** Change le numéro. Affiche la 2ᵉ, puis la 4ᵉ colonne :

```bash
awk -F ';' '{ print $2 }' stock.csv
awk -F ';' '{ print $4 }' stock.csv
```

> [!success]- Afficher la correction — D2
> ```bash
> awk -F ';' '{ print $2 }' stock.csv
> awk -F ';' '{ print $4 }' stock.csv
> ```
>
> La colonne 2 affiche categorie, informatique, informatique, papeterie, informatique, papeterie. La colonne 4 affiche prix, 25, 15, 3, 180, 2.

**D3.** Affiche deux colonnes à la fois. La virgule met un espace entre elles :

```bash
awk -F ';' '{ print $1, $3 }' stock.csv
```

> [!success]- Afficher la correction — D3
> ```bash
> awk -F ';' '{ print $1, $3 }' stock.csv
> ```
>
> Résultat : produit quantite, clavier 8, souris 12, cahier 20, ecran 4, stylo 30. La virgule insère un espace ; sans elle, `$1 $3` concaténerait les champs.

**D4.** `$0` est un cas spécial : la ligne entière.

```bash
awk -F ';' '{ print $0 }' stock.csv
```

> [!success]- Afficher la correction — D4
> ```bash
> awk -F ';' '{ print $0 }' stock.csv
> ```
>
> La sortie est identique à `cat stock.csv`. `$0` représente l’enregistrement complet, avec ses séparateurs.

**D5.** Oublie volontairement le `-F` :

```bash
awk '{ print $1 }' stock.csv
```

Toute la ligne sort dans `$1`. Sans `-F`, `awk` découpe sur les **espaces** — et il n'y en a aucun ici. C'est l'oubli n°1 avec `awk`.

> [!success]- Afficher la correction — D5
> ```bash
> awk '{ print $1 }' stock.csv
> ```
>
> Sans `-F`, le séparateur par défaut traite les espaces et tabulations. Il n’y en a pas dans ces lignes : chaque ligne entière tient dans `$1`, et `$2` est vide.

**D6.** `NR` est le numéro de la ligne en cours. Rends-le visible :

```bash
awk -F ';' '{ print NR, $1 }' stock.csv
```

Attendu :

```text
1 produit
2 clavier
3 souris
4 cahier
5 ecran
6 stylo
```

`NR` n'a pas de `$` : ce n'est pas une colonne, c'est un compteur qu'`awk` tient tout seul.

> [!success]- Afficher la correction — D6
> ```bash
> awk -F ';' '{ print NR, $1 }' stock.csv
> ```
>
> Résultat : 1 produit, 2 clavier, 3 souris, 4 cahier, 5 ecran, 6 stylo. `NR` est le compteur d’enregistrements, sans `$`. Ici, chaque enregistrement est une ligne.

---

## Partie E — awk : choisir des lignes

Jusqu'ici, le bloc `{ }` s'appliquait à toutes les lignes. On peut mettre une **condition devant** : `awk 'condition { action }'`.

**E1.** Saute l'en-tête :

```bash
awk -F ';' 'NR > 1 { print $1, $3 }' stock.csv
```

Attendu : les cinq produits, sans la ligne `produit quantite`.

> [!success]- Afficher la correction — E1
> ```bash
> awk -F ';' 'NR > 1 { print $1, $3 }' stock.csv
> ```
>
> Les cinq produits sont affichés avec leur quantité. `NR > 1` écarte l’en-tête ; la virgule insère un espace.

**E2.** Compare avec la version sans condition (D3) : c'est la seule différence.

> [!success]- Afficher la correction — E2
> Par rapport à D3, seule la ligne **produit quantite** a disparu. `NR > 1` exclut le premier enregistrement, qui contient l’en-tête.

**E3.** Garde une seule catégorie :

```bash
awk -F ';' '$2 == "papeterie" { print $1 }' stock.csv
```

Attendu : `cahier` et `stylo`. Le `==` teste l'égalité ; le texte cherché est entre **guillemets doubles**, à l'intérieur des guillemets simples.

> [!success]- Afficher la correction — E3
> ```bash
> awk -F ';' '$2 == "papeterie" { print $1 }' stock.csv
> ```
>
> Résultat : **cahier**, puis **stylo**. `==` compare exactement le champ 2 à la chaîne `papeterie`, protégée par des guillemets doubles à l’intérieur du programme entre apostrophes.

**E4.** Garde les quantités faibles. `&&` signifie « et » :

```bash
awk -F ';' 'NR > 1 && $3 < 10 { print $1, $3 }' stock.csv
```

Attendu : `clavier 8` et `ecran 4`.

> [!success]- Afficher la correction — E4
> ```bash
> awk -F ';' 'NR > 1 && $3 < 10 { print $1, $3 }' stock.csv
> ```
>
> Résultat : **clavier 8**, puis **ecran 4**.
>
> On garde `NR > 1` pour exclure explicitement l’en-tête. Attention : `$3 < 10` est une **comparaison**, pas une addition. Un champ textuel comme `quantite` n’est pas systématiquement converti en 0 dans cette comparaison ; il ne faut pas confondre comparaison et conversion arithmétique.

---

## Partie F — awk : calculer

**F1.** Additionne les quantités. `total += $3` veut dire « ajoute `$3` à `total` » :

```bash
awk -F ';' 'NR > 1 { total += $3 } END { print total }' stock.csv
```

Attendu : **74**.

`END { }` est un bloc spécial : il s'exécute **une seule fois**, après la dernière ligne. C'est là qu'on affiche un résultat global.

> [!success]- Afficher la correction — F1
> ```bash
> awk -F ';' 'NR > 1 { total += $3 } END { print total }' stock.csv
> ```
>
> Résultat : **74**. Le total est affiché une seule fois, après la dernière ligne.
>
> Détail : 8 + 12 + 20 + 4 + 30 = 74. `END` s’exécute après la lecture de toutes les lignes.

**F2.** Contrairement à Bash, `awk` n'a pas besoin de `total=0` au départ : une variable inconnue vaut 0 dès qu'on calcule avec.

> [!success]- Afficher la correction — F2
> Une variable `awk` non initialisée se comporte comme **0 dans un calcul** et comme une chaîne vide dans un contexte textuel. La première opération `total += $3` peut donc démarrer l’accumulation sans `total=0` préalable.

**F3.** Calcule la valeur du stock : quantité × prix.

```bash
awk -F ';' 'NR > 1 { total += $3 * $4 } END { print total }' stock.csv
```

Attendu : **1220**.

> [!success]- Afficher la correction — F3
> ```bash
> awk -F ';' 'NR > 1 { total += $3 * $4 } END { print total }' stock.csv
> ```
>
> Résultat : **1220** = 200 + 180 + 60 + 720 + 60.

**F4.** Affiche aussi le détail, ligne par ligne, avant le total :

```bash
awk -F ';' 'NR > 1 { print $1, $3 * $4 }' stock.csv
```

Attendu : 200, 180, 60, 720, 60. Vérifie que leur somme fait bien 1220.

> [!success]- Afficher la correction — F4
> ```bash
> awk -F ';' 'NR > 1 { print $1, $3 * $4 }' stock.csv
> ```
>
> Résultat : clavier 200, souris 180, cahier 60, ecran 720, stylo 60. Leur somme vaut **1220**.

---

## Partie G — Le piège à connaître

**G1.** Refais le calcul de F1 **sans** la condition `NR > 1` :

```bash
awk -F ';' '{ total += $3 } END { print total }' stock.csv
```

> [!success]- Afficher la correction — G1
> ```bash
> awk -F ';' '{ total += $3 } END { print total }' stock.csv
> ```
>
> Résultat : **74**, malgré la lecture de l’en-tête.

**G2.** Quel résultat obtiens-tu ? Est-ce le bon ? Comment l'expliques-tu, alors que l'en-tête a bien été lu ?

> [!success]- Afficher la correction — G2
> Le total est bien 74 sur ce fichier : dans **l’addition**, le texte `quantite` est converti en 0. On a donc ajouté 0 à la somme des cinq produits. Cela masque l’absence de filtre.

**G3.** Vérifie ton hypothèse :

```bash
echo 'quantite' | awk '{ print $1 + 0 }'
```

> [!success]- Afficher la correction — G3
> ```bash
> echo 'quantite' | awk '{ print $1 + 0 }'
> ```
>
> Résultat : **0**. L’opération `+ 0` force ici une conversion arithmétique du texte non numérique.

**G4.** Conclusion à écrire avec tes mots : ici, oublier `NR > 1` ne change pas le résultat. Est-ce une raison pour s'en passer ?

> [!success]- Afficher la correction — G4
> Non : conserve `NR > 1`. Le résultat est correct ici parce que l’en-tête textuel ajoute 0. Avec un en-tête contenant `2024` dans le champ 3, le même calcul donnerait **2098** au lieu de 74. Le filtre exprime « je traite les données, pas l’en-tête ».

---

## Bonus — Enchaîner les deux outils

**H1.** `sed` retire l'en-tête, `awk` calcule ce qu'il reçoit :

```bash
sed '1d' stock.csv | awk -F ';' '{ total += $3 } END { print total }'
```

Attendu : 74, comme en F1.

> [!success]- Afficher la correction — H1
> ```bash
> sed '1d' stock.csv | awk -F ';' '{ total += $3 } END { print total }'
> ```
>
> Résultat : **74**. Le tube transmet la sortie de `sed` à l’entrée d’`awk`.

**H2.** Pourquoi le programme `awk` n'a-t-il plus besoin de `NR > 1` ici ?

> [!success]- Afficher la correction — H2
> `sed` a déjà retiré le premier enregistrement. `awk` reçoit uniquement les cinq lignes de produits : il n’a plus d’en-tête à exclure. La version avec `awk` seul et `NR > 1` reste aussi correcte.

---

## Mission accomplie si…

- Tu sais dire ce que font `-n`, `p`, `d`, `s///` et le flag `g`.
- Tu sais expliquer `-F`, `$1`, `$0`, `NR` et `END` avec tes mots.
- Tu obtiens **74** et **1220**.
- Tu sais pourquoi `sed` et `awk` n'ont pas abîmé `stock.csv`.

> Tu es à l'aise ? Enchaîne avec le [TP 06 — Préparer le ravitaillement](https://kayasam.github.io/linux-initiation/bash/06-sed-et-awk/tp/tp-06-sed-et-awk), qui ajoute les rapports, les délimiteurs et la modification sur place.

[← Énoncé du TP](https://kayasam.github.io/linux-initiation/bash/06-sed-et-awk/tp/tp-06-sed-et-awk-2)
