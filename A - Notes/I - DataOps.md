# 📚 DevOps pour la Data (DataOps)

---

## 1. 🌍 Introduction : Qu’est-ce que le DevOps pour la Data ?

* **DevOps classique** = rapprocher Dev (développeurs) et Ops (ops/infra) → livraisons plus rapides, plus fiables.
* **DataOps** = adaptation de DevOps au cycle de vie **des données** :

  * Accélérer ingestion → transformation → livraison.
  * Automatiser la qualité et les déploiements des pipelines.
  * Améliorer la collaboration entre **Data Engineers, Analysts, Scientists et Ops**.

👉 Objectif : **livrer de la valeur Data plus vite, avec plus de qualité et moins d’erreurs**.

---

## 2. 🔄 Cycle de vie DataOps

1. **Ingestion** → Collecte des données (batch, streaming).
2. **Stockage** → Data Lake (S3, HDFS) + Data Warehouse (BigQuery, Snowflake, Redshift).
3. **Transformation** → ETL/ELT (Spark, dbt, Airflow, Dataiku).
4. **Qualité** → tests, validation de schémas (Great Expectations).
5. **Déploiement** → CI/CD pour pipelines, modèles ML, jobs Spark.
6. **Orchestration** → Airflow, Prefect, Dagster.
7. **Monitoring** → performance + qualité + fraisheur des données.
8. **Consommation** → BI (Tableau, Power BI), APIs, modèles ML.

---

## 3. 🧰 Les briques DevOps appliquées à la Data

| Domaine                    | Outils principaux                  | Cas d’usage Data                                |
| -------------------------- | ---------------------------------- | ----------------------------------------------- |
| **Versioning**             | Git, DVC, LakeFS                   | Versionner code ET données                      |
| **CI/CD**                  | GitHub Actions, GitLab CI, Jenkins | Déploiement auto de pipelines, tests de données |
| **Containerisation**       | Docker                             | Standardiser un ETL, un modèle ML               |
| **Orchestration**          | Airflow, Prefect, Dagster          | Gérer dépendances de jobs                       |
| **Infrastructure as Code** | Terraform, Ansible                 | Créer clusters Spark, bases, S3                 |
| **Cloud & Stockage**       | AWS S3, GCP, Azure                 | Data Lake, DWH                                  |
| **Monitoring**             | Grafana, Prometheus, ELK           | Observabilité, alertes                          |
| **Qualité des données**    | Great Expectations, dbt tests      | Contrôles de cohérence et fraîcheur             |
| **Secrets**                | Vault, KMS, Kubernetes Secrets     | Sécuriser accès DB, API, S3                     |

---

## 4. 🔄 CI/CD expliqué simplement

### 1. 📌 Définition

* **CI = Continuous Integration (Intégration Continue)**
  👉 Automatiser le fait de **tester et valider** ton code/data **à chaque modification**.

* **CD = Continuous Delivery / Continuous Deployment (Livraison & Déploiement Continu)**
  👉 Automatiser le fait de **mettre en production** ton code/data de façon **rapide, fiable et répétable**.

---

### 2. ⚙️ Schéma du cycle CI/CD

```
Développeur → Git (commit/push) 
      ↓
Pipeline CI (tests automatiques, qualité de code, tests de données)
      ↓
Pipeline CD (déploiement auto → ETL, DAG Airflow, modèle ML, API)
      ↓
Production (cluster Spark, Airflow, Data Lake, API BI)
```

---

### 3. 🔍 CI (Continuous Integration)

But = **vérifier que le code est bon avant de l’intégrer**.

Exemples dans la Data :

* Tests unitaires sur du code Python ou PySpark.
* Tests de **qualité des données** (ex. pas de doublons, pas de valeurs manquantes inattendues).
* Vérification que les scripts SQL s’exécutent sans erreur.
* Build d’images Docker reproductibles.

👉 CI se lance **à chaque `git push` ou `merge request`**.

---

### 4. 🚀 CD (Continuous Delivery/Deployment)

But = **mettre automatiquement en production ce qui a été validé**.

Exemples dans la Data :

* Déployer un DAG Airflow mis à jour dans le cluster.
* Déployer un job Spark packagé en Docker sur Kubernetes.
* Mettre à jour un modèle ML dans une API.
* Rafraîchir un dashboard (ex : dbt + Tableau).

👉 CD se déclenche après la CI si tout est vert ✅.

---

### 5. 🔧 Exemple pratique (GitHub Actions)

### Cas : un ETL PySpark → testé puis déployé dans Airflow

```yaml
name: Data Pipeline CI/CD
on: [push]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Install deps
        run: pip install -r requirements.txt
      - name: Run unit tests
        run: pytest tests/

  deploy:
    runs-on: ubuntu-latest
    needs: test
    steps:
      - uses: actions/checkout@v2
      - name: Deploy DAG
        run: ./deploy_to_airflow.sh
```

---

### 6. 🎯 Avantages de CI/CD pour la Data

* **Moins d’erreurs** : tout est testé avant d’arriver en prod.
* **Plus rapide** : pas besoin de déployer à la main.
* **Reproductible** : même pipeline de tests et de déploiement pour tout le monde.
* **Collaboration** : plusieurs data engineers/scientists travaillent sans casser le projet.

---

✅ En résumé :

* **CI = tester automatiquement le code + données** à chaque changement.
* **CD = déployer automatiquement en production si tout est OK**.

---

## 5. 📦 CI/CD appliqué à la Data

### CI (Integration Continue) :

* Vérifie le code (lint, tests unitaires).
* Vérifie les **tests de données** (schéma, doublons, nullité).
* Vérifie la reproductibilité (Docker build).

### CD (Déploiement Continu) :

* Déploie un DAG Airflow.
* Déploie un job Spark sur cluster (on-prem ou cloud).
* Déploie un modèle ML en API.

👉 Exemple GitHub Actions pour ETL PySpark :

```yaml
name: CI/CD Data Pipeline
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Install deps
        run: pip install -r requirements.txt
      - name: Run tests
        run: pytest tests/
      - name: Deploy to Airflow
        run: ./deploy_dag.sh
```

---

## 6. 🧪 Tests en DataOps

### a) **Tests unitaires de code**

* Exemple : fonction PySpark qui bucketise un âge.
* Outils : `pytest`, `chispa` (comparaison DataFrames).

### b) **Tests de données**

* Great Expectations → ex : "colonne age > 0".
* dbt tests → unique, not null, foreign keys.

### c) **Tests d’intégration**

* Testcontainers (Kafka, Postgres, MinIO).
* Moto (mock AWS).

### d) **Tests End-to-End**

* Pipeline complet : ingestion → transformation → stockage → consommation.
* Validé en staging avant la prod.

---

## 7. 🏗️ Infrastructure as Code (IaC)

* **Terraform** → provisionne les ressources Cloud :

  * Buckets S3 / Data Lake.
  * Cluster Spark EMR ou GKE.
  * Base Redshift, BigQuery.

👉 Exemple Terraform pour un bucket S3 :

```hcl
resource "aws_s3_bucket" "data_lake" {
  bucket = "my-data-lake"
  acl    = "private"
}
```

* **Ansible** → configure les serveurs (install Spark, Airflow, Kafka).

---

## 8. ☸️ Conteneurs & Orchestration

### Docker :

* Packager un script ETL (Python, PySpark).
* Déployer un modèle ML (FastAPI, Flask).

Exemple Dockerfile :

```dockerfile
FROM python:3.9
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /app
WORKDIR /app
CMD ["python", "etl.py"]
```

### Orchestration (Airflow / Prefect / Dagster) :

* DAGs = dépendances entre jobs (ex : ingestion → transformation → load).
* Monitoring intégré.
* Relance en cas d’échec.

Exemple Airflow DAG :

```python
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG("etl_pipeline", start_date=datetime(2023,1,1), schedule_interval="@daily") as dag:
    ingest = BashOperator(task_id="ingest", bash_command="python ingest.py")
    transform = BashOperator(task_id="transform", bash_command="python transform.py")
    load = BashOperator(task_id="load", bash_command="python load.py")

    ingest >> transform >> load
```

---

## 9. 📊 Monitoring en DataOps

* **Observabilité technique** :

  * CPU, mémoire (Prometheus + Grafana).
  * Logs (ELK Stack).
* **Observabilité Data** :

  * Fraîcheur des tables (Airflow sensors).
  * Qualité des données (Great Expectations).
  * Data Drift en ML (EvidentlyAI, MLflow).

👉 Exemple : alerte Slack si une table n’a pas été mise à jour depuis 24h.

---

## 10. 🔐 Sécurité et Gouvernance

* Secrets : stockés dans Vault / Secrets Manager.
* Accès aux données : IAM, RBAC.
* RGPD : anonymisation, masquage, minimisation.
* Lineage : Data Catalog (ex : Collibra, DataHub, Amundsen).

---

## 11. 🚦 Bonnes pratiques DataOps

1. **Versionner tout** (code + données + infra).
2. **Automatiser les tests** → pipeline bloqué si données KO.
3. **Conteneuriser les jobs** → reproductibles.
4. **Automatiser les déploiements** (CI/CD).
5. **Surveiller la donnée et non seulement le code**.
6. **Infra as Code** → cluster/data lake créés automatiquement.
7. **Collaboration** → Dev + Data Engineer + Analyst + Ops + ML eng.

---

## 12. 📈 Exemple d’architecture DataOps moderne

1. **Ingestion** : Kafka / Fivetran / API.
2. **Stockage** : S3 Data Lake + Snowflake/BigQuery.
3. **Transformation** : dbt + Spark.
4. **Orchestration** : Airflow.
5. **Tests Data** : Great Expectations.
6. **CI/CD** : GitHub Actions (déploiement DAGs + dbt).
7. **Monitoring** : Prometheus + Grafana + Slack alerts.

---

## 13. 🧭 Roadmap d’apprentissage DevOps pour la Data

1. Git + GitHub Actions (CI/CD).
2. Docker (packager un job ETL).
3. Airflow (orchestrer pipelines).
4. Great Expectations (tests data).
5. Terraform (provisionner S3/BigQuery).
6. Monitoring (Prometheus/Grafana).
7. Kubernetes (scalabilité Spark, Airflow, Kafka).

---
