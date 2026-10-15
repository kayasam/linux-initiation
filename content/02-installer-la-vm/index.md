---
title: "02. Installer la machine virtuelle"
---

# Chapitre 02 — Installer la machine virtuelle

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="02-installer-la-vm" style="--resource-count:4"><div class="chapter-resources-heading"><span class="chapter-resources-title">Ressources du chapitre</span><a class="resource-download" href="https://kayasam.github.io/linux-initiation/telechargements/cours/02-installer-la-vm.md" download><span aria-hidden="true">↓</span> Télécharger le .md</a></div><div class="resource-buttons"><a class="resource-button resource-markdown" data-resource-kind="markdown" href="https://kayasam.github.io/linux-initiation/02-installer-la-vm/"><span class="resource-icon" aria-hidden="true"><img src="https://kayasam.github.io/linux-initiation/assets/resource-icons/markdown.svg" alt="" /></span><span class="resource-label">Markdown<small>Lire le cours</small></span></a><a class="resource-button resource-html" data-resource-kind="html" href="https://kayasam.github.io/linux-initiation/cours/02-installer-la-vm-interactif.html"><span class="resource-icon" aria-hidden="true"><img src="https://kayasam.github.io/linux-initiation/assets/resource-icons/html.svg" alt="" /></span><span class="resource-label">HTML<small>Explorer le chapitre</small></span></a><a class="resource-button resource-quiz" data-resource-kind="quiz" href="https://kayasam.github.io/linux-initiation/cours/quiz/02-installer-la-vm.html"><span class="resource-icon" aria-hidden="true"><img src="https://kayasam.github.io/linux-initiation/assets/resource-icons/quiz.svg" alt="" /></span><span class="resource-label">Quiz<small>20 questions</small></span></a><a class="resource-button resource-tp" data-resource-kind="tp" href="https://kayasam.github.io/linux-initiation/02-installer-la-vm/tp"><span class="resource-icon" aria-hidden="true"><img src="https://kayasam.github.io/linux-initiation/assets/resource-icons/tp.svg" alt="" /></span><span class="resource-label">TP<small>Mettre en pratique</small></span></a></div></nav>


---

## 1. Qu'est-ce qu'une machine virtuelle ?

Une **machine virtuelle** (VM) est un ordinateur simulé à l'intérieur de ton ordinateur réel. Elle fonctionne comme un vrai PC mais dans une fenêtre — elle a son propre disque dur, sa propre mémoire, son propre système d'exploitation.

> [!NOTE]
> **Analogie** : une machine virtuelle, c'est comme une maison dans une maison. Tu construis un appartement à l'intérieur de ta propre maison. L'appartement est indépendant — ce qui s'y passe n'affecte pas le reste de la maison.
**Avantages de la VM pour la formation :**
- On peut tout casser sans risque — redémarrer suffit à repartir de zéro
- Pas besoin d'un second ordinateur pour pratiquer Linux
- Isolée du système principal (Windows, macOS)


<!-- illustration-02 -->
![Le PC hôte exécute VirtualBox, qui fait fonctionner le système invité Debian.](https://kayasam.github.io/linux-initiation/ressources/images/02-hote-et-machine-virtuelle.svg)

*Le PC hôte exécute VirtualBox, qui fait fonctionner le système invité Debian.*

---

## 2. VirtualBox — l'outil de virtualisation

**VirtualBox** est le logiciel qui permet de créer et de gérer des machines virtuelles. Il est gratuit et fonctionne sous Windows, macOS et Linux.

Téléchargement : https://www.virtualbox.org/wiki/Downloads

---

## 3. Télécharger Debian

Nous utilisons **Debian 12** (ou 13 si disponible), en version **netinstall** (installation minimale par réseau) ou **DVD ISO**.

Téléchargement officiel : https://www.debian.org/download

---

## 4. Créer la machine virtuelle dans VirtualBox

### Étape 1 — Nouveau

Dans VirtualBox : **Nouvelle** (bouton en haut à gauche)

Paramètres à saisir :

| Champ | Valeur |
|-------|--------|
| Nom | `Debian-Formation` (ou au choix) |
| Type | Linux |
| Version | Debian (64-bit) |

### Étape 2 — Mémoire vive

Alloue **2 Go minimum**, 4 Go si ta machine le permet.

> [!WARNING]
> Ne pas allouer plus de la moitié de la RAM totale de ton ordinateur — sinon ton PC hôte sera ralenti.
### Étape 3 — Disque dur virtuel

- Type : **VDI** (VirtualBox Disk Image)
- Stockage : **dynamique** (le fichier ne grandit que si nécessaire)
- Taille : **20 Go minimum**

### Étape 4 — Réseau

Dans **Configuration > Réseau** :
- **Carte 1** : NAT (accès Internet via l'hôte)

---

## 5. Installer Debian

### Démarrer l'installation

1. Sélectionne ta VM → **Démarrer**
2. VirtualBox te demande de choisir l'ISO → sélectionne le fichier Debian téléchargé
3. Le programme d'installation démarre

Référence visuelle : https://www.server-world.info/en/note?os=Debian_13&p=install

### Déroulement de l'installation

| Étape | Ce qu'il faut faire |
|-------|-------------------|
| Langue | Français |
| Pays | France |
| Clavier | Français |
| Nom de la machine | `debian` (ou au choix, sans espaces) |
| Domaine | Laisser vide |
| Mot de passe root | Choisir et noter |
| Nouvel utilisateur | Créer un compte standard (ex : `stagiaire`) |
| Partitionnement | **Assisté — utiliser un disque entier** (option simple) |
| Logiciels | Cocher **Environnement de bureau Debian** + **Utilitaires standard** |
| GRUB | Installer sur le disque principal (`/dev/sda`) |

> [!TIP]
> L'installation dure environ 10 à 20 minutes selon la connexion. À la fin, la VM redémarre automatiquement sur Debian.
---

## 6. Premier démarrage

Au démarrage, un écran de connexion apparaît. Connecte-toi avec le compte utilisateur créé pendant l'installation (pas root).

> [!DANGER]
> En règle générale, on **ne travaille pas en tant que `root`** au quotidien. Le compte root est réservé aux opérations d'administration. Utilise ton compte utilisateur normal pour commencer.
---

## Récapitulatif des commandes utiles (VirtualBox)

| Action | Comment faire |
|--------|--------------|
| Démarrer la VM | Sélectionner la VM → Démarrer |
| Mettre en pause | Menu Machine → Mettre en pause |
| Éteindre proprement | Dans la VM : Menu → Arrêter le système |
| Prendre un instantané | Menu Machine → Prendre un instantané (sauvegarde de l'état) |
| Redimensionner l'écran | Affichage → Écran virtuel → Ajuster à la fenêtre |

> [!NOTE]
> ### À retenir
>
> - Une **machine virtuelle** est un ordinateur simulé dans l'ordinateur — on peut tout casser sans risque.
> - **VirtualBox** est le logiciel de virtualisation utilisé dans cette formation (gratuit, multiplateforme).
> - Créer une VM : nom, type Linux/Debian, **2 Go de RAM minimum**, disque VDI dynamique **20 Go**.
> - L'installation Debian dure 10 à 20 min : langue, utilisateur, partitionnement assisté, interface graphique.
> - Ne jamais se connecter en **root** pour le travail courant — utiliser le compte utilisateur normal.
> - **Prendre un instantané** avant toute manipulation risquée permet de revenir à l'état précédent.
---

> [!TIP]
> **TP associé** → `tp-02-installer-la-vm.md`
---

---

[← Comprendre Linux](https://kayasam.github.io/linux-initiation/01-comprendre-linux/) · [Chapitre suivant →](https://kayasam.github.io/linux-initiation/03-interface-graphique/)
