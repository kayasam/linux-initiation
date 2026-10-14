# TP 01 — Installer la station Orion

> Chapitre associé : [01 — Le shell et son environnement](https://kayasam.github.io/linux-initiation/bash/01-shell-et-environnement/)

## Mission

Tu arrives à la station Orion. Prépare ton poste, crée le journal de bord et trouve le message radio. Tu travailles dans **Bash sur Debian**, après ta connexion SSH.

## Partie A — Trouver ton poste

**A1.** Affiche ton compte, le nom de la machine et ton dossier courant. Note les trois résultats.

> Indice : les trois commandes sont au début du cours.

**A2.** Prépare ce dossier de mission :

```bash
mkdir -p ~/atelier-bash/01-orion/messages
cd ~/atelier-bash/01-orion
pwd
```

Explique `~`, `-p` et le résultat de `pwd`.

**A3.** Entre dans `messages`, vérifie où tu es, puis reviens au dossier `01-orion`. Utilise `cd`, `pwd` et `..`.

**Point de contrôle :** tu es revenu dans `~/atelier-bash/01-orion`.

## Partie B — Ouvrir le journal de bord

**B1.** Crée le journal :

```bash
printf 'ORION : poste ouvert\n' > journal.txt
```

**B2.** Avec `>>`, ajoute deux lignes : `Radio : OK` et `Reserve : OK`.

**B3.** Affiche le journal. Il doit contenir exactement :

```text
ORION : poste ouvert
Radio : OK
Reserve : OK
```

**B4.** Liste les fichiers avec les détails. Quel caractère de la commande `ls -l` demande cet affichage ?

## Partie C — Recevoir un message

**C1.** Crée le fichier radio :

```bash
printf 'INFO : depart a 09h\nSECRET : suivre Vega\nINFO : ciel degage\n' > messages/radio.txt
```

**C2.** Affiche seulement la ligne contenant `SECRET`, avec `grep`.

**C3.** Refais le même filtre avec deux commandes reliées par un tube. Explique le rôle du tube.

**C4.** Vérifie que les trois lignes du fichier radio sont toujours présentes.

## Bonus — Le dossier au nom piégeux

Crée un dossier nommé `journal de bord` puis entre dedans. Il faut le considérer comme **un seul nom** : entoure-le de guillemets doubles. Reviens ensuite à `01-orion`.

## Mission accomplie si…

- Tu retrouves ton dossier sans fermer la connexion.
- Ton journal contient les trois lignes attendues.
- Tu as trouvé le message secret sans modifier le fichier radio.
- Tu expliques la différence entre `>` et `>>`.

Conserve tes fichiers : aucune suppression n'est demandée.

[← Revenir au cours](https://kayasam.github.io/linux-initiation/bash/01-shell-et-environnement/)
