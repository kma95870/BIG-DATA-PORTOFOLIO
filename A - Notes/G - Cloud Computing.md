# ☁️ Cours Complet – Comprendre le Cloud de A à Z

## 1️⃣ Introduction au Cloud Computing

Le **Cloud Computing** est un modèle de fourniture de ressources informatiques (serveurs, stockage, bases de données, réseaux, logiciels, etc.) **via Internet**, en **libre-service** et **facturées à l’usage**.

### 🎯 Objectifs principaux

* Éviter l’achat et la maintenance d’infrastructures physiques coûteuses.
* Gagner en flexibilité et rapidité de déploiement.
* Payer uniquement ce que l’on utilise.

### Ce qu’on appelle “le Cloud”

Le **Cloud**, ce n’est pas quelque chose d’abstrait dans le ciel ☁️.
C’est **un ensemble de data centers** (centres de données) appartenant à des fournisseurs comme **AWS, Microsoft Azure, Google Cloud, OVH…**.

Ces data centers contiennent :

* Des **serveurs physiques** 🖥 (comme de gros PC ultra-puissants)
* Des **disques de stockage** 📦 (HDD, SSD)
* Du **réseau** 🔌 (switchs, routeurs, fibres optiques)
* Des systèmes de **refroidissement** ❄️
* De la **sécurité physique** (gardes, badges, biométrie)

---

###  Que se passe-t-il quand tu stockes un fichier dans le Cloud ?

Prenons un exemple concret : **tu mets une photo sur Google Drive**.

1. **Envoi via Internet**

   * Ton fichier est envoyé depuis ton PC ou ton téléphone via une connexion sécurisée (HTTPS / TLS).
   * Les données sont **chiffrées en transit** (protégées pendant le transport).

2. **Arrivée dans le data center**

   * Le fichier arrive dans un des serveurs de stockage du fournisseur.
   * Le choix du data center dépend :

     * De ta localisation (pour réduire la latence)
     * Des lois locales (ex. RGPD → stockage en Europe)
     * De la configuration choisie (AWS S3 “région Paris” vs “région Virginie”)

3. **Stockage et réplication**

   * Le fichier est **découpé en blocs** puis stocké sur plusieurs disques (souvent dans plusieurs serveurs différents).
   * Ces blocs sont **répliqués** dans **plusieurs data centers** de la même région pour éviter la perte de données en cas de panne.
   * Exemple : AWS S3 garde **au moins 3 copies** de chaque objet dans des endroits distincts.

4. **Indexation et métadonnées**

   * Le système enregistre **où se trouvent les blocs** (un index).
   * Les métadonnées (nom du fichier, date, taille, permissions) sont stockées séparément.

5. **Sécurité au repos**

   * Les données sont **chiffrées au repos** (AES-256 par exemple) → même si un disque est volé, il est inutilisable sans clé.

6. **Accès ultérieur**

   * Quand tu veux télécharger le fichier, le Cloud :

     1. Vérifie que tu as les droits d’accès.
     2. Rassemble les blocs depuis différents serveurs.
     3. Te renvoie le fichier complet.

---

### Métaphore simple

Stocker dans le Cloud, c’est comme mettre un document dans un **coffre-fort ultra-sécurisé** géré par une société :

* 📦 Ils mettent **plusieurs copies** dans différents coffres.
* 🗺 Ils savent **exactement où** chaque morceau est stocké.
* 🔐 Ils **verrouillent** le coffre avec une clé de chiffrement.
* 🚚 Tu peux y accéder **depuis n’importe où** avec la bonne clé.

---

### Schéma simplifié du trajet

```
[Ton appareil]
   |
   v
(Connexion HTTPS)
   |
   v
[Data center du fournisseur Cloud]
   |
   ├── Réplication dans plusieurs serveurs
   ├── Chiffrement des données
   ├── Sauvegarde dans plusieurs lieux
   |
   v
[Index & stockage]
```

---

💡 **À retenir** :

* Tes données **ne flottent pas dans un nuage**, elles sont **physiquement stockées dans des serveurs**.
* Elles sont **répliquées** pour éviter les pertes.
* Elles sont **chiffrées** pour éviter les accès non autorisés.
* Tu peux **choisir la région** pour des raisons de performance ou de conformité.

---

## 2️⃣ Modèles de services : IaaS, PaaS, SaaS

Ces trois modèles ne sont pas séparés du Cloud, **ce sont trois manières différentes de consommer le Cloud**.
Ils représentent **différents niveaux d’abstraction et de responsabilité**.

| Modèle                                   | Ce que tu gères                 | Ce que le fournisseur gère                           | Exemple                                  |
| ---------------------------------------- | ------------------------------- | ---------------------------------------------------- | ---------------------------------------- |
| **IaaS** *(Infrastructure as a Service)* | OS, middleware, applis, données | Serveurs physiques, stockage, réseau, virtualisation | AWS EC2, Azure VM                        |
| **PaaS** *(Platform as a Service)*       | Applications et données         | OS, middleware, infrastructure                       | Google App Engine, AWS Elastic Beanstalk |
| **SaaS** *(Software as a Service)*       | Juste l’usage                   | Tout (infra → appli)                                 | Gmail, Dropbox, Slack                    |

### Métaphore 🚗

* **IaaS** → On te donne une voiture sans chauffeur (tu conduis et gères l’entretien).
* **PaaS** → On te donne une voiture avec chauffeur (tu donnes juste la destination).
* **SaaS** → Tu prends un taxi ou Uber (tout est déjà prêt).

---

## 3️⃣ Cas d’utilisation et utilisateurs finaux

### **IaaS**

* **Cas** : hébergement de sites complexes, clusters Big Data, bases lourdes, stockage massif.
* **Utilisateurs** : admins systèmes, DevOps, data engineers.
* **Exemples** : AWS EC2, Azure VM.

### **PaaS**

* **Cas** : déploiement rapide d’applis, API, ML, CI/CD.
* **Utilisateurs** : développeurs, data scientists, startups.
* **Exemples** : Google App Engine, Heroku.

### **SaaS**

* **Cas** : messagerie, CRM, bureautique en ligne.
* **Utilisateurs** : grand public, entreprises.
* **Exemples** : Gmail, Slack, Netflix.

---

## 4️⃣ Degré de contrôle

| Élément            | On-Premise | IaaS | PaaS | SaaS |
| ------------------ | ---------- | ---- | ---- | ---- |
| Applications       | ✅          | ✅    | ✅    | ❌    |
| Données            | ✅          | ✅    | ✅    | ✅    |
| Middleware         | ✅          | ✅    | ❌    | ❌    |
| OS                 | ✅          | ✅    | ❌    | ❌    |
| Virtualisation     | ✅          | ❌    | ❌    | ❌    |
| Serveurs physiques | ✅          | ❌    | ❌    | ❌    |

✅ = géré par toi / ❌ = géré par le fournisseur.

---

## 5️⃣ Accès aux différents modèles

* **SaaS** : Lien web, appli mobile/desktop → ex : `https://mail.google.com`.
* **PaaS** : Console web, CLI, API, CI/CD → ex : `gcloud app deploy`.
* **IaaS** : Console web, CLI, API, SSH/RDP → ex : `ssh user@ip_du_serveur`.

---

## 6️⃣ Comment fonctionne le Cloud concrètement ?

### Les données vont :

1. **De ton appareil → Internet (HTTPS/TLS)**.
2. **Arrivent dans un data center** (choix selon localisation, lois, configuration).
3. **Sont découpées en blocs et répliquées** sur plusieurs serveurs/zones.
4. **Chiffrées au repos**.
5. **Réassemblées et envoyées** lors de l’accès.

💡 Tes données **ne flottent pas** dans un nuage : elles sont stockées dans des serveurs physiques, dans un ou plusieurs data centers.

---

## 7️⃣ Stockage Cloud = stockage distribué

* **Par défaut** : répartition sur plusieurs serveurs / data centers.
* **Avantages** : tolérance aux pannes, haute disponibilité, scalabilité, performance.
* **Exceptions** : stockage non répliqué volontaire (rare, “single zone” sur S3).

---

## 8️⃣ Comment communiquer avec les données dans le Cloud

| Méthode              | Exemples                    | Avantage                      | Cas d’usage |
| -------------------- | --------------------------- | ----------------------------- | ----------- |
| API / SDK            | boto3, google-cloud-storage | Contrôle complet              | Scripts ETL |
| SQL distribué        | BigQuery, Athena, Snowflake | Pas de déplacement de données | Analytics   |
| Traitement distribué | Spark, Hadoop               | Scalabilité                   | Big Data    |
| Base managée         | RDS, DynamoDB               | Transactions rapides          | Apps web    |
| Streaming            | Kafka, Kinesis              | Temps réel                    | IoT, fraude |

---

## 9️⃣ Composants clés du Cloud


### ☁️ Les Composants Fondamentaux du Cloud

### 1️⃣ **Compute** – La puissance de calcul

📌 **Rôle** : Fournir la capacité de traitement (processeur, RAM, GPU) pour exécuter des applications ou analyser des données.

**Principales formes :**

* **Machines virtuelles (VM)** : Serveurs virtuels configurables (ex : AWS EC2, Azure VM, GCP Compute Engine).
* **Containers** : Environnements légers isolés (Docker, Kubernetes).
* **Serverless** : Exécution à la demande sans gérer de serveurs (AWS Lambda, Google Cloud Functions).
* **GPU / HPC instances** : Calcul intensif (IA, simulation, rendu 3D).

**Cas d’usage :**

* Héberger un site web.
* Lancer un cluster Big Data.
* Entraîner un modèle de deep learning.

---

### 2️⃣ **Storage** – Le stockage

📌 **Rôle** : Conserver les données sous différentes formes avec des garanties de disponibilité et de performance.

**Types de stockage :**

* **Bloc** *(Block Storage)* : Similaire à un disque dur, attaché à une VM (ex : AWS EBS).
* **Objet** *(Object Storage)* : Stockage massif et distribué, chaque fichier = un objet (ex : AWS S3, Azure Blob Storage).
* **Fichier** *(File Storage)* : Système de fichiers partagé en réseau (ex : AWS EFS, Azure Files).
* **Stockage archivage** : Pour données rarement consultées (AWS Glacier).

**Cas d’usage :**

* **Bloc** → Base de données, OS.
* **Objet** → Sauvegardes, gros fichiers, data lakes.
* **Fichier** → Partage entre plusieurs serveurs.

---

### 3️⃣ **Networking** – La connectivité

📌 **Rôle** : Gérer comment les ressources Cloud communiquent entre elles et avec l’extérieur.

**Éléments clés :**

* **VPC (Virtual Private Cloud)** : Réseau privé isolé.
* **Subnets** : Sous-réseaux pour séparer les ressources.
* **Load Balancer** : Répartit la charge entre plusieurs serveurs.
* **VPN / Direct Connect** : Connexion sécurisée au réseau interne.
* **Pare-feu / Security Groups** : Contrôle du trafic entrant/sortant.

**Cas d’usage :**

* Séparer un environnement de test et de production.
* Accès sécurisé à une base depuis un siège social.
* Répartition du trafic web mondial.

---

### 4️⃣ **Bases de données**

📌 **Rôle** : Stocker, organiser et interroger les données.

**Catégories :**

* **SQL (relationnelles)** : PostgreSQL, MySQL, SQL Server, Oracle.
* **NoSQL** :

  * Clé-Valeur (Redis, DynamoDB)
  * Document (MongoDB, Firestore)
  * Colonne (Cassandra, Bigtable)
  * Graphe (Neo4j)

**Cas d’usage :**

* SQL → Données structurées, transactions.
* NoSQL → Scalabilité, flexibilité, gros volumes.

---

### 5️⃣ **Sécurité & Gestion des accès**

📌 **Rôle** : Protéger les ressources et contrôler qui peut faire quoi.

**Composants :**

* **IAM (Identity & Access Management)** : Gère les utilisateurs, rôles et permissions.
* **Chiffrement** : Données au repos (AES-256), en transit (TLS).
* **Audit & Logs** : Suivi des actions (CloudTrail, Stackdriver).
* **Pare-feu applicatif (WAF)** : Protection contre attaques web.

**Cas d’usage :**

* Restreindre un bucket S3 à un groupe précis.
* Tracer qui a supprimé une ressource.
* Se conformer au RGPD.

---

### 6️⃣ **Services managés**

📌 **Rôle** : Fournir des services “clé en main” sans maintenance lourde.

**Exemples :**

* **Analyse de données** : BigQuery, AWS Redshift.
* **Machine Learning** : SageMaker, Vertex AI.
* **Streaming** : Kinesis, Pub/Sub.
* **CI/CD** : AWS CodePipeline, Cloud Build.

**Cas d’usage :**

* Éviter de gérer l’infrastructure.
* Accélérer le déploiement.
* Profiter d’outils spécialisés sans les installer.

---

### 7️⃣ **Monitoring & Observabilité**

📌 **Rôle** : Surveiller la santé, la performance et la sécurité des ressources.

**Outils :**

* **CloudWatch** (AWS), **Azure Monitor**, **Stackdriver** (GCP).
* **Alertes** : Notifier quand une ressource dépasse un seuil.
* **Logs centralisés** : Analyse d’événements.
* **Tracing** : Suivi des appels d’API.

---

💡 **Résumé visuel mental :**

```
CLOUD
│
├── Compute (VM, Containers, Serverless, GPU)
├── Storage (Bloc, Objet, Fichier, Archivage)
├── Networking (VPC, Subnets, LB, VPN, Security)
├── Bases de données (SQL, NoSQL)
├── Sécurité (IAM, Encryption, WAF, Logs)
├── Services managés (ML, Data, CI/CD)
└── Monitoring (Metrics, Logs, Alerts)
```

---

## 🔟 Modèles économiques du Cloud

| Modèle                 | Description                                   | Avantage                 |
| ---------------------- | --------------------------------------------- | ------------------------ |
| **Pay-as-you-go**      | Facturation à l’usage réel                    | Économie et flexibilité  |
| **Reserved Instances** | Réservation de ressources pour 1 à 3 ans      | Réduction de coûts       |
| **Spot Instances**     | Achat d’instances non utilisées à prix réduit | Idéal pour calculs batch |
| **Free Tier**          | Niveau gratuit limité                         | Idéal pour apprentissage |


## Hébergement

Quand on demande *« chez qui est hébergé x »* :

* On veut savoir **où tournent les serveurs** qui font fonctionner la plateforme.
* Options :

  * **On-Premise** chez Bouygues (data center interne).
  * **Cloud privé** chez un hébergeur (ex : OBS, Equinix).
  * **Cloud public** (AWS, Azure, GCP).
* Importance : sécurité, conformité, performance, coûts.

---

## 🧠 Schéma mental global

```
CLOUD
│
├── Modèles : IaaS / PaaS / SaaS (contrôle ↓)
├── Accès : SaaS (web/appli), PaaS (console/CLI/API), IaaS (console/SSH)
├── Données : envoyées → data center → stockées et répliquées → sécurisées
├── Communication : API/SDK, SQL distribué, Spark, bases managées, streaming
├── Composants : compute, storage, networking, DB, sécurité, services, monitoring
└── Cas spécifiques : hébergement Dataiku = choix fournisseur / interne
```

---

