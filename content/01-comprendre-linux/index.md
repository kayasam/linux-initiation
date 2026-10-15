---
title: "01. Comprendre Linux"
---

# Chapitre 01 — Comprendre Linux

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="01-comprendre-linux" style="--resource-count:3"><div class="chapter-resources-heading"><span class="chapter-resources-title">Ressources du chapitre</span><a class="resource-download" href="https://kayasam.github.io/linux-initiation/telechargements/cours/01-comprendre-linux.md" download><span aria-hidden="true">↓</span> Télécharger le .md</a></div><div class="resource-buttons"><a class="resource-button resource-markdown" data-resource-kind="markdown" href="https://kayasam.github.io/linux-initiation/01-comprendre-linux/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg></span><span class="resource-label">Markdown<small>Lire le cours</small></span></a><a class="resource-button resource-html" data-resource-kind="html" href="https://kayasam.github.io/linux-initiation/01-comprendre-linux/html/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 28 32"><path d="M2 2h24l-2 25-10 3-10-3Z" fill="#e44d26"/><path d="M14 5v22l7-2 2-20Z" fill="#f16529"/><path d="M7 8h15l-.3 3H11l.3 3h10l-.8 9-6.5 2-6.5-2-.4-5h3l.2 2.6 3.7 1 3.7-1 .3-3.6H8Z" fill="#fff"/></svg></span><span class="resource-label">HTML<small>Explorer le chapitre</small></span></a><a class="resource-button resource-quiz" data-resource-kind="quiz" href="https://kayasam.github.io/linux-initiation/01-comprendre-linux/quiz/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="4" y="3" width="24" height="26" rx="6" fill="#7652ad"/><path d="M12 12a4 4 0 1 1 6 3.5c-1.5.8-2 1.4-2 3" fill="none" stroke="#fff" stroke-width="2.8" stroke-linecap="round"/><circle cx="16" cy="23" r="1.6" fill="#fff"/></svg></span><span class="resource-label">Quiz<small>20 questions</small></span></a></div></nav>
<div class="support-toolbar markdown-course-toolbar"><span>Cours Markdown</span><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div>

Vous utilisez peut-être déjà Linux sans le savoir : un téléphone Android, une box Internet ou un serveur qui héberge un site peuvent s’appuyer sur son noyau. Avant d’installer Debian, découvrons ce que recouvrent **Linux**, **GNU**, **logiciel libre** et **distribution**.

> [!NOTE] Objectifs
> À la fin du chapitre, vous pourrez expliquer le rôle d’un système d’exploitation, distinguer GNU de Linux, reconnaître les grandes familles de licences et comprendre pourquoi nous utilisons Debian.
>
> **Aucune commande à mémoriser pour le moment.** L’objectif est de comprendre les mots que vous rencontrerez pendant la formation.

---

## 1. Qu’est-ce qu’un système d’exploitation ?

Un **système d’exploitation**, souvent abrégé **OS** (*Operating System*), fait fonctionner l’ordinateur et permet aux applications d’utiliser son matériel.

Quand vous ouvrez un document, le traitement de texte demande au système de lire le fichier sur le disque. Si vous lancez plusieurs applications, le système répartit entre elles le temps du processeur et la mémoire disponible. Il gère aussi les périphériques et les droits d’accès aux fichiers.

> [!TIP] Une image pour comprendre
> Imaginez un **chef d’orchestre** : les applications demandent des ressources, le système organise leur utilisation et le matériel réalise les opérations.

<!-- illustration-01 -->
![Le système Linux fait le lien entre les applications et le matériel.](https://kayasam.github.io/linux-initiation/ressources/images/01-systeme-linux.svg)

*Les applications s’appuient sur le système pour utiliser le matériel.*

Vous connaissez probablement **Windows**, **macOS**, **Android** ou **iOS**. Sur un ordinateur, **Debian** et **Ubuntu** sont deux exemples de systèmes construits autour du noyau Linux.

Le **noyau** (*kernel*) est la partie centrale du système : il gère notamment le processeur, la mémoire et l’accès aux périphériques. Le navigateur, le bureau graphique et les commandes du terminal sont d’autres logiciels, qui s’appuient sur lui.

---

## 2. D’Unix à GNU/Linux : trois repères

### Unix : les idées de départ

**Unix** apparaît en **1969** aux laboratoires Bell, notamment avec **Ken Thompson** et **Dennis Ritchie**. Il permet à plusieurs personnes d’utiliser un même ordinateur et d’y exécuter plusieurs programmes. [Histoire d’Unix — The Open Group](https://www.unix.org/unix_history.html)

Unix a popularisé une organisation que vous retrouverez sous Linux : des utilisateurs avec des droits distincts, des fichiers rangés dans une arborescence et de petits outils que l’on peut combiner.

**Linux est un système de type Unix** : il reprend de nombreux principes d’Unix, mais son noyau a été développé indépendamment. Linux n’est donc pas simplement « une version gratuite d’Unix ».

### GNU : Richard Stallman et le logiciel libre

En **1983**, **Richard Stallman** annonce le projet **GNU**, dont le développement commence en **1984**. Son objectif est de construire un système compatible avec Unix qui respecte la liberté de ses utilisateurs. Le nom signifie **GNU’s Not Unix**, soit « GNU n’est pas Unix ». [Annonce du projet GNU](https://www.gnu.org/gnu/initial-announcement.html)

Le projet fournit progressivement des outils essentiels : **Bash** pour interpréter les commandes, **GCC** pour transformer du code source en programmes et les **outils GNU** comme `ls` ou `cp`. Vous utiliserez certains de ces outils dans les prochains chapitres.

Richard Stallman fonde également la **Free Software Foundation (FSF)** en **1985**, pour soutenir le logiciel libre. GNU développe de nombreux composants, mais son propre noyau n’est pas encore prêt pour constituer le système recherché. [Repères historiques — FSF](https://www.fsf.org/about/what-is-free-software)

### Linux : le noyau de Linus Torvalds

En **1991**, **Linus Torvalds**, alors étudiant finlandais, lance le noyau **Linux**. Des développeurs rejoignent ensuite le projet. Associé aux outils GNU et à d’autres logiciels, ce noyau permet de construire des systèmes complets.

L’expression **GNU/Linux** rappelle cette association. Dans la conversation courante, on dit souvent simplement « Linux » pour parler de l’ensemble. **Debian est une distribution GNU/Linux.** Tous les systèmes qui utilisent le noyau Linux n’utilisent cependant pas l’environnement GNU : Android en est un exemple. [Présentation du système GNU](https://www.gnu.org/gnu/gnu-history.en.html)

![Unix apporte des principes ; GNU apporte des outils libres ; Linux apporte le noyau. Une distribution assemble ces composants avec d’autres logiciels.](https://kayasam.github.io/linux-initiation/ressources/images/01-unix-gnu-linux.svg)

> [!NOTE] Deux personnes, deux contributions
> **Richard Stallman → GNU et les libertés du logiciel.**
> **Linus Torvalds → le noyau Linux.**
> Le système que nous allons utiliser est le résultat de ces projets et de nombreuses autres contributions.

---

## 3. Logiciel libre, open source et gratuit : quelle différence ?

Le **code source** est l’ensemble des instructions écrites par les développeurs pour construire un logiciel. Vous pouvez utiliser un logiciel sans savoir lire son code, comme vous pouvez utiliser une voiture sans être mécanicien.

### Les quatre libertés du logiciel libre

Un **logiciel libre** donne à ses utilisateurs quatre libertés, traditionnellement numérotées de **0 à 3** :

| Liberté | Ce que cela permet concrètement |
|---|---|
| **0 — Utiliser** | Exécuter le programme pour l’usage de son choix, personnel ou professionnel. |
| **1 — Étudier et modifier** | Comprendre son fonctionnement et l’adapter à ses besoins, grâce au code source. |
| **2 — Partager des copies** | Donner une copie du logiciel à un collègue ou à un proche. |
| **3 — Partager ses modifications** | Redistribuer une version améliorée pour que d’autres en profitent. |

Ces libertés portent sur les **droits accordés**, pas sur le prix du logiciel. [Définition du logiciel libre — GNU/FSF](https://www.gnu.org/philosophy/free-sw.en.html)

### L’open source : le code et les droits qui l’accompagnent

Un logiciel **open source** fournit l’accès à son code source avec une licence autorisant notamment son utilisation, sa modification et sa redistribution. Un code visible sur Internet, accompagné d’une interdiction de le modifier, ne suffit donc pas.

Les expressions **logiciel libre** et **open source** recouvrent largement les mêmes logiciels. La première met l’accent sur les libertés des utilisateurs ; la seconde sur l’ouverture du code et le développement collaboratif. L’**Open Source Initiative (OSI)** définit les critères d’une licence open source. [Définition de l’open source — OSI](https://opensource.org/osd)

> [!TIP] La recette et les permissions
> Le code source ressemble à une **recette de cuisine**. La licence précise si vous pouvez la cuisiner, la modifier et partager votre version. **Pouvoir lire la recette ne donne pas automatiquement tous ces droits.**

### Gratuit ne veut pas dire libre

Un logiciel peut être **gratuit et propriétaire** : vous ne payez rien, mais vous n’avez pas nécessairement accès au code ni le droit de le modifier. À l’inverse, un logiciel libre peut être vendu, et des entreprises peuvent facturer son installation, son hébergement ou son assistance.

La transparence facilite l’étude du logiciel et permet à d’autres de poursuivre son développement. Elle ne garantit toutefois **ni l’absence de failles, ni des mises à jour éternelles**. La maintenance et la bonne configuration restent nécessaires.

---

## 4. Les licences libres : les règles du partage

Une **licence logicielle** est un texte qui précise les droits et les conditions d’utilisation, de modification et de redistribution d’un programme. Les auteurs conservent leurs droits d’auteur : publier un logiciel libre ne signifie pas abandonner tous leurs droits.

Vous n’avez pas besoin d’apprendre ces textes par cœur. Pour débuter, retenez surtout **deux grandes approches**.

### Le copyleft : conserver les libertés lors du partage

La **GNU GPL** (*General Public License*) est une licence à **copyleft**. Lorsqu’une version modifiée d’un programme couvert par la GPL est distribuée, les destinataires doivent conserver les droits prévus par cette licence et pouvoir obtenir le code source correspondant selon ses conditions.

**Exemple :** une entreprise adapte un outil sous GPL et distribue cette version à ses clients. Elle doit respecter la GPL pour cette version et leur permettre d’obtenir son code source. Elle ne peut pas retirer les libertés que la licence leur accorde.

> [!NOTE] Utiliser un programme GPL ne rend pas vos documents publics
> Rédiger un courrier ou utiliser un programme sous GPL ne vous oblige pas à publier votre travail. Une modification conservée pour un usage privé n’a pas non plus à être publiée simplement parce qu’elle existe. Les obligations de partage de la GPL concernent notamment la **distribution du logiciel couvert**, pas les documents que vous créez avec lui. [FAQ des licences GNU](https://www.gnu.org/licenses/gpl-faq.html#GPLRequireSourcePostedPublic)

Le **noyau Linux est sous GPL version 2**. Les autres logiciels d’une distribution ont leurs propres licences : Debian n’est pas un unique programme placé sous une unique licence. [Licence du noyau Linux](https://docs.kernel.org/process/license-rules.html)

### Les licences permissives : autoriser davantage de réutilisations

Les licences **MIT**, **BSD** et **Apache 2.0** autorisent une réutilisation large du code, y compris dans des logiciels propriétaires, sous réserve de respecter leurs conditions. Elles imposent notamment de conserver certains avis de licence et de droits d’auteur. Apache 2.0 comprend aussi des dispositions explicites sur les brevets.

| Approche | Exemples | Idée principale |
|---|---|---|
| **Copyleft** | GNU GPL | Préserver les libertés sur le programme couvert et ses versions dérivées distribuées. |
| **Permissive** | MIT, BSD, Apache 2.0 | Faciliter les réutilisations, sans imposer que toute version dérivée reste libre. |

**Exemple :** une entreprise peut intégrer un composant sous MIT dans une application propriétaire en respectant la licence, notamment les mentions à conserver. Les utilisateurs de l’application complète ne reçoivent pas forcément le code de cette application. [Licence MIT — OSI](https://opensource.org/license/mit), [licence Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)

> [!TIP] Le réflexe utile
> Avant de redistribuer un logiciel ou de réutiliser son code, cherchez son fichier **`LICENSE`**, **`COPYING`** ou sa rubrique **À propos → Licence**. Un téléchargement gratuit ne remplace pas la lecture des permissions.

---

## 5. Une distribution : le système prêt à utiliser

Une **distribution Linux** assemble un noyau Linux, des outils système, des bibliothèques nécessaires aux programmes, un gestionnaire de paquets et des applications. Elle peut aussi proposer un bureau graphique.

Pour **Debian**, on peut se représenter cet assemblage ainsi :

```text
Noyau Linux + outils GNU + autres composants et applications
                      ↓
             Distribution Debian
```

L’équipe d’une distribution choisit les composants, prépare leur installation et fournit des mises à jour. Vous n’avez pas à assembler chaque pièce vous-même.

| Famille ou projet | Exemples | Repère pour la formation |
|---|---|---|
| **Debian** | Debian, Ubuntu, Linux Mint | Ubuntu s’appuie sur Debian ; l’édition principale de Mint s’appuie sur Ubuntu. |
| **Red Hat** | Fedora, RHEL, Rocky Linux, AlmaLinux | Un autre écosystème, fréquent dans les environnements professionnels. |
| **SUSE** | openSUSE, SUSE Linux Enterprise | Un écosystème disposant de ses propres outils d’administration. |
| **Autres projets** | Arch Linux, Kali Linux | Des choix ou usages particuliers ; Kali, basée sur Debian, vise notamment les tests de sécurité. |

> [!TIP] Notre choix : Debian
> Nous utiliserons **Debian** pour apprendre sur une base stable, documentée et utilisable aussi bien avec un bureau que comme serveur. Les principes étudiés vous serviront ensuite dans d’autres distributions.

Une distribution peut contenir des composants sous différentes licences, et éventuellement des éléments propriétaires, comme certains micrologiciels nécessaires au matériel. **Utiliser Linux ne signifie donc pas que chaque composant installé est libre.**

---

## 6. Bureau ou serveur : deux usages du même système

Un **poste de travail** sert directement à une personne : naviguer sur le Web, écrire des documents ou consulter ses fichiers. Un **serveur** fournit des services à d’autres machines, par exemple des pages Web ou un espace de partage.

| Interface | Comment l’utiliser ? | Exemple |
|---|---|---|
| **Bureau graphique** | Fenêtres, icônes, menus et souris. | Ouvrir le gestionnaire de fichiers et créer un dossier. |
| **Terminal** | Saisir des commandes au clavier. | Demander l’affichage du contenu d’un dossier. |

Ces interfaces accèdent au **même système et aux mêmes fichiers**. Vous pouvez ouvrir un terminal dans un bureau graphique ; il n’est pas nécessaire de choisir définitivement entre les deux.

Un serveur peut fonctionner sans bureau pour économiser des ressources et limiter les logiciels à maintenir. Dans cette formation, nous commencerons avec une interface graphique, puis nous découvrirons progressivement le terminal.

---

## 7. Vidéo et échange

Regardez la vidéo proposée, puis utilisez le cours pour répondre aux questions ci-dessous. Sa lecture nécessite une connexion Internet.

<iframe width="560" height="315" style="display:block;width:100%;max-width:900px;height:auto;aspect-ratio:16/9;border:0;border-radius:12px;margin:1rem auto" src="https://www.youtube.com/embed/oL6YcXLegC0?si=0lW4t2mYmfdHQEOa" title="Vidéo proposée pour le chapitre Comprendre Linux" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

[Ouvrir la vidéo sur YouTube](https://www.youtube.com/watch?v=oL6YcXLegC0)

1. Qui a lancé GNU ? Qui a créé le noyau Linux ?
2. Un logiciel gratuit est-il forcément libre ? Expliquez avec les droits de l’utilisateur.
3. Quelle différence principale retenez-vous entre une licence GPL et une licence MIT ?
4. Pourquoi Debian est-elle une distribution plutôt qu’un simple noyau ?

<details>
<summary>Afficher les pistes de réponse</summary>
<p><strong>1.</strong> Richard Stallman a lancé GNU ; Linus Torvalds a créé le noyau Linux.</p>
<p><strong>2.</strong> Non. Le prix ne dit pas si l’on peut étudier, modifier et redistribuer le programme.</p>
<p><strong>3.</strong> La GPL préserve les libertés sur les versions dérivées distribuées du programme couvert. MIT permet aussi des réutilisations propriétaires, à condition de respecter ses mentions et conditions.</p>
<p><strong>4.</strong> Debian assemble le noyau avec des outils, des applications et un système de gestion et de mise à jour des logiciels.</p>
</details>

---

## À retenir

| Mot | L’idée essentielle |
|---|---|
| **Unix** | Un système historique dont Linux reprend de nombreux principes. |
| **GNU** | Le projet libre lancé par Richard Stallman, à l’origine de nombreux outils système. |
| **Linux** | Le noyau lancé par Linus Torvalds en 1991. |
| **GNU/Linux** | L’association du noyau Linux et de l’environnement GNU, avec d’autres composants. |
| **Libre / open source** | Des droits sur l’utilisation, le code, les modifications et le partage ; pas une promesse de gratuité. |
| **Licence** | Le texte qui fixe ces droits et leurs conditions : GPL, MIT, BSD, Apache… |
| **Distribution** | Un ensemble prêt à installer, comme Debian ou Ubuntu. |

Vous pouvez maintenant [faire le quiz de 20 questions](https://kayasam.github.io/linux-initiation/cours/quiz/01-comprendre-linux.html), puis passer au [chapitre 02 — Installer la VM](https://kayasam.github.io/linux-initiation/02-installer-la-vm/).

---

[← Accueil](https://kayasam.github.io/linux-initiation/) · [Chapitre suivant →](https://kayasam.github.io/linux-initiation/02-installer-la-vm/)
