# 📘 Intro to Machine Learning  
---

## 🔹 Données, Data Analytics et Data Science

***“Data science is all about asking interesting questions based on the data you have – or don’t have.” — Sarah Jarvis***

### Qu’est-ce que la Data Analytics ?
- Analyse computationnelle systématique de données ou statistiques.  
- Découverte, interprétation et communication de patterns significatifs.  
- Support à la prise de décision.  
- Science d’analyser des données brutes pour en tirer des conclusions.  
- Souvent automatisée via des algorithmes et processus mécaniques.  
- Objectif : **donner du sens aux données**.

### Data Analytics vs Data Science
- **Data Science** : englobe data analytics, data mining, machine learning, etc.  
- **Data Analytics** : branche de la Data Science, se concentre sur l’extraction et l’exploitation d’insights.  
- Nécessaire pour **Machine Learning** et **Deep Learning**.  

### Data Science
- Terme « parapluie » englobant :
  - Data analytics  
  - Data mining  
  - Machine learning  
  - Deep learning  
  - Disciplines connexes  

---

## 🔹 IA, ML et DL
- **Intelligence Artificielle (IA)** : discipline large visant à reproduire l’intelligence humaine.  
- **Machine Learning (ML)** : sous-domaine de l’IA permettant aux systèmes d’apprendre à partir des données.  
- **Deep Learning (DL)** : sous-domaine du ML basé sur les réseaux de neurones profonds.

---

## 🔹 Métiers de la Data
Exemples de rôles dans le domaine :
- Data scientist  
- Data analyst  
- Data architect  
- Data mining engineer  
- Machine learning engineer  
- Deep learning engineer  
- Hadoop engineer  
- Predictive modeler  

---

## 🔹 Domaines d’application du ML
- Santé  
- Finance (fraude, trading)  
- Marketing (segmentation, analyse de sentiments)  
- Industrie  
- Transport  
- Etc.  

### Exemple en santé
- Recommandations de traitement  
- Détection précoce de maladies  

---

## 🔹 Modèles de Machine Learning
1. **Classification** : déterminer une catégorie → spam / pas spam.  
2. **Clustering** : identifier des patterns dans des données non labellisées.  
3. **Régression** : prédire une valeur continue → prix, poids, revenus.  

---

## 🔹 Types d’apprentissage en ML
- **Supervisé** : données labellisées → prédiction de résultats connus.  
- **Non supervisé** : données non labellisées → découverte de structures.  
- **Semi-supervisé** : mélange des deux.  

---

## 🔹 Apprentissage supervisé
- Données labellisées, inputs et outputs connus.  
- Objectif : apprendre une fonction **Y = f(X)**.  
- Processus itératif → correction d’erreurs jusqu’à performance acceptable.  
- Utilisé pour **classification** et **régression**.  

### Exemples
- Finance : détection de fraude  
- Marketing : analyse de sentiments  
- Santé : diagnostic médical  
- Spam detection  

### Algorithmes populaires
- Régression linéaire et logistique  
- Arbre de décision, Random Forest  
- SVM (Support Vector Machine)  
- KNN (K-Nearest Neighbours)  
- Naive Bayes  
- Réseaux de neurones  

---

## 🔹 Apprentissage non supervisé
- Données **non labellisées**.  
- Recherche de structures et relations dans les données.  

### Deux catégories principales
1. **Clustering** : regroupement par similarité.  
   - Ex. regrouper les clients par comportements d’achat.  
2. **Association** : découverte de relations entre variables.  
   - Ex. maison neuve → achat de meubles.  

### Algorithmes populaires
- K-means clustering  
- PCA (Principal Component Analysis)  
- Réseaux de neurones  
- ICA (Independent Component Analysis)  
- Clustering hiérarchique  
- SVD (Singular Value Decomposition)  

---

## 🔹 Apprentissage semi-supervisé
- Grande quantité de données X, mais peu sont labellisées Y.  
- Ex. Archives photo avec seulement quelques images étiquetées.  
- Combinaison de techniques supervisées et non supervisées.  
- Très courant en pratique car le labelling coûte cher.  

---

## 🔹 Processus de Machine Learning
Trois fonctions principales :
1. **Processus de décision** : classification ou prédiction à partir de données.  
2. **Fonction d’erreur** : mesure l’écart entre prédictions et vérité.  
3. **Optimisation du modèle** : ajustement des poids pour réduire l’erreur.  

---

## 🔹 Préparation des données
### Datasets
- Plus un dataset est grand et diversifié, plus le modèle sera robuste.  
- Nécessite **échantillonnage, nettoyage et découpage**.  

### Découpage des données
- **Training set** (70-80%) → apprentissage.  
- **Test set** (20-30%) → évaluation finale.  
- **Validation set** → choix du modèle.  

⚠️ Attention : ne jamais évaluer un modèle sur ses données d’entraînement.  

Exemple en Python :  
```python
from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(X, y, train_size=0.8)
````

---

## 🔹 Généralisation du modèle

* Capacité du modèle à bien prédire sur des **données jamais vues**.
* Objectif ultime du ML : **minimiser l’erreur sur de nouvelles données**.

---

## 🔹 Étapes d’un projet ML

1. Collecte des données brutes
2. Échantillonnage
3. Nettoyage
4. Split en train/test
5. Création du modèle
6. Entraînement
7. Évaluation et optimisation

---

```

👉 Veux-tu que je génère aussi une **version avec schémas (images/diagrammes)** pour que ça ressemble à un vrai support de cours, comme ton PDF, ou tu préfères garder uniquement le texte en Markdown ?
```
