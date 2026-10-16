---
title: "TP 04 — Correction — Contrôler le sas"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="bash/04-tests-et-conditions" style="--resource-count:4"><div class="resource-buttons"><a class="resource-button resource-markdown" data-resource-kind="markdown" aria-label="Cours — Lire le cours en Markdown" href="https://kayasam.github.io/linux-initiation/bash/04-tests-et-conditions/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg></span><span class="resource-label">Cours<small>Lire le cours en Markdown</small></span></a><a class="resource-button resource-html" data-resource-kind="html" aria-label="HTML — Explorer le chapitre" href="https://kayasam.github.io/linux-initiation/bash/04-tests-et-conditions/html/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 28 32"><path d="M2 2h24l-2 25-10 3-10-3Z" fill="#e44d26"/><path d="M14 5v22l7-2 2-20Z" fill="#f16529"/><path d="M7 8h15l-.3 3H11l.3 3h10l-.8 9-6.5 2-6.5-2-.4-5h3l.2 2.6 3.7 1 3.7-1 .3-3.6H8Z" fill="#fff"/></svg></span><span class="resource-label">HTML<small>Explorer le chapitre</small></span></a><a class="resource-button resource-quiz" data-resource-kind="quiz" aria-label="Quiz — 20 questions" href="https://kayasam.github.io/linux-initiation/bash/04-tests-et-conditions/quiz/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="4" y="3" width="24" height="26" rx="6" fill="#7652ad"/><path d="M12 12a4 4 0 1 1 6 3.5c-1.5.8-2 1.4-2 3" fill="none" stroke="#fff" stroke-width="2.8" stroke-linecap="round"/><circle cx="16" cy="23" r="1.6" fill="#fff"/></svg></span><span class="resource-label">Quiz<small>20 questions</small></span></a><a class="resource-button resource-tp" data-resource-kind="tp" aria-label="TP — Mettre en pratique" href="https://kayasam.github.io/linux-initiation/bash/04-tests-et-conditions/tp"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg></span><span class="resource-label">TP<small>Mettre en pratique</small></span></a></div><div class="resource-actions"><a class="resource-download" href="https://kayasam.github.io/linux-initiation/telechargements/bash/cours/04-tests-et-conditions.md" download aria-label="Télécharger le cours en Markdown"><span aria-hidden="true">↓</span> Télécharger .md</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>

> Énoncé : [TP 04](https://kayasam.github.io/linux-initiation/bash/04-tests-et-conditions/tp)

## Partie A — Préparer les billets

**A1 et A2.**

```bash
mkdir -p ~/atelier-bash/04-sas   # -p : crée les dossiers parents, et ne râle pas si ça existe déjà
cd ~/atelier-bash/04-sas         # on travaille dans l'atelier : tous les chemins suivants sont relatifs
echo 'ORION-OK' > billet-valide.txt      # > écrase (ou crée) le fichier avec cette seule ligne
echo 'AUTRE-STATION' > billet-refuse.txt # le billet qui doit être refusé
cat billet-valide.txt billet-refuse.txt  # affiche les deux contenus à la suite pour vérifier
```

> **À retenir.** `echo 'texte' > fichier` ajoute automatiquement un retour à la ligne à la fin.
> C'est important pour la suite : `grep -x` compare **des lignes entières**.

## Partie B — Programmer le contrôleur

**B1 à B3.** Contenu de `sas.sh` :

<!-- fichier: sas.sh -->
```bash
#!/usr/bin/env bash
# Shebang : indique le programme qui doit interpréter ce fichier.
# "env bash" va chercher bash dans le PATH → plus portable que /bin/bash en dur.

# --- B1 : garde sur le nombre d'arguments -------------------------------
# $# = nombre d'arguments reçus par le script.
# -ne = "not equal" (comparaison NUMÉRIQUE ; pour du texte on utiliserait !=).
if [[ "$#" -ne 1 ]]; then
    # $0 = le nom sous lequel le script a été appelé (./sas.sh).
    # >&2 redirige ce message vers la sortie d'erreur : un message d'erreur
    # ne doit pas polluer la sortie standard qu'un autre script pourrait lire.
    echo "Usage : $0 fichier-billet" >&2
    exit 2   # convention : 2 = mauvaise utilisation du programme
fi

# --- B2 : garde sur le fichier -----------------------------------------
billet="$1"   # on range l'argument dans un nom parlant : le script se relit mieux
# -f : existe ET est un fichier ORDINAIRE (donc "." , un dossier, échoue ici)
# -r : est lisible par l'utilisateur courant
# ! inverse le test, || = "ou" → on sort si l'un des deux problèmes est vrai
# Les guillemets autour de "$billet" sont obligatoires : sans eux,
# un nom contenant un espace serait découpé en plusieurs mots.
if [[ ! -f "$billet" || ! -r "$billet" ]]; then
    echo "Billet absent ou illisible : $billet" >&2
    exit 2
fi

# --- B3 : la décision ---------------------------------------------------
# Ici le "test" du if est une COMMANDE, pas des crochets :
# if se contente de regarder le code de retour de grep (0 = trouvé = vrai).
#   -q : quiet, n'affiche rien, se contente de renvoyer un code de retour
#   -x : la ligne doit correspondre EXACTEMENT (pas "ORION-OK-FAUX")
if grep -qx 'ORION-OK' "$billet"; then
    echo 'SAS OUVERT'
    exit 0   # 0 = succès
else
    echo 'SAS FERME'
    exit 1   # 1 = le programme a bien fonctionné, mais la réponse est "non"
fi
```

> **Pourquoi trois codes différents ?** Chacun raconte une histoire : **0** « tout va bien »,
> **1** « j'ai fait mon travail, et la réponse est non », **2** « tu m'as mal utilisé ».
> C'est la convention UNIX. C'est aussi ce qui permet d'enchaîner le script avec `&&` ou `||`,
> ou de le tester dans le `if` d'un autre script.

**B4.**

```bash
bash -n sas.sh   # -n : "no exec" → bash lit et vérifie la SYNTAXE sans rien exécuter
chmod +x sas.sh  # ajoute le droit d'exécution, sinon ./sas.sh → "Permission denied"
```

## Partie C — La tournée des essais

**C1.**

```bash
./sas.sh billet-valide.txt
echo "Code : $?"              # $? = code de retour de la DERNIÈRE commande terminée
./sas.sh billet-refuse.txt
echo "Code : $?"
./sas.sh absent.txt           # le fichier n'existe pas → garde B2
echo "Code : $?"
./sas.sh                      # aucun argument → garde B1
echo "Code : $?"
./sas.sh .                    # "." existe mais c'est un dossier → -f échoue
echo "Code : $?"
```

Codes attendus : **0, 1, 2, 2, 2**.

> **Piège classique.** `$?` ne vaut que pour la **dernière** commande exécutée. Si tu lances
> `./sas.sh fichier`, puis un `ls`, puis le `echo`, tu lis le code de `ls` et non celui du script.
> D'où la consigne : le `echo "Code : $?"` vient **immédiatement** après le lancement.
>
> **Pas d'inquiétude pour les `exit`** : ils ne ferment pas ta session SSH. Le script s'exécute
> dans un **processus enfant**, et `exit` ne termine que ce processus-là. Ce serait différent
> avec `source sas.sh`, qui exécute le script dans ton shell courant.

**C2.**

```bash
cp billet-valide.txt "billet equipe.txt"   # guillemets : sinon cp verrait 3 arguments
./sas.sh "billet equipe.txt"               # idem à l'appel : un seul argument, pas deux
echo "Code : $?"
```

Résultat : sas ouvert, code 0.

> **Essaie aussi sans guillemets** : `./sas.sh billet equipe.txt`. Le shell découpe le nom en
> deux mots, le script reçoit donc 2 arguments, la garde B1 se déclenche et renvoie le code 2.
> Une seule manipulation qui montre à la fois l'utilité des guillemets et celle de la garde.

**C3.** La garde sur `$#` évite de poursuivre sans le fichier attendu.

> **Réponse détaillée.** Si l'argument manque, `$1` vaut une **chaîne vide** : Bash ne
> signale rien. Le script continuerait avec `billet=""` et afficherait un message bancal
> (« Billet absent ou illisible :  »), sans jamais dire comment l'utiliser correctement.
> Règle générale : on valide les entrées **avant** de s'en servir, et on explique l'usage attendu.

## Bonus — Le menu de la station

<!-- fichier: menu.sh -->
```bash
#!/usr/bin/env bash
# read -p : affiche l'invite puis attend une saisie, rangée dans la variable "choix"
read -p '1 : radio ; 2 : reserve — choix : ' choix

# case = aiguillage sur une valeur ; plus lisible qu'une pile de if/elif
# Chaque branche se termine par ;;  et le bloc entier se ferme par esac (case à l'envers)
case "$choix" in
    1) echo 'Radio disponible' ;;
    2) echo 'Reserve disponible' ;;
    *) echo 'Choix inconnu' >&2; exit 2 ;;   # * = motif "tout le reste" → à mettre en dernier
esac
```

Tester les saisies `1`, `2` et `x`. Les deux premières réussissent ; la dernière renvoie 2.

> **Deux points importants sur `case`.** Les motifs sont des **motifs de fichiers** (globs),
> pas des expressions régulières : `1|radio)` accepterait les deux réponses, `[0-9])` tous les
> chiffres. Et le `*)` final joue le rôle du `else` : il doit rester **en dernier**, car placé
> avant les autres il attraperait tout et les branches suivantes ne serviraient jamais.

[← Énoncé du TP](https://kayasam.github.io/linux-initiation/bash/04-tests-et-conditions/tp)
