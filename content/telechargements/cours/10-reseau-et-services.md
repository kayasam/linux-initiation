# Chapitre 10 — Réseau et services

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
