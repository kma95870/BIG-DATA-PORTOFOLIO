# Dubai Vie — AI Perfume Advisor (RAG Chatbot)

Dubai Vie est un chatbot intelligent basé sur les LLM et le RAG (Retrieval-Augmented Generation), conçu pour recommander des parfums de manière personnalisée.

L'utilisateur décrit ses préférences (notes, saison, budget, occasion), et le système propose des parfums adaptés à partir d’un guide interne.

---

## Fonctionnalités

- Chat interactif (Streamlit)
- Recherche intelligente via FAISS
- Utilisation de modèles LLM (OpenAI)
- Analyse de documents PDF (guide parfums)
- Recommandations personnalisées
- Interface luxe inspirée de Dubai Vie

---

## Architecture du projet

    Utilisateur
        ↓
    Streamlit (UI)
        ↓
    RAG Pipeline
        ↓
    FAISS (recherche vectorielle)
        ↓
    Chunks (fiches parfums)
        ↓
    LLM (OpenAI)

---

## Structure du projet

    llm-chatbot-rag/
    │
    ├── app/
    │   ├── backend/
    │   │   ├── loader.py
    │   │   ├── chunker.py
    │   │   ├── vector_store.py
    │   │   ├── rag_pipeline.py
    │   │   └── prompt.py
    │   │
    │   └── frontend/
    │       ├── streamlit_app.py
    │       └── assets/
    │           └── dubai_vie.png
    │
    ├── data/
    │   ├── raw/
    │   │   └── guide_parfums.pdf
    │   └── vectorstore/
    │
    ├── requirements.txt
    ├── .env
    └── README.md

---

## Installation

### 1. Cloner le projet

    git clone https://github.com/ton-username/llm-chatbot-rag.git
    cd llm-chatbot-rag

### 2. Créer un environnement virtuel

    python -m venv .venv

Activation :

- Windows :

    .venv\Scripts\activate

- Mac/Linux :

    source .venv/bin/activate

### 3. Installer les dépendances

    pip install -r requirements.txt

---

## Configuration

Créer un fichier `.env` :

    OPENAI_API_KEY=your_api_key_here

---

## Construire la base vectorielle

    python -m app.backend.vector_store

---

## Lancer l'application

    streamlit run app/frontend/streamlit_app.py

---

## Exemples d'utilisation

- Je cherche un parfum gourmand pour l'hiver avec de la vanille  
- Compare Bleu de Chanel et Sauvage  
- Je veux un parfum élégant pour une soirée  

---

## Technologies utilisées

- Python  
- LangChain  
- OpenAI API  
- FAISS  
- Streamlit  

---

## Sécurité

- La clé OpenAI est stockée dans un fichier `.env`
- Ce fichier est exclu via `.gitignore`

---

## Améliorations futures

- Cartes parfum visuelles  
- Recommandation guidée  
- Déploiement cloud  
- Base de données réelle  

---

## Auteur

Projet réalisé dans le cadre d’un portfolio Data / AI.