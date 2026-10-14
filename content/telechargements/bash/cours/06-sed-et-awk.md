# Chapitre 06 — sed et awk

> [name=Samuel GUILLARD <sguillard@jehann.fr>]
> [time=2026-04-28]

[TOC]

---

## 1. Pourquoi sed et awk ?

`grep` cherche des lignes. `sed` et `awk` vont plus loin : ils **transforment** le texte.

| Outil | Rôle principal | Cas d'usage typique |
|-------|---------------|---------------------|
| `grep` | Filtrer des lignes | Trouver les lignes contenant "error" |
| `sed` | Modifier du texte | Remplacer un mot, supprimer des lignes |
| `awk` | Extraire et calculer | Afficher la 3e colonne, calculer une somme |

Ces trois outils se combinent naturellement avec les tubes `|`.

---

## 2. sed — l'éditeur de flux

`sed` (*Stream EDitor*) lit un fichier **ligne par ligne** et applique des transformations. Il n'ouvre jamais de fenêtre — tout se passe dans le terminal.

> [!WARNING]
> Par défaut, **sed n'écrit pas dans le fichier** — il affiche le résultat sur la sortie standard. Le fichier original est intact.
### La commande essentielle : substitution `s`

C'est de loin la commande la plus utilisée de sed.

```bash
sed 's/ancien/nouveau/g' fichier.txt
```

| Partie | Signification |
|--------|--------------|
| `s` | substitute — remplacer |
| `ancien` | le texte à chercher |
| `nouveau` | le texte de remplacement |
| `g` | global — remplacer **toutes** les occurrences (sans `g` : seulement la 1ère par ligne) |

**Exemples concrets :**

```bash
# Remplacer "http" par "https" dans un fichier de config
sed 's/http/https/g' config.txt

# Remplacer "erreur" par "error" (insensible à la casse avec I)
sed 's/erreur/error/gI' application.log

# Supprimer un mot (remplacer par rien)
sed 's/DEBUG: //g' app.log

# Remplacer uniquement sur les lignes contenant "serveur"
sed '/serveur/s/localhost/192.168.1.10/g' config.txt
```

### Sauvegarder les modifications

```bash
# Voir le résultat sans toucher au fichier
sed 's/ancien/nouveau/g' fichier.txt

# Sauvegarder dans un nouveau fichier
sed 's/ancien/nouveau/g' fichier.txt > fichier_modifie.txt

# Modifier le fichier directement (-i = in place)
sed -i 's/ancien/nouveau/g' fichier.txt

# Modifier en gardant une sauvegarde (.bak)
sed -i.bak 's/ancien/nouveau/g' fichier.txt
```

### Supprimer des lignes : commande `d`

```bash
# Supprimer les lignes contenant "DEBUG"
sed '/DEBUG/d' app.log

# Supprimer les lignes vides
sed '/^$/d' fichier.txt

# Supprimer les commentaires (lignes commençant par #)
sed '/^#/d' config.conf

# Supprimer les commentaires ET les lignes vides
sed -e '/^#/d' -e '/^$/d' config.conf
```

> [!NOTE]
> `^` = début de ligne, `$` = fin de ligne. `/^$/` = ligne vide (début suivi immédiatement de la fin).
### Afficher certaines lignes : commande `p` avec `-n`

```bash
# -n supprime l'affichage automatique, p affiche explicitement
sed -n '/ERROR/p' app.log         # affiche seulement les lignes ERROR
sed -n '5,10p' fichier.txt        # affiche les lignes 5 à 10
sed -n '1p' fichier.txt           # affiche uniquement la 1ère ligne
sed -n '$p' fichier.txt           # affiche uniquement la dernière ligne
```

### Exemples pratiques

```bash
# Nettoyer un fichier de config : retirer commentaires et lignes vides
sed -e '/^#/d' -e '/^$/d' /etc/ssh/sshd_config

# Changer le port SSH dans sshd_config
sed -i 's/^Port 22$/Port 2222/' /etc/ssh/sshd_config

# Extraire les erreurs d'un log
sed -n '/ERROR/p' /var/log/app.log

# Afficher le fichier sans la première ligne (en-tête)
sed '1d' donnees.csv

# Remplacer les séparateurs virgule par point-virgule dans un CSV
sed 's/,/;/g' fichier.csv
```

---

## 3. awk — le traiteur de colonnes

`awk` lit un fichier **ligne par ligne** et découpe chaque ligne en **champs** selon un séparateur. C'est l'outil idéal pour extraire des colonnes et faire des calculs.

Le nom vient des initiales de ses trois créateurs : **A**ho, **W**einberger, **K**ernighan (Bell Labs, années 1970).

### Principe de base

```bash
awk '{action}' fichier
awk -F'séparateur' '{action}' fichier
```

Chaque ligne est découpée en champs numérotés : `$1`, `$2`, `$3`…

```
root:x:0:0:root:/root:/bin/bash
 $1  $2 $3 $4  $5      $6       $7
```

### Variables intégrées utiles

| Variable | Contenu |
|----------|---------|
| `$0` | La ligne entière |
| `$1`, `$2`… | Le 1er champ, le 2e champ… |
| `NR` | Numéro de la ligne en cours (*Number of Record*) |
| `NF` | Nombre de champs dans la ligne (*Number of Fields*) |
| `FS` | Séparateur de champs (*Field Separator*) — défaut : espace/tabulation |

### Exemples concrets

```bash
# Afficher le 1er champ de /etc/passwd (noms d'utilisateurs)
awk -F: '{print $1}' /etc/passwd

# Afficher le 1er et le 7e champ (nom + shell)
awk -F: '{print $1, $7}' /etc/passwd

# Afficher avec un format personnalisé
awk -F: '{print "Utilisateur : " $1 " → shell : " $7}' /etc/passwd

# Afficher le numéro de ligne devant chaque ligne
awk '{print NR, $0}' fichier.txt

# Afficher la dernière colonne (peu importe combien il y en a)
awk '{print $NF}' fichier.txt
```

### Filtrer avec une condition

```bash
# Afficher les lignes où le 3e champ vaut "Informatique"
awk -F'|' '$3 == "Informatique" {print $0}' employes.txt

# Afficher les lignes où le salaire (4e champ) dépasse 50000
awk -F'|' '$4 > 50000 {print $1, $4}' employes.txt

# Filtrer par motif (comme grep, mais avec accès aux champs)
awk '/ERROR/ {print $0}' app.log

# Combiner condition et motif
awk -F: '$3 >= 1000 {print $1}' /etc/passwd    # utilisateurs avec UID ≥ 1000
```

### BEGIN et END

`BEGIN` s'exécute **avant** de lire le fichier (utile pour les en-têtes et l'initialisation).
`END` s'exécute **après** le dernier enregistrement (utile pour les totaux).

```bash
# Compter les lignes d'un fichier
awk 'BEGIN {n=0} {n++} END {print "Total : " n " lignes"}' fichier.txt

# Calculer la somme d'une colonne
awk -F'|' '{total += $4} END {print "Masse salariale : " total}' employes.txt

# Afficher un en-tête, puis les données, puis un pied
awk -F: 'BEGIN {print "=== Utilisateurs ==="} {print $1} END {print "=== Fin ==="}' /etc/passwd
```

### Comparaison sed vs awk

| Tâche | sed | awk |
|-------|-----|-----|
| Remplacer du texte | `sed 's/a/b/g'` | Possible mais sed est plus simple |
| Supprimer des lignes | `sed '/motif/d'` | `awk '!/motif/'` |
| Extraire une colonne | Compliqué | `awk '{print $2}'` |
| Calculer une somme | Impossible | `awk '{s+=$1} END{print s}'` |
| Filtrer et transformer | Les deux combinés avec `\|` | En une seule commande |

> [!TIP]
> En pratique : utilise **sed** pour modifier du texte (remplacer, supprimer), et **awk** pour extraire des colonnes et faire des calculs. Les deux se combinent très bien avec des tubes.
---

## 4. Exemples combinés

```bash
# Extraire les utilisateurs bash et afficher leur UID
grep '/bin/bash' /etc/passwd | awk -F: '{print $1, $3}'

# Nettoyer un CSV puis calculer la somme de la 4e colonne
sed '/^#/d' employes.csv | awk -F, '{total += $4} END {print total}'

# Afficher les 5 processus qui consomment le plus de CPU
ps aux | sort -k3 -rn | awk 'NR<=5 {print $1, $3"%", $11}'

# Compter les erreurs par type dans un log
awk '/ERROR/ {print $3}' app.log | sort | uniq -c | sort -rn
```

---

## Récapitulatif des commandes

| Commande | Description |
|----------|-------------|
| `sed 's/a/b/g' fichier` | Remplace `a` par `b` (toutes occurrences) |
| `sed 's/a/b/' fichier` | Remplace la 1ère occurrence par ligne |
| `sed -i 's/a/b/g' fichier` | Modifie le fichier directement |
| `sed -i.bak 's/a/b/g' fichier` | Idem avec sauvegarde `.bak` |
| `sed '/motif/d' fichier` | Supprime les lignes contenant le motif |
| `sed '/^#/d' fichier` | Supprime les commentaires |
| `sed '/^$/d' fichier` | Supprime les lignes vides |
| `sed -n '/motif/p' fichier` | Affiche seulement les lignes contenant le motif |
| `sed -n '5,10p' fichier` | Affiche les lignes 5 à 10 |
| `awk '{print $1}' fichier` | Affiche le 1er champ (séparateur = espace) |
| `awk -F: '{print $1}' fichier` | Idem avec `:` comme séparateur |
| `awk -F: '{print $1, $3}'` | Affiche plusieurs champs |
| `awk 'NR==5'` | Affiche uniquement la ligne 5 |
| `awk '$3 > 100'` | Affiche les lignes où le 3e champ > 100 |
| `awk '{s+=$1} END{print s}'` | Calcule la somme du 1er champ |
| `awk 'BEGIN{} {} END{}'` | Structure complète avec initialisation et bilan |

---

> [!NOTE]
> ### À retenir
> 
> - `sed` traite le texte ligne par ligne sans ouvrir d'éditeur — le fichier original est **inchangé** sauf avec `-i`.
> - La commande `s/ancien/nouveau/g` est la plus utilisée de sed : substitution globale sur chaque ligne.
> - `sed '/motif/d'` supprime les lignes correspondantes ; `sed -n '/motif/p'` n'affiche que celles-là.
> - `awk` découpe chaque ligne en champs (`$1`, `$2`…) selon un séparateur défini avec `-F`.
> - `NR` = numéro de ligne, `NF` = nombre de champs, `$NF` = dernier champ.
> - `BEGIN {}` s'exécute avant le fichier, `END {}` après — idéal pour en-têtes et totaux.
> - En pratique : `sed` pour modifier/nettoyer du texte, `awk` pour extraire des colonnes et calculer.
---

> [!TIP]
> **TP associé** → `tp-06-sed-et-awk.md`
