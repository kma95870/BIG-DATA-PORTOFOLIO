# 🧠 Cours Complet — Les LLM (Large Language Models)

---

# Partie 1 : Introduction

# 📘 1. Qu’est-ce qu’un LLM ?

## 🔍 Définition

Un **LLM (Large Language Model)** est un modèle d’intelligence artificielle capable de :

* comprendre du texte
* générer du texte
* répondre à des questions
* traduire, résumer, coder, etc.

Exemples :

* ChatGPT
* Claude
* Gemini

---

## 🧠 Idée clé

Un LLM ne “comprend” pas comme un humain.
Il **prédit le mot suivant** en fonction du contexte.

Exemple :

```
Le chat est sur le ___
```

→ le modèle prédit : *“canapé”*

---

# ⚙️ 2. Comment fonctionne un LLM ?

## 🔄 Principe fondamental : prédiction

Un LLM apprend à :

```
mot1 → mot2 → mot3 → mot4
```

Il calcule des probabilités :

* P(mot suivant | contexte)

---

## 🧱 Architecture : les Transformers

Les LLM sont basés sur une architecture appelée :

Transformer architecture

### 💡 Pourquoi c’est révolutionnaire ?

* Comprend le contexte global
* Traite les phrases en parallèle
* Gère les longues dépendances

---

## 🔥 Le mécanisme clé : l’attention

Attention mechanism

Le modèle “regarde” les mots importants dans une phrase.

Exemple :

```
Le chat qui est noir dort
```

“dort” dépend de “chat”, pas de “noir”

---

# 📊 3. Comment on entraîne un LLM ?

## 🏋️ Phase 1 : Pré-entraînement

Le modèle lit **des milliards de textes** :

* livres
* articles
* sites web

Il apprend les structures du langage

---

## 🎯 Phase 2 : Fine-tuning

On ajuste le modèle pour :

* être plus précis
* éviter les erreurs
* répondre correctement

---

## 🤖 Phase 3 : RLHF

Reinforcement Learning with Human Feedback

Des humains évaluent les réponses → le modèle s’améliore.

---

# 📦 4. Ce qu’un LLM peut faire

## ✨ Capacités

* Génération de texte
* Traduction
* Résumé
* Code
* Chatbot
* Analyse de données textuelles

---

## ❌ Limites

* Peut halluciner (inventer)
* Pas toujours fiable
* Dépend des données d’entraînement
* Pas de “vraie compréhension”

---

# 🧠 5. Pourquoi c’est important 

Dans ton domaine (Data / AI) :

Les LLM sont utilisés partout :

* Chatbots intelligents
* Analyse de documents
* Automatisation métier
* Copilotes (code, data, etc.)

---

# Partie 2 : Tokenization, Embeddings & Prompting

---

# 🔤 1. La Tokenization (ultra important)

## 🧩 Qu’est-ce que c’est ?

Un LLM ne comprend pas directement les mots.
Il découpe le texte en **tokens**.

Exemple :

```text
"ChatGPT est incroyable"
```

peut devenir :

```text
["Chat", "G", "PT", " est", " incroyable"]
```

Un token ≠ un mot
C’est une **unité de texte**

---

## 🧠 Pourquoi c’est crucial ?

* Les modèles travaillent **uniquement sur des tokens**
* Les coûts (API) dépendent du nombre de tokens
* La limite de contexte = nombre max de tokens

---

## 📊 Exemple concret

| Texte                | Tokens |
| -------------------- | ------ |
| Bonjour              | 1      |
| Machine learning     | 2      |
| internationalisation | 3-5    |

---

## ⚠️ Implication importante

Une phrase longue = plus de tokens = plus cher + plus lent

---

# 🔢 2. Les Embeddings (clé des systèmes modernes)

## 🧠 Définition

Un embedding = **représentation numérique d’un texte**

C’est un vecteur de nombres :

```text
"chat" → [0.25, -0.91, 0.78, ...]
```

---

## 💡 Idée clé

Les mots similaires ont des vecteurs proches

Exemple :

* chat 🐱 ≈ chien 🐶
* chat ❌ voiture 🚗

---

## 📐 Similarité (cosinus)

On mesure la proximité entre deux vecteurs :

Cosine similarity

---

## 🚀 Cas d’usage

* Recherche intelligente
* Recommandation
* RAG (très important)
* Clustering de texte

---

## 🧪 Exemple Python

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

emb1 = model.encode("chat")
emb2 = model.encode("chien")

print(emb1)
```

---

# 🧠 3. Prompt Engineering (hyper stratégique)

## 🔥 Définition

Le prompt = ce que tu dis au modèle

Le prompt engineering = **l’art de bien poser la question**

---

## ❌ Mauvais prompt

```text
Explique moi
```

trop vague → réponse moyenne

---

## ✅ Bon prompt

```text
Explique le fonctionnement des LLM en 5 points simples avec exemples
```

précis → réponse excellente

---

## 🧩 Techniques importantes

### 1. Zero-shot

```text
Traduis en anglais : Bonjour
```

---

### 2. Few-shot

```text
Exemple :
chat → cat
chien → dog

Traduis :
oiseau →
```

---

### 3. Chain of Thought

Faire réfléchir le modèle étape par étape

```text
Explique ton raisonnement étape par étape
```

---

### 4. Rôle (très puissant)

```text
Tu es un data engineer expert en Big Data.
Explique Kafka simplement.
```

---

# 🌡️ 4. Paramètres du modèle

## 🔥 Température

| Valeur | Effet        |
| ------ | ------------ |
| 0      | déterministe |
| 0.7    | équilibré    |
| 1+     | créatif      |

---

## 🎲 Top-k / Top-p

* **Top-k** → limite aux k mots probables
* **Top-p** → prend un % de probabilité

contrôle la diversité des réponses

---

# 🧠 5. Contexte (Context Window)

Nombre max de tokens que le modèle peut lire

Exemples :

* 4k tokens
* 32k tokens
* 128k tokens

---

## ⚠️ Problème

Si trop long :

* le modèle oublie le début
* perte d’information

---

## 💡 Solution

Chunking (découper le texte)

---

# 🔥 6. Ce que tu dois absolument retenir

* Token = unité de base
* Embedding = représentation vectorielle
* Prompt = clé de performance
* Température = créativité
* Contexte = limite mémoire

---

# 🧠 Cours LLM — Partie 3 : RAG (Retrieval Augmented Generation)

---

# 🚀 1. Le problème des LLM

Les LLM ont un gros défaut ❌ :

Ils **n’ont pas accès à tes données**
Ils peuvent **halluciner**
Ils ne sont pas à jour

---

## 💡 Exemple

```text
Donne-moi les données météo de mon projet
```

Le LLM ne connaît pas ta base PostgreSQL
Il invente une réponse

---

# 🔥 2. Solution : RAG

Retrieval Augmented Generation

## 🧠 Définition

RAG = Architecture en intelligence artificielle qui consiste à combiner un modèle de langage (LLM) avec un système de recherche d’information afin de produire des réponses plus fiables, précises et basées sur des données réelles.
**on donne au LLM les bonnes informations AVANT qu’il réponde**

---

## 📦 Pipeline RAG

```
Question utilisateur
        ↓
Recherche dans une base (embeddings)
        ↓
Récupération des données pertinentes
        ↓
Injection dans le prompt
        ↓
Réponse du LLM
```

---

# 🧩 3. Architecture RAG (important)

## 🔹 Étape 1 : Indexation

Tu prends tes données :

* PDF
* base SQL
* fichiers texte

Tu les transformes en **embeddings**

---

## 🔹 Étape 2 : Stockage

Tu stockes les vecteurs dans une **Vector DB** :

- FAISS
- Pinecone
- Weaviate

---

## 🔹 Étape 3 : Recherche

Quand l’utilisateur pose une question :

- on transforme la question en embedding
- on cherche les textes les plus proches

---

## 🔹 Étape 4 : Génération

On envoie au LLM :

```text
Contexte : [données récupérées]
Question : [question utilisateur]

Réponds uniquement avec ces informations
```

---

# 🧠 4. Exemple concret (TON projet météo)

## 🎯 Objectif

Créer un chatbot :

```text
"Quelle est la température moyenne cette semaine ?"
```

---

## ⚙️ Pipeline réel

1. Tu récupères tes données PostgreSQL
2. Tu les transformes en texte
3. Tu fais des embeddings
4. Tu stockes dans FAISS
5. Tu poses une question
6. Le système récupère les données
7. Le LLM répond correctement

---

# 💻 5. Exemple simple en Python

## 🔹 Embeddings + FAISS

```python
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    "Température lundi : 18°C",
    "Température mardi : 20°C",
    "Température mercredi : 19°C"
]

embeddings = model.encode(documents)

index = faiss.IndexFlatL2(len(embeddings[0]))
index.add(np.array(embeddings))

# question
query = "Quelle température mardi ?"
q_emb = model.encode([query])

D, I = index.search(np.array(q_emb), k=2)

print([documents[i] for i in I[0]])
```

---

# 🤖 6. Ajouter un LLM

Ensuite tu fais :

```text
Contexte :
Température mardi : 20°C

Question :
Quelle température mardi ?

Réponds :
```

Et le LLM répond correctement ✅

---

# 🔥 7. Pourquoi RAG est ULTRA important

C’est LA techno utilisée partout :

* ChatGPT entreprise
* assistants internes
* copilotes métiers
* moteurs de recherche intelligents

---

# 🧠 8. RAG vs Fine-tuning

| RAG       | Fine-tuning |
| --------- | ----------- |
| dynamique | statique    |
| pas cher  | coûteux     |
| rapide    | long        |
| scalable  | complexe    |

En pratique → **RAG est préféré**

---

# ⚠️ 9. Limites du RAG

* dépend de la qualité des embeddings
* nécessite une bonne base de données
* latence plus élevée

---