---
title: "08. Gestion des paquets"
---

# Chapitre 08 — Gestion des paquets

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="08-gestion-des-paquets" style="--resource-count:4"><div class="resource-buttons"><a class="resource-button resource-markdown" data-resource-kind="markdown" aria-label="Cours — Lire le cours en Markdown" href="https://kayasam.github.io/linux-initiation/08-gestion-des-paquets/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg></span><span class="resource-label">Cours<small>Lire le cours en Markdown</small></span></a><a class="resource-button resource-html" data-resource-kind="html" aria-label="HTML — Explorer le chapitre" href="https://kayasam.github.io/linux-initiation/08-gestion-des-paquets/html/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 28 32"><path d="M2 2h24l-2 25-10 3-10-3Z" fill="#e44d26"/><path d="M14 5v22l7-2 2-20Z" fill="#f16529"/><path d="M7 8h15l-.3 3H11l.3 3h10l-.8 9-6.5 2-6.5-2-.4-5h3l.2 2.6 3.7 1 3.7-1 .3-3.6H8Z" fill="#fff"/></svg></span><span class="resource-label">HTML<small>Explorer le chapitre</small></span></a><a class="resource-button resource-quiz" data-resource-kind="quiz" aria-label="Quiz — 20 questions" href="https://kayasam.github.io/linux-initiation/08-gestion-des-paquets/quiz/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="4" y="3" width="24" height="26" rx="6" fill="#7652ad"/><path d="M12 12a4 4 0 1 1 6 3.5c-1.5.8-2 1.4-2 3" fill="none" stroke="#fff" stroke-width="2.8" stroke-linecap="round"/><circle cx="16" cy="23" r="1.6" fill="#fff"/></svg></span><span class="resource-label">Quiz<small>20 questions</small></span></a><a class="resource-button resource-tp" data-resource-kind="tp" aria-label="TP — Mettre en pratique" href="https://kayasam.github.io/linux-initiation/08-gestion-des-paquets/tp"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg></span><span class="resource-label">TP<small>Mettre en pratique</small></span></a></div><div class="resource-actions"><a class="resource-download" href="https://kayasam.github.io/linux-initiation/telechargements/cours/08-gestion-des-paquets.md" download aria-label="Télécharger le cours en Markdown"><span aria-hidden="true">↓</span> Télécharger .md</a><a class="resource-download resource-pdf" href="https://kayasam.github.io/linux-initiation/telechargements/cours/08-gestion-des-paquets.pdf?v=49e0716ecf1b" download aria-label="Télécharger le cours en PDF"><span aria-hidden="true">↓</span> PDF</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>


---

## 1. Qu'est-ce qu'un paquet ?

Sous Linux, les logiciels sont distribués sous forme de **paquets** — des archives contenant le programme, ses dépendances et ses fichiers de configuration.

> [!NOTE]
> **Analogie** : un paquet Linux, c'est comme un meuble IKEA dans sa boîte. Tout ce qu'il faut est dedans (pièces + notice + chevilles). Le gestionnaire de paquets, c'est comme le livreur qui va chercher la boîte à l'entrepôt (dépôt) et la livre chez toi (ton système).
---

## 2. Les dépôts (repositories)

Un **dépôt** est un serveur officiel qui héberge les paquets. `apt` sait où chercher grâce aux fichiers de configuration dans `/etc/apt/`.

```bash
cat /etc/apt/sources.list      # liste des dépôts configurés
ls /etc/apt/sources.list.d/    # dépôts supplémentaires
```

---

## 3. APT — le gestionnaire de paquets Debian/Ubuntu

`apt` (*Advanced Package Tool*) est l'outil de gestion des logiciels sur Debian et Ubuntu. Il télécharge, installe, met à jour et supprime des paquets automatiquement.

### Mettre à jour la liste des paquets disponibles

```bash
sudo apt update
```

> [!WARNING]
> `apt update` ne met **pas** à jour les logiciels — il met à jour la **liste** des versions disponibles. C'est toujours la première étape avant d'installer ou de mettre à jour.
### Mettre à jour les logiciels installés

```bash
sudo apt upgrade           # met à jour tous les paquets installés
sudo apt full-upgrade      # idem + gère les changements de dépendances
```

### Installer un logiciel

```bash
sudo apt install vim           # installe vim
sudo apt install vim curl git  # installe plusieurs paquets d'un coup
```

### Supprimer un logiciel

```bash
sudo apt remove vim          # supprime le programme (garde la config)
sudo apt purge vim           # supprime le programme ET sa configuration
sudo apt autoremove          # supprime les paquets devenus inutiles
```

### Chercher un logiciel

```bash
apt search editeur-texte    # cherche un paquet par mot-clé
apt show vim                # affiche les détails d'un paquet
```

### Lister les paquets installés

```bash
apt list --installed          # tous les paquets installés
apt list --installed | grep vim  # filtrer par nom
```


<!-- illustration-08 -->
![apt update actualise les listes ; install et upgrade agissent sur les logiciels.](https://kayasam.github.io/linux-initiation/ressources/images/08-apt-listes-et-logiciels.svg)

*apt update actualise les listes ; install et upgrade agissent sur les logiciels.*

---

## 4. La séquence type

Pour installer un logiciel proprement, toujours faire dans cet ordre :

```bash
sudo apt update            # 1. Mettre à jour la liste
sudo apt install nom       # 2. Installer
```

Pour faire la maintenance du système régulièrement :

```bash
sudo apt update && sudo apt upgrade    # met à jour tout
sudo apt autoremove                    # nettoie les paquets inutiles
```

---

## 5. dpkg — travailler avec des fichiers .deb

Parfois on télécharge directement un fichier `.deb` (équivalent d'un `.exe` Windows) depuis un site web. On utilise alors `dpkg` :

```bash
sudo dpkg -i fichier.deb      # installe le paquet
sudo dpkg -l | grep nom       # vérifie si un paquet est installé
```

---

## 6. Exemples d'installations utiles

```bash
sudo apt install curl         # outil de téléchargement en ligne de commande
sudo apt install git          # gestionnaire de versions
sudo apt install htop         # moniteur système interactif
sudo apt install tree         # affiche l'arborescence en forme d'arbre
sudo apt install net-tools    # outils réseau (ifconfig, netstat…)
sudo apt install vim          # éditeur de texte avancé
```

---

## Récapitulatif des commandes

| Commande | Description |
|----------|-------------|
| `sudo apt update` | Met à jour la liste des paquets disponibles |
| `sudo apt upgrade` | Met à jour les paquets installés |
| `sudo apt install nom` | Installe un paquet |
| `sudo apt remove nom` | Supprime un paquet (garde la config) |
| `sudo apt purge nom` | Supprime un paquet et sa configuration |
| `sudo apt autoremove` | Supprime les paquets inutiles |
| `apt search mot-clé` | Recherche un paquet |
| `apt show nom` | Affiche les détails d'un paquet |
| `apt list --installed` | Liste les paquets installés |
| `sudo dpkg -i fichier.deb` | Installe un fichier .deb téléchargé |

---

> [!NOTE]
> ### À retenir
>
> - Un **paquet** est une archive contenant un logiciel + ses dépendances + sa configuration.
> - Les paquets sont hébergés sur des **dépôts** (serveurs officiels) configurés dans `/etc/apt/`.
> - `apt update` met à jour la **liste** des paquets disponibles — ce n'est pas une mise à jour des logiciels.
> - `apt upgrade` met à jour les **logiciels** installés.
> - `apt install nom` installe, `apt remove nom` désinstalle (garde la config), `apt purge` supprime tout.
> - `apt autoremove` nettoie les paquets devenus inutiles.
> - Toujours faire `apt update` avant `apt install`.
---

> [!TIP]
> **TP associé** → `tp-08-paquets.md`
---

---

[← Utilisateurs et permissions](https://kayasam.github.io/linux-initiation/07-utilisateurs-et-permissions/) · [Chapitre suivant →](https://kayasam.github.io/linux-initiation/09-redirections-et-tubes/)
