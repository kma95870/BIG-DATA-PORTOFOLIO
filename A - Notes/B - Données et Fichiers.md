# 📂 Leçon : Les Fichiers dans le Monde de la Donnée

## 🗭 Introduction

Dans l’écosystème de la data, les fichiers sont les **conteneurs de l'information**. Que ce soit dans des bases relationnelles, des APIs, des Data Lakes ou des flux temps réel, **tout commence et finit souvent par un fichier**.

Comprendre les types de fichiers, leur structure, leur usage et leurs limites est **essentiel** pour toute personne travaillant dans l’ingénierie ou l’analyse de données.

---

## 🧱 1. Catégories de fichiers dans la data

| **Catégorie**               | **Types de fichiers**                    | **Utilisation typique**                           |
| --------------------------- | ---------------------------------------- | ------------------------------------------------- |
| Fichiers plats              | `.csv`, `.tsv`, `.txt`                   | Exports Excel, logs, données simples              |
| Fichiers structurés texte   | `.json`, `.xml`, `.yaml`                 | API, fichiers de config, données semi-structurées |
| Fichiers binaires           | `.parquet`, `.avro`, `.orc`              | Big Data, Data Lake, Spark                        |
| Feuilles de calcul          | `.xls`, `.xlsx`, `.ods`                  | Reporting, analyses métier                        |
| Fichiers de base de données | `.sqlite`, `.db`, `.mdb`, `.rds`, `.dta` | Stockage local ou format d'export de BDD          |
| Fichiers compressés         | `.zip`, `.gz`, `.bz2`, `.tar`            | Réduction taille de stockage ou transfert         |
| Fichiers modèles ML         | `.pkl`, `.joblib`, `.onnx`, `.h5`, `.pb` | Sauvegarde de modèles entraînés                   |
| Fichiers logs & traces      | `.log`, `.txt`, `.har`, `.out`           | Monitoring, debugging                             |

---

## 🚀 2. Focus sur les fichiers Big Data

Les formats **Big Data** sont conçus pour traiter de **gros volumes** de données de manière **rapide, efficace et distribuée**. Les plus courants sont :

* **CSV**
* **JSON**
* **Parquet**
* **Avro**
* **ORC**

---

### 📁 2.1 CSV (Comma-Separated Values)

#### ✅ Définition

Format **texte tabulaire**. Chaque ligne est un enregistrement, chaque colonne est séparée par une virgule, un point-virgule ou une tabulation.

#### 🔍 Exemple

```csv
id,name,age
1,Alice,30
2,Bob,25
```

#### 🧠 Contexte d’usage

* Fichiers d’export (Excel, bases de données)
* Données simples, non hiérarchiques

#### 🛠️ Manipulation

**Python (pandas)**

```python
import pandas as pd
df = pd.read_csv("data.csv")
df.to_csv("out.csv", index=False)
```

**Spark**

```python
df = spark.read.csv("data.csv", header=True, inferSchema=True)
df.write.csv("output/", header=True)
```

#### ⚠️ Limites

* Pas de schéma.
* Données typées manuellement.
* Inefficace pour la lecture sélective de colonnes.

---

### 🗞️ 2.2 JSON (JavaScript Object Notation)

#### ✅ Définition

Format **texte hiérarchique**, basé sur des paires clé-valeur. Permet des structures **imbriquées**.

#### 🔍 Exemple

```json
[
  {"id": 1, "user": {"name": "Alice", "age": 30}},
  {"id": 2, "user": {"name": "Bob", "age": 25}}
]
```

#### 🧠 Contexte d’usage

* API REST
* NoSQL (MongoDB)
* Échange de données entre systèmes

#### 🛠️ Manipulation

**Python**

```python
import json
with open("file.json") as f:
    data = json.load(f)
```

**Spark**

```python
df = spark.read.json("file.json")
df.write.json("output/")
```

#### ⚠️ Limites

* Volumineux (verbeux).
* Structure non tabulaire → traitement plus complexe.

---

### 🕦 2.3 Parquet

#### ✅ Définition

Format **binaire colonnaire**, compressé, avec schéma intégré. Très utilisé dans l’écosystème Hadoop/Spark.

#### 🔍 Illustration interne (logique)

```
[Colonne1] [Colonne2] [Colonne3]
→ Lecture optimisée uniquement sur les colonnes nécessaires
```

#### 🧠 Contexte d’usage

* Data Lake
* Spark, Hive, Presto
* Stockage optimisé Cloud (S3, GCS)

#### 🛠️ Manipulation

**Pandas (nécessite `pyarrow` ou `fastparquet`)**

```python
df = pd.read_parquet("data.parquet")
df.to_parquet("out.parquet")
```

**Spark**

```python
df = spark.read.parquet("data.parquet")
df.write.parquet("output/")
```

#### ⚠️ Limites

* Illisible sans outils.
* Plus lent en écriture (surtout petits fichiers).

---

### 🔴 2.4 Avro

#### ✅ Définition

Format **binaire orienté ligne** avec **schéma JSON intégré**. Idéal pour les systèmes distribués (Kafka).

#### 🔍 Exemple de schéma

```json
{
  "type": "record",
  "name": "User",
  "fields": [
    {"name": "id", "type": "int"},
    {"name": "name", "type": "string"}
  ]
}
```

#### 🧠 Contexte d’usage

* Kafka
* Streaming temps réel
* Échange de données évolutif

#### 🛠️ Manipulation

**PySpark**

```python
df = spark.read.format("avro").load("data.avro")
df.write.format("avro").save("output/")
```

**Python avec `fastavro`**

```python
from fastavro import reader
with open("file.avro", "rb") as f:
    for record in reader(f):
        print(record)
```

#### ⚠️ Limites

* Moins performant pour requêtes analytiques (vs Parquet).
* Moins lisible.

---

### 🕘 2.5 ORC (Optimized Row Columnar)

#### ✅ Définition

Format **colonnaire binaire** optimisé pour Hadoop et Hive, avec compression très efficace.

#### 🧠 Contexte d’usage

* Hadoop / Hive
* Data warehouse open source
* Requêtes analytiques lourdes

#### 🛠️ Manipulation

**Spark**

```python
df = spark.read.orc("data.orc")
df.write.orc("output/")
```

#### ⚠️ Limites

* Moins universel (moins supporté hors Hadoop).
* Moins répandu que Parquet en cloud.

---

## ♻️ Tableau comparatif des formats Big Data

| Format      | Type    | Compression | Lecture colonne | Streaming | Schéma intégré | Cas typique              |
| ----------- | ------- | ----------- | --------------- | --------- | -------------- | ------------------------ |
| **CSV**     | Texte   | ❌           | ❌               | ❌         | ❌              | Fichiers d’export / logs |
| **JSON**    | Texte   | ❌           | ❌               | ✅ (JSONL) | ❌              | API / NoSQL              |
| **Parquet** | Binaire | ✅ (Snappy)  | ✅               | ❌         | ✅              | Data Lake / S3 / GCP     |
| **Avro**    | Binaire | ✅           | Moyen           | ✅         | ✅ (JSON)       | Kafka / Streaming        |
| **ORC**     | Binaire | ✅✅          | ✅+              | ❌         | ✅              | Hive / Hadoop            |

---

## ✅ Conclusion

Maîtriser les formats de fichiers, c’est :

* **choisir le bon outil** pour le bon besoin.
* **optimiser le stockage et les performances**.
* **faciliter l’automatisation des pipelines** dans les architectures modernes (ETL, Data Lake, Kafka…).

---
