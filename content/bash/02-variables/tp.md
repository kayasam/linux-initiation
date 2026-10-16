---
title: "TP 02"
---

# TP 02 — Fabriquer ton badge d'équipage

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="bash/02-variables" style="--resource-count:4"><div class="resource-buttons"><a class="resource-button resource-markdown" data-resource-kind="markdown" aria-label="Cours — Lire le cours en Markdown" href="https://kayasam.github.io/linux-initiation/bash/02-variables/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg></span><span class="resource-label">Cours<small>Lire le cours en Markdown</small></span></a><a class="resource-button resource-html" data-resource-kind="html" aria-label="HTML — Explorer le chapitre" href="https://kayasam.github.io/linux-initiation/bash/02-variables/html/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 28 32"><path d="M2 2h24l-2 25-10 3-10-3Z" fill="#e44d26"/><path d="M14 5v22l7-2 2-20Z" fill="#f16529"/><path d="M7 8h15l-.3 3H11l.3 3h10l-.8 9-6.5 2-6.5-2-.4-5h3l.2 2.6 3.7 1 3.7-1 .3-3.6H8Z" fill="#fff"/></svg></span><span class="resource-label">HTML<small>Explorer le chapitre</small></span></a><a class="resource-button resource-quiz" data-resource-kind="quiz" aria-label="Quiz — 20 questions" href="https://kayasam.github.io/linux-initiation/bash/02-variables/quiz/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="4" y="3" width="24" height="26" rx="6" fill="#7652ad"/><path d="M12 12a4 4 0 1 1 6 3.5c-1.5.8-2 1.4-2 3" fill="none" stroke="#fff" stroke-width="2.8" stroke-linecap="round"/><circle cx="16" cy="23" r="1.6" fill="#fff"/></svg></span><span class="resource-label">Quiz<small>20 questions</small></span></a><a class="resource-button resource-tp" data-resource-kind="tp" aria-label="TP — Mettre en pratique" href="https://kayasam.github.io/linux-initiation/bash/02-variables/tp"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg></span><span class="resource-label">TP<small>Mettre en pratique</small></span></a></div><div class="resource-actions"><a class="resource-download" href="https://kayasam.github.io/linux-initiation/telechargements/bash/cours/02-variables.md" download aria-label="Télécharger le cours en Markdown"><span aria-hidden="true">↓</span> Télécharger .md</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>

> Chapitre associé : [02 — Les variables](https://kayasam.github.io/linux-initiation/bash/02-variables/)

## Mission

La station Orion attend son nouvel équipage. Prépare un badge personnalisé et calcule l'énergie du poste. Tout se fait dans le terminal Bash Debian.

## Partie A — Les informations du badge

**A1.** Prépare ton atelier :

```bash
mkdir -p ~/atelier-bash/02-badge
cd ~/atelier-bash/02-badge
```

**A2.** Crée les variables `station`, contenant `Orion Nord`, et `role`, contenant `pilote`.

**A3.** Demande le prénom avec `read -p`. Range-le dans `prenom`.

**A4.** Affiche une phrase construite avec les trois variables. Si tu réponds `Mila`, elle doit donner :

```text
Mila rejoint Orion Nord comme pilote.
```

> Indice : utilise `echo` et une phrase entre guillemets doubles contenant tes trois variables.

## Partie B — Conserver le badge

**B1.** Range le résultat de `hostname` dans `machine` et celui de `date +%F` dans `jour`.

**B2.** Crée `badge.txt` avec le prénom, le rôle, la station, la machine et la date. Une information par ligne suffit. Utilise `>` pour la première ligne, puis `>>`.

**B3.** Lis ton badge avec `cat`. Vérifie que `Orion Nord` apparaît sur une seule ligne.

## Partie C — Charger les batteries

**C1.** Définis `batteries=4` et `energie_par_batterie=25`. Calcule `energie_totale` avec une expansion arithmétique.

**C2.** La radio consomme 15 unités. Calcule l'énergie restante et ajoute-la au badge.

**Points de contrôle :** énergie totale **100**, énergie restante **85**.

**C3.** Affiche une fois le texte littéral `$station`, puis une fois sa valeur. Quels guillemets changes-tu ?

## Bonus — Envoyer le nom de la station

Exporte `NOM_STATION="Orion Nord"`. Lance un second Bash avec `bash -c` et affiche cette variable dedans. Explique le rôle de `export`.

## Mission accomplie si…

- Ton badge contient tes cinq informations et une énergie restante de 85.
- Tu expliques la différence entre `prenom`, `"$prenom"` et `$(hostname)`.
- Tu sais pourquoi les valeurs contenant des espaces restent entre guillemets.

[← Revenir au cours](https://kayasam.github.io/linux-initiation/bash/02-variables/)

[Correction du TP](https://kayasam.github.io/linux-initiation/bash/02-variables/tp-02-variables-corrigev2)

[← Parcours Bash](https://kayasam.github.io/linux-initiation/#bash)

<a href="https://kayasam.github.io/linux-initiation/telechargements/bash/tp/tp-02-variables.md" download>Télécharger le TP en Markdown</a>
