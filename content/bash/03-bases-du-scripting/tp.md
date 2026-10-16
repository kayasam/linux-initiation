---
title: "TP 03"
---

# TP 03 — Programmer le robot d'accueil

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="bash/03-bases-du-scripting" style="--resource-count:4"><div class="resource-buttons"><a class="resource-button resource-markdown" data-resource-kind="markdown" aria-label="Cours — Lire le cours en Markdown" href="https://kayasam.github.io/linux-initiation/bash/03-bases-du-scripting/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg></span><span class="resource-label">Cours<small>Lire le cours en Markdown</small></span></a><a class="resource-button resource-html" data-resource-kind="html" aria-label="HTML — Explorer le chapitre" href="https://kayasam.github.io/linux-initiation/bash/03-bases-du-scripting/html/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 28 32"><path d="M2 2h24l-2 25-10 3-10-3Z" fill="#e44d26"/><path d="M14 5v22l7-2 2-20Z" fill="#f16529"/><path d="M7 8h15l-.3 3H11l.3 3h10l-.8 9-6.5 2-6.5-2-.4-5h3l.2 2.6 3.7 1 3.7-1 .3-3.6H8Z" fill="#fff"/></svg></span><span class="resource-label">HTML<small>Explorer le chapitre</small></span></a><a class="resource-button resource-quiz" data-resource-kind="quiz" aria-label="Quiz — 20 questions" href="https://kayasam.github.io/linux-initiation/bash/03-bases-du-scripting/quiz/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="4" y="3" width="24" height="26" rx="6" fill="#7652ad"/><path d="M12 12a4 4 0 1 1 6 3.5c-1.5.8-2 1.4-2 3" fill="none" stroke="#fff" stroke-width="2.8" stroke-linecap="round"/><circle cx="16" cy="23" r="1.6" fill="#fff"/></svg></span><span class="resource-label">Quiz<small>20 questions</small></span></a><a class="resource-button resource-tp" data-resource-kind="tp" aria-label="TP — Mettre en pratique" href="https://kayasam.github.io/linux-initiation/bash/03-bases-du-scripting/tp"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg></span><span class="resource-label">TP<small>Mettre en pratique</small></span></a></div><div class="resource-actions"><a class="resource-download" href="https://kayasam.github.io/linux-initiation/telechargements/bash/cours/03-bases-du-scripting.md" download aria-label="Télécharger le cours en Markdown"><span aria-hidden="true">↓</span> Télécharger .md</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>

> Chapitre associé : [03 — Écrire son premier script](https://kayasam.github.io/linux-initiation/bash/03-bases-du-scripting/)

## Mission

Le robot Orion doit accueillir les visiteurs avec leur nom et leur rôle. Crée un programme que tout l'équipage pourra relancer.

## Partie A — Construire le robot

**A1.** Prépare son atelier :

```bash
mkdir -p ~/atelier-bash/03-robot
cd ~/atelier-bash/03-robot
```

**A2.** Ouvre `robot.sh` avec nano. Ajoute le shebang Bash en première ligne, puis un commentaire décrivant le rôle du programme.

**A3.** Crée deux variables : `prenom`, qui lit le premier argument ou utilise `visiteur`, et `role`, qui lit le deuxième argument ou utilise `explorateur`.

> Indice : `${1:-visiteur}` ; adapte cette écriture au deuxième argument.

**A4.** Affiche une ligne de cette forme :

```text
Bonjour Mila, ton role sur Orion est pilote.
```

Utilise `echo` et tes deux variables. Enregistre et quitte nano.

## Partie B — Les essais du robot

**B1.** Vérifie la syntaxe avec `bash -n`, puis lance le script avec Bash et les arguments `Mila pilote`.

**B2.** Ajoute le droit d'exécution, puis refais le test avec `./robot.sh`.

**B3.** Teste ensuite ces deux cas :

```bash
./robot.sh
./robot.sh "Mila Vega" "responsable radio"
```

**Points de contrôle :** le premier utilise les valeurs par défaut ; le second conserve les noms composés.

**B4.** Relance le cas `Mila pilote`, récupère immédiatement son code de retour et affiche-le. Attendu : **0**.

## Partie C — Comprendre le programme

**C1.** Lance `bash -x robot.sh Mila pilote`. Repère les affectations des deux variables.

**C2.** Ajoute une ligne qui affiche le nombre d'arguments reçus, puis refais les essais sans argument et avec deux arguments.

**C3.** Explique pourquoi on écrit `./robot.sh` et pourquoi on entoure `Mila Vega` de guillemets.

## Bonus — Le journal des arrivées

Ajoute au programme une ligne qui enregistre le prénom et le rôle dans `arrivees.txt`, avec `>>`. Lance le robot deux fois et lis le journal : les deux arrivées doivent être présentes.

Le journal est créé dans le dossier **depuis lequel tu lances le script**. Pour ce TP, reste dans `03-robot`.

## Mission accomplie si…

- La syntaxe est correcte.
- Les trois essais produisent les bons noms et rôles.
- Le programme indique 0 argument ou 2 arguments selon l'essai.
- Le bonus ajoute des lignes sans remplacer les arrivées précédentes.

[← Revenir au cours](https://kayasam.github.io/linux-initiation/bash/03-bases-du-scripting/)

[← Parcours Bash](https://kayasam.github.io/linux-initiation/#bash)

<a href="https://kayasam.github.io/linux-initiation/telechargements/bash/tp/tp-03-bases-du-scripting.md" download>Télécharger le TP en Markdown</a>
