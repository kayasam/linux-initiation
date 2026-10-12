---
title: "01. Comprendre Linux"
---

# Chapitre 01 — Comprendre Linux

> [!TIP] Ressources du chapitre
> - [Ouvrir le chapitre interactif](https://kayasam.github.io/linux-initiation/cours/01-comprendre-linux-interactif.html)
> - [Faire le quiz](https://kayasam.github.io/linux-initiation/cours/quiz/01-comprendre-linux.html)
> - <a href="https://kayasam.github.io/linux-initiation/telechargements/cours/01-comprendre-linux.md" download>Télécharger ce cours en Markdown</a>





---

## 1. Qu'est-ce qu'un système d'exploitation ?

Avant de parler de Linux, il faut comprendre ce qu'est un **système d'exploitation** (OS pour *Operating System*).

C'est le logiciel de base qui fait fonctionner un ordinateur. Il fait l'intermédiaire entre le matériel (processeur, mémoire, disque) et les applications (navigateur, traitement de texte…).

> [!NOTE]
> **Analogie** : le système d'exploitation, c'est comme le chef d'orchestre d'un concert. Il coordonne tous les musiciens (les composants matériels) pour que la musique (tes applications) fonctionne correctement.
Les systèmes d'exploitation les plus connus :
- **Windows** — Microsoft
- **macOS** — Apple
- **Linux** — communauté open source (dont Android et ChromeOS sont dérivés)


<!-- illustration-01 -->
![Le système Linux fait le lien entre les applications et le matériel.](https://kayasam.github.io/linux-initiation/Ressources/images/01-systeme-linux.svg)

*Le système Linux fait le lien entre les applications et le matériel.*

---

## 2. Qu'est-ce que Linux ?

Linux est un système d'exploitation **libre et gratuit**, créé en 1991 par un étudiant finlandais, **Linus Torvalds**. À 21 ans, il a publié le code source de son système sur Internet et invité le monde entier à l'améliorer.

Aujourd'hui, Linux fait tourner :
- La quasi-totalité des **serveurs** d'Internet (Google, Facebook, Amazon…)
- L'essentiel des **supercalculateurs** mondiaux
- Les **smartphones Android** (noyau Linux)
- Les **objets connectés** (box Internet, NAS, routeurs…)
- De nombreux **postes de travail** en entreprise

> [!TIP]
> Linux est partout — même si tu ne le vois pas, tu l'utilises très probablement tous les jours.
---

## 3. Open Source — qu'est-ce que ça veut dire ?

**Open Source** signifie que le **code source** du logiciel (les instructions qui le composent) est **librement accessible, modifiable et redistribuable** par n'importe qui.

À l'opposé, des logiciels comme Windows ou macOS sont **propriétaires** : leur code est secret et appartient à une entreprise.

Les avantages de l'open source :
- **Gratuit** dans la plupart des cas
- **Transparent** : n'importe qui peut vérifier ce que fait le logiciel
- **Sécurisé** : les failles sont détectées et corrigées rapidement par la communauté
- **Pérenne** : le logiciel ne peut pas être abandonné ou "coupé" par une entreprise

> [!NOTE]
> **Analogie** : un logiciel propriétaire, c'est comme une recette secrète qu'une entreprise garde pour elle. Un logiciel open source, c'est une recette publiée dans un livre de cuisine — tout le monde peut la lire, l'améliorer et la partager.
---

## 4. Les distributions Linux

Linux est un **noyau** (*kernel*) — le cœur du système. Seul, il ne suffit pas. Une **distribution** Linux assemble le noyau avec des outils, une interface et un gestionnaire de logiciels pour former un système complet et utilisable.

Il existe des centaines de distributions. Les principales familles :

| Famille | Exemples | Points forts |
|---------|---------|-------------|
| **Debian / Ubuntu** | Debian, Ubuntu, Linux Mint | Stables, simples, idéales pour débuter |
| **Red Hat** | RHEL, Rocky Linux, AlmaLinux | Orientées entreprise et serveurs |
| **SUSE** | openSUSE, SUSE Enterprise | Outils d'administration puissants |
| **Autres** | Kali, Arch, Raspberry Pi OS | Usages spécialisés |

> [!TIP]
> Dans cette formation, nous utilisons **Debian** — l'une des distributions les plus stables et les plus répandues, idéale pour apprendre les bases de Linux.
Arbre généalogique des distributions : https://upload.wikimedia.org/wikipedia/commons/9/96/Liste_des_distributions_Linux.svg

---

## 5. Linux en mode graphique et en mode texte

Linux peut fonctionner de deux façons :

| Mode | Description | Quand l'utiliser ? |
|------|-------------|-------------------|
| **Mode graphique** | Interface avec fenêtres, icônes et souris (comme Windows) | Postes de travail, apprentissage |
| **Mode texte (terminal)** | Interface en lignes de commandes | Serveurs, administration, automatisation |

> [!NOTE]
> La plupart des serveurs fonctionnent **sans interface graphique** pour économiser des ressources. C'est pourquoi maîtriser le terminal est indispensable pour administrer un système Linux.
---

## Récapitulatif

| Notion | Définition |
|--------|-----------|
| Système d'exploitation | Logiciel de base qui fait fonctionner l'ordinateur |
| Linux | OS libre créé en 1991, open source |
| Open Source | Code source librement accessible et modifiable |
| Distribution | Linux complet = noyau + outils + interface + gestionnaire de paquets |
| Debian | Distribution stable et répandue utilisée dans cette formation |

---

> [!NOTE]
> ### À retenir
>
> - Un **système d'exploitation** fait l'intermédiaire entre le matériel et les applications.
> - **Linux** est un OS libre et gratuit, créé en 1991, qui équipe la majorité des serveurs dans le monde.
> - **Open Source** signifie que le code source est librement accessible, modifiable et redistribuable.
> - Une **distribution** Linux = noyau + outils + interface + gestionnaire de paquets.
> - Les principales familles : **Debian/Ubuntu** (débutants), **Red Hat** (entreprises), **SUSE**.
> - Linux fonctionne en **mode graphique** (interface) ou en **mode texte** (terminal).
---

---

[← Accueil](https://kayasam.github.io/linux-initiation/) · [Chapitre suivant →](https://kayasam.github.io/linux-initiation/02-installer-la-vm/)
