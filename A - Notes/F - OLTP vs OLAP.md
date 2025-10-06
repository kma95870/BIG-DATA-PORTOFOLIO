# OLTP, OLAP, ETL/ELT & Architecture Data Moderne

## 🧠 1. Introduction

Dans le monde de la data, il est crucial de **distinguer deux types de traitements** :
- **OLTP** : traitement transactionnel (en ligne)
- **OLAP** : traitement analytique (en ligne)

Ces deux mondes interagissent via des **pipelines de traitement de données**. Une bonne architecture les combine pour une exploitation optimale des données.

### 🧾 OLTP — Traitement transactionnel en ligne

OLTP désigne les **systèmes qui gèrent les transactions** quotidiennes d'une entreprise, comme les ventes, les réservations, les paiements, etc.

**Caractéristiques**

* Données fortement normalisées pour éviter les redondances.

* Traitement de milliers de requêtes courtes chaque seconde.

* Haute disponibilité et cohérence (souvent ACID).

* Utilisé dans les applications métiers : ERP, CRM, banques, e-commerce...

*Exemples :*

* Retirer de l’argent à un distributeur.

* Passer une commande sur Amazon.

* Réserver un billet d’avion.

### 📊 OLAP — Traitement analytique en ligne

OLAP désigne les **systèmes conçus pour l’analyse de données à grande échelle**, généralement dans des entrepôts de données (data warehouses).

**Caractéristiques**

* Données souvent dénormalisées pour accélérer les lectures.

* Requêtes lourdes et complexes : agrégations, comparaisons temporelles.

* Utilisé pour la décision stratégique, le reporting, les KPIs.

* Utilisé avec des outils de BI comme Tableau, Power BI, Looker…

*Exemples :*

* Visualiser les ventes par région et par trimestre.

* Analyser les tendances de churn client.

* Prédire la demande sur un produit.

### BDD typiques

| OLTP                          | OLAP                                    |
| ----------------------------- | --------------------------------------- |
| MySQL, PostgreSQL, SQL Server | BigQuery, Snowflake, Redshift, Teradata |
| MongoDB, Cassandra            | Apache Hive, ClickHouse, Druid          |

### Types de requêtes

**OLTP**
```SQL
-- Ajouter un nouvel utilisateur
INSERT INTO users (name, email) VALUES ('Alice', 'alice@mail.com');
```

**OLAP**
```sql
-- Total des ventes par année
SELECT year, SUM(sales) 
FROM sales_data 
GROUP BY year;
```

---

## ⚙️ 2. OLTP vs OLAP — Définitions et Comparaison

| Critère                | OLTP (Online Transaction Processing)     | OLAP (Online Analytical Processing)     |
|------------------------|-------------------------------------------|------------------------------------------|
| Objectif               | Gérer les transactions en temps réel     | Analyser de grandes quantités de données |
| Type de requêtes       | CRUD (Create, Read, Update, Delete)      | SELECT complexes (agrégations, regroupements) |
| Modèle de données      | Normalisé (3FN)                           | Dénormalisé (étoile, flocon)             |
| Performances attendues | Très rapides pour 1 ligne                 | Optimisé pour les lectures massives      |
| Volume de données      | Faible à moyen                            | Très grand (historique, multi-source)    |
| Données historiques    | Rarement                                  | Oui, toujours                           |
| Utilisateurs typiques  | Utilisateurs finaux, caisses, CRM         | Analystes, décideurs, BI                 |
| Exemple                | Ajouter une commande client               | Chiffre d’affaires par région            |

***📌 Remarques importantes***
Les deux peuvent coexister dans un système d'information moderne :
* OLTP pour les opérations en direct
* OLAP pour l’analyse a posteriori

ETL / ELT (Extract, Transform, Load) sert de pont entre OLTP (source de données) et OLAP (cible d’analyse).

Les bases de données hybrides (comme PostgreSQL + extension, ou même Snowflake avec des fonctionnalités transactionnelles) brouillent un peu les lignes.
---


## 🛠️ 3. ETL vs ELT 

| Phase       | ETL (Extract → Transform → Load) | ELT (Extract → Load → Transform) |
|-------------|-----------------------------------|-----------------------------------|
| Transformation | Avant chargement dans le DWH     | Après chargement dans le DWH      |
| Où ?         | Serveur intermédiaire ou Spark    | Dans le Data Warehouse lui-même   |
| Avantages    | Meilleur contrôle qualité         | Plus rapide si DWH scalable       |
| Exemples     | Talend, Informatica, Airflow + Python | dbt, BigQuery SQL, Snowflake SQL |

---

## 🔄 4. Fonctionnement global OLTP → ETL → OLAP — Pont entre OLTP et OLAP

**Objectif :**
Transférer les données des systèmes OLTP (sources) vers des entrepôts OLAP (cibles), où elles seront consolidées, nettoyées, historisées et analysées.

1. Extraction des données OLTP
Sources : bases relationnelles (PostgreSQL, MySQL), fichiers logs, API, NoSQL…

Format brut, souvent hétérogène.

Les données sont copiées régulièrement (batch ou stream).

On peut aussi capturer les modifications avec des Change Data Capture (CDC).

2. – Transformation
Nettoyage : suppression doublons, gestion des valeurs manquantes

Harmonisation : formats de dates, unités

Enrichissement : jointure avec d'autres sources, ajout de libellés

Agrégation : total mensuel, moyenne, etc.

Création de dimensions et faits (schéma en étoile/flocon)

🟡 Dans ETL, cela se fait en amont, sur un serveur de traitement intermédiaire.
🔵 Dans ELT, cela se fait directement dans le data warehouse (par ex. SQL sur Snowflake).

3. – Chargement dans l’entrepôt OLAP
Données injectées dans un entrepôt optimisé pour l’analyse : Snowflake, BigQuery, Redshift…

Organisées selon des modèles analytiques : modèle en étoile, flocon, data vault

Fréquence : en batch (quotidien, horaire) ou en streaming (quasi temps réel)


```text
        ┌────────────┐
        │  OLTP DB   │     ← ex: PostgreSQL
        └────┬───────┘
             │
     ┌───────▼────────┐
     │   Extraction   │
     └───────┬────────┘
             │
     ┌───────▼────────┐
     │ Transformation │   ← en Python, Spark, DBT, Talend…
     └───────┬────────┘
             │
     ┌───────▼────────┐
     │     Chargement │
     └───────┬────────┘
             │
        ┌────▼───────┐
        │   OLAP DB  │     ← ex: Snowflake, BigQuery
        └────────────┘
```

---

## 📚 5. Peut-on intervertir OLTP et OLAP ?

| ❓ Cas d’usage                          | Possible ? | Pourquoi c’est déconseillé                                      |
| -------------------------------------- | ---------- | --------------------------------------------------------------- |
| Faire une requête analytique dans OLTP | ✅          | Trop lent, surcharge système, normalisation                     |
| Écrire en direct dans un entrepôt OLAP | ✅          | Pas fait pour du CRUD, absence de contraintes transactionnelles |

🔎 Les **outils analytiques (OLAP)** ne sont **pas faits pour gérer des écritures fréquentes**. Inversement, les systèmes **OLTP ne sont pas conçus pour de l’analyse lourde.**

---

## 🏢 6. Étude de cas : Architecture Data pour Retail

### 🎯 Objectif :

* Suivre ventes, clients, stocks (OLTP)
* Faire des analyses (OLAP)
* Prédire la demande (ML)

---

### 📦 Sources de données (OLTP)

| Système         | Données collectées      | Format      |
| --------------- | ----------------------- | ----------- |
| Caisse (POS)    | Ventes                  | JSON / SQL  |
| Site e-commerce | Commandes, navigation   | API / logs  |
| Stock produits  | Mouvements de stock     | CSV / SQL   |
| Clients         | Profils, historiques    | SQL         |
| Fournisseurs    | Délais, produits livrés | API / Excel |

---

### 🔄 Pipeline ETL / ELT

| Étape          | Outils possibles              |
| -------------- | ----------------------------- |
| Extraction     | Airbyte, Fivetran, Kafka, API |
| Transformation | dbt, Spark, Python            |
| Chargement     | BigQuery, Snowflake, Redshift |

---

### 🗃️ Modélisation OLAP – Modèle en étoile

* **Table de faits** : `Fact_Ventes`
* **Dimensions** : `Dim_Produit`, `Dim_Client`, `Dim_Date`, `Dim_Magasin`

---

### 📊 Dashboards & Analytique

| Service   | Objectif                                 | Outils               |
| --------- | ---------------------------------------- | -------------------- |
| Direction | Ventes globales, marge, CA               | Power BI, Tableau    |
| Marketing | Panier moyen, churn, segmentation client | Looker, Data Studio  |
| Achat     | Prévision de stock, ruptures             | Excel, Dash, BI tool |

---

### 🧠 Use Cases Data Science

| Projet                 | Données utilisées          | Modèle               |
| ---------------------- | -------------------------- | -------------------- |
| Prévision de ventes    | Historique + météo         | XGBoost / Prophet    |
| Détection d’anomalies  | Ventes, stock, fournisseur | Isolation Forest     |
| Recommandation produit | Historique clients, achats | Matrix Factorization |
| Segmentation clients   | Achats, navigation         | K-means              |


---

## ✅ À retenir

* **OLTP** : rapide, fiable, normalisé → gestion des opérations quotidiennes.
* **OLAP** : puissant, analytique, historisé → prise de décision stratégique.
* **ETL/ELT** : relient les deux mondes avec des transformations de données.
* Une **architecture moderne** repose sur une bonne séparation des flux, des outils adaptés et une gouvernance solide.

---