# 🧠 Bases de Données NoSQL 

---

## 📌 Définition

**NoSQL** (Not Only SQL) désigne une famille de bases de données **non relationnelles**, conçues pour :

* Gérer des **volumes massifs de données**
* Assurer une **grande disponibilité**
* Être **scalables horizontalement** (sur plusieurs machines)
* Fonctionner avec des **structures de données flexibles** ou **semi-structurées**

🔁 Elles n'utilisent pas forcément le modèle relationnel (tables, lignes, colonnes), ni le langage SQL — même si certaines le supportent aujourd’hui.

---

## 🌍 Les bases NoSQL les plus connues

| Base         | Type                  | Description rapide                                           |
| ------------ | --------------------- | ------------------------------------------------------------ |
| 🔸 MongoDB   | Documentaire          | Stocke les données sous forme de documents JSON/BSON         |
| 🔸 Redis     | Clé-Valeur            | Stockage en mémoire, ultra-rapide, idéal pour le cache       |
| 🔸 Cassandra | Colonne               | Écriture massive, tolérance aux pannes, très scalable        |
| 🔸 Neo4j     | Graphe                | Représentation des entités et relations sous forme de graphe |
| 🔸 HBase     | Colonne               | Intégré à l’écosystème Hadoop, Big Data distribué            |
| 🔸 Couchbase | Documentaire          | Base hybride document + clé-valeur, très performante         |
| 🔸 DynamoDB  | Clé-Valeur / Document | Gérée par AWS, haute disponibilité, scalabilité automatique  |

---

## 📚 Catégories, explications & cas d’usage

### 📄 1. Bases Documentaires

**Exemples** : MongoDB, Couchbase, Amazon DocumentDB
**Format** : JSON ou BSON

📅 **Idéal pour** :

* Stockage de profils utilisateurs
* Applications web (données semi-structurées)
* Catalogues de produits

📌 **Avantage** : structure flexible, modifiable à la volée.

#### 🔧 Exemple MongoDB

```json
{
  "_id": 1,
  "nom": "Alice",
  "email": "alice@mail.com",
  "commandes": [
    {"produit": "PC", "prix": 1200},
    {"produit": "Souris", "prix": 20}
  ]
}
```

**Requête :**

```js
# Insertion
db.clients.insertOne({ nom: "Alice", age: 30 })

# Recherche
db.clients.find({ age: { $gt: 25 } })

# Mise à jour
db.clients.updateOne({ nom: "Alice" }, { $set: { age: 31 } })

# Suppression
db.clients.deleteOne({ nom: "Alice" })

```

---

### 🔑 2. Bases Clé-Valeur

**Exemples** : Redis, DynamoDB, Riak
**Format** : `clé (string) → valeur (n’importe quoi)`

📅 **Idéal pour** :

* Caches en mémoire
* Sessions utilisateurs
* Jeux en ligne (scoreboard)

📌 **Avantage** : très rapide (O(1)), simple, efficace pour données temporaires.

#### 🔧 Exemple Redis

```bash
SET utilisateur:1 "Alice"
GET utilisateur:1
DEL user:1
```

Ultra-rapide car en mémoire. Utilisé pour du caching, file d’attente, score en temps réel, etc.
---

### 🧱 3. Bases en Colonnes

**Exemples** : Apache Cassandra, HBase, ScyllaDB
**Format** : Colonnes dynamiques regroupées par familles

📅 **Idéal pour** :

* Données analytiques distribuées
* Historique d'événements (logs, capteurs)
* Tableaux de bord

📌 **Avantage** : parfaite pour l’écriture massive et l’analyse distribuée.

#### Cassandra (colonne)

* Développée chez Facebook

* Basée sur BigTable (Google) + Dynamo (Amazon)

* Haute disponibilité, hautement scalable, écritures massives

**Modèle** 

* Keyspace = base

* ColumnFamily = table

* Colonnes = tuples nom/valeur

* SuperColonnes = map de colonne 

*Exemple Cassandra (CQL)*

```sql
CREATE TABLE capteurs (
  id TEXT,
  date TIMESTAMP,
  temperature FLOAT,
  PRIMARY KEY (id, date)
);

INSERT INTO capteurs (id, date, temperature)
VALUES ('capteur_1', toTimestamp(now()), 22.5);
```

---

### 🔗 4. Bases Graphe

**Exemples** : Neo4j, ArangoDB, JanusGraph

**Modèle** 

* Nœuds : entités (ex : Personne)

* Arêtes : relations (ex : AMIS_AVEC)

📅 **Idéal pour** :

* Réseaux sociaux
* Moteurs de recommandation
* Systèmes de détection de fraude

📌 **Avantage** : navigation fluide entre entités très reliées.

#### 🔧 Exemple Neo4j (Cypher)

```cypher
CREATE (a:Person {nom: "Alice"})-[:AMIS_AVEC]->(b:Person {nom: "Bob"})

MATCH (a:Person)-[:AMIS_AVEC]->(b:Person)
WHERE a.nom = "Alice"
RETURN b.nom
```

---

## 🧪 Comment manipuler ces bases ?

| Base      | Client CLI    | Langage de requête    | Interfaces disponibles                       |
| --------- | ------------- | --------------------- | -------------------------------------------- |
| MongoDB   | `mongo`       | Mongo Shell (JS-like) | Compass, Python (PyMongo), Node.js           |
| Redis     | `redis-cli`   | Commandes clé-valeur  | RedisInsight, Python (`redis-py`)            |
| Cassandra | `cqlsh`       | CQL (SQL-like)        | DataStax Studio, Python (`cassandra-driver`) |
| Neo4j     | `neo4j-shell` | Cypher                | Neo4j Browser, Python (`neo4j`)              |

---

## Comparaison avec SQL

| Critère      | SQL                         | NoSQL                      |
| ------------ | --------------------------- | -------------------------- |
| Schéma       | Fixe                        | Flexible ou inexistant     |
| Langage      | SQL                         | Spécifique à chaque moteur |
| Jointures    | Oui                         | Non (ou très limitées)     |
| Transactions | ACID                        | BASE (souvent)             |
| Scalabilité  | Verticale                   | Horizontale                |
| Performance  | Excellente en mono-instance | Excellente en distribué    |

---

### Intérêts & Limites

**✅ Avantages NoSQL**

* Très performant sur de gros volumes

* Hautement disponible

* Schema-less : facile à adapter

* Open source souvent

* Idéal pour le temps réel, le Big Data, le Cloud

**❌ Inconvénients**

* Moins de standardisation

* Pas ou peu de transactions complexes

* Pas de jointures faciles

* Moins d’outils pour monitoring / debugging

* Courbe d’apprentissage selon le moteur

---

## ⚙️ Cas concrets d’utilisation

| Domaine                | Besoin                                 | Base NoSQL idéale |
| ---------------------- | -------------------------------------- | ----------------- |
| E-commerce             | Produits, clients, commandes flexibles | MongoDB           |
| Jeu vidéo              | Sessions et scores temporaires         | Redis             |
| Réseau social          | Relations complexes entre utilisateurs | Neo4j             |
| Capteurs / IoT         | Historique horodaté de mesures         | Cassandra         |
| Cloud à grande échelle | Performance & scalabilité automatique  | DynamoDB          |

---

## Conclusion

*Les bases de données NoSQL représentent une réponse moderne et puissante aux défis du Big Data, du cloud computing et des applications à forte variabilité. Leur flexibilité, leur capacité à évoluer horizontalement et leur performance en font des outils indispensables dans l’arsenal du data engineer ou du développeur. Bien qu’elles ne remplacent pas les bases relationnelles, elles les complètent, et le choix entre SQL et NoSQL doit toujours se faire en fonction des besoins métier, du type de données et des contraintes de scalabilité.*