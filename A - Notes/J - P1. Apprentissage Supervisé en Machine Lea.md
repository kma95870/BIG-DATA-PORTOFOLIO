#  Apprentissage Supervisé en Machine Learning

---

## 🔹 1. Introduction

Le **Machine Learning supervisé** est une méthode où l’on entraîne un modèle à partir de **données étiquetées** :

* **X** : variables explicatives (features)
* **y** : variable cible (label)

Objectif → apprendre une fonction $f : X \to y$ capable de **généraliser** sur de nouvelles données.

### Types de problèmes

* **Classification** → prédire une **catégorie** (spam / non spam).
* **Régression** → prédire une **valeur continue** (prix d’une maison).

---

## 🔹 2. Pipeline d’un projet supervisé

1. **Préparation des données** (nettoyage, encodage, normalisation).
2. **Split Train/Test** (souvent 70/30).
3. **Choix du modèle** (logistique, arbre, RF, etc.).
4. **Entraînement (`fit`)** → souvent via **descente de gradient**.
5. **Évaluation** (métriques adaptées).
6. **Optimisation** (hyperparamètres, régularisation).
7. **Déploiement** (API, dashboard, batch).

---

## 🔹 3. Métriques d’évaluation

* Le but d’un modèle n’est **pas seulement d’apprendre les données d’entraînement**, mais de **généraliser**.
* Pour mesurer cette capacité, on compare :

  * Les **prédictions** du modèle ($\hat{y}$)
  * Aux **valeurs réelles** ($y$)

👉 Les métriques servent donc à **quantifier la qualité** des prédictions.

### 📊 Classification

### Matrice de Confusion

La **base de toutes les métriques de classification**.

| Réalité ↓ / Prédiction → | Positif (1)       | Négatif (0)       |
| ------------------------ | ----------------- | ----------------- |
| **Positif (1)**          | TP (Vrai Positif) | FN (Faux Négatif) |
| **Négatif (0)**          | FP (Faux Positif) | TN (Vrai Négatif) |

* **TP** : le modèle prédit 1 et c’est bien 1.
* **TN** : le modèle prédit 0 et c’est bien 0.
* **FP** : le modèle prédit 1 alors que c’était 0 (**fausse alerte**).
* **FN** : le modèle prédit 0 alors que c’était 1 (**raté**).

---

### Accuracy (Exactitude) : proportion correcte

**Formule :**

$$
Accuracy = \frac{TP + TN}{TP + TN + FP + FN}
$$

**Exemple :**

* Sur 100 mails, le modèle en classe 90 correctement → Accuracy = 90%.

**Cas d’utilisation :**

* OK si les classes sont **équilibrées**.
* Mauvais si les classes sont **déséquilibrées** (ex : 99% non-fraude → accuracy de 99% même si aucune fraude détectée).

---

### Précision : parmi les positifs prédits, combien sont vrais.

**Formule :**

$$
Précision = \frac{TP}{TP + FP}
$$

**Exemple :**

* Le modèle prédit 20 spams, dont 15 corrects → précision = 15/20 = **0.75**.

**Cas d’utilisation :**

* Quand **le coût d’un faux positif est élevé**.
  Ex : filtrage d’emails (ne pas marquer un email important comme spam).

---

### Rappel (Recall ou Sensibilité) : parmi les vrais positifs, combien détectés.

**Formule :**

$$
Recall = \frac{TP}{TP + FN}
$$

**Exemple :**

* Sur 30 vrais spams, le modèle en détecte 25 → recall = 25/30 = **0.83**.

**Cas d’utilisation :**

* Quand **le coût d’un faux négatif est élevé**.
  Ex : détection de cancer (mieux vaut alerter trop que de rater un vrai malade).

---

### F1-score : compromis Précision/Recall.

**Formule :**

$$
F1 = 2 \cdot \frac{Précision \cdot Recall}{Précision + Recall}
$$

**Exemple :**

* Précision = 0.75, Recall = 0.83

$$
F1 = 2 \cdot \frac{0.75 \cdot 0.83}{0.75 + 0.83} \approx 0.79
$$

**Cas d’utilisation :**

* Quand il faut un **équilibre entre précision et rappel**.
* Exemple : détection de fraude (éviter de rater une fraude mais sans trop d’alertes inutiles).

---

### AUC-ROC (Area Under the Curve – Receiver Operating Characteristic) : performance globale, indépendamment du seuil.

* La courbe ROC trace :

  * Axe X : Taux de Faux Positifs (FPR) = $\frac{FP}{FP+TN}$
  * Axe Y : Taux de Vrais Positifs (TPR = Recall)

* L’**AUC** est l’aire sous la courbe :

  * **1.0 = parfait**
  * **0.5 = aléatoire**

**Cas d’utilisation :**

* Pour comparer des modèles indépendamment d’un seuil de décision.
* Très utilisé en **finance** et **médical**.

---

### Balanced Accuracy : moyenne des recalls, utile en déséquilibre de classes.

**Formule :**

$$
Balanced\ Accuracy = \frac{Recall_{classe\ 1} + Recall_{classe\ 0}}{2}
$$

**Cas d’utilisation :**

* Quand les classes sont **très déséquilibrées**.

---

### 📈 Régression

#### Erreur Quadratique Moyenne (MSE)

**Formule :**

$$
MSE = \frac{1}{n}\sum_{i=1}^n (y_i - \hat{y}_i)^2
$$

* Amplifie les grandes erreurs (car au carré).

**Exemple :**

* Vrai prix : \[100, 200], Prédit : \[110, 220]

$$
MSE = \frac{(100-110)^2 + (200-220)^2}{2} = \frac{100 + 400}{2} = 250
$$

**Cas d’utilisation :**

* Quand les grosses erreurs doivent être fortement pénalisées.

---

#### RMSE (Root Mean Squared Error)

**Formule :**

$$
RMSE = \sqrt{MSE}
$$

* Même unité que la variable cible.
* Plus interprétable que le MSE.

**Exemple (suite) :**

$$
RMSE = \sqrt{250} \approx 15.8
$$

---

#### MAE (Mean Absolute Error) : erreur absolue moyenne (robuste aux outliers).

**Formule :**

$$
MAE = \frac{1}{n}\sum_{i=1}^n |y_i - \hat{y}_i|
$$

**Exemple :**

* Vrai prix : \[100, 200], Prédit : \[110, 220]

$$
MAE = \frac{|100-110| + |200-220|}{2} = \frac{10 + 20}{2} = 15
$$

**Cas d’utilisation :**

* Plus robuste aux valeurs aberrantes (outliers) que le MSE/RMSE.

---

#### R² (Coefficient de Détermination) : proportion de variance expliquée.

**Formule :**

$$
R^2 = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}
$$

* Varie entre :

  * **1** : prédiction parfaite
  * **0** : modèle aussi mauvais que la moyenne
  * **< 0** : pire que prédire la moyenne !

**Cas d’utilisation :**

* Mesure la proportion de variance expliquée par le modèle.

---

## 🔹 4. Cas d’usage et choix des métriques

* **Détection de fraude** :

  * ⚠️ Peu de fraudes → classes déséquilibrées
  * → Utiliser **Recall, F1, AUC-ROC**

* **Filtrage de spam** :

  * ⚠️ Ne pas bloquer de vrais emails → faux positifs coûteux
  * → Utiliser **Précision, F1**

* **Prédiction de prix immobilier** :

  * ⚠️ Valeurs aberrantes (maisons de luxe)
  * → Utiliser **MAE** si robustesse souhaitée, sinon **RMSE**

* **Santé (cancer, maladies)** :

  * ⚠️ Rater un malade est grave
  * → Utiliser **Recall**, puis ajuster avec **F1**

---

✅ **Conclusion :**
Les métriques ne sont pas universelles → **elles dépendent du contexte métier**.
Il est souvent utile de **combiner plusieurs métriques** pour bien juger un modèle.

---

## 🔹 4. Descente de Gradient

La **descente de gradient** est la méthode d’optimisation la plus utilisée.

### Étapes :

1. Définir une **fonction de coût** (ex. MSE, log-loss).
2. Calculer le **gradient** (dérivée de la loss par rapport aux poids).
3. Mettre à jour les poids :

   $$
   \theta \leftarrow \theta - \eta \cdot \nabla J(\theta)
   $$

   * $\eta$ = learning rate.

### Variantes :

* **Batch GD** : tout le dataset.
* **Stochastic GD (SGD)** : un échantillon à la fois.
* **Mini-batch GD** : compromis.

### Où est-elle utilisée ?

* Implémentée automatiquement dans :

  * Régression logistique (`solver="saga"`, `lbfgs`…)
  * SVM (solveurs internes)
  * Gradient Boosting (le "gradient" vient de là !)
  * Réseaux de neurones (`solver="sgd"`, `adam`)

⚠️ Pas utilisée dans kNN, Arbres de décision, Random Forest.

---

## 🔹 5. Algorithmes Supervisés

### 📌 Régression Linéaire

* **Principe** : relation linéaire entre X et y.
* **Formule** : $y = \beta_0 + \beta_1 x_1 + … + \epsilon$.
* **Paramètres** : `fit_intercept`, `positive`, `n_jobs`.
* **Métriques** : MSE, RMSE, R².
* **Cas d’usage** : prévision de prix.

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression(
    fit_intercept=True, #ajoute une constante. Si False, l’équation passe par l’origine.
    copy_X=True, #copie X avant fit (utile pour ne pas modifier les données).
    n_jobs=None, #parallélisation (None → 1 cœur, -1 → tous les cœurs).
    positive=False #force les coefficients à être positifs (utile en économie ou physique).
)
```

---

### 📌 Régression Logistique

* **Principe** : classification binaire via sigmoïde.
* **Formule** :

  $$
  P(y=1|X) = \frac{1}{1 + e^{-(\beta_0 + \beta X)}}
  $$
* **Paramètres** : `penalty`, `C`, `solver`, `max_iter`.
* **Métriques** : Accuracy, Précision, Recall, F1, AUC.
* **Cas d’usage** : détection fraude, diagnostic médical.

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(
    penalty='l2', #régularisation : "l1", "l2", "elasticnet", "none".
    dual=False, #formulation duale (rare, utile si nb_features > nb_samples).
    tol=1e-4, #tolérance d’arrêt pour l’optimisation.
    C=1.0, #inverse de la régularisation (petit C = forte régularisation).
    fit_intercept=True, #ajoute le biais.
    intercept_scaling=1, #utile avec solver "liblinear".
    class_weight=None, #pondération des classes (utile si déséquilibrées).
    random_state=None, #reproductibilité.
    solver='lbfgs', #algorithme : "newton-cg", "lbfgs", "liblinear", "sag", "saga".
    max_iter=100, #itérations max.
    multi_class='auto', #"auto", "ovr" (un contre tous), "multinomial".
    verbose=0, #niveau de logs.
    warm_start=False, #garde les coefficients d’un précédent fit.
    n_jobs=None, #parallélisation (seulement pour liblinear).
    l1_ratio=None #uniquement si penalty="elasticnet".
)
```

---

### 📌 k-Nearest Neighbors (kNN)

* **Principe** : un point est classé selon les k plus proches voisins.
* **Paramètres** : `n_neighbors`, `weights`, `p`, `metric`.
* **Métriques** : Accuracy, F1 (classif), MAE (régr.).
* **Cas d’usage** : reconnaissance de formes, recommandation.

```python
from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(
    n_neighbors=5, #nombre de voisins k.
    weights='uniform', #"uniform" (égaux) ou "distance" (pondérés).
    algorithm='auto', #"auto", "ball_tree", "kd_tree", "brute".
    leaf_size=30, #taille des feuilles (optimisation KDTree/BallTree).
    p=2, #puissance → p=1 (Manhattan), p=2 (Euclidean).
    metric='minkowski', #distance → "minkowski", "manhattan", "euclidean", etc.
    metric_params=None, #paramètres supplémentaires pour metric custom.
    n_jobs=None #parallélisation.
)
```


---

### 📌 Arbres de Décision

* **Principe** : règles successives (if/else) via entropie ou Gini.
* **Paramètres** : `criterion`, `max_depth`, `min_samples_split`.
* **Métriques** : Accuracy, F1, MSE.
* **Cas d’usage** : segmentation clients, scoring risque.

```python
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(
    criterion='gini', # mesure d’impureté ("gini", "entropy", "log_loss").
    splitter='best', # "best" ou "random".
    max_depth=None, # profondeur max.
    min_samples_split=2, # nb min pour split.
    min_samples_leaf=1, # nb min dans une feuille.
    min_weight_fraction_leaf=0.0, # proportion min du poids total.
    max_features=None, # nb max de features à tester par split.
    random_state=None, 
    max_leaf_nodes=None, # limite du nb de feuilles.
    min_impurity_decrease=0.0, # seuil d’impureté pour split.
    class_weight=None, # "balanced" ou dict.
    ccp_alpha=0.0 # élagage via complexité.
)
```

---

### 📌 Random Forest

* **Principe** : ensemble de plusieurs arbres → vote/moyenne.
* **Paramètres** : `n_estimators`, `max_features`, `bootstrap`, `oob_score`.
* **Métriques** : Accuracy, F1, MSE, R².
* **Cas d’usage** : baseline robuste sur données tabulaires.

```python
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(
    n_estimators=100, # nb d’arbres.
    criterion='gini', # critère d’impureté.
    max_depth=None, # comme arbre.
    min_samples_split=2, # comme arbre.
    min_samples_leaf=1, # comme arbre.
    min_weight_fraction_leaf=0.0, 
    max_features='sqrt', 
    max_leaf_nodes=None, 
    min_impurity_decrease=0.0, 
    bootstrap=True, # échantillonnage avec remise.
    oob_score=False, # calcule score out-of-bag.
    n_jobs=None, 
    random_state=None, 
    verbose=0, 
    warm_start=False, # ajoute des arbres sans réentraîner tout.
    class_weight=None, # pondération des classes.
    ccp_alpha=0.0, # élagage.
    max_samples=None # nb d’échantillons tirés si bootstrap=True.
)
```
---

### 📌 Gradient Boosting

* **Principe** : arbres séquentiels corrigeant les erreurs des précédents.
* **Paramètres** : `loss`, `learning_rate`, `n_estimators`, `subsample`.
* **Métriques** : AUC (classif), RMSE (régr.).
* **Cas d’usage** : Kaggle, données structurées complexes.

```python
from sklearn.ensemble import GradientBoostingClassifier

model = GradientBoostingClassifier(
    loss='log_loss', #fonction de perte → "log_loss", "exponential".
    learning_rate=0.1, #vitesse d’apprentissage (plus petit → plus lent mais plus précis).
    n_estimators=100, #nb d’arbres.
    subsample=1.0, #fraction d’échantillons utilisés à chaque itération.
    criterion='friedman_mse', #mesure d’impureté.
    min_samples_split=2, 
    min_samples_leaf=1, 
    min_weight_fraction_leaf=0.0, 
    max_depth=3, 
    min_impurity_decrease=0.0, 
    init=None, #modèle initial.
    random_state=None, 
    max_features=None, 
    verbose=0, 
    max_leaf_nodes=None, 
    warm_start=False, 
    validation_fraction=0.1, #proportion utilisée pour early stopping.
    n_iter_no_change=None, #early stopping si pas d’amélioration
    tol=1e-4, 
    ccp_alpha=0.0 
)
```

---

### 📌 Support Vector Machines (SVM)

* **Principe** : séparer les classes par un hyperplan à marge max.
* **Paramètres** : `C`, `kernel`, `gamma`, `degree`.
* **Métriques** : Accuracy, F1, AUC.
* **Cas d’usage** : bioinformatique, reconnaissance faciale.

```python
from sklearn.svm import SVC

model = SVC(
    C=1.0, # régularisation (petit C → marge plus large).
    kernel='rbf', # "linear", "poly", "rbf", "sigmoid".
    degree=3, # degré polynôme (si poly).
    gamma='scale', # "scale", "auto", float.
    coef0=0.0, # paramètre indépendant (poly/sigmoid).
    shrinking=True, # heuristique pour accélérer.
    probability=False, # calcule des probabilités (lent).
    tol=1e-3, #
    cache_size=200, # mémoire cache (MB).
    class_weight=None, # pondération.
    verbose=False, #
    max_iter=-1, # -1 = infini.
    decision_function_shape='ovr', #
    break_ties=False, # "ovr" ou "ovo".
    random_state=None # gestion d’égalité.
)
```

---

### 📌 Réseaux de Neurones (MLP)

* **Principe** : couches de neurones reliés par des poids, entraînés via backpropagation + gradient descent.
* **Paramètres** : `hidden_layer_sizes`, `activation`, `solver`, `alpha`, `learning_rate`.
* **Métriques** : Accuracy, F1 (classif), MSE, R² (régr.).
* **Cas d’usage** : données non linéaires, vision, NLP.

---

## 🔹 6. Hyperparamètres – Fiche Synthèse

| Algorithme            | Paramètres clés                                       | Impact                                            |
| --------------------- | ----------------------------------------------------- | ------------------------------------------------- |
| Régression Linéaire   | `fit_intercept`, `positive`                           | Ajuste le biais, contrainte de signe              |
| Régression Logistique | `penalty`, `C`, `solver`, `max_iter`                  | Régularisation, optimisation                      |
| kNN                   | `n_neighbors`, `weights`, `p`                         | Nb de voisins, pondération, distance              |
| Décision Tree         | `criterion`, `max_depth`, `min_samples_split`         | Qualité split, profondeur, taille                 |
| Random Forest         | `n_estimators`, `max_features`, `bootstrap`           | Nb arbres, diversité, échantillonnage             |
| Gradient Boosting     | `learning_rate`, `n_estimators`, `subsample`          | Vitesse, nb d’arbres, sous-échantillonnage        |
| SVM                   | `C`, `kernel`, `gamma`, `degree`                      | Régularisation, type noyau, influence locale      |
| Réseaux de Neurones   | `hidden_layer_sizes`, `activation`, `solver`, `alpha` | Architecture, fonction d’activation, optimisation |

---

## ✅ Conclusion

* L’apprentissage supervisé repose sur :

  1. Des **données étiquetées**.
  2. Des **modèles adaptés** (linéaires, arbres, forêts, réseaux…).
  3. Une **optimisation via descente de gradient** (selon l’algo).
  4. Une **évaluation par métriques** adaptées au contexte métier.

👉 Choisir le bon algorithme dépend de la **nature des données**, du **volume**, et de la **métrique business** à optimiser.

---