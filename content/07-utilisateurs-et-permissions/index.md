---
title: "07. Utilisateurs et permissions"
---

# Chapitre 07 — Utilisateurs et permissions

> [!TIP] Ressources du chapitre
> - [Ouvrir le chapitre interactif](https://kayasam.github.io/linux-initiation/cours/07-utilisateurs-et-permissions-interactif.html)
> - [Faire le quiz](https://kayasam.github.io/linux-initiation/cours/quiz/07-utilisateurs-et-permissions.html)
> - <a href="https://kayasam.github.io/linux-initiation/telechargements/cours/07-utilisateurs-et-permissions.md" download>Télécharger ce cours en Markdown</a>
> - [Passer au TP](https://kayasam.github.io/linux-initiation/07-utilisateurs-et-permissions/tp)


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
