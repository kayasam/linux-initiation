---
title: "Correction — Programmer le robot d'accueil"
---

# TP 03 — Correction — Le robot d'accueil

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="bash/03-bases-du-scripting" style="--resource-count:4"><div class="resource-buttons"><a class="resource-button resource-markdown" data-resource-kind="markdown" aria-label="Cours — Lire le cours en Markdown" href="https://kayasam.github.io/linux-initiation/bash/03-bases-du-scripting/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg></span><span class="resource-label">Cours<small>Lire le cours en Markdown</small></span></a><a class="resource-button resource-html" data-resource-kind="html" aria-label="HTML — Explorer le chapitre" href="https://kayasam.github.io/linux-initiation/bash/03-bases-du-scripting/html/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 28 32"><path d="M2 2h24l-2 25-10 3-10-3Z" fill="#e44d26"/><path d="M14 5v22l7-2 2-20Z" fill="#f16529"/><path d="M7 8h15l-.3 3H11l.3 3h10l-.8 9-6.5 2-6.5-2-.4-5h3l.2 2.6 3.7 1 3.7-1 .3-3.6H8Z" fill="#fff"/></svg></span><span class="resource-label">HTML<small>Explorer le chapitre</small></span></a><a class="resource-button resource-quiz" data-resource-kind="quiz" aria-label="Quiz — 20 questions" href="https://kayasam.github.io/linux-initiation/bash/03-bases-du-scripting/quiz/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="4" y="3" width="24" height="26" rx="6" fill="#7652ad"/><path d="M12 12a4 4 0 1 1 6 3.5c-1.5.8-2 1.4-2 3" fill="none" stroke="#fff" stroke-width="2.8" stroke-linecap="round"/><circle cx="16" cy="23" r="1.6" fill="#fff"/></svg></span><span class="resource-label">Quiz<small>20 questions</small></span></a><a class="resource-button resource-tp" data-resource-kind="tp" aria-label="TP — Mettre en pratique" href="https://kayasam.github.io/linux-initiation/bash/03-bases-du-scripting/tp"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg></span><span class="resource-label">TP<small>Mettre en pratique</small></span></a></div><div class="resource-actions"><a class="resource-download" href="https://kayasam.github.io/linux-initiation/telechargements/bash/cours/03-bases-du-scripting.md" download aria-label="Télécharger le cours en Markdown"><span aria-hidden="true">↓</span> Télécharger .md</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>

> Énoncé : [TP 03](https://kayasam.github.io/linux-initiation/bash/03-bases-du-scripting/tp)

## Partie A — Construire le robot

**A1.**

```bash
mkdir -p ~/atelier-bash/03-robot
cd ~/atelier-bash/03-robot
```

**A2 à A4.** Contenu final de `robot.sh`, avec l'ajout demandé en C2 :

<!-- fichier: robot.sh -->
```bash
#!/usr/bin/env bash

# Accueillir un visiteur de la station.
prenom="${1:-visiteur}"
role="${2:-explorateur}"
echo "Bonjour $prenom, ton role sur Orion est $role."
echo "Arguments recus : $#"
```

## Partie B — Les essais du robot

**B1 à B4.**

```bash
bash -n robot.sh
bash robot.sh Mila pilote
chmod +x robot.sh
./robot.sh Mila pilote
./robot.sh
./robot.sh "Mila Vega" "responsable radio"
./robot.sh Mila pilote
code=$?
echo "Code : $code"
```

Attendus : `Mila/pilote`, `visiteur/explorateur`, puis `Mila Vega/responsable radio`. Le dernier code est `0`.

## Partie C — Comprendre le programme

**C1.**

```bash
bash -x robot.sh Mila pilote
```

**C2.** `$#` produit `0` sans argument, `2` avec un prénom et un rôle.

**C3.** `./` désigne le dossier courant. Les guillemets conservent chaque nom composé dans un seul argument.

## Bonus — Le journal des arrivées

Ajoute cette ligne à la fin du script, puis refais deux lancements :

<!-- ajouter: robot.sh -->
```bash
echo "$prenom ; $role" >> arrivees.txt
```

Cette ligne se place **dans `robot.sh`**, après les affectations. Le fichier dépend du dossier courant au lancement. `>>` conserve les arrivées précédentes.

[← Énoncé du TP](https://kayasam.github.io/linux-initiation/bash/03-bases-du-scripting/tp)
