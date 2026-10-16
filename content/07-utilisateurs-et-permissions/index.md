---
title: "07. Utilisateurs et permissions"
---

# Chapitre 07 — Utilisateurs et permissions

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="07-utilisateurs-et-permissions" style="--resource-count:4"><div class="resource-buttons"><a class="resource-button resource-markdown" data-resource-kind="markdown" aria-label="Cours — Lire le cours en Markdown" href="https://kayasam.github.io/linux-initiation/07-utilisateurs-et-permissions/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg></span><span class="resource-label">Cours<small>Lire le cours en Markdown</small></span></a><a class="resource-button resource-html" data-resource-kind="html" aria-label="HTML — Explorer le chapitre" href="https://kayasam.github.io/linux-initiation/07-utilisateurs-et-permissions/html/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 28 32"><path d="M2 2h24l-2 25-10 3-10-3Z" fill="#e44d26"/><path d="M14 5v22l7-2 2-20Z" fill="#f16529"/><path d="M7 8h15l-.3 3H11l.3 3h10l-.8 9-6.5 2-6.5-2-.4-5h3l.2 2.6 3.7 1 3.7-1 .3-3.6H8Z" fill="#fff"/></svg></span><span class="resource-label">HTML<small>Explorer le chapitre</small></span></a><a class="resource-button resource-quiz" data-resource-kind="quiz" aria-label="Quiz — 20 questions" href="https://kayasam.github.io/linux-initiation/07-utilisateurs-et-permissions/quiz/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="4" y="3" width="24" height="26" rx="6" fill="#7652ad"/><path d="M12 12a4 4 0 1 1 6 3.5c-1.5.8-2 1.4-2 3" fill="none" stroke="#fff" stroke-width="2.8" stroke-linecap="round"/><circle cx="16" cy="23" r="1.6" fill="#fff"/></svg></span><span class="resource-label">Quiz<small>20 questions</small></span></a><a class="resource-button resource-tp" data-resource-kind="tp" aria-label="TP — Mettre en pratique" href="https://kayasam.github.io/linux-initiation/07-utilisateurs-et-permissions/tp"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg></span><span class="resource-label">TP<small>Mettre en pratique</small></span></a></div><div class="resource-actions"><a class="resource-download" href="https://kayasam.github.io/linux-initiation/telechargements/cours/07-utilisateurs-et-permissions.md" download aria-label="Télécharger le cours en Markdown"><span aria-hidden="true">↓</span> Télécharger .md</a><a class="resource-download resource-pdf" href="https://kayasam.github.io/linux-initiation/telechargements/cours/07-utilisateurs-et-permissions.pdf?v=38be07571752" download aria-label="Télécharger le cours en PDF"><span aria-hidden="true">↓</span> PDF</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>


---

## 1. Pourquoi des utilisateurs et des permissions ?

Linux est un système **multi-utilisateurs** : plusieurs personnes peuvent utiliser la même machine, chacune avec son propre espace et ses propres droits. Les permissions garantissent que chaque utilisateur ne peut accéder qu'à ce qui lui appartient ou lui est autorisé.

> [!NOTE]
> **Analogie** : imagine un immeuble. Chaque locataire a sa clé (son compte). Il peut entrer dans son appartement (son `/home`) mais pas chez les voisins. Le gardien (root) a un passe-partout.
---

## 2. Les utilisateurs

### Le compte root

`root` est le **superutilisateur** — il a tous les droits sur le système. Il peut tout lire, modifier, supprimer.

> [!DANGER]
> On n'utilise **jamais root pour le travail courant**. Une erreur en root peut détruire le système entier. On utilise un compte normal et on élève les privilèges uniquement quand nécessaire.
### Les comptes utilisateurs

Chaque personne a son propre compte avec un nom, un mot de passe et un dossier personnel.

```bash
whoami        # affiche le nom de l'utilisateur courant
id            # affiche l'UID, le GID et les groupes
who           # liste les utilisateurs connectés
```

### La commande sudo

`sudo` (*Superuser Do*) permet d'exécuter une commande **avec les droits root** sans se connecter en tant que root :

```bash
sudo apt update          # mise à jour avec les droits admin
sudo nano /etc/hosts     # modifier un fichier système
```

Linux demande ton mot de passe pour confirmer.

---

## 3. Les groupes

Un **groupe** rassemble plusieurs utilisateurs qui partagent les mêmes droits sur certaines ressources.

```bash
groups              # affiche les groupes de l'utilisateur courant
cat /etc/group      # liste tous les groupes du système
```

---

## 4. Gérer les utilisateurs

Ces commandes nécessitent les droits root (`sudo`) :

```bash
# Créer un utilisateur
sudo adduser alice          # interactif — demande le mot de passe et les infos

# Changer le mot de passe
sudo passwd alice

# Ajouter un utilisateur à un groupe
sudo usermod -aG sudo alice    # donne les droits sudo à alice

# Supprimer un utilisateur
sudo deluser alice
sudo deluser --remove-home alice    # supprime aussi son dossier personnel
```

---

## 5. Les permissions

### Lire les permissions

```bash
ls -l
```

Exemple de sortie :
```
-rw-r--r--  1  stagiaire  stagiaire  1234  28 avr  notes.txt
drwxr-xr-x  2  stagiaire  stagiaire  4096  28 avr  Documents/
```

Décomposons la première colonne `-rw-r--r--` :

```
- rw- r-- r--
│ │   │   └── autres utilisateurs : lecture seule
│ │   └─────── groupe : lecture seule
│ └─────────── propriétaire : lecture + écriture
└───────────── type : - fichier  d dossier  l lien
```

### Les trois droits

| Lettre | Droit | Sur un fichier | Sur un dossier |
|--------|-------|----------------|----------------|
| `r` | **read** — lire | Lire le contenu | Lister le contenu |
| `w` | **write** — écrire | Modifier le contenu | Créer / supprimer des fichiers |
| `x` | **execute** — exécuter | Lancer le fichier | Entrer dans le dossier |

### Les trois catégories

| Catégorie | Symbole | Signification |
|-----------|---------|--------------|
| Propriétaire | `u` (*user*) | La personne qui possède le fichier |
| Groupe | `g` (*group*) | Les membres du groupe associé |
| Autres | `o` (*others*) | Tous les autres utilisateurs |

---

## 6. Modifier les permissions — `chmod`

### Mode symbolique (facile à lire)

```bash
chmod u+x script.sh      # ajoute le droit d'exécution au propriétaire
chmod g-w fichier.txt    # retire le droit d'écriture au groupe
chmod o+r rapport.txt    # donne le droit de lecture aux autres
chmod a+x script.sh      # donne l'exécution à tous (a = all)
```

### Mode numérique (rapide et précis)

Chaque droit a une valeur : `r=4`, `w=2`, `x=1`

On additionne les valeurs pour chaque catégorie :

| Valeur | Droits |
|--------|--------|
| `7` | `rwx` (4+2+1) |
| `6` | `rw-` (4+2) |
| `5` | `r-x` (4+1) |
| `4` | `r--` (4) |
| `0` | `---` (rien) |

```bash
chmod 644 fichier.txt    # rw-r--r-- (standard pour un fichier)
chmod 755 script.sh      # rwxr-xr-x (standard pour un script)
chmod 700 secret.txt     # rwx------ (uniquement pour le propriétaire)
```


<!-- illustration-07 -->
![Lire les trois blocs de permissions et leur valeur numérique.](https://kayasam.github.io/linux-initiation/ressources/images/07-permissions-utilisateur-groupe-autres.svg)

*Lire les trois blocs de permissions et leur valeur numérique.*

---

## 7. Changer le propriétaire — `chown`

```bash
sudo chown alice fichier.txt          # change le propriétaire
sudo chown alice:stagiaires fichier.txt  # change propriétaire ET groupe
sudo chown -R alice /home/alice/      # récursif sur tout un dossier
```

---

## 8. Exemples concrets

```bash
# Créer un script et le rendre exécutable
touch monscript.sh
chmod +x monscript.sh

# Protéger un fichier — lecture seule pour tout le monde
chmod 444 confidentiel.txt

# Donner accès à un dossier à tout le monde
chmod 755 partage/

# Vérifier qui possède un fichier
ls -l fichier.txt
```

---

## Récapitulatif des commandes

| Commande | Description |
|----------|-------------|
| `whoami` | Affiche l'utilisateur courant |
| `id` | Affiche UID, GID et groupes |
| `groups` | Liste les groupes de l'utilisateur |
| `who` | Liste les utilisateurs connectés |
| `sudo commande` | Exécute avec les droits root |
| `sudo adduser nom` | Crée un nouvel utilisateur |
| `sudo passwd nom` | Change le mot de passe |
| `sudo usermod -aG groupe nom` | Ajoute un utilisateur à un groupe |
| `sudo deluser nom` | Supprime un utilisateur |
| `ls -l` | Affiche les permissions des fichiers |
| `chmod permissions fichier` | Modifie les permissions |
| `sudo chown user fichier` | Change le propriétaire |

---

> [!NOTE]
> ### À retenir
>
> - Chaque fichier appartient à un **utilisateur** et à un **groupe**, et possède des droits d'accès.
> - **Ne jamais travailler en root** au quotidien — utiliser `sudo` pour les opérations ponctuelles.
> - Les droits se lisent en trois blocs : propriétaire (`u`), groupe (`g`), autres (`o`).
> - Les trois droits : `r` lire, `w` écrire, `x` exécuter (fichier) / entrer (dossier).
> - `chmod` modifie les permissions — mode symbolique (`u+x`) ou numérique (`755`, `644`).
> - `chown` change le propriétaire d'un fichier ou dossier.
> - Valeurs numériques : `r=4`, `w=2`, `x=1` — ex : `7 = rwx`, `6 = rw-`, `4 = r--`.
---

> [!TIP]
> **TP associé** → `tp-07-permissions.md`
---

---

[← L'arborescence Linux](https://kayasam.github.io/linux-initiation/06-arborescence-linux/) · [Chapitre suivant →](https://kayasam.github.io/linux-initiation/08-gestion-des-paquets/)
