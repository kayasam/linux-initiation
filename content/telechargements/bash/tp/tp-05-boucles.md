# TP 05 — Programmer le robot copieur

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

**A2.** Liste le dossier `messages` avec `ls -l`. Identifie les trois fichiers texte, le fichier image et le dossier dont le nom finit par `.txt`.

## Partie B — Construire le robot

Crée `copieur.sh` en t'aidant de l'exemple du cours.

**B1.** Accepte zéro ou un argument. Sans argument, utilise `messages`. Si le dossier n'existe pas, affiche une erreur et termine avec le code 2.

**B2.** Crée un dossier `copies` à l'intérieur du dossier choisi. Prévois un message et un code 1 si cette création échoue.

**B3.** Initialise le compteur à 0, puis parcours `"$source"/*.txt`.

**B4.** Pour chaque élément :

1. S'il n'est pas un fichier ordinaire, passe au suivant.
2. Copie-le dans `copies`, en conservant les guillemets.
3. En cas d'échec de la copie, affiche une erreur et termine avec le code 1.
4. Sinon, augmente le compteur.

**B5.** Affiche `Copies realisees : N`, avec le vrai nombre, puis vérifie la syntaxe.

## Partie C — Les essais pièges

**C1.** Lance le robot sur `messages`. Attendu : **3 copies**. Vérifie les contenus des copies et la présence des originaux.

**C2.** Relance-le : il remplace les copies de même nom, sans créer de doublon. Le résultat reste 3.

**C3.** Lance-le sur `vide`. Attendu : **0 copie**, pas une erreur.

**C4.** Lance-le sur un dossier inexistant. Attendu : message d'erreur, code 2.

**C5.** Explique pourquoi le dossier `faux.txt` et le fichier `photo.png` ne sont pas copiés.

## Bonus — L'appel de l'équipage

Crée un fichier `equipe.txt` contenant `Mila Vega` et `Noe`, une personne par ligne. Parcours-le avec `while IFS= read -r personne` et affiche une ligne d'accueil par personne.

**Défi supplémentaire :** essaie une dernière ligne sans retour à la ligne. Pour la conserver, utilise cette condition : `while IFS= read -r personne || [[ -n "$personne" ]]; do`. Explique pourquoi le deuxième test permet de traiter la valeur encore présente.

## Mission accomplie si…

Tu obtiens les nombres **3, 3 et 0**, les noms composés restent intacts et l'erreur de dossier renvoie 2.

[← Revenir au cours](https://kayasam.github.io/linux-initiation/bash/05-boucles/)
