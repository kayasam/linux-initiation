---
title: "TP 04"
---

# TP 04 — Contrôler le sas de la station

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="bash/04-tests-et-conditions" style="--resource-count:4"><div class="resource-buttons"><a class="resource-button resource-markdown" data-resource-kind="markdown" aria-label="Cours — Lire le cours en Markdown" href="https://kayasam.github.io/linux-initiation/bash/04-tests-et-conditions/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg></span><span class="resource-label">Cours<small>Lire le cours en Markdown</small></span></a><a class="resource-button resource-html" data-resource-kind="html" aria-label="HTML — Explorer le chapitre" href="https://kayasam.github.io/linux-initiation/bash/04-tests-et-conditions/html/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 28 32"><path d="M2 2h24l-2 25-10 3-10-3Z" fill="#e44d26"/><path d="M14 5v22l7-2 2-20Z" fill="#f16529"/><path d="M7 8h15l-.3 3H11l.3 3h10l-.8 9-6.5 2-6.5-2-.4-5h3l.2 2.6 3.7 1 3.7-1 .3-3.6H8Z" fill="#fff"/></svg></span><span class="resource-label">HTML<small>Explorer le chapitre</small></span></a><a class="resource-button resource-quiz" data-resource-kind="quiz" aria-label="Quiz — 20 questions" href="https://kayasam.github.io/linux-initiation/bash/04-tests-et-conditions/quiz/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="4" y="3" width="24" height="26" rx="6" fill="#7652ad"/><path d="M12 12a4 4 0 1 1 6 3.5c-1.5.8-2 1.4-2 3" fill="none" stroke="#fff" stroke-width="2.8" stroke-linecap="round"/><circle cx="16" cy="23" r="1.6" fill="#fff"/></svg></span><span class="resource-label">Quiz<small>20 questions</small></span></a><a class="resource-button resource-tp" data-resource-kind="tp" aria-label="TP — Mettre en pratique" href="https://kayasam.github.io/linux-initiation/bash/04-tests-et-conditions/tp"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg></span><span class="resource-label">TP<small>Mettre en pratique</small></span></a></div><div class="resource-actions"><a class="resource-download" href="https://kayasam.github.io/linux-initiation/telechargements/bash/cours/04-tests-et-conditions.md" download aria-label="Télécharger le cours en Markdown"><span aria-hidden="true">↓</span> Télécharger .md</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>

> Chapitre associé : [04 — Tests et conditions](https://kayasam.github.io/linux-initiation/bash/04-tests-et-conditions/)

## Mission

Le sas d'Orion est une simulation locale. Ton programme lit un fichier billet et choisit d'accepter ou de refuser l'entrée. Il doit aussi expliquer les erreurs d'utilisation.

## Partie A — Préparer les billets

**A1.** Crée ton atelier et deux billets :

```bash
mkdir -p ~/atelier-bash/04-sas
cd ~/atelier-bash/04-sas
echo 'ORION-OK' > billet-valide.txt
echo 'AUTRE-STATION' > billet-refuse.txt
```

**A2.** Affiche leurs contenus et vérifie qu'ils sont différents.

## Partie B — Programmer le contrôleur

Crée `sas.sh` dans nano, avec son shebang.

**B1.** Le programme attend exactement un argument. Si `$#` ne vaut pas 1, affiche une ligne d'utilisation sur la sortie d'erreur et termine avec `exit 2`.

**B2.** Range le premier argument dans `billet`. Vérifie qu'il désigne un fichier ordinaire lisible. Sinon, affiche une erreur et termine avec le code 2.

**B3.** Cherche une ligne exactement égale à `ORION-OK` avec `grep -qx`.

- Si la recherche réussit : affiche `SAS OUVERT`, puis termine avec le code 0.
- Sinon : affiche `SAS FERME`, puis termine avec le code 1.

> Indice : une commande placée après `if` sert elle-même de test.

**B4.** Vérifie la syntaxe et ajoute le droit d'exécution.

## Partie C — La tournée des essais

**C1.** Teste les situations ci-dessous. Après **chaque** lancement, utilise immédiatement `echo "Code : $?"`.

| Lancement | Résultat attendu | Code |
|---|---|---|
| `./sas.sh billet-valide.txt` | SAS ouvert | 0 |
| `./sas.sh billet-refuse.txt` | SAS fermé | 1 |
| `./sas.sh absent.txt` | Erreur de fichier | 2 |
| `./sas.sh` | Aide d'utilisation | 2 |
| `./sas.sh .` | Erreur de fichier : `.` est un dossier | 2 |

**C2.** Copie le billet valide vers un fichier nommé `billet equipe.txt`, puis teste ce nom composé. Il doit être accepté quand tu utilises les guillemets.

**C3.** Explique pourquoi le script vérifie le nombre d'arguments avant de lire `$1`.

## Bonus — Le menu de la station

Crée `menu.sh`. Il demande un choix avec `read -p`, puis utilise `case` :

- `1` affiche `Radio disponible`.
- `2` affiche `Reserve disponible`.
- Toute autre réponse affiche `Choix inconnu` et termine avec le code 2.

Ce menu fait un seul choix puis se termine. Une boucle pour le répéter sera vue au prochain chapitre.

## Mission accomplie si…

Les cinq cas du tableau donnent les résultats et codes attendus, et le billet au nom composé fonctionne.

[← Revenir au cours](https://kayasam.github.io/linux-initiation/bash/04-tests-et-conditions/)

[← Parcours Bash](https://kayasam.github.io/linux-initiation/#bash)

<a href="https://kayasam.github.io/linux-initiation/telechargements/bash/tp/tp-04-tests-et-conditions.md" download>Télécharger le TP en Markdown</a>
