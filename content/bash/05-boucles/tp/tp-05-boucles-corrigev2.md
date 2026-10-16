---
title: "TP 05 — Programmer le robot copieur — Corrigév2"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="bash/05-boucles" style="--resource-count:4"><div class="resource-buttons"><a class="resource-button resource-markdown" data-resource-kind="markdown" aria-label="Cours — Lire le cours en Markdown" href="https://kayasam.github.io/linux-initiation/bash/05-boucles/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg></span><span class="resource-label">Cours<small>Lire le cours en Markdown</small></span></a><a class="resource-button resource-html" data-resource-kind="html" aria-label="HTML — Explorer le chapitre" href="https://kayasam.github.io/linux-initiation/bash/05-boucles/html/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 28 32"><path d="M2 2h24l-2 25-10 3-10-3Z" fill="#e44d26"/><path d="M14 5v22l7-2 2-20Z" fill="#f16529"/><path d="M7 8h15l-.3 3H11l.3 3h10l-.8 9-6.5 2-6.5-2-.4-5h3l.2 2.6 3.7 1 3.7-1 .3-3.6H8Z" fill="#fff"/></svg></span><span class="resource-label">HTML<small>Explorer le chapitre</small></span></a><a class="resource-button resource-quiz" data-resource-kind="quiz" aria-label="Quiz — 20 questions" href="https://kayasam.github.io/linux-initiation/bash/05-boucles/quiz/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="4" y="3" width="24" height="26" rx="6" fill="#7652ad"/><path d="M12 12a4 4 0 1 1 6 3.5c-1.5.8-2 1.4-2 3" fill="none" stroke="#fff" stroke-width="2.8" stroke-linecap="round"/><circle cx="16" cy="23" r="1.6" fill="#fff"/></svg></span><span class="resource-label">Quiz<small>20 questions</small></span></a><a class="resource-button resource-tp" data-resource-kind="tp" aria-label="TP — Mettre en pratique" href="https://kayasam.github.io/linux-initiation/bash/05-boucles/tp"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg></span><span class="resource-label">TP<small>Mettre en pratique</small></span></a></div><div class="resource-actions"><a class="resource-download" href="https://kayasam.github.io/linux-initiation/telechargements/bash/cours/05-boucles.md" download aria-label="Télécharger le cours en Markdown"><span aria-hidden="true">↓</span> Télécharger .md</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>

> Essaie chaque question avant de cliquer sur **Afficher la correction**. Chaque réponse s’ouvre et se referme indépendamment.

> Chapitre associé : [05 — Les boucles](https://kayasam.github.io/linux-initiation/bash/05-boucles/)

## Mission

Le robot doit copier les messages `.txt` d'Orion, compter ses copies et laisser les originaux en place. Un fichier au nom composé et un faux dossier essaieront de le piéger.

## Partie A — Préparer les messages

**A1.** Colle ce bloc :

```bash
mkdir -p ~/atelier-bash/05-copieur/messages/faux.txt
cd ~/atelier-bash/05-copieur
echo 'Poste ouvert' > messages/accueil.txt
echo 'Canal 7' > "messages/journal radio.txt"
echo 'Reserve complete' > messages/reserve.txt
echo 'Image fictive' > messages/photo.png
mkdir -p vide
```

> [!success]- Afficher la correction — A1
> Exécute le bloc de l’énoncé depuis ton terminal Bash. L’atelier contient `messages`, avec trois fichiers `.txt`, une image `.png` et un **dossier** `faux.txt`. Le dossier `vide` servira à tester l’absence de fichier.

**A2.** Liste le dossier `messages` avec `ls -l`. Identifie les trois fichiers texte, le fichier image et le dossier dont le nom finit par `.txt`.

> [!success]- Afficher la correction — A2
> ```bash
> ls -l messages
> ```
>
> Les fichiers texte sont `accueil.txt`, `journal radio.txt` et `reserve.txt`. `photo.png` est l’image. Le `d` au début de la ligne de `faux.txt` indique un dossier ; un fichier ordinaire commence par `-`.

## Partie B — Construire le robot

Crée `copieur.sh` en t'aidant de l'exemple du cours.

**B1.** Accepte zéro ou un argument. Sans argument, utilise `messages`. Si le dossier n'existe pas, affiche une erreur et termine avec le code 2.

> [!success]- Afficher la correction — B1
> ```bash
> #!/usr/bin/env bash
>
> if [[ "$#" -gt 1 ]]; then
>     echo "Usage : $0 [dossier]" >&2
>     exit 2
> fi
>
> source="${1:-messages}"
> if [[ ! -d "$source" ]]; then
>     echo "Dossier absent : $source" >&2
>     exit 2
> fi
> ```
>
> Place ce début dans `copieur.sh`. On accepte 0 ou 1 argument ; `${1:-messages}` choisit le dossier par défaut. La garde `-d` vérifie le dossier avant toute copie.

**B2.** Crée un dossier `copies` à l'intérieur du dossier choisi. Prévois un message et un code 1 si cette création échoue.

> [!success]- Afficher la correction — B2
> ```bash
> destination="$source/copies"
> if ! mkdir -p -- "$destination"; then
>     echo 'Destination impossible' >&2
>     exit 1
> fi
> ```
>
> Ajoute ce bloc après B1. `-p` accepte une destination déjà présente ; `--` marque la fin des options. `if !` entre dans la branche d’erreur si `mkdir` échoue.

**B3.** Initialise le compteur à 0, puis parcours `"$source"/*.txt`.

> [!success]- Afficher la correction — B3
> ```bash
> compteur=0
> ```
>
> Ajoute cette initialisation avant la boucle. Celle-ci commencera par `for fichier in "$source"/*.txt; do` et se terminera par `done` : le bloc complet est donné en B4. Seule la variable est entre guillemets, afin que `*` reste un motif.

**B4.** Pour chaque élément :

1. S'il n'est pas un fichier ordinaire, passe au suivant.
2. Copie-le dans `copies`, en conservant les guillemets.
3. En cas d'échec de la copie, affiche une erreur et termine avec le code 1.
4. Sinon, augmente le compteur.

> [!success]- Afficher la correction — B4
> ```bash
> for fichier in "$source"/*.txt; do
>     if [[ ! -f "$fichier" ]]; then
>         continue
>     fi
>     if ! cp -- "$fichier" "$destination/"; then
>         echo "Copie impossible : $fichier" >&2
>         exit 1
>     fi
>     compteur=$((compteur + 1))
> done
> ```
>
> Place cette boucle après l’initialisation B3. `continue` ignore l’élément courant. Le compteur augmente **seulement après une copie réussie**. Le `/` final indique que la destination doit être un dossier.

**B5.** Affiche `Copies realisees : N`, avec le vrai nombre, puis vérifie la syntaxe.

> [!success]- Afficher la correction — B5
> ```bash
> echo "Copies realisees : $compteur"
> ```
>
> Ajoute cette ligne **après le `done`** dans `copieur.sh`. Enregistre le fichier, puis exécute dans le terminal :
>
> ```bash
> bash -n copieur.sh
> chmod +x copieur.sh
> ```
>
> Si la syntaxe est correcte, `bash -n` n’affiche rien. Le script assemble les blocs B1, B2, B3, B4 et cet affichage, dans cet ordre.

## Partie C — Les essais pièges

**C1.** Lance le robot sur `messages`. Attendu : **3 copies**. Vérifie les contenus des copies et la présence des originaux.

> [!success]- Afficher la correction — C1
> ```bash
> ./copieur.sh messages
> ls messages/copies
> cat "messages/copies/journal radio.txt"
> cat "messages/journal radio.txt"
> ```
>
> Attendu : `Copies realisees : 3`. Les deux lectures donnent `Canal 7`. Les trois originaux sont toujours dans `messages` : `cp` copie, il ne déplace pas.

**C2.** Relance-le : il remplace les copies de même nom, sans créer de doublon. Le résultat reste 3.

> [!success]- Afficher la correction — C2
> ```bash
> ./copieur.sh messages
> ls messages/copies
> ```
>
> Le résultat reste **3**. Les copies existantes sont remplacées ; aucun doublon n’est créé. Le compteur est réinitialisé au début de chaque lancement.

**C3.** Lance-le sur `vide`. Attendu : **0 copie**, pas une erreur.

> [!success]- Afficher la correction — C3
> ```bash
> ./copieur.sh vide
> echo "Code : $?"
> ```
>
> Attendu : `Copies realisees : 0`, puis `Code : 0`. Avec les réglages habituels de Bash, le motif non remplacé `vide/*.txt` passe dans la boucle ; le test `-f` échoue et `continue` l’ignore.

**C4.** Lance-le sur un dossier inexistant. Attendu : message d'erreur, code 2.

> [!success]- Afficher la correction — C4
> ```bash
> ./copieur.sh absent
> echo "Code : $?"
> ```
>
> La garde B1 affiche `Dossier absent : absent` et le code est **2**. Lis `$?` immédiatement après le lancement.

**C5.** Explique pourquoi le dossier `faux.txt` et le fichier `photo.png` ne sont pas copiés.

> [!success]- Afficher la correction — C5
> `*.txt` écarte `photo.png` avant le début de la boucle. Le dossier `faux.txt` correspond au motif, mais le test `-f` l’écarte ensuite. Le motif et le test jouent donc deux rôles complémentaires.

## Bonus — L'appel de l'équipage

Crée un fichier `equipe.txt` contenant `Mila Vega` et `Noe`, une personne par ligne. Parcours-le avec `while IFS= read -r personne` et affiche une ligne d'accueil par personne.

**Défi supplémentaire :** essaie une dernière ligne sans retour à la ligne. Pour la conserver, utilise cette condition : `while IFS= read -r personne || [[ -n "$personne" ]]; do`. Explique pourquoi le deuxième test permet de traiter la valeur encore présente.

> [!success]- Afficher la correction — Bonus
> ```bash
> printf 'Mila Vega\nNoe' > equipe.txt
> while IFS= read -r personne || [[ -n "$personne" ]]; do
>     echo "Bienvenue $personne"
> done < equipe.txt
> ```
>
> Résultat : `Bienvenue Mila Vega`, puis `Bienvenue Noe`. La dernière ligne n’a pas de retour final : `read` récupère ses caractères, mais renvoie un échec en atteignant la fin. `|| [[ -n "$personne" ]]` autorise le dernier passage pour cette valeur encore présente. Au tour suivant, la variable est vide et la boucle s’arrête.
>
> `IFS=` conserve les espaces de début et de fin ; `-r` conserve les antislashs ; `< equipe.txt` fournit le fichier comme entrée.

## Mission accomplie si…

Tu obtiens les nombres **3, 3 et 0**, les noms composés restent intacts et l'erreur de dossier renvoie 2.

[← Énoncé du TP](https://kayasam.github.io/linux-initiation/bash/05-boucles/tp/tp-05-boucles)
