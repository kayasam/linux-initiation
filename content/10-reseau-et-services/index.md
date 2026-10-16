---
title: "10. Réseau et services"
---

# Chapitre 10 — Réseau et services

<nav class="chapter-resources" aria-label="Ressources du chapitre" data-course-key="10-reseau-et-services" style="--resource-count:4"><div class="resource-buttons"><a class="resource-button resource-markdown" data-resource-kind="markdown" aria-label="Cours — Lire le cours en Markdown" href="https://kayasam.github.io/linux-initiation/10-reseau-et-services/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24"><rect x="1" y="1" width="30" height="22" rx="3" fill="none" stroke="#34495e" stroke-width="2"/><path d="M5 18V6h3l4 5 4-5h3v12h-3v-7l-4 5-4-5v7Z" fill="#34495e"/><path d="M23 6h3v7h3l-4.5 5-4.5-5h3Z" fill="#34495e"/></svg></span><span class="resource-label">Cours<small>Lire le cours en Markdown</small></span></a><a class="resource-button resource-html" data-resource-kind="html" aria-label="HTML — Explorer le chapitre" href="https://kayasam.github.io/linux-initiation/10-reseau-et-services/html/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 28 32"><path d="M2 2h24l-2 25-10 3-10-3Z" fill="#e44d26"/><path d="M14 5v22l7-2 2-20Z" fill="#f16529"/><path d="M7 8h15l-.3 3H11l.3 3h10l-.8 9-6.5 2-6.5-2-.4-5h3l.2 2.6 3.7 1 3.7-1 .3-3.6H8Z" fill="#fff"/></svg></span><span class="resource-label">HTML<small>Explorer le chapitre</small></span></a><a class="resource-button resource-quiz" data-resource-kind="quiz" aria-label="Quiz — 20 questions" href="https://kayasam.github.io/linux-initiation/10-reseau-et-services/quiz/"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="4" y="3" width="24" height="26" rx="6" fill="#7652ad"/><path d="M12 12a4 4 0 1 1 6 3.5c-1.5.8-2 1.4-2 3" fill="none" stroke="#fff" stroke-width="2.8" stroke-linecap="round"/><circle cx="16" cy="23" r="1.6" fill="#fff"/></svg></span><span class="resource-label">Quiz<small>20 questions</small></span></a><a class="resource-button resource-tp" data-resource-kind="tp" aria-label="TP — Mettre en pratique" href="https://kayasam.github.io/linux-initiation/10-reseau-et-services/tp"><span class="resource-icon" aria-hidden="true"><svg class="resource-symbol" width="24" height="24" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect x="2" y="4" width="28" height="24" rx="5" fill="#237b60"/><path d="m8 12 5 4-5 4m9 0h7" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg></span><span class="resource-label">TP<small>Mettre en pratique</small></span></a></div><div class="resource-actions"><a class="resource-download" href="https://kayasam.github.io/linux-initiation/telechargements/cours/10-reseau-et-services.md" download aria-label="Télécharger le cours en Markdown"><span aria-hidden="true">↓</span> Télécharger .md</a><button type="button" class="support-focus-toggle" aria-pressed="false">Masquer les menus</button></div></nav>


---

## 1. Vérifier la connectivité réseau

### Afficher les interfaces réseau

```bash
ip address         # affiche toutes les interfaces et leurs adresses IP
ip -br address     # version courte et lisible
```

Exemple de sortie :
```
lo     UNKNOWN   127.0.0.1/8
enp0s3 UP        10.0.2.15/24
```

| Interface | Description |
|-----------|-------------|
| `lo` | Loopback — interface locale (127.0.0.1) |
| `enp0s3` | Carte réseau Ethernet |
| `wlan0` | Carte réseau Wi-Fi |

### Tester la connectivité — `ping`

```bash
ping 8.8.8.8          # teste la connectivité vers un serveur Google
ping google.com        # teste aussi la résolution DNS
ping -c 4 google.com   # envoie 4 paquets et s'arrête
```

```bash
Ctrl + C    # pour arrêter un ping en cours
```

---

## 2. Se connecter à distance — SSH

**SSH** (*Secure Shell*) permet de se connecter à un autre ordinateur Linux **en ligne de commande**, de façon sécurisée et chiffrée.

> [!NOTE]
> **Analogie** : SSH, c'est comme un téléphone sécurisé entre toi et un serveur distant. Tu tapes des commandes chez toi, elles s'exécutent là-bas.
```bash
ssh utilisateur@adresse_ip          # connexion standard
ssh stagiaire@192.168.1.10          # exemple avec IP locale
ssh -p 2222 stagiaire@192.168.1.10  # port non standard
```

Pour quitter une session SSH :
```bash
exit
# ou Ctrl + D
```

> [!TIP]
> SSH est l'outil principal pour administrer des serveurs Linux à distance. La quasi-totalité de l'administration système professionnelle se fait via SSH.
<!-- illustration-10 -->
![Les commandes SSH s’exécutent sur la machine distante.](https://kayasam.github.io/linux-initiation/ressources/images/10-connexion-ssh.svg)

*Les commandes SSH s’exécutent sur la machine distante.*

---

## 3. Résoudre des noms — DNS

Le **DNS** (*Domain Name System*) traduit les noms de domaine (google.com) en adresses IP (142.250.74.46).

```bash
# Vérifier la résolution DNS
host google.com
nslookup google.com

# Afficher les DNS configurés
cat /etc/resolv.conf
```

Le fichier `/etc/hosts` permet de définir des correspondances locales (sans DNS) :
```bash
cat /etc/hosts
# 127.0.0.1   localhost
# 192.168.1.10  mon-serveur
```

---

## 4. Les services (daemons)

Un **service** (ou *daemon*) est un programme qui tourne en arrière-plan en permanence. Exemples : serveur web, serveur SSH, base de données…

Linux moderne utilise **systemd** pour gérer les services.

### Commandes essentielles

```bash
# État d'un service
sudo systemctl status ssh

# Démarrer / arrêter / redémarrer
sudo systemctl start ssh
sudo systemctl stop ssh
sudo systemctl restart ssh

# Activer / désactiver au démarrage
sudo systemctl enable ssh     # démarre automatiquement à chaque boot
sudo systemctl disable ssh    # ne démarre plus automatiquement

# Lister tous les services
systemctl list-units --type=service
systemctl list-units --type=service --state=running   # uniquement les actifs
```

### Voir les logs d'un service

```bash
sudo journalctl -u ssh          # tous les logs du service ssh
sudo journalctl -u ssh -f       # en temps réel
sudo journalctl -u ssh --since "1 hour ago"  # depuis 1 heure
```

---

## 5. Informations réseau utiles

```bash
ss -tulnp          # liste les ports en écoute (remplace netstat)
ss -tulnp | grep 22   # vérifier si SSH est en écoute

ip route           # table de routage (passerelle par défaut)
```

---

## Récapitulatif des commandes

| Commande | Description |
|----------|-------------|
| `ip address` | Affiche les interfaces réseau et leurs adresses IP |
| `ip -br address` | Version courte et lisible |
| `ping adresse` | Teste la connectivité réseau |
| `ping -c 4 adresse` | Envoie 4 paquets et s'arrête |
| `ssh user@ip` | Connexion SSH à distance |
| `exit` | Quitter une session SSH |
| `host domaine` | Résolution DNS d'un nom de domaine |
| `cat /etc/hosts` | Voir les correspondances DNS locales |
| `sudo systemctl status service` | État d'un service |
| `sudo systemctl start service` | Démarrer un service |
| `sudo systemctl stop service` | Arrêter un service |
| `sudo systemctl restart service` | Redémarrer un service |
| `sudo systemctl enable service` | Activer au démarrage |
| `sudo systemctl disable service` | Désactiver au démarrage |
| `sudo journalctl -u service` | Voir les logs d'un service |
| `ss -tulnp` | Liste les ports en écoute |

---

> [!NOTE]
> ### À retenir
>
> - `ip address` (ou `ip -br a`) affiche les interfaces réseau et leurs adresses IP.
> - `ping adresse` teste la connectivité réseau — `Ctrl+C` pour arrêter.
> - **SSH** permet de se connecter à distance de façon sécurisée : `ssh utilisateur@ip`.
> - Le fichier `/etc/hosts` définit des correspondances nom ↔ IP locales (sans DNS).
> - Un **service** (daemon) est un programme tournant en arrière-plan — géré par **systemd**.
> - `systemctl start/stop/restart` démarre/arrête/redémarre un service.
> - `systemctl enable/disable` configure le démarrage automatique au boot.
> - `journalctl -u service` consulte les logs d'un service.
---

---

[← Redirections et tubes](https://kayasam.github.io/linux-initiation/09-redirections-et-tubes/) · [Revenir à l’accueil →](https://kayasam.github.io/linux-initiation/)
