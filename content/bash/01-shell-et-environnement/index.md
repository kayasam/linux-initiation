---
title: "01. Le shell et son environnement"
---

# Chapitre 01 — Le shell et son environnement

> [!TIP] Ressources du chapitre
> - [Version HTML interactive](https://kayasam.github.io/linux-initiation/bash/cours/01-shell-et-environnement-interactif.html)
> - <a href="https://kayasam.github.io/linux-initiation/telechargements/bash/cours/01-shell-et-environnement.md" download>Télécharger le cours en Markdown</a>
> - [Passer au TP](https://kayasam.github.io/linux-initiation/bash/01-shell-et-environnement/tp)


> [name=Samuel GUILLARD <sguillard@jehann.fr>]
> [time=2026-04-27]

[TOC]

---

## 1. Qu'est-ce que le shell ?

http://aral.iut-rodez.fr/fr/sanchis/enseignement/bash/ch01-Introduction-a-Bash.html#idm47 :

> Sous Unix, on appelle *shell* l'interpréteur de commandes qui fait office d'interface entre l'utilisateur et le système d'exploitation. Les shells sont des interpréteurs : cela signifie que chaque commande saisie par l'utilisateur (ou lue à partir d'un fichier) est syntaxiquement vérifiée puis exécutée.
>
> Un shell possède un double aspect :
> - un aspect *environnement interactif de travail*
> - un aspect *langage de programmation*

> [!NOTE]
> Le mot *shell* vient de l'anglais : c'est la "coquille" qui entoure le noyau (*kernel*) du système. Tu interagis avec la coquille, pas directement avec le noyau.
### Le prompt

Quand tu ouvres un terminal, le shell affiche un **prompt** — le signe qui indique qu'il est prêt à recevoir une commande.

```
samuel@debian:~$         ← utilisateur normal
root@debian:~#           ← superutilisateur (root)
```

Le prompt affiche en général : `utilisateur@machine:répertoire$`

---

## 2. Les différents shells

Il existe plusieurs shells. Ils partagent la même idée de base mais diffèrent par leur syntaxe et leurs fonctionnalités.

| Shell | Nom complet | Notes |
|-------|------------|-------|
| `sh` | Bourne Shell | Shell historique (1977), base commune, standard POSIX |
| `bash` | Bourne Again Shell | Standard sur la plupart des Linux, on l'utilise dans ce cours |
| `zsh` | [Z Shell](https://zsh.sourceforge.io/) | Shell par défaut de macOS et Kali Linux, plus puissant en interactif |
| `dash` | Debian Almquist Shell | Très rapide, utilisé par Debian/Ubuntu pour les scripts système |
| `fish` | [Friendly Interactive Shell](https://fr.wikipedia.org/wiki/Friendly_Interactive_Shell) | Moderne, pensé pour la facilité d'utilisation |

> [!TIP]
> **Dans ce cours, on travaille avec `bash`.** C'est le shell le plus répandu sur Linux et celui que tu trouveras sur presque tous les serveurs.
https://ftp.traduc.org/doc-vf/guides/Bash-Beginners-Guide/Bash-Beginners-Guide.html#sect_01_02 :

> **sh** ou Bourne Shell : le Shell originel toujours en vigueur sur les systèmes UNIX. C'est le Shell de base, un petit programme avec peu de possibilités. Il est disponible sur les systèmes Linux par souci de compatibilité.
>
> **bash** ou Bourne Again shell : le Shell standard GNU, intuitif et souple. Sur Linux, **bash** est le Shell standard pour l'utilisateur courant. C'est un *sur-ensemble* du Bourne Shell : les commandes reconnues par **sh** le sont aussi par **bash**, mais l'inverse n'est pas toujours vrai. Bash peut exécuter la plupart des scripts sh sans modification.

> [!NOTE]
> Sur la plupart des systèmes modernes, `sh` est un lien symbolique vers un autre shell (souvent `bash` ou `dash`), car le Bourne Shell d'origine n'est plus utilisé.
Pour connaître le shell que tu utilises en ce moment :

```bash
echo $SHELL        # shell configuré pour ton utilisateur
echo $0            # shell du processus courant
```

Pour lister les shells disponibles sur le système :

```bash
cat /etc/shells
```

Pour aller plus loin : [tableau comparatif de tous les shells](https://en.wikipedia.org/wiki/Comparison_of_command_shells) — et pour la culture : [Stephen Bourne raconte les débuts d'Unix et la conception de sh (vidéo, EN)](https://www.youtube.com/watch?v=2kEJoWfobpA)

---

## 3. Rappels — Flux, redirections et tubes

[LPI 103.4 — Utilisation des flux, des tubes et des redirections](https://learning.lpi.org/fr/learning-materials/101-500/103/103.4/)

### Les trois flux standard

Chaque commande Linux dispose de trois flux de données :

```
                 ┌─────────┐
stdin (0) ──────►│ commande │──────► stdout (1)
                 │         │──────► stderr (2)
                 └─────────┘
```

| Flux | Numéro | Défaut | Description |
|------|--------|--------|-------------|
| `stdin` | 0 | Clavier | Entrée standard — données reçues par la commande |
| `stdout` | 1 | Écran | Sortie standard — résultat normal |
| `stderr` | 2 | Écran | Sortie d'erreur — messages d'erreur |

> [!WARNING]
> `stdout` et `stderr` sont tous les deux affichés à l'écran par défaut — mais ce sont deux flux séparés. Cela a son importance quand on redirige.
### Les redirections

Des opérateurs permettent de dévier ces flux vers des fichiers. Description complète et exemples : https://abs.traduc.org/abs-fr/ch20.html

```bash
# Rediriger stdout vers un fichier (écrase le fichier s'il existe)
ls /etc > liste.txt

# Rediriger stdout et AJOUTER à la fin du fichier
ls /var >> liste.txt

# Rediriger stderr vers un fichier
ls /dossier-inexistant 2> erreurs.txt

# Rediriger stdout ET stderr vers le même fichier
ls /etc /dossier-inexistant &> tout.txt
# ou en version longue :
ls /etc /dossier-inexistant > tout.txt 2>&1

# Ignorer stderr (jeter les erreurs)
ls /dossier-inexistant 2> /dev/null
```

> [!NOTE]
> `/dev/null` est un "trou noir" : tout ce qu'on y envoie est jeté. Très utile pour ignorer les erreurs qu'on ne veut pas voir.
### Les tubes (pipes)

> Le tube `|` (*pipe* en anglais) permet à deux processus de communiquer. En pratique, il redirige la sortie stdout d'une commande vers l'entrée stdin de la suivante. ([source : Wikipedia](https://fr.wikipedia.org/wiki/Tube_(shell))) — [Le récit historique — Bell Labs](https://web.archive.org/web/20250114110838/https://www.bell-labs.com/usr/dmr/www/hist.html#pipes)

```bash
# Compter le nombre de fichiers dans /etc
ls /etc | wc -l

# Trouver les lignes contenant "error" dans un log
cat /var/log/syslog | grep "error"

# On peut enchaîner autant de tubes qu'on veut
cat /etc/passwd | grep bash | cut -d: -f1 | sort
```

> [!TIP]
> Le tube est l'une des idées les plus puissantes d'Unix : des petites commandes spécialisées, combinées ensemble, font des traitements complexes.
### Exercices — redirections et tubes

**Consignes** : écrire les commandes qui réalisent ce qui est demandé.

1. Compter le nombre d'utilisateurs existants dans l'OS (fichier `/etc/passwd`) en utilisant une **redirection d'entrée standard**.
2. Stocker dans un nouveau fichier `~/contenus_de_dossiers.txt` la liste de tous les fichiers et dossiers (y compris cachés) du dossier personnel, avec les permissions associées.
3. **Ajouter** à la fin de `~/contenus_de_dossiers.txt` la liste de tous les fichiers et dossiers (y compris cachés) dans `/tmp/`, avec les permissions.
   - Attention : ne pas confondre `/tmp` (Linux) et le dossier `temp` (Windows) ;-)
4. Stocker dans un nouveau fichier `~/messages_d_erreur.txt` le message d'erreur produit quand on essaie de lister `/dossier/inexistant/`.
5. Exécuter `find /etc -name "*.conf" -type f` en ajoutant la liste des fichiers trouvés à la fin de `~/contenus_de_dossiers.txt`, et les erreurs de permissions à la fin de `~/messages_d_erreur.txt`.
6. À partir de `~/contenus_de_dossiers.txt`, stocker uniquement les fichiers de configuration de systemd dans un nouveau fichier `~/fichiers_de_conf_systemd.txt`.

> [!TIP]
> **Solutions**
> 
> ```bash
> # 1
> wc -l < /etc/passwd
> 
> # 2
> ls -la ~ > ~/contenus_de_dossiers.txt
> 
> # 3
> ls -la /tmp/ >> ~/contenus_de_dossiers.txt
> 
> # 4
> ls -la /dossier/inexistant/ 2> ~/messages_d_erreur.txt
> 
> # 5
> find /etc -name "*.conf" -type f >> ~/contenus_de_dossiers.txt 2>> ~/messages_d_erreur.txt
> 
> # 6
> cat ~/contenus_de_dossiers.txt | grep /etc/systemd > ~/fichiers_de_conf_systemd.txt
> ```
---

## 4. Types de shell

https://learning.lpi.org/fr/learning-materials/102-500/105/105.1/105.1_01/#_types_de_shell_interactif_vs_non_interactif_et_connexion_vs_simple :

> La séquence exacte de fichiers de démarrage dépend d'un paramètre très important : le type de shell.

Bash distingue deux axes indépendants pour classer les shells :

### Login shell vs non-login shell

| Type | Quand ? | Exemple |
|------|---------|---------|
| **Login shell** | Au moment de la connexion de l'utilisateur | Connexion SSH, connexion console texte (TTY) |
| **Non-login shell** | Shell ouvert après connexion | Nouveau terminal dans une session graphique, sous-shell |

Pour tester si ton shell courant est un login shell :

```bash
shopt login_shell
# login_shell     on   ← c'est un login shell
# login_shell     off  ← ce n'est pas un login shell
```

### Interactif vs non-interactif

- Shell **interactif** : tu tapes des commandes, il répond. C'est le cas d'un terminal ouvert à la main.
- Shell **non-interactif** : aucune intervention humaine. C'est le cas d'un script ou d'une tâche cron.

> [!NOTE]
> Il existe aussi le cas rare du **shell de connexion non-interactif** : par exemple quand on envoie la sortie d'une commande directement dans une connexion SSH.
> 
> ```bash
> <commande> | ssh utilisateur@serveur
> ```
> 
> Le shell s'authentifie (connexion) mais ne répond à aucune saisie (non-interactif). Cas marginal, juste pour la culture.
> [!NOTE]
> Pourquoi c'est important ? Bash ne charge pas les mêmes fichiers de configuration selon le type de shell. C'est ce qu'on voit dans la section suivante.
---

## 5. Fichiers de configuration de Bash

Les fichiers de démarrage sont des scripts lus et exécutés automatiquement par Bash quand il démarre. Ils permettent de **personnaliser l'environnement** : prompt, variables, alias, fonctions…

Référence complète : https://learning.lpi.org/fr/learning-materials/102-500/105/105.1/105.1_01/#sec.105.1.01-IN-StartUpFiles

### Ordre de chargement

```
Connexion (login shell)
    ├── /etc/profile          (global, tous les utilisateurs)
    └── ~/.bash_profile       (ou ~/.profile ou ~/.bash_login)
            └── (charge souvent ~/.bashrc)

Nouveau terminal (interactive non-login shell)
    ├── /etc/bash.bashrc      (global)
    └── ~/.bashrc             (personnel)

Script (non-interactif)
    └── Aucun fichier de config chargé par défaut
```

### Les fichiers clés

| Fichier | Qui ? | Quand chargé ? |
|---------|-------|----------------|
| `/etc/profile` | Système | Login shell — tous les utilisateurs |
| `/etc/bash.bashrc` | Système | Shell interactif — tous les utilisateurs |
| `~/.bash_profile` | Utilisateur | Login shell |
| `~/.bashrc` | Utilisateur | Shell interactif non-login |
| `~/.bash_logout` | Utilisateur | À la déconnexion |

> [!TIP]
> **Dans la pratique**, tu mets presque tout dans `~/.bashrc` : alias, fonctions, variables personnalisées. C'est le fichier chargé à chaque fois que tu ouvres un terminal.
### /etc/skel — le modèle des nouveaux utilisateurs

Quand un compte utilisateur est créé (`useradd` ou `adduser`), les fichiers de `/etc/skel` sont copiés dans son répertoire personnel.

```bash
ls -la /etc/skel
# .bash_logout
# .bashrc
# .profile
```

Si tu veux que tous les nouveaux utilisateurs aient un `.bashrc` personnalisé, modifie `/etc/skel/.bashrc`.

### Recharger la configuration sans redémarrer

Après avoir modifié `.bashrc`, il faut le recharger dans le shell courant avec `source` (ou son équivalent POSIX `.`) :

```bash
source ~/.bashrc
# ou version courte (POSIX, compatible tous les shells) :
. ~/.bashrc
```

([Différence entre `source` et `.` selon les shells](https://unix.stackexchange.com/questions/58514/what-is-the-difference-between-and-source-in-shells))

> [!WARNING]
> Exécuter directement `bash ~/.bashrc` lance un **sous-shell** — les changements ne s'appliquent PAS au shell courant. Il faut absolument utiliser `source` ou `.`.
---

## 6. Les alias

https://learning.lpi.org/fr/learning-materials/102-500/105/105.1/105.1_03/ :

> Les alias permettent à une chaîne d'être substituée par un mot quand il est utilisé comme le premier mot d'une commande simple.

Un alias est un raccourci : un mot court qui remplace une commande plus longue.

### Syntaxe

```bash
alias nom='commande'
```

### Exemples utiles

```bash
# Navigation
alias ll='ls -lh'
alias la='ls -lha'
alias ..='cd ..'
alias ...='cd ../..'

# Sécurité — demander confirmation avant d'écraser ou supprimer
alias cp='cp -i'
alias mv='mv -i'
alias rm='rm -i'

# Réseau
alias ports='ss -tulnp'
alias myip='ip -br a'

# systemd
alias sctl='sudo systemctl'

# Mise à jour Debian/Ubuntu
alias maj='sudo apt update && sudo apt full-upgrade'
```

Pour encore plus d'idées : https://www.cyberciti.biz/tips/bash-aliases-mac-centos-linux-unix.html

### Alias temporaire vs permanent

```bash
# Temporaire (valable seulement dans ce terminal)
alias bonjour='echo "Bonjour le monde !"'

# Permanent → l'ajouter dans ~/.bashrc, puis :
source ~/.bashrc
```

Quand les alias deviennent nombreux, on peut les isoler dans `~/.bash_aliases` (sourcé automatiquement par `.bashrc` sur Debian/Ubuntu).

### Lister et supprimer les alias

```bash
# Lister tous les alias actifs
alias

# Supprimer un alias (temporairement)
unalias bonjour

# Contourner un alias ponctuellement (exécuter la vraie commande)
\rm fichier.txt     # exécute /bin/rm, pas l'alias rm='rm -i'
```

> [!TIP]
> Précéder un alias d'un antislash `\` désactive son interprétation et appelle directement l'exécutable système. Utile quand on veut contourner ponctuellement un alias.
> [!WARNING]
> Attention si tu alias des commandes système comme `rm`, `cp` ou `mv` — ces alias ne seront pas présents sur toutes les machines. Ne compte pas sur eux pour travailler sur un serveur inconnu.
Référence : https://doc.ubuntu-fr.org/alias

---

## 7. Les fonctions shell

Un alias ne peut faire qu'une chose simple. Pour des comportements plus complexes (arguments, conditions, plusieurs commandes), on utilise une **fonction**.

http://aral.iut-rodez.fr/fr/sanchis/enseignement/bash/ch14-Fonctions-shell.html

### Syntaxe

```bash
# Syntaxe recommandée
nom_fonction() {
    commandes
}

# Syntaxe équivalente
function nom_fonction {
    commandes
}
```

### Exemples

```bash
# Créer un dossier et s'y déplacer directement
mkcd() {
    mkdir -p "$1" && cd "$1"
}

# Afficher l'utilisation disque triée
du_top() {
    du -sh "$1"/* 2>/dev/null | sort -rh | head -10
}
```

### Arguments dans une fonction

Les arguments se récupèrent avec `$1`, `$2`, etc. (comme dans un script) :

```bash
saluer() {
    echo "Bonjour, $1 !"
}

saluer Samuel          # affiche : Bonjour, Samuel !
saluer "tout le monde" # affiche : Bonjour, tout le monde !
```

### Alias vs fonction — quand utiliser quoi ?

| Situation | Utiliser |
|-----------|---------|
| Renommer une commande, ajouter des options par défaut | Alias |
| Utiliser des arguments | Fonction |
| Faire plusieurs commandes enchaînées avec logique | Fonction |
| Traitement conditionnel (`if`, `for`…) | Fonction |

> [!TIP]
> Les fonctions définies dans `.bashrc` sont disponibles dans tous tes terminaux, comme les alias.
> [!WARNING]
> Tu ne peux pas définir un alias et une fonction avec le même nom. Si besoin, fais d'abord `unalias nom` avant de définir la fonction.
---

## Récapitulatif des commandes

| Commande | Description |
|----------|-------------|
| `echo $SHELL` | Affiche le shell configuré pour l'utilisateur |
| `echo $0` | Affiche le shell du processus courant (`-bash` = login shell) |
| `cat /etc/shells` | Liste les shells disponibles sur le système |
| `cat fichier` | Affiche le contenu d'un fichier |
| `shopt login_shell` | Indique si le shell courant est un login shell |
| `source ~/.bashrc` | Recharge `.bashrc` dans le shell courant |
| `. ~/.bashrc` | Équivalent POSIX de `source` |
| `nano fichier` | Ouvre un fichier dans l'éditeur nano |
| `pwd` | Affiche le répertoire courant |
| `alias nom='cmd'` | Crée un alias |
| `alias` | Liste tous les alias actifs |
| `unalias nom` | Supprime un alias |
| `\commande` | Contourne un alias et appelle l'exécutable directement |
| `grep "motif" fichier` | Affiche les lignes contenant le motif |
| `wc -l fichier` | Compte le nombre de lignes d'un fichier |
| `find /chemin -name "*.ext" -type f` | Recherche des fichiers par nom dans un dossier |
| `>` | Redirige stdout vers un fichier (écrase) |
| `>>` | Redirige stdout vers un fichier (ajoute à la fin) |
| `2>` | Redirige stderr vers un fichier (écrase) |
| `2>>` | Redirige stderr vers un fichier (ajoute à la fin) |
| `&>` | Redirige stdout et stderr vers un fichier |
| `2>&1` | Redirige stderr vers stdout |
| `<` | Utilise un fichier comme entrée stdin |
| `\|` | Tube : connecte stdout d'une commande à stdin de la suivante |
| `/dev/null` | "Trou noir" : supprime tout ce qui y est envoyé |
| `ls -la /etc/skel` | Affiche le modèle copié dans tout nouveau répertoire utilisateur |

---

> [!NOTE]
> ### À retenir
> 
> - Le **shell** est l'intermédiaire entre l'utilisateur et le système : mode interactif et mode script.
> - `bash` est le shell standard sur Linux — c'est celui qu'on utilise dans ce cours.
> - Les trois flux de données : `stdin` (0), `stdout` (1), `stderr` (2) — séparés et redirigables.
> - `>` écrase, `>>` ajoute, `2>` redirige les erreurs, `|` connecte deux commandes.
> - `/dev/null` est le trou noir — tout ce qu'on y envoie est supprimé.
> - Le shell est **login** (connexion SSH/TTY) ou **non-login** (terminal graphique) — ça détermine quels fichiers de config sont chargés.
> - `~/.bashrc` est chargé à chaque ouverture de terminal : c'est là qu'on met les alias et fonctions.
> - Recharger sans fermer le terminal : `source ~/.bashrc` ou `. ~/.bashrc`.
> - Un **alias** remplace un mot par une commande fixe ; une **fonction** peut recevoir des arguments et contenir de la logique.
---

> [!TIP]
> **TP associé** → [tp-01-environnement.md](https://kayasam.github.io/linux-initiation/bash/01-shell-et-environnement/tp)

[← Parcours Bash](https://kayasam.github.io/linux-initiation/#bash) · [Tous les TP Bash](https://kayasam.github.io/linux-initiation/bash/tp/)
