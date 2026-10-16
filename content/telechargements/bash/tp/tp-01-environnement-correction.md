# TP 01 — Correction — Installer la station Orion

> Énoncé : [TP 01](https://kayasam.github.io/linux-initiation/bash/01-shell-et-environnement/tp)

## Partie A — Trouver ton poste

**A1.**

```bash
whoami
hostname
pwd
```

Sur la VM de référence : `stagiaire`, `debian` et normalement `/home/stagiaire` à la connexion.

**A2.**

```bash
mkdir -p ~/atelier-bash/01-orion/messages
cd ~/atelier-bash/01-orion
pwd
```

`~` est le dossier personnel ; `-p` crée les parents manquants. Le chemin se termine par `/atelier-bash/01-orion`.

**A3.**

```bash
cd messages
pwd
cd ..
pwd
```

## Partie B — Ouvrir le journal de bord

**B1 à B3.**

```bash
echo "ORION : poste ouvert" > journal.txt
echo "Radio : OK" >> journal.txt
echo "Reserve : OK" >> journal.txt
cat journal.txt
```

Le premier `>` initialise le fichier. Les deux `>>` ajoutent les lignes suivantes.

**B4.**

```bash
ls -l
```

L'option `-l` demande les détails.

## Partie C — Recevoir un message

**C1 à C4.**

```bash
echo "INFO : depart a 09h" > messages/radio.txt
echo "SECRET : suivre Vega" >> messages/radio.txt
echo "INFO : ciel degage" >> messages/radio.txt
grep SECRET messages/radio.txt
cat messages/radio.txt | grep SECRET
cat messages/radio.txt
```

Les deux filtres renvoient `SECRET : suivre Vega`. La lecture finale affiche encore les trois lignes.

## Partie D — La cabine du sous-shell

**D1.**

```bash
readlink -f /bin/sh
ps -p $$ -o comm=
```

Sur la VM de référence : `/usr/bin/dash`, puis `bash`.

**D2 et D3.**

```bash
pwd
(
    cd messages
    pwd
)
pwd
```

Le chemin du milieu finit par `/01-orion/messages`. Le premier et le dernier finissent par `/01-orion` : le changement de dossier reste dans le sous-shell.

## Bonus — Le dossier au nom piégeux

```bash
mkdir -p "journal de bord"
cd "journal de bord"
pwd
cd ..
```

Les guillemets empêchent de traiter les trois mots comme trois arguments.

[← Énoncé du TP](https://kayasam.github.io/linux-initiation/bash/01-shell-et-environnement/tp)
