---
title: "06. L'arborescence Linux"
---

# Chapitre 06 — L'arborescence Linux

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="06-arborescence-linux" style="--resource-count:4"><div class="chapter-resources-heading"><span class="chapter-resources-title">Ressources du chapitre</span><a class="resource-download" href="https://kayasam.github.io/linux-initiation/telechargements/cours/06-arborescence-linux.md" download><span aria-hidden="true">↓</span> Télécharger le .md</a></div><div class="resource-buttons"><a class="resource-button resource-markdown" data-resource-kind="markdown" href="https://kayasam.github.io/linux-initiation/06-arborescence-linux/"><span class="resource-icon" aria-hidden="true"><img src="https://kayasam.github.io/linux-initiation/assets/resource-icons/markdown.svg" alt="" /></span><span class="resource-label">Markdown<small>Lire le cours</small></span></a><a class="resource-button resource-html" data-resource-kind="html" href="https://kayasam.github.io/linux-initiation/06-arborescence-linux/html/"><span class="resource-icon" aria-hidden="true"><img src="https://kayasam.github.io/linux-initiation/assets/resource-icons/html.svg" alt="" /></span><span class="resource-label">HTML<small>Explorer le chapitre</small></span></a><a class="resource-button resource-quiz" data-resource-kind="quiz" href="https://kayasam.github.io/linux-initiation/06-arborescence-linux/quiz/"><span class="resource-icon" aria-hidden="true"><img src="https://kayasam.github.io/linux-initiation/assets/resource-icons/quiz.svg" alt="" /></span><span class="resource-label">Quiz<small>20 questions</small></span></a><a class="resource-button resource-tp" data-resource-kind="tp" href="https://kayasam.github.io/linux-initiation/06-arborescence-linux/tp"><span class="resource-icon" aria-hidden="true"><img src="https://kayasam.github.io/linux-initiation/assets/resource-icons/tp.svg" alt="" /></span><span class="resource-label">TP<small>Mettre en pratique</small></span></a></div></nav>
<div class="support-toolbar markdown-course-toolbar"><span>Cours Markdown</span><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div>


---

## 1. Tout part de la racine

Sous Linux, il n'y a **pas de lettre de lecteur** (pas de `C:\`, `D:\` comme Windows). Il y a une seule **racine**, notée `/`, et tout le système de fichiers part de là.

```
/
├── etc/       ← configuration
├── home/      ← dossiers personnels des utilisateurs
├── var/       ← données variables (logs, bases de données…)
├── tmp/       ← fichiers temporaires
├── usr/       ← programmes installés
├── bin/       ← commandes essentielles
├── boot/      ← fichiers de démarrage
├── dev/       ← périphériques
└── ...
```

> [!NOTE]
> **Analogie** : l'arborescence Linux, c'est comme un immeuble avec des étages bien organisés. La racine `/` est le rez-de-chaussée, et chaque dossier est un étage avec un rôle précis.
Cette organisation suit le standard **FHS** (*Filesystem Hierarchy Standard*), adopté par toutes les distributions Linux.


<!-- illustration-06 -->
![Quelques repères pour retrouver les dossiers essentiels.](https://kayasam.github.io/linux-initiation/ressources/images/06-reperes-arborescence.svg)

*Quelques repères pour retrouver les dossiers essentiels.*

---

## 2. Les dossiers essentiels à connaître

### `/home` — les dossiers personnels

Chaque utilisateur a son propre dossier dans `/home` :

```
/home/
├── stagiaire/    ← dossier de l'utilisateur "stagiaire"
├── alice/
└── bob/
```

`~` est un raccourci pour ton dossier personnel. `~/Documents` = `/home/stagiaire/Documents`.

### `/etc` — la configuration du système

Contient les fichiers de configuration de tous les logiciels installés.

```bash
ls /etc
# passwd   hosts   fstab   apt/   ssh/   ...
```

Exemples importants :

| Fichier | Rôle |
|---------|------|
| `/etc/passwd` | Liste des utilisateurs du système |
| `/etc/hosts` | Correspondance noms ↔ adresses IP locales |
| `/etc/fstab` | Points de montage des disques |
| `/etc/apt/` | Configuration du gestionnaire de paquets |

### `/var` — les données variables

Contient les données qui changent en permanence : logs, bases de données, files d'attente…

```
/var/
├── log/       ← journaux système
│   ├── syslog
│   └── auth.log
├── cache/     ← cache des applications
└── lib/       ← données persistantes des applications
```

```bash
tail -f /var/log/syslog    # voir les logs en temps réel
```

### `/tmp` — les fichiers temporaires

Espace de travail temporaire. **Tout son contenu est effacé au redémarrage.**

```bash
ls /tmp    # souvent quelques fichiers de session
```

> [!WARNING]
> Ne jamais stocker des données importantes dans `/tmp` — elles seront perdues au prochain redémarrage.
### `/usr` — les programmes

Contient la majorité des programmes installés et leurs ressources.

```
/usr/
├── bin/       ← commandes utilisateur (ls, cp, grep…)
├── sbin/      ← commandes administrateur
├── lib/       ← bibliothèques partagées
└── share/     ← données partagées (docs, icônes…)
```

### `/bin` et `/sbin` — les commandes essentielles

Contiennent les commandes indispensables au démarrage du système (`ls`, `cp`, `bash`…). Sur les systèmes modernes, `/bin` est souvent un lien symbolique vers `/usr/bin`.

### `/dev` — les périphériques

Représentation des périphériques matériels sous forme de fichiers :

```bash
ls /dev/
# sda   sda1   sda2   tty   null   zero   ...
```

| Fichier | Représente |
|---------|-----------|
| `/dev/sda` | Premier disque dur |
| `/dev/sda1` | Première partition du disque |
| `/dev/null` | "Trou noir" — jette tout ce qu'on y envoie |
| `/dev/tty` | Terminal courant |

### `/boot` — le démarrage

Contient le noyau Linux et les fichiers nécessaires au démarrage (GRUB).

```bash
ls /boot
# vmlinuz-6.1.0   initrd.img-6.1.0   grub/
```

---

## 3. Comparer avec Windows

| Linux | Windows | Contenu |
|-------|---------|---------|
| `/home/utilisateur/` | `C:\Users\Nom\` | Dossier personnel |
| `/etc/` | `C:\Windows\System32\` (en partie) | Configuration système |
| `/var/log/` | Observateur d'événements | Journaux système |
| `/tmp/` | `C:\Windows\Temp\` | Fichiers temporaires |
| `/usr/bin/` | `C:\Program Files\` | Programmes installés |
| `/dev/sda` | `C:`, `D:` | Disques et partitions |

---

## 4. Commandes utiles pour explorer

```bash
df -h              # espace disque disponible sur chaque partition
du -sh /var/log    # taille du dossier /var/log
lsblk              # liste les disques et partitions
findmnt            # affiche les points de montage actifs
```

---

## Récapitulatif des dossiers clés

| Dossier | Contient |
|---------|---------|
| `/` | Racine — tout part de là |
| `/home/` | Dossiers personnels des utilisateurs |
| `/etc/` | Fichiers de configuration |
| `/var/log/` | Journaux système |
| `/tmp/` | Fichiers temporaires (effacés au redémarrage) |
| `/usr/bin/` | Programmes installés |
| `/dev/` | Périphériques matériels |
| `/boot/` | Noyau et fichiers de démarrage |
| `~` | Raccourci pour le dossier personnel |

---

> [!NOTE]
> ### À retenir
>
> - Sous Linux, tout part de la **racine `/`** — pas de lettre de lecteur comme Windows.
> - Cette organisation suit le standard **FHS** adopté par toutes les distributions.
> - `/home/` : dossiers personnels des utilisateurs — `~` est le raccourci du dossier courant.
> - `/etc/` : **configuration** de tous les logiciels installés.
> - `/var/log/` : **journaux** système, à consulter pour diagnostiquer des problèmes.
> - `/tmp/` : fichiers **temporaires**, effacés à chaque redémarrage — ne jamais y stocker des données.
> - `/usr/bin/` : la majorité des **programmes** installés.
> - `df -h` affiche l'espace disque, `du -sh` la taille d'un dossier.
---

> [!TIP]
> **TP associé** → `tp-06-arborescence.md`
---

---

[← Fichiers et répertoires](https://kayasam.github.io/linux-initiation/05-fichiers-et-repertoires/) · [Chapitre suivant →](https://kayasam.github.io/linux-initiation/07-utilisateurs-et-permissions/)
