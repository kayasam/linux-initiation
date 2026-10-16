---
title: "TP 02 — Installer la machine virtuelle"
---

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="02-installer-la-vm" style="--resource-count:4"><div class="resource-buttons"><a class="resource-button resource-markdown" data-resource-kind="markdown" aria-label="Cours — Lire le cours en Markdown" href="https://kayasam.github.io/linux-initiation/02-installer-la-vm/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg></span><span class="resource-label">Cours<small>Lire le cours en Markdown</small></span></a><a class="resource-button resource-html" data-resource-kind="html" aria-label="HTML — Explorer le chapitre" href="https://kayasam.github.io/linux-initiation/02-installer-la-vm/html/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 28 32"><path d="M2 2h24l-2 25-10 3-10-3Z" fill="#e44d26"/><path d="M14 5v22l7-2 2-20Z" fill="#f16529"/><path d="M7 8h15l-.3 3H11l.3 3h10l-.8 9-6.5 2-6.5-2-.4-5h3l.2 2.6 3.7 1 3.7-1 .3-3.6H8Z" fill="#fff"/></svg></span><span class="resource-label">HTML<small>Explorer le chapitre</small></span></a><a class="resource-button resource-quiz" data-resource-kind="quiz" aria-label="Quiz — 20 questions" href="https://kayasam.github.io/linux-initiation/02-installer-la-vm/quiz/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="4" y="3" width="24" height="26" rx="6" fill="#7652ad"/><path d="M12 12a4 4 0 1 1 6 3.5c-1.5.8-2 1.4-2 3" fill="none" stroke="#fff" stroke-width="2.8" stroke-linecap="round"/><circle cx="16" cy="23" r="1.6" fill="#fff"/></svg></span><span class="resource-label">Quiz<small>20 questions</small></span></a><a class="resource-button resource-tp" data-resource-kind="tp" aria-label="TP — Mettre en pratique" href="https://kayasam.github.io/linux-initiation/02-installer-la-vm/tp"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg></span><span class="resource-label">TP<small>Mettre en pratique</small></span></a></div><div class="resource-actions"><a class="resource-download" href="https://kayasam.github.io/linux-initiation/telechargements/tp/tp-02-installer-la-vm.md" download aria-label="Télécharger le TP en Markdown">↓ Télécharger le TP (.md)</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>


> Durée estimée : 1h (guidé par le formateur)

---

## Objectifs
Créer une machine virtuelle sous VirtualBox et installer Debian.

---

## Étape 1 — Créer la VM dans VirtualBox

1. Ouvre VirtualBox → clique sur **Nouvelle**
2. Remplis les champs :
   - **Nom** : `Debian-Formation`
   - **Type** : Linux
   - **Version** : Debian (64-bit)
3. **RAM** : alloue 2 Go (2048 Mo) minimum
4. **Disque** : crée un nouveau disque virtuel de 20 Go (type VDI, dynamique)
5. Clique sur **Finir**

---

## Étape 2 — Configurer le réseau

1. Sélectionne ta VM → **Configuration** → **Réseau**
2. Carte 1 : mode **NAT** ✓ (accès Internet)

---

## Étape 3 — Démarrer l'installation

1. Sélectionne ta VM → **Démarrer**
2. Sélectionne l'ISO Debian fournie par le formateur
3. Au menu de démarrage, choisis **Graphical Install**

---

## Étape 4 — Suivre l'installation

| Étape | Valeur à choisir |
|-------|----------------|
| Langue | Français |
| Pays | France |
| Clavier | Français |
| Nom machine | `debian` |
| Domaine | (laisser vide) |
| Mot de passe root | À ton choix — **note-le !** |
| Nom utilisateur | `stagiaire` |
| Mot de passe | À ton choix — **note-le !** |
| Partitionnement | Assisté — disque entier |
| Schéma | Tout dans une seule partition |
| Miroir | France, deb.debian.org |
| Logiciels | Cocher : **Environnement de bureau Debian** + **Utilitaires standard** |
| GRUB | Oui, sur `/dev/sda` |

---

## Étape 5 — Premier démarrage

1. La VM redémarre automatiquement après l'installation
2. Connecte-toi avec le compte `stagiaire` et ton mot de passe
3. Explore l'interface graphique quelques minutes
4. Ouvre un terminal : **Activités** → taper `terminal`

---

## Vérification finale

Dans le terminal, tape les commandes suivantes et vérifie que tout fonctionne :

```bash
whoami          # doit afficher : stagiaire
hostname        # doit afficher : debian
ping -c 3 8.8.8.8  # doit recevoir des réponses (connexion Internet)
```

[← Revenir au cours](https://kayasam.github.io/linux-initiation/02-installer-la-vm/)

<a href="https://kayasam.github.io/linux-initiation/telechargements/tp/tp-02-installer-la-vm.md" download>Télécharger ce TP en Markdown</a>
