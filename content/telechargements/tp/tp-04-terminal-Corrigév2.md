# TP 04 — Le terminal — Corrigév2

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
