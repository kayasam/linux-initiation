---
title: "Bash — TP Synthèse — Script d'audit système"
---

# TP Synthèse — Script d'audit système

> Durée estimée : 1h30

---

## Objectifs

Construire un script complet et fonctionnel en partant de zéro. Chaque étape ajoute des fonctionnalités en réutilisant tout ce qui a été vu pendant la formation :

- Structure d'un script (shebang, options de sécurité)
- Variables et substitution de commande
- Arguments et variables spéciales
- Tests sur fichiers, chaînes et nombres
- Conditions `if/elif/else`
- Boucles `for`

---

## Contexte

Tu vas écrire `audit-systeme.sh`, un script qui collecte des informations sur une machine Linux et génère un rapport lisible. Ce type de script est très courant en administration système.

À la fin, le script devra afficher quelque chose comme :

```
========================================
   RAPPORT D'AUDIT — monserveur
   2026-04-27 14:32:05
========================================

--- Informations système ---
Hostname    : monserveur
OS          : Debian GNU/Linux 13
Noyau       : 6.1.0-21-amd64
Uptime      : up 3 days, 4 hours

--- Espace disque ---
/          : 45% utilisé
/home      : 12% utilisé

--- Fichiers critiques ---
[OK]  /etc/passwd    existe et lisible
[OK]  /etc/hosts     existe et lisible
[OK]  /etc/fstab     existe et lisible
[MANQUANT]  /etc/motd

--- Utilisateurs avec bash ---
root
samuel

--- Commandes disponibles ---
[OK]  curl
[OK]  git
[ABSENT]  ansible
[OK]  vim

========================================
   Fin du rapport
========================================
```

---

## Étape 1 — Structure de base et informations système (30 min)

**Crée le fichier** `~/scripting/audit-systeme.sh` avec le contenu suivant comme point de départ :

```bash
#!/usr/bin/env bash

set -euo pipefail

# Variables
HOSTNAME_MACHINE=$(hostname)
DATE_RAPPORT=$(date '+%Y-%m-%d %H:%M:%S')
```

**1.1** Ajoute l'affichage de l'en-tête du rapport avec les séparateurs `===`, le nom de la machine et la date. Utilise des variables.

**1.2** Ajoute une section `--- Informations système ---` qui affiche :
- Le hostname
- Le nom de l'OS (contenu de `/etc/os-release`, variable `PRETTY_NAME`)
  > Indice : `source /etc/os-release` charge les variables du fichier, dont `$PRETTY_NAME`
- La version du noyau (`uname -r`)
- L'uptime (`uptime -p`)

**1.3** Rends le script exécutable et teste-le :
```bash
chmod +x ~/scripting/audit-systeme.sh
~/scripting/audit-systeme.sh
```

---

## Étape 2 — Boucles et tests (40 min)

**2.1 — Espace disque**

Ajoute une section `--- Espace disque ---` qui affiche le pourcentage d'utilisation de chaque partition montée.

> Indice : `df -h --output=target,pcent` affiche les points de montage et leur utilisation. Utilise une boucle `while read` pour traiter chaque ligne.

**2.2 — Vérification de fichiers critiques**

Définis une liste de fichiers à vérifier :
```bash
fichiers_critiques=(
    /etc/passwd
    /etc/hosts
    /etc/fstab
    /etc/motd
    /etc/ssh/sshd_config
)
```

Ajoute une section `--- Fichiers critiques ---` avec une boucle `for` qui affiche pour chaque fichier :
- `[OK]  <chemin>    existe et lisible` s'il existe et est lisible
- `[MANQUANT]  <chemin>` s'il n'existe pas

**2.3 — Utilisateurs avec bash**

Ajoute une section `--- Utilisateurs avec bash ---` qui lit `/etc/passwd` et affiche uniquement les utilisateurs dont le shell est `/bin/bash`.

> Indice : `while read -r ligne` + test sur `*"/bin/bash"` + `cut -d: -f1`

---

## Étape 3 — Argument et commandes disponibles (20 min)

**3.1 — Argument optionnel**

Modifie le script pour qu'il accepte un argument optionnel : le nom d'un fichier de sortie.

- Si aucun argument n'est passé → affiche sur le terminal (comportement actuel)
- Si un argument est passé → redirige toute la sortie vers ce fichier

> Indice : utilise `$#` pour tester si un argument existe. Si oui, redirige avec `exec > "$1"`.

**3.2 — Commandes disponibles**

Définis une liste de commandes à vérifier :
```bash
commandes=(curl git vim ansible python3 rsync)
```

Ajoute une section `--- Commandes disponibles ---` avec une boucle `for` qui affiche pour chaque commande :
- `[OK]  <commande>` si elle est installée
- `[ABSENT]  <commande>` si elle ne l'est pas

> Indice : `command -v nom > /dev/null`

**3.3** Ajoute le pied de page `=== Fin du rapport ===`.

Teste le script avec et sans argument :
```bash
./audit-systeme.sh                        # affiche dans le terminal
./audit-systeme.sh /tmp/rapport.txt       # écrit dans un fichier
cat /tmp/rapport.txt                      # vérifie le fichier
```

---

## Questions de vérification

- [ ] À quoi sert `set -euo pipefail` dans ce script ?
- [ ] Comment récupère-t-on la valeur d'une variable depuis un fichier externe (`/etc/os-release`) ?
- [ ] Pourquoi utilise-t-on `while read -r` plutôt que `for` pour lire un fichier ligne par ligne ?
- [ ] Comment tester si une commande est disponible sur le système ?
- [ ] Que fait `exec > "$1"` ?

[← Parcours Bash](https://kayasam.github.io/linux-initiation/#bash)

<a href="https://kayasam.github.io/linux-initiation/telechargements/bash/tp/tp-synthese.md" download>Télécharger le TP en Markdown</a>
