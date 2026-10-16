---
title: "TP 10 — Réseau et services"
---

# TP 10 — Mission : remettre la station Debian en ligne

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="10-reseau-et-services" style="--resource-count:4"><div class="resource-buttons"><a class="resource-button resource-markdown" data-resource-kind="markdown" aria-label="Cours — Lire le cours en Markdown" href="https://kayasam.github.io/linux-initiation/10-reseau-et-services/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg></span><span class="resource-label">Cours<small>Lire le cours en Markdown</small></span></a><a class="resource-button resource-html" data-resource-kind="html" aria-label="HTML — Explorer le chapitre" href="https://kayasam.github.io/linux-initiation/10-reseau-et-services/html/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 28 32"><path d="M2 2h24l-2 25-10 3-10-3Z" fill="#e44d26"/><path d="M14 5v22l7-2 2-20Z" fill="#f16529"/><path d="M7 8h15l-.3 3H11l.3 3h10l-.8 9-6.5 2-6.5-2-.4-5h3l.2 2.6 3.7 1 3.7-1 .3-3.6H8Z" fill="#fff"/></svg></span><span class="resource-label">HTML<small>Explorer le chapitre</small></span></a><a class="resource-button resource-quiz" data-resource-kind="quiz" aria-label="Quiz — 20 questions" href="https://kayasam.github.io/linux-initiation/10-reseau-et-services/quiz/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="4" y="3" width="24" height="26" rx="6" fill="#7652ad"/><path d="M12 12a4 4 0 1 1 6 3.5c-1.5.8-2 1.4-2 3" fill="none" stroke="#fff" stroke-width="2.8" stroke-linecap="round"/><circle cx="16" cy="23" r="1.6" fill="#fff"/></svg></span><span class="resource-label">Quiz<small>20 questions</small></span></a><a class="resource-button resource-tp" data-resource-kind="tp" aria-label="TP — Mettre en pratique" href="https://kayasam.github.io/linux-initiation/10-reseau-et-services/tp"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg></span><span class="resource-label">TP<small>Mettre en pratique</small></span></a></div><div class="resource-actions"><a class="resource-download" href="https://kayasam.github.io/linux-initiation/telechargements/cours/10-reseau-et-services.md" download aria-label="Télécharger le cours en Markdown"><span aria-hidden="true">↓</span> Télécharger .md</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>

> Chapitre associé : [10 — Réseau et services](https://kayasam.github.io/linux-initiation/10-reseau-et-services/)
> Niveau : débutant — une VM par personne

---

## La mission

Tu prends le poste de technicien de la station Debian. Connecte-toi à distance, vérifie son réseau, puis crée ton badge personnel : une clé SSH. Si tu termines la mission, les bonus te proposent de créer une balise web, de la dépanner et de construire un tunnel !

**Objectifs :** identifier IP et passerelle, distinguer réseau et DNS, utiliser SSH et se connecter avec une clé. **Bonus :** créer un service web, le dépanner et utiliser un tunnel SSH.

**Prérequis :** Windows avec PowerShell et le client OpenSSH ; VM Debian démarrée ; compte `stagiaire` avec accès à `sudo` ; accès à la console de la VM.

| Élément | Valeur du TP |
|---|---|
| VM Debian | `192.168.84.10` |
| Compte et dossier personnel | `stagiaire`, `/home/stagiaire` |
| SSH | TCP `22` |
| Balise web du bonus depuis Windows | `http://192.168.84.10:8088` |
| Accès web du bonus sur Windows | `127.0.0.1:18088` |

Adapte l'adresse si ta VM utilise une autre IP.

> [!TIP] Deux machines, deux terminaux
> Les blocs `bash` s'exécutent sur **Debian** (console ou session SSH). Les blocs `powershell` s'exécutent sur **Windows**. La page web se consulte dans le navigateur Windows.

> [!WARNING] Périmètre de la mission
> N'arrête pas `ssh` et ne modifie pas le réseau ni les services existants. Tu manipuleras seulement `tp10-web`. Sa définition sera créée dans `/etc/systemd/system/`, le dossier des services locaux. Elle sera retirée à la fin du TP.

Prépare un compte rendu court avec les réponses et les preuves demandées. Chaque partie valide un badge.

---

## Départ — Connexion à la station

Dans **PowerShell Windows**, ouvre directement ta session :

```powershell
ssh stagiaire@192.168.84.10
```

- `ssh` : ouvre une connexion sécurisée ; avant `@` : compte distant ; après `@` : IP de la VM.

À la première connexion à cette VM de formation, accepte avec `yes`, puis saisis le mot de passe si demandé : aucun caractère ne s'affiche. Une clé déjà installée peut être utilisée directement.

Garde cette session ouverte et ouvre une **deuxième fenêtre PowerShell** pour les tests Windows. Les commandes Linux suivantes s'exécutent dans la session SSH.

---

## Partie A — Éclaireur réseau

**A1. Où suis-je ? — Session SSH Debian.**

```bash
hostname
whoami
ip -br address
ip route
```

- `-br` : format court ; `ip route` : routes, dont la passerelle sur la ligne `default via`.

Note le nom de la machine, l'utilisateur, l'interface active, son IPv4/préfixe et la passerelle. Quelle interface représente la boucle locale ?

**A2. La liaison répond-elle ? — Session SSH Debian.**

```bash
ping -c 4 127.0.0.1
```

- `-c 4` : quatre requêtes puis arrêt ; `127.0.0.1` : la machine elle-même.

Teste ensuite la passerelle : remplace le texte ci-dessous par l'adresse trouvée en A1.

```bash
ping -c 4 ADRESSE_PASSERELLE
```

Relève le pourcentage de perte. Un équipement peut filtrer le ping : une absence de réponse ne suffit pas à prouver une coupure réseau.

**A3. L'annuaire des noms fonctionne-t-il ? — Session SSH Debian.**

```bash
getent hosts localhost
host debian.org
cat /etc/resolv.conf
```

- `getent hosts` : utilise la résolution de noms du système, notamment `/etc/hosts` selon sa configuration.
- `host` : effectue une recherche DNS.
- `/etc/resolv.conf` : indique les résolveurs configurés, parfois un relais local.

Relève une adresse de `debian.org`. Les réponses peuvent varier. Si le DNS externe est indisponible, note l'erreur et poursuis : le reste du TP utilise le réseau local.

**Question :** résoudre un nom prouve-t-il que le service web correspondant fonctionne ?

**Badge : cartographe** — tu sais retrouver l'IP de ta VM et sa passerelle.

---

## Partie B — Télécommande sécurisée

**B2. Inspecte le service qui permet la connexion — Session SSH.**

```bash
systemctl is-active ssh
systemctl is-enabled ssh
sudo systemctl status ssh --no-pager
sudo ss -ltnp | grep 22
sudo journalctl -u ssh -n 10 --no-pager
```

- `is-active` : état actuel ; `is-enabled` : activation au démarrage.
- `--no-pager` : affichage direct, sans lecteur interactif.
- `ss -ltnp` : écoute (`l`), TCP (`t`), ports numériques (`n`), processus (`p`).
- `| grep 22` : affiche les lignes contenant `22` ; vérifie la colonne du port local pour repérer `:22`.
- `journalctl -u ssh -n 10` : dix dernières lignes du journal de SSH.

Relève l'état du service et une trace de connexion. Masque les informations personnelles avant de partager ton compte rendu.

**Badge : pilote à distance** — tu distingues client et serveur SSH.

---

## Partie C — Ton badge personnel : la clé SSH

Tu vas créer une paire de clés sur Windows et installer la clé publique sur Debian. Garde ta première session SSH ouverte pendant les essais.

### C1. Prépare une clé dédiée — Nouvelle fenêtre PowerShell

```powershell
Test-Path "$env:USERPROFILE\.ssh\id_ed25519_tp10"
```

- `Test-Path` : vérifie si cette clé existe ; `$env:USERPROFILE` : dossier utilisateur Windows.

Si le résultat est `True`, réutilise-la sans l'écraser. Sinon :

```powershell
ssh-keygen -t ed25519 -f "$env:USERPROFILE\.ssh\id_ed25519_tp10"
```

- `-t ed25519` : type de clé ; `-f` : nom dédié, sans remplacer ta clé habituelle.

Choisis une phrase secrète. Quel fichier reste sur Windows et lequel peut être envoyé ?

### C2. Dépose le badge public — PowerShell

```powershell
Get-Content "$env:USERPROFILE\.ssh\id_ed25519_tp10.pub" | ssh stagiaire@192.168.84.10 'umask 077; mkdir -p ~/.ssh; cat >> ~/.ssh/authorized_keys; chmod 700 ~/.ssh; chmod 600 ~/.ssh/authorized_keys'
```

- `Get-Content` lit la clé publique ; `|` la transmet à SSH.
- `umask 077` protège les nouveaux fichiers et dossiers.
- `>>` ajoute la clé sans effacer celles déjà présentes.
- `chmod 700` protège le dossier ; `chmod 600` protège le fichier.

Exécute cette étape une seule fois pour éviter les doublons.

### C3. Prouve que la clé fonctionne — PowerShell

```powershell
ssh -i "$env:USERPROFILE\.ssh\id_ed25519_tp10" -o IdentitiesOnly=yes -o PasswordAuthentication=no -o KbdInteractiveAuthentication=no stagiaire@192.168.84.10
```

- `-i` : sélectionne la clé privée ; `-o` : définit une option du client.
- `IdentitiesOnly=yes` : limite les identités aux clés explicitement configurées.
- Les deux dernières options refusent les méthodes pouvant demander le mot de passe du compte pour cette connexion.

Avec la configuration standard du client, la clé choisie sera utilisée. Sa phrase secrète peut être demandée : ce n'est pas le mot de passe de `stagiaire`. Vérifie `whoami`, puis quitte cette nouvelle session avec `exit`.

**Badge : gardien des clés** — tu sais te connecter avec ta clé et distinguer sa phrase secrète du mot de passe du compte.

Le parcours principal est terminé. Tu peux passer au compte rendu, puis quitter ta session avec `exit`. Si tu as fini, poursuis avec les bonus ci-dessous.

---

## Partie D — Bonus : construis ta balise web

> [!NOTE] Pour ceux qui ont terminé
> Le parcours principal s'arrête après la partie C. Ce bonus crée un serveur web que tu consulteras dans le navigateur Windows.

**Les commandes Linux s'exécutent dans la session SSH ; les tests PowerShell et le navigateur sont sur Windows.**

**D1. Prépare la page de la station.**

```bash
mkdir -p ~/tp-10-reseau
printf '<h1>Mission reseau : service operationnel !</h1>\n' > ~/tp-10-reseau/index.html
```

- `mkdir -p` : crée le dossier s'il manque.
- `printf` : écrit le texte ; `\n` : retour à la ligne.
- `>` : écrit dans le fichier en remplaçant son contenu.

Personnalise le titre avec ton prénom. Réserve ce dossier au TP.

**D2. Vérifie que la place est libre.**

```bash
command -v python3 curl
systemctl show tp10-web.service -p LoadState
sudo ss -ltnp | grep 8088
```

- `command -v` : emplacement des programmes ; `-p LoadState` : propriété de chargement de l'unité.
- `| grep 8088` : conserve les lignes contenant `8088`. Si rien ne correspond, aucune ligne ne s'affiche.

Attendu avant la première création : `LoadState=not-found` et aucune écoute sur 8088. Sinon, appelle le formateur pour identifier ce qui existe déjà. Si un outil manque, le formateur peut l'installer avec APT.

**D3. Donne une fiche de mission à systemd.**

Les services créés par l'administrateur se définissent dans `/etc/systemd/system/`. Colle **tout le bloc**, jusqu'à la ligne `EOF` seule.

```bash
sudo tee /etc/systemd/system/tp10-web.service > /dev/null <<'EOF'
[Unit]
Description=TP 10 - Serveur web de mission
After=network.target

[Service]
User=stagiaire
WorkingDirectory=/home/stagiaire/tp-10-reseau
ExecStart=/usr/bin/python3 -m http.server 8088 --bind 0.0.0.0

[Install]
WantedBy=multi-user.target
EOF
```

- `tee` : écrit le texte dans le fichier avec les droits de `sudo`.
- `> /dev/null` : masque la recopie du texte par `tee`.
- `<<'EOF'` : fournit les lignes suivantes à la commande, jusqu'à `EOF`.
- `User` : compte exécutant le serveur ; `WorkingDirectory` : dossier de la page.
- `ExecStart` : programme lancé ; `-m http.server` : serveur web Python.
- `8088` : port choisi ; `--bind 0.0.0.0` : écoute sur toutes les interfaces IPv4 de la VM, pour permettre l'accès depuis Windows.

**D4. Fais décoller le service.**

```bash
sudo systemd-analyze verify /etc/systemd/system/tp10-web.service
sudo systemctl daemon-reload
sudo systemctl start tp10-web
systemctl is-active tp10-web
```

- `verify` : vérifie la définition ; aucune sortie indique qu'aucun problème n'a été détecté.
- `daemon-reload` : fait relire les définitions à systemd.
- `start` : démarre ce service ; `is-active` : vérifie son état.

Attendu : `active`.

Dans la **deuxième fenêtre PowerShell Windows** :

```powershell
Test-NetConnection 192.168.84.10 -Port 8088
```

- `-Port 8088` : teste si une connexion TCP peut être établie vers le serveur web.

Attendu : `TcpTestSucceeded : True`. Ouvre ensuite le **navigateur Windows** à cette adresse :

```text
http://192.168.84.10:8088
```

Tu dois voir ton titre personnalisé ! Un test TCP réussi prouve l'accès au port ; le navigateur permet aussi de vérifier la réponse du service web. Si le premier test arrive trop tôt, attends une seconde puis recommence.

**D5. Observe la balise.**

```bash
sudo ss -ltnp | grep 8088
sudo journalctl -u tp10-web -n 10 --no-pager
```

Relève l'adresse d'écoute, le processus et une ligne `GET /` avec le code HTTP `200`.

**Question :** que signifie `0.0.0.0:8088` dans la sortie de `ss` ? Pourquoi utilise-t-on l'IP de la VM dans le navigateur, et pas `0.0.0.0` ?

**Badge : responsable de service** — ta balise fonctionne et tu sais le prouver.

---

## Partie E — Bonus : dépanne ta balise

**E1. Provoque une panne contrôlée — Session SSH Debian.**

```bash
sudo systemctl stop tp10-web
```

- `stop` : arrête uniquement le service du TP.

Dans la deuxième fenêtre PowerShell, relance `Test-NetConnection 192.168.84.10 -Port 8088`, puis recharge la page du navigateur. Attendu : `TcpTestSucceeded : False` et une erreur de connexion. Ta session SSH doit rester ouverte.

**E2. Enquête avant de réparer.** Avec les commandes déjà utilisées, relève :

1. L'état de `tp10-web`.
2. La présence ou l'absence d'écoute sur 8088.
3. Les dernières lignes de son journal.
4. L'état de `ssh`.

**E3. Rétablis la balise.** Retrouve la commande pour démarrer le service, puis vérifie le port avec `Test-NetConnection` et recharge la page dans Windows. Teste ensuite `restart` et refais ces vérifications.

**Question :** quelle différence entre `start`, `restart` et `daemon-reload` ?

**Badge : dépanneur** — tu as réparé le service sans couper ton accès distant.

---

## Partie F — Bonus avancé : le passage secret SSH

> [!NOTE] Pour aller plus loin
> Termine les bonus D et E avant cette partie. Tu réutilises la clé SSH créée en partie C pour accéder à la balise par un tunnel.

### F1. Cache la balise — Session SSH Debian

```bash
sudo nano /etc/systemd/system/tp10-web.service
```

Dans `ExecStart`, remplace `--bind 0.0.0.0` par `--bind 127.0.0.1`. La ligne devient :

```ini
ExecStart=/usr/bin/python3 -m http.server 8088 --bind 127.0.0.1
```

Enregistre avec `Ctrl+O`, valide avec Entrée, puis quitte avec `Ctrl+X`.

```bash
sudo systemctl daemon-reload
sudo systemctl restart tp10-web
sudo ss -ltnp | grep 8088
curl http://127.0.0.1:8088
```

- `daemon-reload` : relit le fichier modifié ; `restart` : relance le serveur avec sa nouvelle adresse d'écoute.
- `curl` : vérifie depuis Debian que la balise répond encore localement.

Attendu : écoute sur `127.0.0.1:8088` et page reçue dans Debian. Depuis Windows, le test du port 8088 donne maintenant `False` et l'accès direct au navigateur échoue. C'est volontaire : tu vas créer un autre chemin.

### F2. Ouvre le passage secret — PowerShell

Vérifie dans ta première session SSH que `tp10-web` fonctionne. Dans la nouvelle fenêtre PowerShell :

```powershell
ssh -i "$env:USERPROFILE\.ssh\id_ed25519_tp10" -o IdentitiesOnly=yes -o ExitOnForwardFailure=yes -N -L 127.0.0.1:18088:127.0.0.1:8088 stagiaire@192.168.84.10
```

- `-N` : aucun shell distant, seulement le tunnel.
- `-L` : transmet les connexions d'un port local à travers SSH.
- Le premier `127.0.0.1:18088` désigne Windows ; le second `127.0.0.1:8088` est joint depuis Debian.
- `ExitOnForwardFailure=yes` : arrête SSH si l'établissement du tunnel échoue, par exemple si le port local est occupé.

La fenêtre reste occupée sans invite : c'est normal. Dans le navigateur **Windows**, ouvre :

```text
http://127.0.0.1:18088
```

Tu dois retrouver ta page ! Si 18088 est occupé, remplace-le par 18089 dans la commande et l'URL.

```text
Navigateur Windows → Windows:18088 → SSH (VM:22) → Debian:8088
```

### F3. Le défi du détective

1. Pourquoi `127.0.0.1` désigne-t-il deux machines dans cette commande ?
2. Arrête `tp10-web` depuis ta première session SSH et recharge la page : que se passe-t-il ?
3. Redémarre le service et vérifie que la page revient.
4. Ferme le tunnel avec `Ctrl+C` dans PowerShell. Pourquoi la page devient-elle inaccessible alors que le service fonctionne toujours sur Debian ?
5. Pourquoi n'as-tu pas besoin de changer le port SSH ni d'exposer 8088 au réseau ?

**Badge bonus : architecte du passage secret** — montre ta page dans Windows, l'écoute locale 8088 sur Debian et explique le trajet.

---

## Partie G — Ranger la station après les bonus

Cette partie concerne uniquement ceux qui ont créé le service web. Ferme le tunnel s'il tourne encore. Dans la session SSH Debian :

```bash
sudo systemctl stop tp10-web
sudo rm /etc/systemd/system/tp10-web.service
sudo systemctl daemon-reload
systemctl show tp10-web.service -p LoadState
```

- `rm` : supprime seulement la définition créée pour le TP.
- Après relecture : `LoadState=not-found`.

Tu peux conserver la page et la clé du TP. Ne supprime pas `authorized_keys`, qui peut contenir d'autres clés.

```bash
exit
```

- `exit` : ferme la session SSH et rend la main à PowerShell.

## Compte rendu — Contrôle de mission

| Preuve | À relever |
|---|---|
| Réseau | Interface, IPv4/préfixe, passerelle et résultat du ping |
| Noms | Résultats local et DNS, ou erreur expliquée |
| SSH | Compte distant, port, état et activation au démarrage |
| Bonus web | Test TCP 8088, page dans le navigateur Windows, adresse d'écoute et trace HTTP 200 |
| Bonus incident | Diagnostic, réparation et preuve du rétablissement |
| Clé SSH | Rôle des fichiers public/privé et connexion par clé réussie |
| Bonus avancé | Trajet du tunnel et page reçue via le port local Windows |

**Débrief :** explique en trois phrases la différence entre une machine joignable, un nom résolu et un service disponible.

[← Revenir au cours](https://kayasam.github.io/linux-initiation/10-reseau-et-services/)

<a href="https://kayasam.github.io/linux-initiation/telechargements/tp/tp-10-reseau-et-services.md" download>Télécharger ce TP en Markdown</a>
