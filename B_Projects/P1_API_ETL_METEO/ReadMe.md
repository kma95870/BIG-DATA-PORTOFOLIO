# 🌦️ Open-Meteo ETL — Pipeline météo automatisé avec Docker, PostgreSQL & Streamlit

---

## 🧠 **Objectif du projet**

Ce projet met en place un **pipeline ETL complet** permettant de :

1. **Ingest** → Récupérer les données météo depuis l’API **Open-Meteo**.
2. **Transform** → Nettoyer, structurer et stocker les données en **Parquet**.
3. **Load** → Charger ces données dans une base **PostgreSQL** (via Docker).
4. **Visualiser** → Afficher les résultats dans un **dashboard Streamlit** interactif.

Ce projet démontre une architecture de données moderne, conteneurisée et automatisée — prête à être étendue vers le cloud.

---

## 🧩 **Architecture**

```
        ┌────────────────────┐
        │ ingest.py          │  → Appel API Open-Meteo (JSON)
        ├────────────────────┤
        │ transform.py       │  → Nettoyage + format Parquet
        ├────────────────────┤
        │ load.py            │  → Chargement dans PostgreSQL
        └────────────────────┘
                │
                ▼
        ┌────────────────────┐
        │ PostgreSQL (Docker)│  → Tables weather_hourly & weather_daily
        └────────────────────┘
                │
                ▼
        ┌────────────────────┐
        │ Streamlit Dashboard│  → Visualisation des données météo
        └────────────────────┘
```

---

## ⚙️ **Technologies**

| Composant        | Rôle                          | Outil                                 |
| ---------------- | ----------------------------- | ------------------------------------- |
| Source           | API de données météo          | [Open-Meteo](https://open-meteo.com/) |
| Extraction       | Appel API + JSON              | `requests`                            |
| Transformation   | Structuration & nettoyage     | `pandas`, `pyarrow`                   |
| Chargement       | Base de données relationnelle | `PostgreSQL` via Docker               |
| Visualisation    | Dashboard interactif          | `Streamlit`                           |
| Conteneurisation | Environnement reproductible   | `Docker Compose`                      |

---

## 🧱 **Structure du projet**

```
P1_API_ETL_METEO/
├── scripts/
│   ├── ingest.py              # Appel API Open-Meteo
│   ├── transform.py           # Nettoyage + Parquet
│   └── load.py                # Chargement PostgreSQL
├── data/
│   ├── raw/                   # Données brutes (JSON)
│   └── processed/             # Données nettoyées (Parquet)
├── app.py                     # Dashboard Streamlit
├── docker-compose.yml         # Stack Docker (Postgres + Adminer + Streamlit)
├── requirements.txt           # Dépendances Python
└── README.md
```

---

## 🚀 **Installation & Lancement**

### 1️⃣ Cloner le dépôt

```bash
git clone https://github.com/tonprofil/BIG-DATA-PORTOFOLIO.git
cd B_Projects/P1_API_ETL_METEO
```

### 2️⃣ Lancer les conteneurs Docker

```bash
docker compose up -d
```

✅ Cela démarre :

* **PostgreSQL** → base de données `etl_db` (port `5433`)
* **Adminer** → interface web SQL (port `8080`)
* **Streamlit** → dashboard météo (port `8501`)

---

### 3️⃣ Vérifier les services

| Service       | URL                                            | Description                   |
| ------------- | ---------------------------------------------- | ----------------------------- |
| **Adminer**   | [http://localhost:8080](http://localhost:8080) | Interface SQL pour PostgreSQL |
| **Streamlit** | [http://localhost:8501](http://localhost:8501) | Dashboard météo interactif    |

---

## 🧮 **Exécution manuelle du pipeline**

Tu peux exécuter les étapes individuellement depuis le terminal :

```bash
python scripts/ingest.py      # 1️⃣ Récupération API Open-Meteo
python scripts/transform.py   # 2️⃣ Transformation en Parquet
python scripts/load.py        # 3️⃣ Chargement dans PostgreSQL
```

Les fichiers produits seront visibles ici :

```
data/raw/20251017/openmeteo_20251017TxxxxxxZ.json
data/processed/hourly.parquet
data/processed/daily.parquet
```

---

## 📊 **Visualisation avec Streamlit**

Le dashboard affiche :

* Les dernières températures min / max 🌡️
* Les précipitations journalières 🌧️
* Le vent horaire 💨
* Des statistiques résumées sur la période collectée 📈

### Lancement manuel :

```bash
streamlit run app.py
```

Puis ouvrir : [http://localhost:8501](http://localhost:8501)

---

## 🗄️ **Connexion à PostgreSQL**

* **Host** : `localhost`
* **Port** : `5433`
* **Database** : `etl_db`
* **User** : `postgres`
* **Password** : `postgres`

Tu peux te connecter via :
👉 **Adminer** (interface web)
ou
👉 **psql / DBeaver / Python (SQLAlchemy)**

---

## 🧠 **Améliorations futures**

* Ajout de l’orchestration automatique (Airflow).
* Ajout d’un contrôle qualité des données (vérifications d’intégrité).
* Extension multi-villes (Paris, Lyon, Berlin...).
* Déploiement du pipeline sur le Cloud (AWS ou GCP).
* Intégration d’un cache API ou d’un mode incrémental.

---

## ⚠️ **Problèmes rencontrés & solutions**

| 💥 Problème                                                             | 🔍 Cause                                              | 🧩 Solution                                                         |
| ----------------------------------------------------------------------- | ----------------------------------------------------- | ------------------------------------------------------------------- |
| `requests.exceptions.Timeout` lors de l’appel API                       | L’API Open-Meteo met parfois trop de temps à répondre | Ajout d’un `timeout=30` dans `requests.get()`                       |
| Erreur `"AttributeError: 'DatetimeIndex' object has no attribute 'dt'"` | Mauvaise conversion dans `pd.to_datetime()`           | Corrigé avec `.to_series().dt.date`                                 |
| Connexion SQLAlchemy impossible                                         | Mauvais port ou container Postgres non démarré        | Vérification avec `docker ps` + port `5433`                         |
| Erreur `OperationalError` sur PostgreSQL                                | Docker Postgres pas encore prêt                       | Attendre quelques secondes ou relancer `docker compose up -d`       |
| Images manquantes sur GitHub                                            | Mauvais chemin relatif dans le README                 | Corriger avec `![texte](images/nom_image.png)` ou dossier `/assets` |

---

## 📚 **Exemple de résultats**

| date       | tmin_c | tmax_c | precip_sum_mm |
| ---------- | -----: | -----: | ------------: |
| 2025-10-17 |    9.2 |   18.6 |           0.0 |
| 2025-10-18 |   11.1 |   20.2 |           1.4 |
| 2025-10-19 |   10.8 |   19.7 |           2.3 |

---

## 👨‍💻 **Auteur**

**Moha Krim**
📊 Data Engineer / Analyst — Passionné de Big Data & Cloud
📫 [LinkedIn](https://www.linkedin.com/in/mohamed-amine-krim-65bb09220/) · [GitHub](https://github.com/kma95870)

---
