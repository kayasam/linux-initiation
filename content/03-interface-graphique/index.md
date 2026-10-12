---
title: "03. L'interface graphique"
---

# Chapitre 03 — L'interface graphique

> [!TIP] Ressources du chapitre
> - [Ouvrir le chapitre interactif](https://kayasam.github.io/linux-initiation/cours/03-interface-graphique-interactif.html)
> - [Faire le quiz](https://kayasam.github.io/linux-initiation/cours/quiz/03-interface-graphique.html)
> - <a href="https://kayasam.github.io/linux-initiation/telechargements/cours/03-interface-graphique.md" download>Télécharger ce cours en Markdown</a>


---

## 1. Les environnements de bureau

Sous Linux, l'interface graphique n'est pas intégrée au système — c'est un composant séparé appelé **environnement de bureau**. Il en existe plusieurs, chacun avec son style et ses outils.

| Environnement | Style | Points forts |
|---------------|-------|-------------|
| **GNOME** | Moderne, épuré | Simple, très répandu (Ubuntu, Debian) |
| **KDE Plasma** | Riche, personnalisable | Ressemble à Windows, nombreuses options |
| **XFCE** | Léger, classique | Idéal pour les vieilles machines |
| **MATE** | Classique | Stabilité, peu gourmand |

> [!NOTE]
> Dans cette formation, nous utilisons **GNOME**, l'environnement par défaut de Debian Desktop.
---

## 2. Découvrir GNOME

### Le bureau

Au premier démarrage sous GNOME, le bureau est intentionnellement minimaliste — pas d'icônes par défaut sur le bureau.

Les éléments principaux :

| Élément | Emplacement | Rôle |
|---------|-------------|------|
| **Barre supérieure** | Haut de l'écran | Heure, réseau, son, paramètres système |
| **Activités** | Bouton en haut à gauche | Ouvrir le menu des applications et voir les fenêtres ouvertes |
| **Dock** | Bas ou côté gauche | Applications favorites en accès rapide |

### Ouvrir une application

Deux méthodes :
1. Cliquer sur **Activités** → taper le nom de l'application
2. Cliquer sur **Activités** → grille d'applications (9 points)

---

## 3. Les applications courantes sous Linux

Linux dispose d'équivalents libres pour la plupart des logiciels courants :

| Besoin | Windows | Équivalent Linux |
|--------|---------|----------------|
| Navigateur web | Chrome, Edge | Firefox, Chromium |
| Bureautique | Microsoft Office | LibreOffice (Writer, Calc, Impress) |
| Email | Outlook | Thunderbird |
| Images | Paint, Photoshop | GIMP, Eye of GNOME |
| Lecteur vidéo | Windows Media Player | VLC |
| Gestionnaire de fichiers | Explorateur Windows | Nautilus (Fichiers) |
| Terminal | Invite de commandes | GNOME Terminal, Konsole |

---

## 4. Le gestionnaire de fichiers (Nautilus)

**Nautilus** (appelé simplement "Fichiers") est l'équivalent de l'Explorateur Windows.

Il permet de :
- Naviguer dans les dossiers
- Créer, copier, déplacer, renommer des fichiers
- Accéder aux disques et périphériques

> [!NOTE]
> Le dossier personnel de l'utilisateur est `/home/ton_nom/`. C'est l'équivalent du dossier `C:\Users\Nom` sous Windows. C'est là que tu trouves tes Documents, Images, Téléchargements…
---

## 5. Paramètres système

**Menu Activités → Paramètres** (icône engrenage) :

- **Réseau** : configurer Wi-Fi, Ethernet
- **Affichage** : résolution, disposition des écrans
- **Son** : volume, périphériques audio
- **Utilisateurs** : gérer les comptes
- **Mises à jour** : vérifier les mises à jour système

---

## 6. Ouvrir un terminal

Le terminal est l'outil central de l'administration Linux. Depuis GNOME, plusieurs façons de l'ouvrir :

- **Activités** → taper `terminal` → Entrée
- Clic droit sur le bureau → **Ouvrir dans un terminal** (si disponible)
- Raccourci : `Ctrl + Alt + T` (selon la configuration)

> [!TIP]
> À partir du module suivant, on travaille exclusivement dans le terminal. L'interface graphique est utile au quotidien, mais le terminal est indispensable pour l'administration.
<!-- illustration-03 -->
![Le bureau et le terminal manipulent les mêmes fichiers.](https://kayasam.github.io/linux-initiation/ressources/images/03-bureau-et-terminal.svg)

*Le bureau et le terminal manipulent les mêmes fichiers.*

---

## Récapitulatif

| Notion | À retenir |
|--------|-----------|
| Environnement de bureau | Interface graphique de Linux (GNOME, KDE, XFCE…) |
| GNOME | Environnement par défaut de Debian, moderne et épuré |
| Nautilus | Gestionnaire de fichiers GNOME |
| `/home/utilisateur/` | Dossier personnel de l'utilisateur |
| Terminal | Outil en ligne de commande — indispensable pour l'administration |

---

> [!NOTE]
> ### À retenir
>
> - L'interface graphique sous Linux s'appelle un **environnement de bureau** — elle est séparée du système.
> - **GNOME** est l'environnement par défaut de Debian : bureau épuré, menu Activités, Dock.
> - Linux dispose d'équivalents libres pour tous les logiciels courants (LibreOffice, Firefox, VLC…).
> - Le dossier personnel de l'utilisateur est `/home/ton_nom/`, accessible via le raccourci `~`.
> - Le **terminal** s'ouvre depuis Activités → taper "terminal". C'est l'outil central de l'administration.
---

---

[← Installer la machine virtuelle](https://kayasam.github.io/linux-initiation/02-installer-la-vm/) · [Chapitre suivant →](https://kayasam.github.io/linux-initiation/04-le-terminal/)
