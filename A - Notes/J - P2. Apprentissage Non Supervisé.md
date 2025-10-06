Parfait 👍
On va construire un **cours complet sur le Machine Learning non supervisé**.
Je vais suivre une structure pédagogique claire :

1. **Introduction & définitions**
2. **Différences avec l’apprentissage supervisé**
3. **Principaux objectifs**
4. **Familles d’algorithmes non supervisés**

   * Clustering
   * Réduction de dimensions
   * Détection d’anomalies
   * Association Rules
5. **Détails des algorithmes les plus importants**

   * Méthodes de clustering (K-Means, DBSCAN, Hiérarchique…)
   * PCA / t-SNE / UMAP
   * Isolation Forest, One-Class SVM
   * Apriori, FP-Growth
6. **Évaluation & métriques (comment juger un modèle sans labels)**
7. **Applications réelles**
8. **Exemple pratique en Python (syntaxe de base)**
9. **Résumé & points clés**

---

# 📘 Cours : Machine Learning Non Supervisé

## 1. Introduction

L’**apprentissage non supervisé** est une branche du machine learning où l’on entraîne des modèles **sans disposer de labels** (c’est-à-dire sans variable cible à prédire).
L’objectif est de **découvrir des structures cachées** ou des **modèles sous-jacents** dans les données.

👉 Contrairement à l’apprentissage supervisé, il n’y a pas de “bonne réponse” fournie.

---

## 2. Différences avec l’apprentissage supervisé

| Critère   | Apprentissage supervisé                  | Apprentissage non supervisé                    |
| --------- | ---------------------------------------- | ---------------------------------------------- |
| Données   | Features + labels (entrée/sortie connue) | Seulement les features (entrée)                |
| But       | Prédire une sortie connue                | Découvrir des structures cachées               |
| Exemple   | Prédire le prix d’une maison             | Regrouper des clients par similarité           |
| Métriques | Accuracy, RMSE, AUC, etc.                | Indices internes (silhouette, Davies-Bouldin…) |

---

## 3. Objectifs de l’apprentissage non supervisé

* **Regrouper** des objets similaires (clustering).
* **Réduire la dimensionnalité** des données (simplification, visualisation).
* **Détecter les anomalies** ou comportements atypiques.
* **Découvrir des associations** ou règles de co-occurrence.

---

## 4. Familles d’algorithmes non supervisés

### A. Clustering

But : **regrouper les données** en clusters homogènes.

* **K-Means** (partitionnement basé sur la distance aux centroïdes).
* **Clustering hiérarchique** (arbre de regroupement).
* **DBSCAN** (densité, détection de formes complexes, robustes aux outliers).

### B. Réduction de dimensions

But : **projeter les données** dans un espace de dimension plus faible.

* **PCA (ACP)** : projection linéaire maximisant la variance.
* **t-SNE, UMAP** : méthodes non linéaires de visualisation.

### C. Détection d’anomalies

But : trouver des **points rares ou atypiques**.

* **Isolation Forest** (arbres qui isolent les anomalies).
* **One-Class SVM** (sépare la “masse” de données normales des anomalies).

### D. Règles d’association

But : **extraire des règles du type “si A alors B”** dans les données transactionnelles.

* **Apriori**
* **FP-Growth**

---

## 5. Algorithmes en détail

### 1. 🔹 K-Means

#### 📖 Principe

* Inventé par **MacQueen (1967)**.
* Objectif : choisir `k` centres, puis affecter chaque point au centre le plus proche, recalculer les centres jusqu’à convergence.
* Paramètres : `k`, nombre max d’itérations, initialisation.
* Limites : nécessite de connaître `k`, sensible aux outliers, clusters sphériques.
* Fonction objectif :

  $$
  J = \sum_{i=1}^k \sum_{x \in C_i} ||x - \mu_i||^2
  $$

  où $\mu_i$ est le centroïde du cluster $C_i$.

#### ⚙️ Paramètres principaux (`sklearn.cluster.KMeans`)

* `n_clusters` : nombre de clusters (k).
* `init` : méthode d’initialisation (`'k-means++'` recommandé, `'random'` possible).
* `n_init` : nombre de fois que K-means sera lancé (par défaut 10, choisir plus pour robustesse).
* `max_iter` : nombre maximum d’itérations (par défaut 300).
* `tol` : tolérance de convergence.
* `random_state` : graine aléatoire (pour reproductibilité).
* `algorithm` : `'lloyd'`, `'elkan'` (Elkan plus rapide sur petits datasets).

#### 💡 Cas d’utilisation

* Segmentation clients en marketing.
* Compression d’images (quantification de couleurs).
* Prétraitement pour d’autres modèles.

#### 🐍 Exemple Python

```python
from sklearn.cluster import KMeans

kmeans = KMeans(
    n_clusters=4,
    init='k-means++',
    n_init=10,
    max_iter=300,
    tol=1e-4,
    random_state=42,
    algorithm='lloyd'
)

labels = kmeans.fit_predict(X)
```

#### 📊 Métriques associées

* Inertia (valeur de la fonction coût).
* Silhouette score.

---

### 2. 🔹 DBSCAN (Density-Based Spatial Clustering of Applications with Noise)

#### 📖 Principe

* Introduit par **Ester et al., 1996**.
* Objectif : regrouper points s’ils ont suffisamment de voisins dans un rayon `eps`.
* Basé sur la densité : un cluster est une zone dense séparée par des zones moins denses.
* Paramètres : `eps`, `min_samples`.
* Avantages : pas besoin de `k`, gère les formes arbitraires.
* Limites : choix des paramètres délicat.
* Catégories de points :

  * **Core points** : ≥ `min_samples` voisins dans un rayon `eps`.
  * **Border points** : voisins de core points.
  * **Noise points** : isolés.

#### ⚙️ Paramètres (`sklearn.cluster.DBSCAN`)

* `eps` : rayon de voisinage.
* `min_samples` : nombre minimal de points pour former un cluster.
* `metric` : distance utilisée (`'euclidean'`, `'manhattan'`, etc.).
* `algorithm` : `'auto'`, `'ball_tree'`, `'kd_tree'`, `'brute'`.
* `leaf_size` : taille des feuilles (impacte vitesse).
* `n_jobs` : parallélisation.

#### 💡 Cas d’utilisation

* Détection de fraudes.
* Segmentation géospatiale.
* Clusters de formes non sphériques.

#### 🐍 Exemple Python

```python
from sklearn.cluster import DBSCAN

dbscan = DBSCAN(
    eps=0.5,
    min_samples=5,
    metric='euclidean',
    algorithm='auto',
    leaf_size=30,
    n_jobs=-1
)

labels = dbscan.fit_predict(X)
```

#### 📊 Métriques associées

* Silhouette score.
* Nombre de clusters trouvés.

---

### 3. 🔹 PCA (Principal Component Analysis)

#### 📖 Principe

* Objectif : diagonalisation de la matrice de covariance → nouvelles variables (composantes principales).
* Crée de nouvelles variables (composantes principales) qui maximisent la variance.
* Réduit la dimensionnalité tout en préservant l’information.
* Utilité : compression, visualisation 2D/3D.

#### ⚙️ Paramètres (`sklearn.decomposition.PCA`)

* `n_components` : nombre de composantes (peut être un entier, un float (variance à conserver), `'mle'`).
* `svd_solver` : méthode de décomposition (`'auto'`, `'full'`, `'arpack'`, `'randomized'`).
* `whiten` : normalisation des composantes.
* `random_state`.

#### 💡 Cas d’utilisation

* Compression d’images.
* Visualisation en 2D/3D.
* Prétraitement pour accélérer l’apprentissage supervisé.

#### 🐍 Exemple Python

```python
from sklearn.decomposition import PCA

pca = PCA(
    n_components=2,
    svd_solver='auto',
    whiten=False,
    random_state=42
)

X_reduced = pca.fit_transform(X)
```

---

### 4. 🔹 Isolation Forest

#### 📖 Principe

* Chaque donnée est isolée via un arbre de partition.
* Les anomalies sont isolées plus rapidement (profondeur plus faible).
* Utile pour : fraude, défauts industriels.

#### ⚙️ Paramètres (`sklearn.ensemble.IsolationForest`)

* `n_estimators` : nombre d’arbres.
* `max_samples` : nombre d’échantillons utilisés par arbre.
* `contamination` : proportion attendue d’anomalies.
* `max_features` : nb de features utilisées par arbre.
* `bootstrap` : échantillonnage avec ou sans remise.
* `n_jobs`, `random_state`.

#### 💡 Cas d’utilisation

* Détection de fraude bancaire.
* Maintenance prédictive.

#### 🐍 Exemple Python

```python
from sklearn.ensemble import IsolationForest

iso = IsolationForest(
    n_estimators=100,
    max_samples='auto',
    contamination=0.1,
    max_features=1.0,
    bootstrap=False,
    random_state=42,
    n_jobs=-1
)

labels = iso.fit_predict(X)
```

---

### 6. 🔹 Règles d’association (Apriori)

#### 📖 Principe

* Objectif : explorer les ensembles d’items fréquents et extraire des règles.
* Exemple : “80% des clients qui achètent du pain achètent aussi du beurre”.
* Recherche des ensembles d’items fréquents.
* Génère des règles du type :

  * Support : fréquence de l’itemset.
  * Confiance : probabilité que B apparaisse sachant A.
  * Lift : mesure d’indépendance (si >1 → corrélation positive).

#### ⚙️ Paramètres (`mlxtend.frequent_patterns.apriori`)

* `min_support` : support minimal.
* `use_colnames` : renommer les items avec colonnes originales.
* `max_len` : taille max des itemsets.

#### 💡 Cas d’utilisation

* Panier d’achat (market basket analysis).
* Recommandation de produits.

#### 🐍 Exemple Python

```python
from mlxtend.frequent_patterns import apriori, association_rules

# Extraction des itemsets fréquents
frequent_itemsets = apriori(df, min_support=0.1, use_colnames=True, max_len=None)

# Génération des règles
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.0)
```

---

### 7. 🔹 Clustering hiérarchique (Agglomerative Clustering)

#### 📖 Principe


* Construire un **dendrogramme** (arbre).
* **Agglomératif** : on fusionne les points progressivement (bottom-up).
* Choix de la métrique de lien :

  * `ward` (minimisation variance).
  * `complete` (distance max).
  * `average` (distance moyenne).

#### ⚙️ Paramètres (`sklearn.cluster.AgglomerativeClustering`)

* `n_clusters` : nombre de clusters (si fixé).
* `metric` : distance (`'euclidean'`, `'manhattan'`, etc.).
* `linkage` : `'ward'`, `'complete'`, `'average'`, `'single'`.
* `distance_threshold` : permet de couper l’arbre à une distance donnée au lieu de fixer `n_clusters`.

#### 💡 Cas d’utilisation

* Classification de documents.
* Taxonomies (bio-informatique).

#### 🐍 Exemple Python

```python
from sklearn.cluster import AgglomerativeClustering

agg = AgglomerativeClustering(
    n_clusters=3,
    affinity='euclidean',
    linkage='ward',
    distance_threshold=None
)

labels = agg.fit_predict(X)
```

---

## 6. Évaluation & métriques

Comment évaluer sans labels ?

* **Indices internes** :

  * Coefficient de silhouette (mesure de séparation des clusters).
  * Indice de Davies-Bouldin.

* **Indices externes** (si labels dispo pour évaluation seulement) :

  * ARI (Adjusted Rand Index).
  * NMI (Normalized Mutual Information).

---

## 7. Applications réelles

* Segmentation clients (marketing).
* Détection de fraudes bancaires.
* Compression et visualisation de données.
* Analyse de réseaux sociaux.
* Bio-informatique (gènes similaires).
* Systèmes de recommandation.

---

## 8. Exemple pratique en Python

```python
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

# Données
X, _ = load_iris(return_X_y=True)

# Clustering avec K-Means
kmeans = KMeans(n_clusters=3, random_state=42)
labels = kmeans.fit_predict(X)

# Réduction dimensionnelle pour visualisation
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)

# Visualisation
plt.scatter(X_reduced[:,0], X_reduced[:,1], c=labels, cmap='viridis')
plt.title("Clustering K-Means sur Iris")
plt.show()
```

---

## 9. Résumé & points clés

* L’apprentissage non supervisé explore les **structures cachées** des données.
* Principales tâches : clustering, réduction de dimension, anomalies, règles d’association.
* Algorithmes phares : **K-Means, DBSCAN, PCA, Isolation Forest, Apriori**.
* Métriques adaptées : **silhouette, Davies-Bouldin, ARI, NMI**.
* Applications variées : segmentation, fraude, biologie, recommandation.














