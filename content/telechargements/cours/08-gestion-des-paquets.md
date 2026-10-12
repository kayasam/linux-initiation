# Chapitre 08 — Gestion des paquets

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
![apt update actualise les listes ; install et upgrade agissent sur les logiciels.](https://kayasam.github.io/linux-initiation/Ressources/images/08-apt-listes-et-logiciels.svg)

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
