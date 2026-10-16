---
title: "03. L'interface graphique"
---

# Chapitre 03 — L'interface graphique

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="03-interface-graphique" style="--resource-count:3"><div class="resource-buttons"><a class="resource-button resource-markdown" data-resource-kind="markdown" aria-label="Cours — Lire le cours en Markdown" href="https://kayasam.github.io/linux-initiation/03-interface-graphique/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg></span><span class="resource-label">Cours<small>Lire le cours en Markdown</small></span></a><a class="resource-button resource-html" data-resource-kind="html" aria-label="HTML — Explorer le chapitre" href="https://kayasam.github.io/linux-initiation/03-interface-graphique/html/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 28 32"><path d="M2 2h24l-2 25-10 3-10-3Z" fill="#e44d26"/><path d="M14 5v22l7-2 2-20Z" fill="#f16529"/><path d="M7 8h15l-.3 3H11l.3 3h10l-.8 9-6.5 2-6.5-2-.4-5h3l.2 2.6 3.7 1 3.7-1 .3-3.6H8Z" fill="#fff"/></svg></span><span class="resource-label">HTML<small>Explorer le chapitre</small></span></a><a class="resource-button resource-quiz" data-resource-kind="quiz" aria-label="Quiz — 20 questions" href="https://kayasam.github.io/linux-initiation/03-interface-graphique/quiz/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="4" y="3" width="24" height="26" rx="6" fill="#7652ad"/><path d="M12 12a4 4 0 1 1 6 3.5c-1.5.8-2 1.4-2 3" fill="none" stroke="#fff" stroke-width="2.8" stroke-linecap="round"/><circle cx="16" cy="23" r="1.6" fill="#fff"/></svg></span><span class="resource-label">Quiz<small>20 questions</small></span></a></div><div class="resource-actions"><a class="resource-download" href="https://kayasam.github.io/linux-initiation/telechargements/cours/03-interface-graphique.md" download aria-label="Télécharger le cours en Markdown"><span aria-hidden="true">↓</span> Télécharger .md</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>


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
