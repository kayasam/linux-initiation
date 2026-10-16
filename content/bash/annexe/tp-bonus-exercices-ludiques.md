---
title: "TP bonus — Trois jeux dans le terminal"
aliases: ["bash/ateliers/tp-bonus-exercices-ludiques"]
---

<nav class="chapter-resources workshop-resources" aria-label="Ressources de l’atelier" data-workshop-key="bash/annexe/tp-bonus-exercices-ludiques"><div class="resource-buttons"><a class="resource-button" href="https://kayasam.github.io/linux-initiation/bash/annexe/tp-bonus-exercices-ludiques" aria-current="page"><span class="resource-icon"><svg class="resource-symbol" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 7h10c4 0 6 10 3 11-2 1-4-3-5-3H9c-1 0-3 4-5 3C1 17 3 7 7 7Z"/><path d="M6 10v4M4 12h4M15 11h.01M18 13h.01"/></svg></span><span class="resource-label">Énoncé</span></a><a class="resource-button" href="https://kayasam.github.io/linux-initiation/bash/annexe/tp-bonus-exercices-ludiques-corrigev2"><span class="resource-icon"><svg class="resource-symbol" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="m5 12 4 4L19 6"/></svg></span><span class="resource-label">Corrigé v2</span></a></div><div class="resource-actions"><a class="resource-download" href="https://kayasam.github.io/linux-initiation/telechargements/bash/tp/tp-bonus-exercices-ludiques.md" download aria-label="Télécharger ce support en Markdown">↓ Télécharger .md</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>

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

[Correction du TP](https://kayasam.github.io/linux-initiation/bash/annexe/tp-bonus-exercices-ludiques-corrigev2)

[← Parcours Bash](https://kayasam.github.io/linux-initiation/#bash)

<a href="https://kayasam.github.io/linux-initiation/telechargements/bash/tp/tp-bonus-exercices-ludiques.md" download>Télécharger le TP en Markdown</a>
