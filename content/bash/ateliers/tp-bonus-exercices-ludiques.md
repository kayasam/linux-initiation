---
title: "TP bonus — Trois jeux dans le terminal"
---

# TP bonus — Trois jeux dans le terminal

## Mission

Tu as terminé le parcours ? Choisis un jeu et construis-le avec les outils déjà vus. Chaque jeu est indépendant. Les données restent dans ton atelier Debian.

```bash
mkdir -p ~/atelier-bash/bonus
cd ~/atelier-bash/bonus
```

## Jeu A — Le compte à rebours

**A1.** Crée `depart.sh` avec son shebang. Une boucle affiche `3`, `2`, `1`, puis `Decollage !`.

**A2.** Vérifie sa syntaxe, puis lance-le. Pour les premiers essais, aucune pause n'est nécessaire.

**A3.** Bonus : demande à Bash d'attendre une seconde entre deux nombres avec `sleep 1`. Cette commande met en pause le programme ; elle ne change pas le compteur.

## Jeu B — Le quiz de la station

**B1.** Crée `quiz.sh`. Initialise `score=0`.

**B2.** Pose trois questions avec `read -p` :

1. Quel shell utilisons-nous ? Réponse : `Bash` ou `bash`.
2. Quel outil du cours calcule une somme par colonnes ? Réponse : `awk`.
3. Quel code indique généralement la réussite d'une commande ? Réponse : `0`.

**B3.** Utilise `case` ou `if` pour ajouter un point par bonne réponse. Affiche `Score : N/3`.

**B4.** Si la saisie est interrompue par une fin d'entrée (**Ctrl+D** sur une ligne vide), affiche `Saisie interrompue` et termine avec le code 2. Indice : `if ! read ...; then ... fi`.

**B5.** Teste trois bonnes réponses, puis trois mauvaises. Un score de 0 n'est pas une panne du programme : le quiz s'est bien déroulé et peut se terminer avec le code 0.

## Jeu C — Le trésor caché

**C1.** Crée `tresor.sh`. Pour pouvoir vérifier tes essais, fixe d'abord `secret=7` et `essais=0`.

**C2.** Tant que le nombre d'essais valides est inférieur à 3, demande un chiffre de 0 à 9.

**C3.** Vérifie la saisie avec `case` : le motif `[0-9]` accepte exactement un chiffre. Une autre saisie affiche un message puis passe au tour suivant avec `continue`, sans compter d'essai.

**C4.** Compte chaque chiffre valide. S'il égale le secret, affiche `Tresor trouve` et termine avec 0. Sinon, indique `Plus grand` ou `Plus petit`.

**C5.** Après trois essais valides ratés, affiche le secret et termine avec 1. Une fin d'entrée doit terminer avec 2.

**C6.** Teste : réussite immédiate avec `7` ; réussite après `4` puis `7` ; défaite avec `1`, `2`, `3` ; saisie invalide `chat` suivie de `7`.

**Défi supplémentaire :** une fois les tests réussis, remplace la valeur fixe par `$((RANDOM % 10))`. Bash fournit `RANDOM`, un entier pseudo-aléatoire ; le reste de la division par 10 fournit ici une valeur de 0 à 9. Garde la version fixe pour reproduire tes essais.

## Livraison

Montre ton jeu à un camarade. Il doit pouvoir comprendre les questions, essayer une mauvaise réponse et quitter proprement. Explique les cas testés, pas seulement la réussite.

[← Parcours Bash](https://kayasam.github.io/linux-initiation/#bash)

<a href="https://kayasam.github.io/linux-initiation/telechargements/bash/tp/tp-bonus-exercices-ludiques.md" download>Télécharger le TP en Markdown</a>
