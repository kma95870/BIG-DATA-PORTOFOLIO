# 📂 Leçon complète : Bases de données relationnelles (BDR)

---

## 🔖 1. Introduction

Une **base de données relationnelle (BDR)** est un système de stockage organisé de données en **tables**. Elle repose sur le **modèle relationnel** introduit par Edgar F. Codd. Les données sont stockées sous forme de lignes et de colonnes, avec des relations logiques entre les tables.

---

## 📊 2. Structure d'une base relationnelle

### Concepts fondamentaux

* **Relation** : tableau à deux dimensions (table)

* **Attributs** : colonnes d'une relation

* **Domaine** : ensemble de valeurs autorisées pour un attribut

* **N-uplets (tuples)** : lignes d'une relation


### Table

Une table est une structure tabulaire composée de :
* **colonnes** (attributs) : définissent le type de données (nom, date, nombre…)
* **lignes** (enregistrements) : chaque ligne représente une entité ou une observation

Chaque table représente une entité (Client, Produit, Commande...)

### Clés

* **Clé primaire** : identifie de façon unique chaque ligne (ex : id)
* **Clé étrangère** : référence la clé primaire d'une autre table pour créer des relations
* **Clé candidate** : ensemble minimal d’attributs identifiant un tuple

### Types de relations

Les bases relationnelles permettent de modéliser des **relations entre entités** grâce aux clés étrangères.

| Type de relation | Exemple                                                 |
| ---------------- | ------------------------------------------------------- |
| 1 à 1            | Un utilisateur ↔ un seul profil                         |
| 1 à N            | Un client → plusieurs commandes                         |
| N à N            | Un étudiant ↔ plusieurs cours (via table intermédiaire) |

---

#### Schéma relationnel visuel

Un modèle de gestion de commandes :

* `Clients(id_client, nom)`
* `Produits(id_produit, nom)`
* `Commandes(id_commande, id_client, date)`
* `Commandes_Produits(id_commande, id_produit, quantite)`

Représentation :

```
Clients ──└─→ Commandes ──└─→ Commandes_Produits ←┘── Produits
```

---

### Contraintes d’intégrité

* **Contrainte de domaine** : type, valeurs valides

* **Contrainte d’entité** : chaque relation a une clé primaire non nulle

* **Contrainte référentielle** : valeur de clé étrangère doit exister ailleurs

* **Contrainte déclarative** : NOT NULL, DEFAULT, UNIQUE, etc.

## 🏠 3. CRUD : Créer, Lire, Modifier, Supprimer

Le modèle **CRUD** correspond aux 4 opérations de base sur les données :

| Action | Nom    | Description         |
| ------ | ------ | ------------------- |
| C      | Create | Ajouter une ligne   |
| R      | Read   | Lire des données    |
| U      | Update | Modifier une ligne  |
| D      | Delete | Supprimer une ligne |

---

## 🔮 4. Vues (Views)

### Vue

Une **vue** est une **table virtuelle** issue d'une requête SQL. Elle ne stocke pas les données mais présente un résultat dynamique.

### Avantages

* Simplifie les requêtes complexes
* Restreint l'accès à certaines colonnes
* Pratique pour les outils de BI

### Vue matérialisée

* Copie physique d'une vue
* Plus rapide à lire, mais à rafraîchir manuellement

### Utilisation des vues

* Sécurité : masquer certaines colonnes

* Simplicité : enregistrer des requêtes complexes

* Mise à jour possible si certaines conditions sont remplies

---

## 🔄 5. Transactions et propriétés ACID

Une **transaction** est un groupe d'opérations SQL qui doivent s'exécuter ensemble.

### ACID

ACID = propriétés essentielles pour garantir la fiabilité des transactions :

| Propriété      | Définition                                         | Exemple concret                                              |
| -------------- | -------------------------------------------------- | ------------------------------------------------------------ |
| A - Atomicité  | Tout ou rien                                       | Virement bancaire = retrait + ajout doivent réussir ensemble |
| C - Cohérence  | Les règles d'intégrité sont respectées             | Impossible d'insérer une commande sans client                |
| I - Isolation  | Les transactions ne se perturbent pas entre elles  | Deux achats simultanés : un seul produit disponible          |
| D - Durabilité | Les données sont sauvegardées même en cas de crash | Une commande validée n'est jamais perdue                     |

#### ⚙️ Propriété ACID d'une base de données relationnelle

---

 * 🅰️ A — Atomicité  
🔹 **"Tout ou rien"**

*📌 Exemple :*
**Scénario** : Virement bancaire de 100 € de ton compte vers celui d’un ami.

- Étape 1 : Retirer 100 € de ton compte  
- Étape 2 : Ajouter 100 € à celui de ton ami

✅ Si les deux étapes réussissent → la transaction est validée  
❌ Si une des deux échoue (ex : serveur tombe après le retrait) → tout est annulé → ton compte n’est **pas débité**

🧠 Ce que ça empêche :
- Incohérence (tu perds de l’argent sans que l’autre ne le reçoive)  
- Opérations à moitié faites

---

* 🅲 C — Cohérence  
🔹 **"La base reste dans un état valide selon les règles définies"**

*📌 Exemple :*
**Règle métier** : chaque commande doit être liée à un client existant.  
Tu essaies d’insérer une commande avec un `id_client` qui n’existe pas.

❌ Si la base accepte cette commande → elle devient incohérente (violation d’intégrité)  
✅ Grâce à la cohérence, la **contrainte de clé étrangère** bloque l’insertion → la base reste **fiable**

🧠 Ce que ça garantit :
- Les règles métier sont toujours respectées  
- Pas de données “orphelines” ou illogiques

---

* 🅸 I — Isolation  
🔹 **"Les transactions ne doivent pas interférer entre elles"**

*📌 Exemple :*
Deux utilisateurs passent une commande en même temps, et il ne reste qu’un seul produit en stock.

- Utilisateur A vérifie le stock → OK  
- Utilisateur B fait la même chose → aussi OK  
- Les deux essaient d’acheter → **conflit**

✅ Grâce à l’isolation :
- Une seule transaction est traitée à la fois  
- L’autre attend ou échoue selon le système

🧠 Ce que ça empêche :
- Lectures ou écritures basées sur des données non validées  
- Anomalies : *lectures fantômes*, *données sales (dirty reads)*

---

* 🅳 D — Durabilité  
🔹 **"Une fois validée, la transaction est conservée à jamais, même en cas de crash"**

*📌 Exemple :*
Tu passes une commande en ligne. Tu reçois la confirmation.  
🔌 Ensuite, le serveur plante.

✅ Grâce à la durabilité :
- Les données sont **sauvegardées dans le journal (log)**  
- Même après redémarrage, la commande est retrouvée et enregistrée

🧠 Ce que ça garantit :
- **Pas de perte d’information**  
- L’engagement du système est **fiable dans le temps**

---

### Mécanismes garantissant ACID

* WAL / redo logs / undo logs

* Verrous (Locks), MVCC (PostgreSQL)

* Validation (COMMIT) / Annulation (ROLLBACK)

## 🔢 6. Les Formes Normales (FN)

### Définition

Les **formes normales** sont des règles pour structurer les tables afin de :

* ✅ Réduire la redondance
* ✅ Éviter les anomalies (mise à jour, suppression)
* ✅ Améliorer la cohérence

### 1NF - Valeurs atomiques

Chaque cellule contient une seule valeur (pas de liste ou répétition)

*❌ Mauvais exemple :*
| id\_client | nom   | produits\_achetés |
| ---------- | ----- | ----------------- |
| 1          | Alice | Clavier, Souris   |

*✅ En 1NF :*
| id\_client | nom   | produit\_acheté |
| ---------- | ----- | --------------- |
| 1          | Alice | Clavier         |
| 1          | Alice | Souris          |


### 2NF - Dépendance entière de la clé

Aucune colonne ne doit dépendre que d'une partie de la clé primaire (dans le cas de clés composées)

*❌ Mauvais exemple (clé composée + dépendance partielle) :*
| id\_commande | id\_produit | nom\_client |
| ------------ | ----------- | ----------- |
➡️ nom_client ne dépend que de id_commande, pas de la combinaison.

*✅ En 2NF :*
* Une table Commandes avec id_commande, nom_client
* Une table Commandes_Produits avec id_commande, id_produit

### 3NF - Pas de dépendance transitive

Une colonne ne doit pas dépendre d'une autre colonne non-clé

*❌ Mauvais exemple :*
| id\_client | nom | code\_postal | ville |
| ---------- | --- | ------------ | ----- |
➡️ ville dépend de code_postal, pas de la clé id_client

*✅ En 3NF :*
* Table Clients : id_client, nom, code_postal
* Table Code_Postal : code_postal, ville

---

## 🚀 7. Moteurs de bases relationnelles (SGBDR)

| Moteur         | Caractéristiques principales                        |
| -------------- | --------------------------------------------------- |
| PostgreSQL     | Solide, ACID, types avancés, MVCC                   |
| MySQL (InnoDB) | Populaire, open source, supporte ACID depuis InnoDB |
| MariaDB        | Fork de MySQL, 100% libre                           |
| SQLite         | Ultra-léger, pas besoin de serveur                  |
| Oracle DB      | Très robuste, utilisé en entreprise                 |
| SQL Server     | Version Microsoft, très intégrée                    |
| BigQuery       | Cloud, très rapide, orienté analyse                 |
| Amazon RDS     | Service de base managé dans AWS                     |

---
## ⚙️ 8. Langage SQL et ses composants

Le langage **SQL (Structured Query Language)** est le langage standard pour interagir avec une base relationnelle. Il se divise en trois grandes catégories de commandes :

🏗️ **DDL (Data Definition Language)* — Définition des structures

Permet de créer, modifier ou supprimer des objets de la base comme les tables, vues, index ou utilisateurs.

`CREATE` : créer une table, une vue, un index...

`ALTER` : modifier la structure d’un objet

`DROP`: supprimer un objet

*Exemple :* création d’une table "Produit" avec une clé primaire et des contraintes de type.

🧱 **DML (Data Manipulation Language)* — Manipulation des données

Permet de manipuler les lignes (tuples) dans les tables.

`INSERT` : insérer une ligne

`UPDATE` : modifier une ou plusieurs lignes

`DELETE` : supprimer une ou plusieurs lignes

`SELECT` : lire ou interroger les données (requêtes)

SELECT peut être combiné avec :

`WHERE` : filtrer les résultats

`GROUP BY` / `HAVING` : regrouper et filtrer les agrégats

`ORDER BY` : trier les résultats

🔐 **DCL (Data Control Language)* — Sécurité et contrôle d’accès

Permet de gérer les droits d’accès et le comportement des transactions.

`GRANT` / `REVOKE` : accorder ou retirer des privilèges d'accès

`COMMIT` / `ROLLBACK` : valider ou annuler une transaction

🧠 Remarque importante

Les instructions SQL sont souvent automatiquement validées (autocommit) sauf si une transaction explicite est commencée.

### Opérations de l’algèbre relationnelle

L'algèbre relationnelle est le fondement théorique du SQL. Elle définit les opérations de manipulation des relations (tables) en tant qu'ensembles mathématiques.

🔍 Opérations principales

1. Sélection (σ)

Filtre les lignes selon un critère (ex : tous les clients de Paris)

2. Projection (π)

Extrait certaines colonnes d’une table (ex : nom et prénom seulement)

3. Jointure (⨝)

Combine deux relations en fonction d’un lien logique (clé étrangère)

Types : jointure interne, naturelle, externe (gauche/droite)

4. Division

Utilisée pour des requêtes comme : "trouver les clients qui ont commandé tous les produits"

Rare mais puissante, elle permet d’identifier des relations couvrant un ensemble complet d'autres relations

📌 Autres opérations

Union, Différence, Intersection, Produit cartésien

🧠 Pourquoi c’est utile ?

Comprendre l’algèbre relationnelle permet de mieux :

Optimiser ses requêtes

Comprendre ce que fait le SGBD sous le capot

Anticiper les résultats d’une requête SQL complexe

### Concepts avancés

**🔥 Triggers (Déclencheurs)**

Mécanismes automatiques exécutés lorsqu’un événement se produit sur une table (INSERT, UPDATE, DELETE)

Très utiles pour :

Mettre à jour des champs dérivés automatiquement

Empêcher certaines actions non valides

Maintenir des contraintes complexes

*Exemple :* Si on insère une ligne dans "Commandes", créer automatiquement une notification ou journaliser l’action

🧾 Procédures stockées (Stored Procedures)

Blocs de code SQL enregistrés dans la base, exécutables à la demande

Utilisent des variables, conditions, boucles…

Évitent de dupliquer de la logique côté application

*Exemple :* une procédure qui insère une commande et calcule automatiquement le total

**🔒 Gestion de la concurrence** 

Dans un environnement multi-utilisateurs, plusieurs transactions peuvent modifier les mêmes données simultanément.

🔧 Solutions utilisées par le SGBD

Verrouillage (Locks) : empêche les conflits

MVCC (Multiversion Concurrency Control) : chaque transaction voit une version stable des données

Granularité : on peut verrouiller une ligne, une table, ou même une page mémoire

Détection de deadlock : le système annule l’une des transactions si un blocage circulaire est détecté

*Exemple concret :*

Deux agents essaient de réserver la même place à la même seconde. Le SGBD :

1. Attribue un verrou à l’un

2. Met l’autre en attente

3. Valide ou annule selon l’ordre d’arrivée

***Comprendre ces mécanismes permet d’éviter des bugs comme la perte de mise à jour ou les lectures fantômes.***

## 📝 9. Conclusion

Les bases relationnelles sont la fondation de nombreuses applications. Comprendre les **structures (tables, clés)**, les **contraintes**, les **transactions ACID**, les **formes normales** et les **vues** permet de construire des systèmes robustes, cohérents et performants.

### Cas d’usage :

* Applications web (back-end)

* Systèmes de gestion clients (CRM)

* Applications de comptabilité

* ERP (Enterprise Resource Planning)

* Analyse de données via requêtes SQL


