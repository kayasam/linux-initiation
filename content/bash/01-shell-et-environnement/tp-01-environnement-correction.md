---
title: "Correction — Installer la station Orion"
---

# TP 01 — Correction — Installer la station Orion

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="bash/01-shell-et-environnement" style="--resource-count:4"><div class="resource-buttons"><a class="resource-button resource-markdown" data-resource-kind="markdown" aria-label="Cours — Lire le cours en Markdown" href="https://kayasam.github.io/linux-initiation/bash/01-shell-et-environnement/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg></span><span class="resource-label">Cours<small>Lire le cours en Markdown</small></span></a><a class="resource-button resource-html" data-resource-kind="html" aria-label="HTML — Explorer le chapitre" href="https://kayasam.github.io/linux-initiation/bash/01-shell-et-environnement/html/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 28 32"><path d="M2 2h24l-2 25-10 3-10-3Z" fill="#e44d26"/><path d="M14 5v22l7-2 2-20Z" fill="#f16529"/><path d="M7 8h15l-.3 3H11l.3 3h10l-.8 9-6.5 2-6.5-2-.4-5h3l.2 2.6 3.7 1 3.7-1 .3-3.6H8Z" fill="#fff"/></svg></span><span class="resource-label">HTML<small>Explorer le chapitre</small></span></a><a class="resource-button resource-quiz" data-resource-kind="quiz" aria-label="Quiz — 20 questions" href="https://kayasam.github.io/linux-initiation/bash/01-shell-et-environnement/quiz/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="4" y="3" width="24" height="26" rx="6" fill="#7652ad"/><path d="M12 12a4 4 0 1 1 6 3.5c-1.5.8-2 1.4-2 3" fill="none" stroke="#fff" stroke-width="2.8" stroke-linecap="round"/><circle cx="16" cy="23" r="1.6" fill="#fff"/></svg></span><span class="resource-label">Quiz<small>20 questions</small></span></a><a class="resource-button resource-tp" data-resource-kind="tp" aria-label="TP — Mettre en pratique" href="https://kayasam.github.io/linux-initiation/bash/01-shell-et-environnement/tp"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg></span><span class="resource-label">TP<small>Mettre en pratique</small></span></a></div><div class="resource-actions"><a class="resource-download" href="https://kayasam.github.io/linux-initiation/telechargements/bash/cours/01-shell-et-environnement.md" download aria-label="Télécharger le cours en Markdown"><span aria-hidden="true">↓</span> Télécharger .md</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>

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
