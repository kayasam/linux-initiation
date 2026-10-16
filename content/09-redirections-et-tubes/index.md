---
title: "09. Redirections et tubes"
---

# Chapitre 09 — Redirections et tubes

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="09-redirections-et-tubes" style="--resource-count:4"><div class="resource-buttons"><a class="resource-button resource-markdown" data-resource-kind="markdown" aria-label="Cours — Lire le cours en Markdown" href="https://kayasam.github.io/linux-initiation/09-redirections-et-tubes/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg></span><span class="resource-label">Cours<small>Lire le cours en Markdown</small></span></a><a class="resource-button resource-html" data-resource-kind="html" aria-label="HTML — Explorer le chapitre" href="https://kayasam.github.io/linux-initiation/09-redirections-et-tubes/html/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 28 32"><path d="M2 2h24l-2 25-10 3-10-3Z" fill="#e44d26"/><path d="M14 5v22l7-2 2-20Z" fill="#f16529"/><path d="M7 8h15l-.3 3H11l.3 3h10l-.8 9-6.5 2-6.5-2-.4-5h3l.2 2.6 3.7 1 3.7-1 .3-3.6H8Z" fill="#fff"/></svg></span><span class="resource-label">HTML<small>Explorer le chapitre</small></span></a><a class="resource-button resource-quiz" data-resource-kind="quiz" aria-label="Quiz — 20 questions" href="https://kayasam.github.io/linux-initiation/09-redirections-et-tubes/quiz/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="4" y="3" width="24" height="26" rx="6" fill="#7652ad"/><path d="M12 12a4 4 0 1 1 6 3.5c-1.5.8-2 1.4-2 3" fill="none" stroke="#fff" stroke-width="2.8" stroke-linecap="round"/><circle cx="16" cy="23" r="1.6" fill="#fff"/></svg></span><span class="resource-label">Quiz<small>20 questions</small></span></a><a class="resource-button resource-tp" data-resource-kind="tp" aria-label="TP — Mettre en pratique" href="https://kayasam.github.io/linux-initiation/09-redirections-et-tubes/tp"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg></span><span class="resource-label">TP<small>Mettre en pratique</small></span></a></div><div class="resource-actions"><a class="resource-download" href="https://kayasam.github.io/linux-initiation/telechargements/cours/09-redirections-et-tubes.md" download aria-label="Télécharger le cours en Markdown"><span aria-hidden="true">↓</span> Télécharger .md</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>



---

## 1. Les trois flux de données

Chaque commande Linux travaille avec trois canaux de communication :

```
              ┌─────────┐
clavier ─────►│ commande │──────► écran (résultat)
              │         │──────► écran (erreurs)
              └─────────┘
```

| Flux | Numéro | Défaut | Description |
|------|--------|--------|-------------|
| `stdin` | 0 | Clavier | Ce que reçoit la commande |
| `stdout` | 1 | Écran | Le résultat normal |
| `stderr` | 2 | Écran | Les messages d'erreur |

> [!NOTE]
> **Analogie** : imagine une machine à café. Tu mets des grains (stdin), tu obtiens du café (stdout), et si quelque chose cloche la machine affiche une erreur (stderr). Les redirections te permettent de changer d'où viennent les grains et où va le café.
---

## 2. Rediriger la sortie vers un fichier

### `>` — écrire dans un fichier (écrase)

```bash
ls /etc > liste.txt         # sauvegarde le résultat dans liste.txt
date > date_du_jour.txt     # écrit la date dans un fichier
```

> [!DANGER]
> `>` **écrase** le fichier s'il existe déjà. Son contenu précédent est perdu.
### `>>` — ajouter à la fin d'un fichier

```bash
echo "Ligne 1" > journal.txt    # crée le fichier avec "Ligne 1"
echo "Ligne 2" >> journal.txt   # ajoute "Ligne 2" à la fin
echo "Ligne 3" >> journal.txt   # ajoute "Ligne 3" à la fin
cat journal.txt
# Ligne 1
# Ligne 2
# Ligne 3
```

### `2>` — rediriger les erreurs

```bash
ls /dossier-inexistant 2> erreurs.txt   # redirige l'erreur dans un fichier
ls /etc /dossier-inexistant &> tout.txt # redirige résultat ET erreurs
```

### Jeter les erreurs — `/dev/null`

```bash
ls /dossier-inexistant 2> /dev/null    # l'erreur disparaît silencieusement
```

`/dev/null` est le "trou noir" de Linux — tout ce qu'on y envoie est supprimé.

---

## 3. Les tubes (pipes) — `|`

Le tube `|` connecte la **sortie d'une commande** à l'**entrée de la suivante**. C'est l'outil le plus puissant du terminal Linux.

> [!NOTE]
> **Analogie** : un tube de plomberie. L'eau sort d'un robinet (commande 1) et entre directement dans le seau (commande 2) sans toucher le sol.
```bash
commande1 | commande2 | commande3
```

### Exemples

```bash
# Compter les fichiers dans /etc
ls /etc | wc -l

# Chercher un mot dans la liste des processus
ps aux | grep firefox

# Voir les 5 premières lignes de la liste des paquets installés
apt list --installed | head -5

# Chercher un utilisateur dans /etc/passwd
cat /etc/passwd | grep stagiaire

# Combiner tri et comptage
ls /etc | sort | uniq | wc -l
```


<!-- illustration-09 -->
![Observer les lignes qui passent d’une commande à la suivante.](https://kayasam.github.io/linux-initiation/ressources/images/09-tubes-et-circulation-des-donnees.svg)

*Observer les lignes qui passent d’une commande à la suivante.*

---

## 4. Rechercher du texte — `grep`

`grep` filtre les lignes qui contiennent un motif :

```bash
grep "erreur" /var/log/syslog          # lignes contenant "erreur"
grep -i "erreur" /var/log/syslog       # insensible à la casse
grep -n "root" /etc/passwd             # avec numéro de ligne
grep -v "commentaire" fichier.conf     # lignes qui NE contiennent PAS le motif
grep -r "mot" /etc/                    # recherche récursive dans un dossier
```

### `grep` combiné avec un tube

```bash
# Chercher les erreurs dans les logs
cat /var/log/syslog | grep -i "error"

# Compter les erreurs
grep -i "error" /var/log/syslog | wc -l

# Trouver les utilisateurs avec bash
cat /etc/passwd | grep "/bin/bash"
```

---

## 5. Quelques commandes de traitement utiles

| Commande | Rôle |
|----------|------|
| `wc -l` | Compte le nombre de lignes |
| `sort` | Trie les lignes par ordre alphabétique |
| `sort -n` | Trie numériquement |
| `uniq` | Supprime les lignes en double (après un `sort`) |
| `head -n 5` | Affiche les 5 premières lignes |
| `tail -n 5` | Affiche les 5 dernières lignes |
| `cut -d: -f1` | Coupe selon un séparateur et garde le 1er champ |

```bash
# Afficher uniquement les noms d'utilisateurs depuis /etc/passwd
cut -d: -f1 /etc/passwd | sort

# Trouver les 3 plus gros fichiers dans /var/log
du -sh /var/log/* 2>/dev/null | sort -rh | head -3
```

---

## Récapitulatif des commandes

| Commande / Symbole | Description |
|-------------------|-------------|
| `commande > fichier` | Redirige stdout vers un fichier (écrase) |
| `commande >> fichier` | Ajoute stdout à la fin d'un fichier |
| `commande 2> fichier` | Redirige stderr vers un fichier |
| `commande &> fichier` | Redirige stdout et stderr vers un fichier |
| `commande 2> /dev/null` | Jette les erreurs |
| `cmd1 \| cmd2` | Connecte la sortie de cmd1 à l'entrée de cmd2 |
| `grep "motif" fichier` | Filtre les lignes contenant le motif |
| `grep -i` | Insensible à la casse |
| `grep -v` | Lignes qui ne contiennent PAS le motif |
| `wc -l` | Compte les lignes |
| `sort` | Trie les lignes |
| `head -n N` | Affiche les N premières lignes |
| `tail -n N` | Affiche les N dernières lignes |
| `cut -d: -f1` | Découpe une ligne selon un séparateur |

---

> [!NOTE]
> ### À retenir
>
> - Chaque commande a trois flux : `stdin` (entrée), `stdout` (résultat), `stderr` (erreurs).
> - `>` redirige stdout vers un fichier en **écrasant** ; `>>` **ajoute** à la fin.
> - `2>` redirige uniquement les erreurs ; `&>` redirige les deux.
> - `/dev/null` est le trou noir du système — tout ce qu'on y envoie est supprimé.
> - Le **tube** `|` connecte la sortie d'une commande à l'entrée de la suivante.
> - `grep "motif"` filtre les lignes contenant un texte — indispensable combiné aux tubes.
> - `wc -l` compte les lignes, `sort` trie, `head`/`tail` extraient le début/la fin.
---

> [!TIP]
> **TP associé** → `tp-09-redirections.md`
---

---

[← Gestion des paquets](https://kayasam.github.io/linux-initiation/08-gestion-des-paquets/) · [Chapitre suivant →](https://kayasam.github.io/linux-initiation/10-reseau-et-services/)
