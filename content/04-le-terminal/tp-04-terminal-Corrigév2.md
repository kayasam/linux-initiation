---
title: "TP 04 — Le terminal — Corrigév2"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="04-le-terminal" style="--resource-count:4"><div class="resource-buttons"><a class="resource-button resource-markdown" data-resource-kind="markdown" aria-label="Cours — Lire le cours en Markdown" href="https://kayasam.github.io/linux-initiation/04-le-terminal/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg></span><span class="resource-label">Cours<small>Lire le cours en Markdown</small></span></a><a class="resource-button resource-html" data-resource-kind="html" aria-label="HTML — Explorer le chapitre" href="https://kayasam.github.io/linux-initiation/04-le-terminal/html/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 28 32"><path d="M2 2h24l-2 25-10 3-10-3Z" fill="#e44d26"/><path d="M14 5v22l7-2 2-20Z" fill="#f16529"/><path d="M7 8h15l-.3 3H11l.3 3h10l-.8 9-6.5 2-6.5-2-.4-5h3l.2 2.6 3.7 1 3.7-1 .3-3.6H8Z" fill="#fff"/></svg></span><span class="resource-label">HTML<small>Explorer le chapitre</small></span></a><a class="resource-button resource-quiz" data-resource-kind="quiz" aria-label="Quiz — 20 questions" href="https://kayasam.github.io/linux-initiation/04-le-terminal/quiz/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="4" y="3" width="24" height="26" rx="6" fill="#7652ad"/><path d="M12 12a4 4 0 1 1 6 3.5c-1.5.8-2 1.4-2 3" fill="none" stroke="#fff" stroke-width="2.8" stroke-linecap="round"/><circle cx="16" cy="23" r="1.6" fill="#fff"/></svg></span><span class="resource-label">Quiz<small>20 questions</small></span></a><a class="resource-button resource-tp" data-resource-kind="tp" aria-label="TP — Mettre en pratique" href="https://kayasam.github.io/linux-initiation/04-le-terminal/tp"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg></span><span class="resource-label">TP<small>Mettre en pratique</small></span></a></div><div class="resource-actions"><a class="resource-download" href="https://kayasam.github.io/linux-initiation/telechargements/cours/04-le-terminal.md" download aria-label="Télécharger le cours en Markdown"><span aria-hidden="true">↓</span> Télécharger .md</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>

> Durée estimée : 30 min
>
> Essaie chaque question avant de cliquer sur **Afficher la correction**. Les réponses s’ouvrent et se referment indépendamment.

---

## Objectifs
Se repérer dans le terminal, naviguer dans l'arborescence et lire des fichiers.

---

**A1.** Ouvre un terminal. Quel est ton répertoire courant ?

> [!success]- Afficher la correction — A1
> ```bash
> pwd
> # /home/stagiaire
> ```
> `pwd` affiche le chemin du répertoire courant. Le résultat dépend de ton utilisateur et de ta session ; `/home/stagiaire` est un exemple.

**A2.** Liste le contenu de ton dossier personnel, d'abord en simple, puis en détail.

> [!success]- Afficher la correction — A2
> ```bash
> ls
> ls -l
> ```
> Depuis ton dossier personnel, `ls` affiche les noms ; `ls -l` ajoute notamment les permissions, le propriétaire et la taille.

**A3.** Déplace-toi dans `/etc`. Vérifie que tu y es bien.

> [!success]- Afficher la correction — A3
> ```bash
> cd /etc
> pwd
> # /etc
> ```
> `cd` change de répertoire ; `pwd` permet de vérifier le résultat.

**A4.** Remonte d'un niveau. Dans quel dossier es-tu ?

> [!success]- Afficher la correction — A4
> ```bash
> cd ..
> pwd
> # /
> ```
> `..` désigne le répertoire parent. Le parent de `/etc` est `/`, la racine.

**A5.** Va dans `/var/log` en une seule commande. Liste son contenu.

> [!success]- Afficher la correction — A5
> ```bash
> cd /var/log
> ls
> ```
> Le chemin commence par `/` : il est absolu et fonctionne quel que soit ton répertoire courant.

**A6.** Retourne dans ton dossier personnel en une seule commande.

> [!success]- Afficher la correction — A6
> ```bash
> cd        # sans argument = dossier personnel
> # ou
> cd ~
> ```
> Les deux commandes ramènent dans ton dossier personnel. Il suffit d’en choisir une.

**A7.** Affiche le contenu du fichier `/etc/hostname`. Puis affiche les 5 premières lignes de `/etc/passwd`.

> [!success]- Afficher la correction — A7
> ```bash
> cat /etc/hostname
> head -5 /etc/passwd
> ```
> `cat` affiche le fichier entier ; `head -5` limite l’affichage aux cinq premières lignes.

**A8.** Ouvre le fichier `/etc/hosts` avec `less`. Navigue dedans avec les flèches, puis quitte avec `q`.

> [!success]- Afficher la correction — A8
> ```bash
> less /etc/hosts
> # Flèches haut/bas pour naviguer, q pour quitter
> ```
> `less` permet de consulter le fichier sans le modifier. Si tout tient à l’écran, il peut ne pas y avoir de défilement visible.

**A9.** Affiche l'aide de la commande `ls` (version courte avec `--help`).

> [!success]- Afficher la correction — A9
> ```bash
> ls --help
> ```
> Cette aide présente l’utilisation de `ls` et les options disponibles.

**A10.** Affiche l'historique de tes 10 dernières commandes.

> [!success]- Afficher la correction — A10
> ```bash
> history | tail -10
> ```
> `history` affiche l’historique ; `tail -10` ne garde que ses dix dernières lignes. Avec moins de dix commandes enregistrées, la liste sera plus courte.

[← Énoncé du TP](https://kayasam.github.io/linux-initiation/04-le-terminal/tp)
