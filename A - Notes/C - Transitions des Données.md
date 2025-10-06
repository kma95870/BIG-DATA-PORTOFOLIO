
# 🔄 Comment les données se déplacent sur Internet — De la requête à la réponse

## 🌐 1. Qu’est-ce qu’Internet ?

Internet est un **réseau mondial d’infrastructures physiques** (câbles, routeurs, satellites...) permettant à des milliards de machines de communiquer entre elles grâce à des **protocoles standardisés**, notamment TCP/IP.

### 🏗️ Infrastructures réseau qui composent Internet

| Type d'infrastructure      | Exemple réel                        | Rôle                                                 |
|----------------------------|-------------------------------------|------------------------------------------------------|
| 🧵 Câbles sous-marins      | TAT-14, SEA-ME-WE                   | Connecter les continents                             |
| 🛰️ Satellites              | Starlink, Eutelsat                  | Accès dans les zones isolées                         |
| 📡 Antennes 4G/5G          | Free, Orange, SFR                   | Connexion mobile                                     |
| 🛣️ Backbone Internet       | Cogent, Level 3, Orange Business    | « Autoroutes » du trafic mondial                     |
| 🏢 Fournisseurs d’accès    | Orange, SFR, Free, Bouygues         | Accès au réseau pour les particuliers et entreprises |
| 🏠 Réseaux locaux (LAN)    | Box chez toi, réseaux d’entreprise  | Connexion locale des machines                        |
| 📶 Wi-Fi / Ethernet        | Routeur, câble RJ45                 | Connexion physique ou sans fil                       |
| 🔁 Routeurs                | Cisco, Juniper                     | Acheminent les paquets de données                    |
| 🔀 Switches                | TP-Link, Netgear                   | Dirigent les paquets dans un réseau local            |

📌 *Tous ces éléments forment ensemble la toile physique d’Internet.*

📌 Il repose notamment sur le protocole TCP/IP pour échanger des données de manière fiable.

## 📡 2. Protocole TCP/IP

### 📖 Qu’est-ce qu’un protocole ?

Un **protocole** est un ensemble de **règles standardisées** permettant à deux machines de **communiquer correctement**.

📌 C’est un langage commun : les deux appareils doivent le comprendre et l’appliquer exactement pareil.

**Exemples :*

* TCP/IP : envoi de paquets de manière fiable

* HTTP : récupération de pages web

* SMTP : envoi d’e-mails

* SSH : connexion sécurisée à distance


### 🧩 Les deux piliers de TCP/IP

| Protocole | Rôle |
|----------|------|
| **TCP** (Transmission Control Protocol) | Découpe les données en paquets, les numérote, garantit leur ordre et redemande ceux perdus |
| **IP** (Internet Protocol) | Achemine chaque paquet vers la bonne destination grâce à son adresse IP |

📌 IP = où envoyer / TCP = comment envoyer correctement

### 🧠 Vulgarisation TCP/IP

> **TCP**, c’est comme un **service postal intelligent** :  
> Il découpe un colis en morceaux, les numérote, vérifie qu’ils arrivent tous, et redemande ceux perdus.  
>  
> **IP**, c’est comme un **GPS** :  
> Il guide chaque paquet jusqu’à sa bonne adresse.

✅ Ensemble, **TCP/IP garantit que tes données arrivent intactes, dans l’ordre, et à bon port.**

## 🧭 3. Adresses IP et Ports

### 🔢 Adresse IP

Une adresse IP (Internet Protocol) est un **identifiant unique attribué à chaque machine** connectée à un réseau (Internet ou local).
Elle sert à envoyer et recevoir des données.

Il en existe deux versions principales :

- IPv4 (la plus répandue aujourd’hui)

- IPv6 (plus récente, pour remplacer l’épuisement des IPv4)

**🔢 IPv4 : comment est-elle construite ?**
Une adresse IPv4 est composée de 4 nombres entiers séparés par des points, appelés octets (ou "bytes").

**✅ Exemple :*
192.168.1.10
Chaque nombre est compris entre 0 et 255, car 1 octet = 8 bits → 2⁸ = 256 valeurs possibles.

🧠 Pourquoi cette forme ?
Chaque adresse fait 32 bits au total → 4 × 8 bits = 32 bits.

Ce format permet 4,29 milliards d’adresses uniques possibles (2³²).

🔍 Découpage logique d’une adresse IP
Une adresse IP est souvent divisée en deux parties :

| Partie      | Rôle                                    |
|-------------|------------------------------------------|
| Network ID  | Identifie le réseau                      |
| Host ID     | Identifie un appareil (hôte) dans ce réseau |

Le masque de sous-réseau (ex : /24) permet de savoir combien de bits sont utilisés pour le réseau.

**Exemple :*
```192.168.1.10/24``` signifie :

1. Les 24 premiers bits (donc 192.168.1) → réseau

2. Le dernier octet 10 → machine

#### 🧭 Types d’adresses IP

| Type       | Plage d’adresse         | Utilisation                                  |
|------------|--------------------------|-----------------------------------------------|
| Publique   | Variable                 | Visible sur Internet                          |
| Privée     | 192.168.x.x, 10.x.x.x    | Utilisée dans les réseaux locaux              |
| Loopback   | 127.0.0.1                | Adresse de la machine elle-même              |
| Broadcast  | 255.255.255.255          | Envoyer à tous les appareils du réseau        |
| APIPA (auto) | 169.254.x.x            | Adresse par défaut si pas d’accès DHCP        |


**🔒 IPv6 : pourquoi et comment ?**
📉 Problème :
Les IPv4 sont limitées (environ 4 milliards), or aujourd’hui on a des milliards d’objets connectés.

✅ Solution :
IPv6 permet 2¹²⁸ adresses (≈ 3,4 × 10³⁸ adresses possibles !)

🔧 Format :
8 groupes de 4 chiffres hexadécimaux (base 16)

Séparés par des deux-points :

**Exemple :*
```2001:0db8:85a3:0000:0000:8a2e:0370:7334```

**🧠 À retenir*
#### 🌐 Comparaison IPv4 vs IPv6

| IPv4                  | IPv6                            |
|------------------------|----------------------------------|
| 4 octets (32 bits)     | 8 groupes (128 bits)             |
| Ex: 192.168.0.1        | Ex: 2001:db8::1                  |
| Limité (2³²)           | Presque infini (2¹²⁸)           |
| Facile à lire          | Plus complexe                   |
| Utilisé partout        | En cours de généralisation       |


### 🔌 Ports

Un port, c’est comme une **porte d’entrée numérique** sur un ordinateur ou un serveur.
***Il permet à plusieurs services ou applications de coexister sur une même machine.***

🏠 Métaphore simple
Imagine que ton ordinateur est un immeuble :

L’adresse IP = l’adresse de l’immeuble (ex. : 192.168.0.10)

Les ports = les appartements à l’intérieur
Chaque service (web, mail, SSH...) a son propre port

Résultat : plusieurs services différents peuvent fonctionner en même temps sur une même machine.

**🧠 Exemple illustré :*
Quand tu tapes https://www.google.com :

1. Tu contactes l’adresse IP du serveur de Google.

2. Tu précises que tu veux passer par le port 443 (car c’est du HTTPS).

3. Le serveur te répond via ce port avec la page demandée.

➡️ Tu peux visiter un site Web, envoyer un mail, et jouer en ligne en même temps, car chaque activité utilise un port différent.

🔢 Les numéros de ports
Les ports vont de 0 à 65535, divisés en 3 grandes zones :

#### 🔌 Plages de ports TCP/UDP

| Plage          | Nom                       | Utilisation                                                                 |
|----------------|----------------------------|------------------------------------------------------------------------------|
| 0–1023         | Ports réservés/standards   | Utilisés par les services connus (HTTP, FTP...)                             |
| 1024–49151     | Ports enregistrés          | Utilisés par des logiciels connus (ex : PostgreSQL = 5432)                  |
| 49152–65535    | Ports dynamiques/privés    | Utilisés temporairement par ton PC pour initier une connexion               |

**📬 Exemples de services connus :*

| Service | Port | Utilisation |
|---------|------|-------------|
| HTTP | 80 | Navigation Web non sécurisée |
| HTTPS | 443 | Navigation Web sécurisée |
| FTP | 21 | Transfert de fichiers |
| SMTP | 25 | Envoi d’e-mails |
| SSH | 22 | Connexion à distance |

## 📦 4. Le paquet de données

Un paquet (ou data packet) est une **petite unité de donnée envoyée sur un réseau**.
**Quand tu veux envoyer un fichier, une vidéo, ou un message… on ne l’envoie pas d’un seul bloc : on le découpe en petits morceaux appelés paquets, qui seront transmis un par un.*

🔄 Pourquoi on découpe la donnée en paquets ?

* Pour accélérer la transmission

* Pour permettre le routage intelligent (chaque paquet peut prendre un chemin différent)

* Pour pouvoir retransmettre seulement les paquets perdus

* Pour standardiser la communication (tout le monde parle le même "langage réseau")

🛠️ Comment la transformation en paquets se passe-t-elle (techniquement) ?

Étapes en simplifié :
1. Tu veux envoyer une donnée
**Exemple : un fichier .jpg ou un message dans WhatsApp.*

2. Le système d’exploitation prépare la donnée
Il passe par les couches réseau du modèle OSI ou TCP/IP :

Application (ce que tu écris / envoies)

Transport (division en paquets)

Réseau (ajout de l’adresse IP)

Liaison de données (ajout de l’adresse MAC)

Physique (0 et 1 sur le câble ou l’antenne)

3. Encapsulation = création du paquet
À chaque niveau, on ajoute un petit "en-tête" d’info (comme une enveloppe) :

🧱 Contenu d’un paquet :

| Élément                 | Rôle                                        |
| ----------------------- | ------------------------------------------- |
| IP source/destination   | Où envoyer et d’où ça vient                 |
| Port source/destination | Identifier le service emmetteur/demandé     |
| Protocole               | TCP, HTTP, etc.                             |
| Numéro de séquence (TCP)| Permet de reconstruire l’ordre              |
| Donnée utile            | Le contenu réel (texte, image, commande...) |

✅ Le paquet contient donc les informations nécessaires pour être routé, interprété, remis dans l’ordre et traité.


1. Transmission
Le paquet est envoyé bit par bit sur un support physique :

* Câble Ethernet (fibre optique ou cuivre)

* Onde Wi-Fi ou 4G

* Satellite

2. Réception
L’appareil destinataire reconstitue le message en rassemblant les paquets dans l’ordre (grâce au numéro de séquence).

**Exemple concret :*
 1. Tu veux envoyer un fichier de 5 Mo.

 2. Le système le divise en +/- 3 500 paquets de 1 500 octets chacun.

 3. Chaque paquet contient une partie du fichier + des infos comme :
 * Numéro du paquet (ex : 122/3500)
 * Adresse IP de destination
 * Adresse MAC (Media Access Control : identifiant physique unique attribué à chaque carte réseau (Wi-Fi, Ethernet, etc.) d’un appareil. Elle sert à identifier une machine sur un réseau local (LAN)) de ta machine
 * Type de protocole (TCP, UDP…)

 4. Le fichier arrive chez le destinataire, qui recolle les morceaux dans le bon ordre, comme un puzzle numérique.

📬 Résumé simple :
### 🔄 Étapes du transfert de données sur Internet

| Étape       | Explication                                                  |
|-------------|--------------------------------------------------------------|
| 1️⃣ Encodage  | Tes données sont converties en bits (0 et 1)                |
| 2️⃣ Découpage | Elles sont découpées en paquets                             |
| 3️⃣ Enrobage  | On ajoute une enveloppe avec l’adresse, type, numéro, etc.  |
| 4️⃣ Envoi     | Chaque paquet part sur le réseau                            |
| 5️⃣ Réception | Les paquets sont reconstruits en un tout cohérent           |


## 🌐 5. Le Web et HTTP(S)

Le Web (ou World Wide Web) est un **service qui utilise Internet pour permettre l’accès à des pages web via un navigateur et les protocoles HTTP/HTTPS.** 

Fonctionnement :
1. Tu tapes une URL dans ton navigateur (https://wikipedia.org)

2. Le navigateur contacte le serveur web via HTTP/HTTPS

3. Le serveur envoie une page HTML en réponse

4. Le navigateur l’affiche

➡️ HTTP utilise le port 80, HTTPS utilise le port 443.

## 🌍 6. DNS : comment on passe d’un nom à une IP

Le DNS (Domain Name System) est un **service qui traduit les noms de domaine (lisibles) en adresses IP (utilisables par les machines).**

**Exemple :*

www.wikipedia.org → 198.35.26.96
Fonctionnement simplifié :
1. Le navigateur demande au DNS : “quelle est l’IP de ce site ?”

2. Le DNS consulte plusieurs serveurs (racine → TLD → autorité)

3. Une fois l’IP trouvée, elle est renvoyée au navigateur

4. Le navigateur établit une connexion TCP/IP à cette IP

## 🧩 Résumé global

```
[ Tu tapes une URL ]
       ↓
[ DNS : traduction du nom en IP ]
       ↓
[ TCP/IP : découpage + adresse + protocole ]
       ↓
[ Internet physique : câble, antenne, fibre, Wi-Fi ]
       ↓
[ Serveur distant : reçoit et répond ]
       ↓
[ Les paquets sont vérifiés, triés, reconstitués ]
       ↓
[ Le navigateur affiche la page ]
```

## ✅ À retenir pour un data engineer
***Toute communication numérique repose sur des paquets transmis via TCP/IP***

Le DNS est indispensable pour résoudre les noms de domaines

Les ports permettent d’identifier les services (HTTP, SSH, FTP…)

Ces notions sont fondamentales pour comprendre :

- les API REST

- les pipelines de données

- les connexions client ↔ serveur dans le cloud
