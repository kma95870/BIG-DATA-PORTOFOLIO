

---

# 📘 Partie 1 : Fondamentaux du Traitement Distribué

---

## 1️⃣ Introduction au traitement distribué

### 📌 Définition

Le **traitement distribué** consiste à exécuter un programme ou un calcul sur plusieurs machines (appelées *nœuds*) connectées en réseau, afin de **partager la charge** et **accélérer le traitement**.

👉 Idée clé : *Diviser pour régner*.
Un gros problème est découpé en sous-problèmes, chacun est traité indépendamment, puis les résultats sont agrégés.

---

### 🎯 Pourquoi en avons-nous besoin ?

1. **Explosion des données** (Big Data).

   * Exemple : Google doit indexer des milliards de pages web.
2. **Accélérer les calculs lourds**.

   * Exemple : entraînement de modèles IA avec des milliards de paramètres.
3. **Tolérance aux pannes**.

   * Exemple : un serveur tombe en panne ? D’autres prennent le relais.
4. **Scalabilité**.

   * On ajoute des machines plutôt que d’acheter un seul super-ordinateur :
      * Data Scaling : techniques pour gérer, stocker et traiter de très grands volumes de données:
      - Vertical Scaling = augmenter la capacité d’une seule machine (CPU, RAM).
      - Horizontal Scaling = ajouter plusieurs machines (cluster distribué).

---

### 🔄 Différence avec d’autres approches

* **Centralisé** : tout est traité sur une seule machine.
* **Parallèle** : plusieurs processeurs dans une seule machine (ex : CPU multi-cœurs).
* **Distribué** : plusieurs machines indépendantes, reliées par un réseau.

---

### 🏢 Exemples concrets

* **Google Search** : utilise MapReduce puis Spark pour traiter les requêtes.
* **Netflix** : Spark pour recommandations personnalisées.
* **Uber** : Kafka + Flink pour analyser les trajets GPS en temps réel.
* **Safran / Airbus** : Spark Streaming pour analyser les capteurs moteurs.

---

## 2️⃣ Architecture d’un système distribué

Un **système distribué** est composé de plusieurs nœuds qui collaborent.

### 🔧 Rôles

* **Nœud maître (Master)** : coordonne et répartit les tâches.
* **Nœuds travailleurs (Workers)** : exécutent les calculs.
* **Système de stockage distribué** : garde les données accessibles à tous (HDFS, S3, etc.).

---

### 📊 Schéma simplifié

```
         +-------------------+
         |    Utilisateur    |
         +---------+---------+
                   |
             [Master Node]
          (coordonne le travail)
             /     |     \
   [Worker 1] [Worker 2] [Worker 3]
       |          |          |
   Données 1   Données 2   Données 3
```

---

### ⚡ Caractéristiques d’un système distribué

1. **Scalabilité horizontale** : on ajoute des machines pour plus de puissance.
2. **Tolérance aux pannes** : si un nœud échoue, un autre reprend le calcul.
3. **Parallélisme** : les données ou tâches sont traitées en même temps.
4. **Communication réseau** : les nœuds échangent des données.
5. **Hétérogénéité** : les machines peuvent être différentes (CPU, mémoire, OS).

---

## 3️⃣ Modèles de parallélisation

Il existe plusieurs façons de répartir le travail :

1. **Data Parallelism** : même tâche sur des morceaux différents de données.
   → Exemple : compter les mots dans 1 000 fichiers.

2. **Task Parallelism** : tâches différentes exécutées en parallèle.
   → Exemple : une tâche calcule la moyenne, une autre calcule la variance.

3. **Pipeline Parallelism** : les étapes se suivent comme une chaîne de montage.
   → Exemple : prétraitement → nettoyage → analyse → stockage.

4. **Embarrassingly Parallel** (parallélisme simple) :
   * Les tâches sont faciles à diviser et indépendantes.
   * Chaque nœud peut travailler seul sans communiquer avec les autres.
   → Exemple : appliquer la même fonction à 1 000 images.

5. **Non-Embarrassingly Parallel** (parallélisme complexe) :
   * Les tâches doivent communiquer entre elles.
   * Échanges fréquents entre nœuds (réseau).
   → Exemple : algorithmes où chaque étape dépend d’une autre (graphes, ML distribué).
   * Plus fragile : un seul nœud en panne peut bloquer le calcul.
---

## 4️⃣ Tolérance aux pannes

* **Réplication des données** : chaque fichier est stocké sur plusieurs nœuds.
* **Re-exécution des tâches** : si une machine tombe, une autre reprend.
* **Checkpointing** : sauvegarde intermédiaire des calculs pour éviter de tout recommencer.

---

## 5️⃣ Mini TP : Paralléliser un calcul en Python 🐍

Avant de passer à Hadoop/Spark, voyons un **exemple simple de traitement distribué** en Python avec le module `multiprocessing`.
But : calculer le carré de plusieurs nombres **en parallèle**.

```python
import multiprocessing

# Fonction à exécuter
def square(x):
    return x * x

if __name__ == "__main__":
    # Données à traiter
    data = [1, 2, 3, 4, 5, 6, 7, 8]

    # Création d'un pool de 4 workers
    pool = multiprocessing.Pool(processes=4)

    # Distribution des tâches
    results = pool.map(square, data)

    pool.close()
    pool.join()

    print("Résultats :", results)
```

👉 Ici, les 8 calculs sont distribués à 4 *workers* (processus) → plus rapide que séquentiel.
C’est le même principe qu’un cluster distribué, mais à l’échelle d’un seul ordinateur.

---

## ✅ Conclusion Partie 1

* Le traitement distribué = **partage du travail entre plusieurs machines**.
* Il repose sur **scalabilité, parallélisme et tolérance aux pannes**.
* On distingue plusieurs modèles (data, task, pipeline parallelism).
* En pratique, les systèmes modernes (Hadoop, Spark, Flink) implémentent ces principes.

---

# 📘 Partie 2 : Hadoop et l’ère MapReduce

---

## 1️⃣ Pourquoi Hadoop ?

👉 Problème de départ (années 2000) :

* Explosion du volume de données (web, logs, capteurs, etc.).
* Besoin d’un système **scalable**, **tolérant aux pannes** et **peu coûteux** (clusters de machines standards au lieu de supercalculateurs).

👉 Réponse : **Apache Hadoop**, inspiré des papiers de Google sur **Google File System (GFS)** et **MapReduce**.

---

## 2️⃣ Composants principaux d’Hadoop

Hadoop repose sur **3 briques principales** :

1. **HDFS (Hadoop Distributed File System)** → Stockage distribué.
2. **MapReduce** → Modèle de calcul distribué.
3. **YARN (Yet Another Resource Negotiator)** → Gestionnaire de ressources et d’exécutions.

---

## 3️⃣ HDFS (Hadoop Distributed File System)

### 📌 Fonctionnement

* Write Once, Read Many → on ne modifie pas un fichier existant, on ajoute des données nouvelles (append).
* Un fichier est découpé en **blocs** (par défaut 128 Mo).
* Chaque bloc est **répliqué** (souvent 3 copies) sur différents nœuds.
* Deux types de nœuds :

  * **NameNode** (maître) → tient la carte des fichiers et blocs.
  * **DataNodes** (travailleurs) → stockent réellement les blocs.

### 📊 Schéma

```
        +----------------+
        |    NameNode    | <-- gère la "métadonnée"
        +----------------+
           /    |     \
          /     |      \
 +----------+ +----------+ +----------+
 | DataNode | | DataNode | | DataNode |
 |  Bloc 1  | |  Bloc 2  | |  Bloc 3  |
 +----------+ +----------+ +----------+
```

### ✅ Avantages

* **Tolérance aux pannes** (réplication).
* **Scalabilité horizontale**.
* Accès distribué aux données.

---

## 4️⃣ MapReduce

### 📌 Définition

Un modèle de programmation inventé par Google (2004).
Deux étapes principales :

1. **Map** : appliquer une fonction à chaque élément des données (parallèle).
2. **Reduce** : agréger les résultats intermédiaires.

👉 Exemple : **Word Count** (compter les mots dans des millions de documents).

### 🔄 Exemple logique

Texte d’entrée :

```
"Alice aime Bob. Bob aime Alice."
```

* **Map** :

```
(Alice, 1), (aime, 1), (Bob, 1), (Bob, 1), (aime, 1), (Alice, 1)
```

* **Shuffle & Sort** (regroupement par clé) :

```
(Alice, [1, 1]), (aime, [1, 1]), (Bob, [1, 1])
```

* **Reduce** :

```
(Alice, 2), (aime, 2), (Bob, 2)
```

---

## 5️⃣ YARN (Yet Another Resource Negotiator)

### 📌 Rôle

* Introduit dans Hadoop 2.0 pour remplacer l’ancien gestionnaire.
* Gère **les ressources** (CPU, RAM) et **les jobs** sur le cluster.
* Permet à différents frameworks (MapReduce, Spark, Tez, etc.) de coexister sur le même cluster.

### ⚡ Fonctionnement

* **Resource Manager (RM)** : décide quelle tâche s’exécute où.
* **Node Manager (NM)** : gère les ressources de chaque machine.

---

## 6️⃣ Avantages et limites de Hadoop MapReduce

✅ Avantages :

* Très robuste et tolérant aux pannes.
* Conçu pour traiter du **Big Data massif**.
* Open-source et déployable sur des clusters de machines standards.

❌ Limites :

* **Lent** car écrit/lu sur disque à chaque étape (I/O coûteux).
* Modèle de programmation rigide (difficile à coder des algorithmes complexes).
* Nécessité d’outils complémentaires (Pig, Hive, Spark…).

👉 C’est cette lenteur qui a poussé à la création de **Apache Spark** (partie 3).

---

## 7️⃣ Mini TP : MapReduce en pseudo-code

Pour bien comprendre, voici un petit **MapReduce simulé en Python**.
On fait un **WordCount** distribué.

```python
from collections import defaultdict

# Étape MAP
def map_phase(texts):
    mapped = []
    for text in texts:
        for word in text.split():
            mapped.append((word.lower(), 1))
    return mapped

# Étape SHUFFLE (groupement par clé)
def shuffle_phase(mapped):
    grouped = defaultdict(list)
    for word, count in mapped:
        grouped[word].append(count)
    return grouped

# Étape REDUCE
def reduce_phase(grouped):
    reduced = {}
    for word, counts in grouped.items():
        reduced[word] = sum(counts)
    return reduced

# Jeu de données
texts = [
    "Alice aime Bob",
    "Bob aime Alice",
    "Alice adore Spark"
]

mapped = map_phase(texts)
grouped = shuffle_phase(mapped)
reduced = reduce_phase(grouped)

print("Résultat WordCount :", reduced)
```

👉 Résultat attendu :

```
{'alice': 3, 'aime': 2, 'bob': 2, 'adore': 1, 'spark': 1}
```

⚡ Ce code imite le **flux Map → Shuffle → Reduce** d’Hadoop.

---

## ✅ Conclusion Partie 2

* Hadoop a introduit **HDFS** pour le stockage et **MapReduce** pour le calcul distribué.
* **YARN** permet de gérer les ressources et d’exécuter plusieurs frameworks.
* MapReduce a été une révolution mais est devenu limité par sa lenteur → Spark est né.

---

# 📘 Partie 3 : Spark – le nouveau standard

---

## 1️⃣ Introduction à Spark

### 📌 Qu’est-ce que Spark ?

* Un **moteur de traitement distribué** open-source (créé en 2009 à l’université de Berkeley).
* Né pour **remplacer MapReduce** : plus rapide, plus flexible, plus facile à utiliser.
* Utilise la **mémoire vive (in-memory computing)** pour accélérer les calculs (au lieu de réécrire sur disque à chaque étape).
* Compatible avec : Scala, Python (PySpark), Java, R.

👉 Résultat : **jusqu’à 100x plus rapide que Hadoop MapReduce** dans certains cas.

---

### ⚡ Composants principaux

Spark n’est pas qu’un moteur, c’est tout un **écosystème** :

* **Spark Core** → moteur de base (RDD, DAG, scheduling).
* **Spark SQL** → manipulation de DataFrames et requêtes SQL.
* **MLlib** → Machine Learning distribué.
* **GraphX** → calculs sur graphes.
* **Spark Streaming / Structured Streaming** → traitement de flux en temps réel.

---

### 📊 Architecture Spark

Un cluster Spark ressemble à Hadoop/YARN mais avec sa logique propre :

* **Driver** → programme principal qui coordonne tout.
* **Cluster Manager** (YARN, Mesos ou Spark Standalone) → gère les ressources.
* **Executors** → processus qui exécutent les tâches sur les workers.

```
        [Driver Program]
        /       |       \
 [Executor 1] [Executor 2] [Executor 3]
       |            |            |
   Task 1.1     Task 2.1     Task 3.1
   Task 1.2     Task 2.2     Task 3.2
```

---

## 2️⃣ Spark Core : RDD et DAG

### 🔹 RDD (Resilient Distributed Dataset)

* Structure **de base** de Spark : collection distribuée, immuable, tolérante aux pannes.
* Dataset distribué sur plusieurs machines.
* Chaque transformation (map, filter, reduce) est appliquée en parallèle sur les partitions.
* **Résilient** : assurée par l’immutabilité et le DAG (Directed Acyclic Graph).

👉 Exemple :

```python
rdd = spark.sparkContext.parallelize([1, 2, 3, 4, 5])
```

---

### 🔹 DAG (Directed Acyclic Graph)

* Spark représente les transformations comme un **graphe orienté acyclique**.
* Permet l’optimisation automatique et la relance en cas de panne.

---

## 3️⃣ Transformations et Actions Spark

### ⚡ Transformations (lazy = différées)

* `map`, `flatMap`, `filter`, `reduceByKey`, `groupByKey`…
  👉 Ne s’exécutent pas directement → Spark construit un plan (DAG).

### ⚡ Actions (déclenchent le calcul)

* `collect()`, `count()`, `take()`, `saveAsTextFile()`…
  👉 Déclenchent réellement l’exécution du DAG.

---

### 📝 Exemple simple

```python
# Charger un RDD
rdd = spark.sparkContext.parallelize([1, 2, 3, 4, 5])

# Transformation
squared = rdd.map(lambda x: x * x)

# Action (exécution)
print(squared.collect())  # [1, 4, 9, 16, 25]
```

---

## 4️⃣ Spark SQL & DataFrames

### 📌 DataFrames

* Abstraction haut-niveau comme Pandas.
* Permet d’écrire des requêtes SQL sur des données distribuées.

👉 Exemple :

```python
df = spark.read.json("hdfs://data/people.json")
df.printSchema()
df.select("name").show()
df.filter(df["age"] > 21).show()
```

---

### 📌 Spark SQL

* Interface SQL pour requêter directement les DataFrames.

👉 Exemple :

```python
df.createOrReplaceTempView("people")
spark.sql("SELECT name, age FROM people WHERE age > 21").show()
```

---

## 5️⃣ Spark MLlib (Machine Learning)

* Librairie ML distribuée.
* Algorithmes : régression, classification, clustering, recommandation.
* Pipelines ML (prétraitement → features → modèle → évaluation).

👉 Exemple : régression logistique distribuée pour prédire du churn.

---

## 6️⃣ Spark Streaming

### 📌 Deux modes

1. **DStreams (legacy)** → micro-batchs.
2. **Structured Streaming (moderne)** → API unifiée DataFrame pour le temps réel.

👉 Exemple : lecture d’un flux Kafka.

```python
df = spark \
  .readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "localhost:9092") \
  .option("subscribe", "topic1") \
  .load()

df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)") \
  .writeStream \
  .format("console") \
  .start() \
  .awaitTermination()
```

---

## 7️⃣ Exemple pratique complet : WordCount en PySpark

```python
from pyspark.sql import SparkSession

# Créer session Spark
spark = SparkSession.builder.appName("WordCount").getOrCreate()

# Charger un fichier texte distribué
text_file = spark.sparkContext.textFile("hdfs://cluster/data/text.txt")

# Transformation
word_counts = (text_file
               .flatMap(lambda line: line.split(" "))
               .map(lambda word: (word, 1))
               .reduceByKey(lambda a, b: a + b))

# Action (collect)
print(word_counts.collect())
```

---

## 8️⃣ Avantages et limites de Spark

✅ Avantages :

* Ultra-rapide (in-memory).
* API riche et facile (SQL, ML, Streaming).
* Intégration avec Kafka, HDFS, S3, Cassandra…
* Compatible Python, Scala, Java, R.

❌ Limites :

* Peut consommer beaucoup de RAM.
* Optimisation parfois complexe (shuffle, partitionnement).
* Pas forcément adapté au **temps réel ultra faible latence** (Flink est meilleur).

---

## ✅ Conclusion Partie 3

* Spark est devenu le **standard** du traitement distribué.
* Remplace MapReduce en offrant un moteur **in-memory**, **flexible** et **rapide**.
* Écosystème complet : Core, SQL, MLlib, Streaming.
* Base de beaucoup de projets Big Data modernes (Netflix, Uber, Safran, etc.).

---

# 📘 Partie 4 : Alternatives et Extensions

---

## 1️⃣ Apache Flink

### 📌 Définition

* Framework de **traitement distribué en flux (stream-first)**.
* Né en 2015, souvent présenté comme le **concurrent direct de Spark Streaming**.

### ⚡ Différences avec Spark

* Spark Structured Streaming = micro-batchs (mini-lots de quelques ms/s).
* Flink = **vrai streaming temps réel** (event-at-a-time).

👉 Conséquence :

* **Spark** = bon compromis pour batch + streaming.
* **Flink** = spécialisé dans le temps réel **ultra faible latence**.

### 🏢 Cas d’usage

* Surveillance de capteurs IoT.
* Détection de fraudes bancaires en temps réel.
* Monitoring de systèmes critiques (finance, aéronautique).

---

## 2️⃣ Apache Kafka

### 📌 Qu’est-ce que Kafka ?

* Un **système de messagerie distribué** créé par LinkedIn (2011).
* Permet de gérer des **flux massifs de données en temps réel**.

### 🔧 Principes

* **Producer** → envoie des messages.
* **Topic** → file d’attente partitionnée, persistée.
* **Consumer** → lit les messages.
* **Broker** → serveur Kafka qui stocke les messages.

### 📊 Schéma

```
Producer --> [Kafka Topic Partitionné] --> Consumer
```

### 🏢 Cas d’usage

* Uber → flux de positions GPS.
* Netflix → suivi des logs utilisateurs.
* Safran → ingestion des données capteurs moteurs.

👉 Kafka **ne traite pas** les données → il les transporte.
Il est souvent couplé avec Spark ou Flink pour le calcul.

---

## 3️⃣ Bases de données distribuées (NoSQL)

Les systèmes de stockage distribués ne se limitent pas à HDFS ou S3 :
Certaines bases NoSQL sont conçues pour fonctionner en cluster.

### 🔹 Cassandra

* Base orientée colonnes.
* Scalabilité horizontale énorme (clusters mondiaux).
* Utilisée par Instagram, Netflix.

### 🔹 HBase

* Inspirée de Google BigTable.
* Fonctionne au-dessus de HDFS.
* Excellente pour les **grandes écritures/lectures distribuées**.

### 🔹 MongoDB (sharding + réplication)

* Base orientée documents JSON.
* Peut être distribuée grâce au **sharding** (partage horizontal des données).

### 🏢 Cas d’usage

* **Cassandra** → réseaux sociaux, logs.
* **HBase** → time series, IoT.
* **MongoDB** → applications web modernes, API.

---

## 4️⃣ Exemple pratique : Kafka → Spark Streaming

Exemple d’un flux **Kafka → Spark Streaming** qui lit des messages en temps réel.

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("KafkaSparkExample") \
    .getOrCreate()

# Lecture du flux Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "transactions") \
    .load()

# Transformer les données (clé/valeur en texte)
messages = df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")

# Écrire les résultats en temps réel dans la console
query = messages.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()
```

👉 Ici :

* Kafka alimente Spark avec un flux de données (ex. transactions bancaires).
* Spark Streaming les traite en temps réel (fraudes, agrégations, anomalies).

---

## 5️⃣ Avantages et inconvénients

✅ Avantages des extensions :

* Kafka : ingestion massive, scalable, résilient.
* Flink : meilleur temps réel que Spark.
* NoSQL distribuées : lecture/écriture ultra rapides.

❌ Inconvénients :

* Plus complexes à administrer.
* Pas toujours nécessaires si on reste dans le batch.
* Nécessitent souvent un écosystème complet (Kafka seul ne sert à rien, il faut un consommateur type Spark/Flink).

---

## ✅ Conclusion Partie 4

* **Flink** → temps réel ultra faible latence.
* **Kafka** → colonne vertébrale des flux Big Data.
* **Bases NoSQL distribuées** → stockage et accès rapides aux données massives.

👉 Dans beaucoup d’architectures modernes :
`Kafka → Spark/Flink → Stockage (HDFS/S3/NoSQL) → Dashboard (Tableau/Streamlit)`.

---

# 📘 Partie 5 : Le Cloud et la Data moderne

---

## 1️⃣ Pourquoi le Cloud pour le traitement distribué ?

### 📌 Problème

* Monter et gérer un cluster Hadoop/Spark **on-premise** (dans l’entreprise) est coûteux et complexe :

  * Acheter et maintenir les serveurs.
  * Configurer Hadoop/Spark, YARN, Kafka, etc.
  * Gérer la sécurité et la tolérance aux pannes.

### ⚡ Solution : Cloud

* Le cloud propose des **clusters managés** (Hadoop/Spark prêts à l’emploi).
* Facturation **à l’usage** → pas besoin d’investir dans du matériel.
* Scalabilité **quasi infinie** (ajout de nœuds à la demande).

👉 C’est la norme aujourd’hui : **le Big Data = Spark + Cloud**.

---

## 2️⃣ Déploiement Spark/Hadoop dans le Cloud

### 🔹 AWS

* **Amazon EMR (Elastic MapReduce)** : cluster Hadoop/Spark managé.
* **Amazon S3** : stockage distribué objet (remplace HDFS dans le cloud).
* **Glue** : ETL serverless.

### 🔹 Google Cloud Platform (GCP)

* **Dataproc** : cluster Hadoop/Spark managé.
* **BigQuery** : Data Warehouse serverless, SQL sur données massives.

### 🔹 Microsoft Azure

* **HDInsight** : cluster Hadoop/Spark.
* **Azure Synapse** : Data Warehouse cloud.

---

## 3️⃣ Nouvelles générations de solutions cloud

### 📌 Data Warehouse Cloud (Serverless)

* **BigQuery (GCP)** :

  * Pas de cluster à gérer.
  * Requêtes SQL sur des pétaoctets.

* **Snowflake** :

  * Data Warehouse multi-cloud.
  * Optimisé pour stockage + calcul séparés.

* **Amazon Redshift** :

  * Data Warehouse SQL distribué sur AWS.

👉 Ici, l’utilisateur **n’a même plus besoin de gérer le cluster**.
Tout est abstrait → on écrit du SQL, le cloud gère la distribution.

---

## 4️⃣ Exemple d’architecture Big Data moderne

```
            [Sources de données]
      IoT, Web logs, Transactions, API
                     |
                 (Kafka)
                     |
      +--------------------------------+
      |         Traitement Cloud       |
      |  - Spark (EMR / Dataproc)      |
      |  - Flink (Dataflow)            |
      +--------------------------------+
                     |
       +----------------------------+
       |  Stockage / Data Warehouse |
       |  - S3 / GCS / ADLS         |
       |  - BigQuery / Snowflake    |
       +----------------------------+
                     |
           [Visualisation / BI]
     Tableau, Power BI, Streamlit, Looker
```

---

## 5️⃣ Avantages du cloud

✅ **Scalabilité** : cluster ajustable en temps réel.
✅ **Pay as you go** : tu paies uniquement ce que tu utilises.
✅ **Pas d’infrastructure à maintenir**.
✅ **Multi-services intégrés** : stockage, IA, BI, orchestration.

---

## 6️⃣ Inconvénients du cloud

❌ **Coût caché** : mal optimisé, le cloud peut coûter cher.
❌ **Dépendance fournisseur (lock-in)**.
❌ **Sécurité et gouvernance** → données sensibles (banque, santé).

---

## 7️⃣ CI/CD et orchestration dans le cloud

### 🔹 Airflow

* Orchestrateur de workflows (ETL, ML pipelines).
* Permet de programmer les jobs Spark/BigQuery/Kafka.

### 🔹 Docker

* Emballe les applications (Spark job, API ML…) dans des conteneurs.
* Déploiement portable (cloud, local, Kubernetes).

### 🔹 Kubernetes (K8s)

* Orchestre des milliers de conteneurs (Docker).
* Spark peut tourner sur Kubernetes → très populaire.

---

## 8️⃣ Cas d’usage réels

* **Netflix** : Spark sur AWS EMR, S3 pour stockage, Tableau pour reporting.
* **Airbus** : analyse des capteurs en temps réel (Kafka + Spark + GCP).
* **Uber** : Kafka + Flink + Hadoop, migration vers Google Cloud.
* **Bouygues Telecom** (ton cas 😉) : BigQuery comme Data Warehouse, Spark en support.

---

## ✅ Conclusion Partie 5

* Le cloud a **révolutionné le traitement distribué** en le rendant accessible et flexible.
* Deux approches :

  * **Cluster managé** (EMR, Dataproc, HDInsight) → Hadoop/Spark sans maintenance.
  * **Serverless** (BigQuery, Snowflake) → SQL direct, plus de cluster.
* Le futur va vers des **architectures hybrides** : Kafka → Spark/Flink → Data Warehouse cloud → BI.

---



