---
title: "TP 04 — Contrôler le sas de la station — Corrigév2"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="bash/04-tests-et-conditions" style="--resource-count:4"><div class="resource-buttons"><a class="resource-button resource-markdown" data-resource-kind="markdown" aria-label="Cours — Lire le cours en Markdown" href="https://kayasam.github.io/linux-initiation/bash/04-tests-et-conditions/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg></span><span class="resource-label">Cours<small>Lire le cours en Markdown</small></span></a><a class="resource-button resource-html" data-resource-kind="html" aria-label="HTML — Explorer le chapitre" href="https://kayasam.github.io/linux-initiation/bash/04-tests-et-conditions/html/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 28 32"><path d="M2 2h24l-2 25-10 3-10-3Z" fill="#e44d26"/><path d="M14 5v22l7-2 2-20Z" fill="#f16529"/><path d="M7 8h15l-.3 3H11l.3 3h10l-.8 9-6.5 2-6.5-2-.4-5h3l.2 2.6 3.7 1 3.7-1 .3-3.6H8Z" fill="#fff"/></svg></span><span class="resource-label">HTML<small>Explorer le chapitre</small></span></a><a class="resource-button resource-quiz" data-resource-kind="quiz" aria-label="Quiz — 20 questions" href="https://kayasam.github.io/linux-initiation/bash/04-tests-et-conditions/quiz/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="4" y="3" width="24" height="26" rx="6" fill="#7652ad"/><path d="M12 12a4 4 0 1 1 6 3.5c-1.5.8-2 1.4-2 3" fill="none" stroke="#fff" stroke-width="2.8" stroke-linecap="round"/><circle cx="16" cy="23" r="1.6" fill="#fff"/></svg></span><span class="resource-label">Quiz<small>20 questions</small></span></a><a class="resource-button resource-tp" data-resource-kind="tp" aria-label="TP — Mettre en pratique" href="https://kayasam.github.io/linux-initiation/bash/04-tests-et-conditions/tp"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg></span><span class="resource-label">TP<small>Mettre en pratique</small></span></a></div><div class="resource-actions"><a class="resource-download" href="https://kayasam.github.io/linux-initiation/telechargements/bash/tp/tp-04-tests-et-conditions-corrigev2.md" download aria-label="Télécharger le corrigé en Markdown">↓ Télécharger le corrigé (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>
<nav class="exercise-resources" aria-label="Ressources du TP"><a href="https://kayasam.github.io/linux-initiation/bash/04-tests-et-conditions/tp">Énoncé</a><a class="exercise-correction" href="https://kayasam.github.io/linux-initiation/bash/04-tests-et-conditions/tp-04-tests-et-conditions-corrigev2" aria-current="page">Corrigé</a></nav>

> Essaie chaque question avant de cliquer sur **Afficher la correction**. Chaque réponse s’ouvre et se referme indépendamment.

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

> [!success]- Afficher la correction — A1
> ```bash
> mkdir -p ~/atelier-bash/04-sas
> cd ~/atelier-bash/04-sas
> echo 'ORION-OK' > billet-valide.txt
> echo 'AUTRE-STATION' > billet-refuse.txt
> ```
>
> `>` initialise chaque fichier. `echo` ajoute un retour à la ligne : les billets contiennent chacun une ligne complète.

**A2.** Affiche leurs contenus et vérifie qu'ils sont différents.

> [!success]- Afficher la correction — A2
> ```bash
> cat billet-valide.txt billet-refuse.txt
> ```
>
> Les deux lignes sont `ORION-OK`, puis `AUTRE-STATION`. Leurs contenus sont différents.

## Partie B — Programmer le contrôleur

Crée `sas.sh` dans nano, avec son shebang.

**B1.** Le programme attend exactement un argument. Si `$#` ne vaut pas 1, affiche une ligne d'utilisation sur la sortie d'erreur et termine avec `exit 2`.

> [!success]- Afficher la correction — B1
> ```bash
> #!/usr/bin/env bash
>
> if [[ "$#" -ne 1 ]]; then
>     echo "Usage : $0 fichier-billet" >&2
>     exit 2
> fi
> ```
>
> Place ce début dans `sas.sh`. `$#` compte les arguments ; `-ne` compare des nombres. `>&2` envoie le message sur la sortie d’erreur. `exit 2` arrête le script en signalant une mauvaise utilisation.

**B2.** Range le premier argument dans une variable `billet`. Vérifie qu'il désigne un fichier ordinaire lisible. Sinon, affiche une erreur et termine avec le code 2.

> [!success]- Afficher la correction — B2
> ```bash
> billet="$1"
> if [[ ! -f "$billet" || ! -r "$billet" ]]; then
>     echo "Billet absent ou illisible : $billet" >&2
>     exit 2
> fi
> ```
>
> Ajoute ce bloc **après la garde B1**. `-f` vérifie un fichier ordinaire, `-r` sa lisibilité ; `!` inverse le test et `||` signifie « ou ».

**B3.** Cherche une ligne exactement égale à `ORION-OK` avec `grep -qx`.

- Si la recherche réussit : affiche `SAS OUVERT`, puis termine avec le code 0.
- Sinon : affiche `SAS FERME`, puis termine avec le code 1.

> Indice : une commande placée après `if` sert elle-même de test.

> [!success]- Afficher la correction — B3
> ```bash
> if grep -qx 'ORION-OK' "$billet"; then
>     echo 'SAS OUVERT'
>     exit 0
> else
>     echo 'SAS FERME'
>     exit 1
> fi
> ```
>
> Ajoute ce bloc après B2. `if` regarde le code de retour de `grep`. `-q` supprime l’affichage de la recherche et `-x` exige une ligne entière : `ORION-OK-FAUX` n’est pas accepté. Dans ce TP, les codes 0, 1 et 2 distinguent acceptation, refus et erreur d’utilisation.

**B4.** Vérifie la syntaxe et ajoute le droit d'exécution.

> [!success]- Afficher la correction — B4
> ```bash
> bash -n sas.sh
> chmod +x sas.sh
> ```
>
> `bash -n` vérifie la syntaxe sans exécuter le script ; il reste silencieux en cas de succès. `chmod +x` autorise le lancement direct.

## Partie C — La tournée des essais

**C1.** Teste les situations ci-dessous. Après **chaque** lancement, utilise immédiatement `echo "Code : $?"`.

| Lancement | Résultat attendu | Code |
|---|---|---|
| `./sas.sh billet-valide.txt` | SAS ouvert | 0 |
| `./sas.sh billet-refuse.txt` | SAS fermé | 1 |
| `./sas.sh absent.txt` | Erreur de fichier | 2 |
| `./sas.sh` | Aide d'utilisation | 2 |
| `./sas.sh .` | Erreur de fichier : `.` est un dossier | 2 |

> [!success]- Afficher la correction — C1
> ```bash
> ./sas.sh billet-valide.txt
> echo "Code : $?"
> ./sas.sh billet-refuse.txt
> echo "Code : $?"
> ./sas.sh absent.txt
> echo "Code : $?"
> ./sas.sh
> echo "Code : $?"
> ./sas.sh .
> echo "Code : $?"
> ```
>
> Codes attendus : **0, 1, 2, 2, 2**. Lis `$?` immédiatement après chaque lancement. Les `exit` terminent le processus du script, pas ta session SSH ; lance le script normalement, sans `source`.

**C2.** Copie le billet valide vers un fichier nommé `billet equipe.txt`, puis teste ce nom composé. Il doit être accepté quand tu utilises les guillemets.

> [!success]- Afficher la correction — C2
> ```bash
> cp billet-valide.txt "billet equipe.txt"
> ./sas.sh "billet equipe.txt"
> echo "Code : $?"
> ```
>
> Résultat : `SAS OUVERT`, puis `Code : 0`. Sans les guillemets au lancement, le shell transmettrait deux arguments : la garde B1 renverrait 2.

**C3.** Explique pourquoi le script vérifie le nombre d'arguments avant de lire `$1`.

> [!success]- Afficher la correction — C3
> La garde valide les entrées avant leur utilisation. Sans argument, et sans option `nounset`, `$1` est vide : le script continuerait avec `billet=""` et afficherait une erreur de fichier peu claire. La garde donne immédiatement le bon message d’utilisation.

## Bonus — Le menu de la station

Crée `menu.sh`. Il demande un choix avec `read -p`, puis utilise `case` :

- `1` affiche `Radio disponible`.
- `2` affiche `Reserve disponible`.
- Toute autre réponse affiche `Choix inconnu` et termine avec le code 2.

Ce menu fait un seul choix puis se termine. Une boucle pour le répéter sera vue au prochain chapitre.

> [!success]- Afficher la correction — Bonus
> ```bash
> #!/usr/bin/env bash
> read -p '1 : radio ; 2 : reserve — choix : ' choix
>
> case "$choix" in
>     1) echo 'Radio disponible' ;;
>     2) echo 'Reserve disponible' ;;
>     *) echo 'Choix inconnu' >&2; exit 2 ;;
> esac
> ```
>
> Enregistre dans `menu.sh`, puis lance `bash menu.sh` pour tester `1`, `2` et `x`. Les deux premiers choix réussissent ; le dernier renvoie 2. La branche `*)` traite tous les autres choix et doit rester en dernier.

## Mission accomplie si…

Les cinq cas du tableau donnent les résultats et codes attendus, et le billet au nom composé fonctionne.

[← Énoncé du TP](https://kayasam.github.io/linux-initiation/bash/04-tests-et-conditions/tp)
