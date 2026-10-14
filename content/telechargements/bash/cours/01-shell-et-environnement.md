# Chapitre 01 — Le shell et son environnement

> [!NOTE] Objectif
> Te repérer dans le terminal, lancer une commande et créer ton espace de travail. Tu n'as encore aucun script à écrire.

**À connaître :** `pwd`, `ls`, `cd`, `mkdir`, `cat`, `printf`, `>`, `>>`, `|`.
---

## 1. Où taper les commandes ?

Depuis **PowerShell sur Windows**, connecte-toi à ta VM :

```powershell
ssh stagiaire@192.168.84.10
```

La suite se déroule dans le terminal **Debian**, après la connexion. Adapte l'adresse si ton formateur t'en donne une autre. Le mot de passe ne s'affiche pas pendant la saisie.

Une ligne semblable à celle-ci attend ta commande :

```text
stagiaire@debian:~$
```

Ne recopie pas cette invite ni le signe `$` : tape seulement la commande.

![Du terminal à la commande exécutée](https://kayasam.github.io/linux-initiation/bash/images/bash-01-terminal.svg)

Le **terminal** est la fenêtre. Le **shell** est le programme qui interprète tes commandes. Ici, ce shell est **Bash**. SSH transporte tes échanges avec la VM.

## 2. Une commande, ses options et ses arguments

```bash
ls -l /tmp
```

| Élément | Ce qu'il demande |
|---|---|
| `ls` | Lister un dossier |
| `-l` | Afficher les détails : c'est une option |
| `/tmp` | Choisir le dossier à lister : c'est un argument |

Une commande se termine quand tu appuies sur **Entrée**. Bash distingue les majuscules et les minuscules : `ls` et `LS` sont deux noms différents.

## 3. Se repérer avant d'agir

```bash
whoami
hostname
pwd
```

- `whoami` : ton compte ; ici, normalement `stagiaire`.
- `hostname` : le nom de la machine distante.
- `pwd` : le dossier où tu travailles ; au départ, normalement `/home/stagiaire`.

Crée un espace réservé à cette formation :

```bash
mkdir -p ~/atelier-bash/decouverte
cd ~/atelier-bash/decouverte
pwd
```

`~` désigne ton dossier personnel. `-p` crée aussi les parents manquants et accepte qu'un dossier existe déjà. `cd` change le dossier courant.

| Chemin | Signification |
|---|---|
| `/home/stagiaire` | Chemin absolu, depuis la racine `/` |
| `decouverte` | Chemin relatif au dossier courant |
| `.` | Dossier courant |
| `..` | Dossier parent |
| `~` | Dossier personnel |

```bash
cd ..
pwd
cd decouverte
```

Tu reviens maintenant dans `~/atelier-bash/decouverte`.

## 4. Écrire puis lire un fichier

```bash
printf 'Station Orion ouverte\n' > journal.txt
cat journal.txt
```

Résultat :

```text
Station Orion ouverte
```

`printf` affiche du texte. `\n` demande un retour à la ligne. Le signe `>` dirige ce texte vers un fichier : **il crée le fichier ou remplace son contenu**.

Pour ajouter une ligne :

```bash
printf 'Radio disponible\n' >> journal.txt
cat journal.txt
```

`>>` ajoute à la fin. Il ne remplace pas les lignes déjà présentes.

> [!WARNING] Avant d'utiliser `>`
> Vérifie le nom du fichier et ton dossier avec `pwd`. Dans le cours, nous écrivons seulement dans notre espace de travail.

## 5. Passer un résultat à une autre commande

```bash
cat journal.txt | grep Radio
```

Le tube `|` transmet la sortie de `cat` à `grep`. `grep` garde les lignes contenant `Radio`. Le fichier d'origine reste intact.

On peut aussi demander directement à `grep` de lire le fichier :

```bash
grep Radio journal.txt
```

Ces deux exemples affichent `Radio disponible`. Le premier montre comment relier deux commandes ; le second est plus court pour ce besoin précis.

## 6. Les raccourcis utiles

| Geste | Effet |
|---|---|
| **Tab** | Complète un nom ; deux appuis peuvent proposer les choix |
| **Flèche haut** | Rappelle une commande précédente |
| **Ctrl+C** | Interrompt la commande en cours |
| **Ctrl+L** | Nettoie l'affichage sans effacer les fichiers |
| `exit` | Ferme la session SSH |

L'aide de `ls` se consulte avec `ls --help`. Pour une commande intégrée à Bash, comme `cd`, utilise `help cd`. Le lecteur `man ls` se quitte avec **q**.

## 7. Pour aller plus loin : un alias temporaire

Un alias donne un raccourci à une commande. Cet exemple agit seulement dans ton shell actuel :

```bash
alias ll='ls -l'
ll
unalias ll
```

Nous ne modifions pas encore les fichiers de configuration du shell. Plus tard, `~/.bashrc` permettra de conserver des réglages pour les shells Bash interactifs qui le lisent.

## À retenir

- Tu tapes dans un terminal ; Bash interprète les commandes sur Debian.
- `pwd` permet de vérifier où tu es avant d'écrire un fichier.
- `>` remplace ; `>>` ajoute ; `|` transmet un résultat.

**À toi :** quelle différence entre `cd ..` et `cd ~` ? Que contient le journal après deux ajouts ?

[Passer au TP](https://kayasam.github.io/linux-initiation/bash/01-shell-et-environnement/tp)
