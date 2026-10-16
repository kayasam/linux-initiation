# TP 01 — Installer la station Orion — Corrigév2

> Essaie chaque question avant de cliquer sur **Afficher la correction**. Chaque réponse s’ouvre et se referme indépendamment.

> Chapitre associé : [01 — Le shell et son environnement](https://kayasam.github.io/linux-initiation/bash/01-shell-et-environnement/)

## Mission

Tu arrives à la station Orion. Prépare ton poste, crée le journal de bord et trouve le message radio. Tu travailles dans **Bash sur Debian**, après ta connexion SSH.

## Partie A — Trouver ton poste

**A1.** Affiche ton compte, le nom de la machine et ton dossier courant. Note les trois résultats.

> Indice : les trois commandes sont au début du cours.

> [!success]- Afficher la correction — A1
> ```bash
> whoami
> hostname
> pwd
> ```
>
> Sur la VM de référence : `stagiaire`, `debian` et normalement `/home/stagiaire` à la connexion. Les résultats dépendent de ton compte, de ta machine et du dossier courant.

**A2.** Prépare ce dossier de mission :

```bash
mkdir -p ~/atelier-bash/01-orion/messages
cd ~/atelier-bash/01-orion
pwd
```

Explique `~`, `-p` et le résultat de `pwd`.

> [!success]- Afficher la correction — A2
> `~` désigne ton dossier personnel. `mkdir -p` crée les dossiers parents manquants et accepte les dossiers déjà présents. Après le `cd`, `pwd` affiche un chemin se terminant par `/atelier-bash/01-orion`.

**A3.** Entre dans `messages`, vérifie où tu es, puis reviens au dossier `01-orion`. Utilise `cd`, `pwd` et `..`.

**Point de contrôle :** tu es revenu dans `~/atelier-bash/01-orion`.

> [!success]- Afficher la correction — A3
> ```bash
> cd messages
> pwd
> cd ..
> pwd
> ```
>
> Le premier chemin se termine par `/01-orion/messages`. `..` désigne le parent : le second chemin se termine par `/01-orion`.

## Partie B — Ouvrir le journal de bord

**B1.** Crée le journal :

```bash
echo "ORION : poste ouvert" > journal.txt
```

> [!success]- Afficher la correction — B1
> ```bash
> echo "ORION : poste ouvert" > journal.txt
> ```
>
> `>` crée le fichier ou remplace son contenu existant.

**B2.** Avec `>>`, ajoute deux lignes : `Radio : OK` et `Reserve : OK`.

> [!success]- Afficher la correction — B2
> ```bash
> echo "Radio : OK" >> journal.txt
> echo "Reserve : OK" >> journal.txt
> ```
>
> `>>` ajoute chaque ligne à la fin sans effacer la première.

**B3.** Affiche le journal. Il doit contenir exactement :

```text
ORION : poste ouvert
Radio : OK
Reserve : OK
```

> [!success]- Afficher la correction — B3
> ```bash
> cat journal.txt
> ```
>
> Tu dois retrouver les trois lignes de l’énoncé, dans le même ordre.

**B4.** Liste les fichiers avec les détails. Quel caractère de la commande `ls -l` demande cet affichage ?

> [!success]- Afficher la correction — B4
> ```bash
> ls -l
> ```
>
> C’est l’option `-l` : la lettre est un L minuscule. Elle demande l’affichage détaillé.

## Partie C — Recevoir un message

**C1.** Crée le fichier radio :

```bash
echo "INFO : depart a 09h" > messages/radio.txt
echo "SECRET : suivre Vega" >> messages/radio.txt
echo "INFO : ciel degage" >> messages/radio.txt
```

> [!success]- Afficher la correction — C1
> ```bash
> echo "INFO : depart a 09h" > messages/radio.txt
> echo "SECRET : suivre Vega" >> messages/radio.txt
> echo "INFO : ciel degage" >> messages/radio.txt
> ```
>
> La première ligne initialise le fichier ; les suivantes s’ajoutent à la fin.

**C2.** Affiche seulement la ligne contenant `SECRET`, avec `grep`.

> [!success]- Afficher la correction — C2
> ```bash
> grep SECRET messages/radio.txt
> ```
>
> Résultat : `SECRET : suivre Vega`. Les autres lignes ne sont pas affichées.

**C3.** Refais le même filtre avec deux commandes reliées par un tube. Explique le rôle du tube.

> [!success]- Afficher la correction — C3
> ```bash
> cat messages/radio.txt | grep SECRET
> ```
>
> Le tube `|` transmet la sortie standard de `cat` à l’entrée standard de `grep`. On obtient le même résultat qu’en C2.

**C4.** Vérifie que les trois lignes du fichier radio sont toujours présentes.

> [!success]- Afficher la correction — C4
> ```bash
> cat messages/radio.txt
> ```
>
> Les trois lignes sont toujours présentes. `grep` filtre l’affichage ; il ne modifie pas le fichier.

## Partie D — La cabine du sous-shell

**D1.** Vérifie quel programme se cache derrière `/bin/sh`, puis affiche le nom de ton shell actuel. Utilise les commandes du cours : sont-ils identiques sur cette VM ?

> [!success]- Afficher la correction — D1
> ```bash
> readlink -f /bin/sh
> ps -p $$ -o comm=
> ```
>
> Sur la VM de référence, les résultats sont `/usr/bin/dash` et `bash`. `/bin/sh` pointe donc vers Dash, alors que ta session utilise Bash.

**D2.** Depuis `01-orion`, affiche ton dossier. Exécute ensuite `cd messages` et `pwd` dans un groupe entre parenthèses, comme au cours.

> [!success]- Afficher la correction — D2
> ```bash
> pwd
> (
>     cd messages
>     pwd
> )
> ```
>
> Le premier chemin se termine par `/01-orion`. Dans les parenthèses, il se termine par `/01-orion/messages`.

**D3.** Une fois le groupe terminé, relance `pwd`. Es-tu resté dans `messages` ? Explique pourquoi.

**Point de contrôle :** tu es toujours dans `01-orion` ; seule la cabine du sous-shell s'est déplacée.

> [!success]- Afficher la correction — D3
> ```bash
> pwd
> ```
>
> Tu es revenu dans `01-orion`. Le groupe entre parenthèses s’exécute dans un sous-shell : son changement de dossier ne change pas celui du shell parent.

## Bonus — Le dossier au nom piégeux

Crée un dossier nommé `journal de bord` puis entre dedans. Il faut le considérer comme **un seul nom** : entoure-le de guillemets doubles. Reviens ensuite à `01-orion`.

> [!success]- Afficher la correction — Bonus
> ```bash
> mkdir -p "journal de bord"
> cd "journal de bord"
> pwd
> cd ..
> ```
>
> Les guillemets conservent `journal de bord` comme un seul argument. Le dernier `cd ..` ramène dans `01-orion`.

## Mission accomplie si…

- Tu retrouves ton dossier sans fermer la connexion.
- Ton journal contient les trois lignes attendues.
- Tu as trouvé le message secret sans modifier le fichier radio.
- Tu expliques la différence entre `>` et `>>`.

Conserve tes fichiers : aucune suppression n'est demandée.

[← Énoncé du TP](https://kayasam.github.io/linux-initiation/bash/01-shell-et-environnement/tp)
