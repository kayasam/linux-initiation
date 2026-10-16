# TP 06 bis — sed et awk pas à pas

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

**A2.** Affiche-le :

```bash
cat stock.csv
```

**A3.** Réponds par écrit, en regardant l'affichage :

- Quel caractère sépare les colonnes ?
- Combien y a-t-il de colonnes ?
- Combien y a-t-il de lignes en tout ? Et combien de **produits** ?
- Dans la ligne `clavier;informatique;8;25`, que représente le `25` ?

**A4.** Compte les lignes pour vérifier ta réponse :

```bash
wc -l stock.csv
```

---

## Partie B — sed : remplacer du texte

**B1.** Remplace un mot :

```bash
sed 's/informatique/materiel/' stock.csv
```

Attendu : les trois lignes `informatique` affichent maintenant `materiel`.

**B2.** Vérifie que le fichier n'a pas bougé :

```bash
cat stock.csv
```

`informatique` est toujours là. **`sed` a affiché un résultat, il n'a rien écrit.**

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

**B4.** Pour garder un résultat, redirige-le vers un **autre** fichier :

```bash
sed 's/informatique/materiel/g' stock.csv > stock-corrige.csv
cat stock-corrige.csv
cat stock.csv
```

Deux fichiers différents : le corrigé et l'original.

> [!WARNING] Jamais le même nom des deux côtés
> `sed 's/.../.../' stock.csv > stock.csv` **vide** le fichier. Le shell prépare la destination avant que `sed` ait pu lire. Utilise toujours un nom différent.

---

## Partie C — sed : choisir des lignes

**C1.** Affiche une ligne précise :

```bash
sed -n '2p' stock.csv
```

Attendu : uniquement `clavier;informatique;8;25`.

**C2.** Retire l'option `-n` et relance :

```bash
sed '2p' stock.csv
```

La ligne 2 apparaît **deux fois**. Pourquoi ? Par défaut `sed` affiche chaque ligne qu'il lit ; `p` en demande une de plus. L'option `-n` coupe l'affichage automatique, et il ne reste que ce que `p` demande.

**C3.** Affiche une plage de lignes :

```bash
sed -n '2,4p' stock.csv
```

Attendu : clavier, souris, cahier.

**C4.** Retire l'en-tête :

```bash
sed '1d' stock.csv
```

Attendu : les cinq produits, sans la ligne `produit;categorie;quantite;prix`.

**C5.** Retire les lignes qui contiennent un mot :

```bash
sed '/papeterie/d' stock.csv
```

Attendu : l'en-tête et les trois produits informatiques.

> [!NOTE] Les trois actions de base
> `p` affiche (avec `-n`), `d` supprime de l'affichage, `s///` remplace. Devant chacune, on peut mettre un **numéro de ligne** (`1d`), une **plage** (`2,4p`) ou un **motif entre slashs** (`/papeterie/d`).

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

**D2.** Change le numéro. Affiche la 2ᵉ, puis la 4ᵉ colonne :

```bash
awk -F ';' '{ print $2 }' stock.csv
awk -F ';' '{ print $4 }' stock.csv
```

**D3.** Affiche deux colonnes à la fois. La virgule met un espace entre elles :

```bash
awk -F ';' '{ print $1, $3 }' stock.csv
```

**D4.** `$0` est un cas spécial : la ligne entière.

```bash
awk -F ';' '{ print $0 }' stock.csv
```

**D5.** Oublie volontairement le `-F` :

```bash
awk '{ print $1 }' stock.csv
```

Toute la ligne sort dans `$1`. Sans `-F`, `awk` découpe sur les **espaces** — et il n'y en a aucun ici. C'est l'oubli n°1 avec `awk`.

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

---

## Partie E — awk : choisir des lignes

Jusqu'ici, le bloc `{ }` s'appliquait à toutes les lignes. On peut mettre une **condition devant** : `awk 'condition { action }'`.

**E1.** Saute l'en-tête :

```bash
awk -F ';' 'NR > 1 { print $1, $3 }' stock.csv
```

Attendu : les cinq produits, sans la ligne `produit quantite`.

**E2.** Compare avec la version sans condition (D3) : c'est la seule différence.

**E3.** Garde une seule catégorie :

```bash
awk -F ';' '$2 == "papeterie" { print $1 }' stock.csv
```

Attendu : `cahier` et `stylo`. Le `==` teste l'égalité ; le texte cherché est entre **guillemets doubles**, à l'intérieur des guillemets simples.

**E4.** Garde les quantités faibles. `&&` signifie « et » :

```bash
awk -F ';' 'NR > 1 && $3 < 10 { print $1, $3 }' stock.csv
```

Attendu : `clavier 8` et `ecran 4`.

---

## Partie F — awk : calculer

**F1.** Additionne les quantités. `total += $3` veut dire « ajoute `$3` à `total` » :

```bash
awk -F ';' 'NR > 1 { total += $3 } END { print total }' stock.csv
```

Attendu : **74**.

`END { }` est un bloc spécial : il s'exécute **une seule fois**, après la dernière ligne. C'est là qu'on affiche un résultat global.

**F2.** Contrairement à Bash, `awk` n'a pas besoin de `total=0` au départ : une variable inconnue vaut 0 dès qu'on calcule avec.

**F3.** Calcule la valeur du stock : quantité × prix.

```bash
awk -F ';' 'NR > 1 { total += $3 * $4 } END { print total }' stock.csv
```

Attendu : **1220**.

**F4.** Affiche aussi le détail, ligne par ligne, avant le total :

```bash
awk -F ';' 'NR > 1 { print $1, $3 * $4 }' stock.csv
```

Attendu : 200, 180, 60, 720, 60. Vérifie que leur somme fait bien 1220.

---

## Partie G — Le piège à connaître

**G1.** Refais le calcul de F1 **sans** la condition `NR > 1` :

```bash
awk -F ';' '{ total += $3 } END { print total }' stock.csv
```

**G2.** Quel résultat obtiens-tu ? Est-ce le bon ? Comment l'expliques-tu, alors que l'en-tête a bien été lu ?

**G3.** Vérifie ton hypothèse :

```bash
echo 'quantite' | awk '{ print $1 + 0 }'
```

**G4.** Conclusion à écrire avec tes mots : ici, oublier `NR > 1` ne change pas le résultat. Est-ce une raison pour s'en passer ?

---

## Bonus — Enchaîner les deux outils

**H1.** `sed` retire l'en-tête, `awk` calcule ce qu'il reçoit :

```bash
sed '1d' stock.csv | awk -F ';' '{ total += $3 } END { print total }'
```

Attendu : 74, comme en F1.

**H2.** Pourquoi le programme `awk` n'a-t-il plus besoin de `NR > 1` ici ?

---

## Mission accomplie si…

- Tu sais dire ce que font `-n`, `p`, `d`, `s///` et le flag `g`.
- Tu sais expliquer `-F`, `$1`, `$0`, `NR` et `END` avec tes mots.
- Tu obtiens **74** et **1220**.
- Tu sais pourquoi `sed` et `awk` n'ont pas abîmé `stock.csv`.

> Tu es à l'aise ? Enchaîne avec le [TP 06 — Préparer le ravitaillement](https://kayasam.github.io/linux-initiation/bash/06-sed-et-awk/tp/tp-06-sed-et-awk), qui ajoute les rapports, les délimiteurs et la modification sur place.

[← Revenir au cours](https://kayasam.github.io/linux-initiation/bash/06-sed-et-awk/)
