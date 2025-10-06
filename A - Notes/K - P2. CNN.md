# 🧠 Deep Learning – Convolutional Neural Networks (CNN)

---

## 📚 Références principales

* *Machine Learning A-Z* — Kirill Eremenko, Hadelin de Ponteves (@SuperDataScience)
* *Deep Learning – Artificial Intelligence* — Sarah Malaeb

---

## 🔹 1. Introduction aux CNN

Un **Convolutional Neural Network (CNN)** est un type de réseau de neurones artificiels conçu pour **traiter des données multidimensionnelles**, en particulier des **images**.

![CNN](./images/CNN.png)


Les CNN sont extrêmement efficaces pour :

* la **classification d’images**,
* la **détection d’objets**,
* la **segmentation**,
* et d’autres tâches de **vision par ordinateur**.

![CNN example](./images/CNN_example.png)

---

## 🔹 2. Pourquoi utiliser des CNN ?

Contrairement à un ANN classique :

* Les CNN exploitent la **structure spatiale** des données (les pixels voisins d’une image sont corrélés).
* Ils apprennent automatiquement des **caractéristiques locales** grâce aux **filtres de convolution**.

📘 En résumé :

> Un CNN est un réseau de neurones capable d’identifier des motifs visuels (formes, contours, textures) dans les données d’entrée.

---

## 🔹 3. Domaines d’application

Bien que les CNN soient conçus pour les **images**, ils peuvent aussi être utilisés pour :

* 🎞️ **Vidéos** : reconnaissance d’actions, détection d’objets en mouvement.
* 🧠 **NLP (texte)** : classification de phrases, analyse de sentiment.
* 🎵 **Audio** : reconnaissance vocale, classification musicale.
* 📈 **Séries temporelles** : détection d’anomalies, prévisions.

---

## 🔹 4. Représentation des images

Avant toute convolution, il faut comprendre comment un **ordinateur “voit” une image** 👁️‍🗨️

### 🔸 4.1. Image = matrice de pixels

Une **image numérique** est une **matrice de valeurs** où chaque élément correspond à l’**intensité lumineuse** d’un pixel.

![Image binaire](./images/Image_binary.png)

Exemples :

* 🖤 **Image en niveaux de gris (grayscale)** → matrice 2D
  [
  I(x,y)
  ]
  Chaque pixel a une valeur entre **0 (noir)** et **255 (blanc)**.

  ![Image 2D](./images/image_2D.png)

* 🎨 **Image couleur (RGB)** → matrice 3D
  [
  I(x,y,c)
  ]
  où $c \in {R,G,B}$ (Rouge, Vert, Bleu).
  Ainsi, une image de 64×64 pixels possède une matrice de taille **64×64×3**.

  ![Image 3D](./images/image_3D.png)

---

### 🔸 4.2. Exemple

Pour un pixel rouge pur :

* R = 255
* G = 0
* B = 0

📊 Exemple visuel (pour une image 2×2 couleur) :

| Pixel | R   | G   | B   |
| ----- | --- | --- | --- |
| (1,1) | 255 | 0   | 0   |
| (1,2) | 0   | 255 | 0   |
| (2,1) | 0   | 0   | 255 |
| (2,2) | 255 | 255 | 0   |

---

### 🔸 4.3. Image = tenseur

En deep learning, une image est stockée sous forme de **tenseur** (matrice multidimensionnelle).
Exemple :

* Image couleur : `shape = (hauteur, largeur, canaux)`
* Batch d’images : `shape = (nombre_images, hauteur, largeur, canaux)`

📘 Exemple concret :

```
Image RGB : (64, 64, 3)
Batch de 100 images : (100, 64, 64, 3)
```

---

### 🔸 4.4. Normalisation des pixels

Avant d’envoyer une image dans un CNN, on **normalise les valeurs de pixels** :
[
I_{norm} = \frac{I}{255}
]
Cela ramène les valeurs entre **0 et 1**, ce qui :

* stabilise la descente de gradient,
* accélère la convergence,
* évite des valeurs trop grandes pour la backpropagation.

---

## 🔹 5. Structure générale d’un CNN

Un CNN comprend généralement plusieurs **types de couches** :

1. **Couche d’entrée (Input Layer)** : reçoit les données brutes (ex : une image 28x28x3).
2. **Couche de convolution (Convolutional Layer)** : extrait les features via des filtres.
3. **Couche d’activation (ReLU)** : introduit la non-linéarité.
4. **Couche de pooling** : réduit la dimension spatiale.
5. **Flattening** : transforme les matrices en vecteur 1D.
6. **Couches entièrement connectées (Fully Connected Layers)** : classification.
7. **Couche de sortie (Output Layer)** : produit la prédiction finale.

![CNN structure](./images/CNN_structure.png)

---

## 🔸 5.1 Étape 1 — Convolution

### 🔹 Principe

La **convolution** consiste à faire glisser un **filtre (kernel)** sur l’image pour en extraire des motifs.

[
\text{Feature map} = \text{Image} * \text{Filtre}
]

![Convultion Example](./images/Convultion_Example.png)

Chaque **filtre** détecte un motif spécifique :

* bords,
* textures,
* contours,
* zones lumineuses, etc.

### 🧮 Exemple :

* Image : matrice de pixels (28×28).
* Filtre : matrice 3×3.
* À chaque position → produit scalaire entre le filtre et la zone couverte → valeur de sortie.

![Convultion Start](./images/Convultion_Step_Start.png)

📘 Résultat : une **Feature Map**, qui indique où le motif est détecté.

![Convultion End](./images/Convultion_Step_End.png)
---

### ✅ Avantages :

* Réduction du nombre de paramètres (poids partagés).
* Capacité à détecter des motifs **indépendamment de leur position**.

### ⚠️ Inconvénients :

* Perte d’information lors de la réduction dimensionnelle.

---

### 💡 Pour limiter cette perte :

* A travers l'entraînement, nous décidons quels **features** sont les plus importants.
* On utilise **plusieurs filtres** → plusieurs **feature maps**.
* Chaque filtre apprend un **motif différent** pendant l’entraînement.

![Convultion Loss](./images/Convultion_Loss.png)

---

#### 🧩 5.1.1 Définition mathématique

La **convolution** est une opération mathématique qui combine deux fonctions :

* une **entrée** ( f(t) ) (ex : une image, un signal ou une série de données),
* et un **filtre** ou **noyau** ( g(t) ) (ex : un détecteur de motifs).

Elle est définie comme :

[
(f * g)(t) = \int_{-\infty}^{+\infty} f(\tau), g(t - \tau), d\tau
]

📘 Cette intégrale mesure la **similarité** entre la fonction d’entrée ( f ) et une version décalée du filtre ( g ).

> Autrement dit, ( g ) “glisse” sur ( f ) et calcule leur recouvrement (produit scalaire) pour chaque position ( t ).

---

#### 🧠 5.1.2 Interprétation intuitive

Dans un **CNN**, la convolution permet de **détecter des motifs** (features) dans une image, comme :

* des bords,
* des textures,
* des formes ou couleurs spécifiques.

➡️ Le filtre ( g ) agit comme une **loupe** qui “scanne” l’image ( f ).
À chaque position, il multiplie localement les valeurs et additionne le tout :
→ Cela produit une nouvelle **feature map** qui indique **où** un certain motif apparaît.

---

#### ⚙️ 5.1.3 Signification des variables

| Symbole        | Signification                              |
| -------------- | ------------------------------------------ |
| ( f )          | Fonction d’entrée (image, signal original) |
| ( g )          | Filtre ou noyau de convolution             |
| ( t )          | Position de décalage du filtre             |
| ( \tau )       | Variable d’intégration / décalage interne  |
| ( (f * g)(t) ) | Résultat de la convolution (feature map)   |

---

#### 🔢 5.1.4 Forme discrète (cas des images numériques)

Dans le cas d’images (qui sont des matrices de pixels), la convolution devient une **somme discrète** :

[
S(i, j) = \sum_m \sum_n I(i - m, j - n) , K(m, n)
]

où :

* ( I ) = image d’entrée,
* ( K ) = kernel (filtre),
* ( S(i,j) ) = pixel de la **feature map de sortie**.

Chaque valeur de ( S ) est donc une **combinaison locale** des pixels voisins dans ( I ), pondérée par les coefficients du filtre ( K ).

---

#### 🧭 5.1.5 Interprétation : “modifier la forme de l’autre fonction”

La phrase :

> “One function modifies the shape of the other”

signifie que le **filtre** ( g ) transforme localement la forme de l’entrée ( f ).
Chaque type de filtre produit un effet différent :

| Type de filtre            | Effet sur l’image     |
| ------------------------- | --------------------- |
| Détecteur de bords        | Souligne les contours |
| Floutage (Gaussian blur)  | Adoucit les zones     |
| Rehaussement de contraste | Accentue les détails  |

Le CNN apprend **automatiquement** ces filtres pendant l’entraînement.

---

#### 🧮 5.1.6 Vue vectorisée (formules matricielles)

Les formules à droite de ton image représentent la **convolution vectorisée** utilisée dans la rétropropagation (backpropagation).

Elles expriment la **dérivée du résultat** ( z ) de la convolution par rapport à :

* l’entrée ( Y ),
* et les poids du filtre ( F ).

Exemple :

[
\frac{\partial z}{\partial(\text{vec}(y)^T)}(F^T \otimes I) = (F \otimes I)\frac{\partial z}{\partial \text{vec}(y)}
]

📘 Cela permet de **calculer les gradients** pour **ajuster les poids du filtre** lors de l’entraînement du CNN — c’est le cœur du **deep learning**.

---

#### 📊 5.1.7 Résumé visuel

| Élément           | Interprétation                          |
| ----------------- | --------------------------------------- |
| ( f )             | Entrée (image ou signal)                |
| ( g )             | Filtre (noyau)                          |
| ( * )             | Opération de convolution                |
| ( (f * g)(t) )    | Résultat (feature map)                  |
| Intégrale / somme | Produit scalaire entre entrée et filtre |

---

## 🔸 5.2 Étape 1’ — ReLU Layer (Rectified Linear Unit)

Après chaque convolution, on applique une **fonction d’activation ReLU** :
[
f(x) = \max(0, x)
]

### 🎯 Pourquoi ?

* Pour **introduire la non-linéarité** (les images sont des données non linéaires).
* Pour **supprimer les valeurs négatives** issues de la convolution.

📊 **Avant ReLU** : valeurs positives et négatives.
📊 **Après ReLU** : seulement des valeurs positives → simplifie la propagation.

---

## 🔸 5.3 Étape 2 — Pooling (Sous-échantillonnage)

### 🎯 Objectif

Réduire la taille des **feature maps** tout en gardant l’information essentielle.
→ Moins de paramètres, moins de calculs, moins d’overfitting.

### 🔧 Types de pooling :

* **Max pooling** : garde la valeur maximale du patch.
* **Average pooling** : moyenne du patch.
* **Global pooling** : réduit chaque map en une seule valeur.

### ⚙️ Paramètres :

* **Taille du kernel** : souvent 2×2.
* **Stride** : pas de déplacement (souvent 2).

📘 Exemple :
Une feature map 4×4 devient une 2×2 après max pooling 2×2.


![Max Pooling](./images/Max_pooling.png)

---

## 🔸 5.4 Étape 3 — Flattening

---

### 🧩 5.4.1 Contexte : pourquoi le Flattening existe

Dans un **réseau de neurones convolutionnel (CNN)**, les premières couches (Convolution + Pooling) ont pour rôle :

* d’extraire des **caractéristiques locales** (bords, textures, formes, couleurs, etc.),
* et de produire des **feature maps** sous forme de **matrices 2D** (ou 3D si on compte les canaux).

Exemple :
Après plusieurs couches, on peut obtenir un tenseur de taille **(32, 32, 64)** :

* 32×32 = dimensions spatiales (hauteur, largeur),
* 64 = nombre de **filtres** → donc 64 **feature maps**.

💡 Chaque feature map correspond à une caractéristique apprise (par ex. “bord vertical”, “courbe”, “yeux”, etc.).

Problème :
➡️ La prochaine étape du CNN est un **réseau de neurones dense (Fully Connected)**, or celui-ci **ne peut traiter que des vecteurs 1D** (liste de valeurs).

C’est là qu’intervient le **Flattening**.

---

### 🧮 5.4.2 Définition du Flattening

Le **Flattening** est une opération de **mise à plat** (ou “vectorisation”) :

> On transforme le tenseur 3D issu des convolutions/poolings en un **vecteur 1D**.


![Flattening](./images/Flattening.png)

Formellement :
[
\text{Flattening : } \mathbb{R}^{h \times w \times c} \longrightarrow \mathbb{R}^{(h \cdot w \cdot c)}
]

Exemple :

* Avant flattening : feature maps = (7, 7, 64)
* Après flattening : vecteur = (7×7×64) = 3136 valeurs.

---

### 🧠 5.4.3 Interprétation conceptuelle

On peut voir le flattening comme :

> “Prendre toutes les caractéristiques locales extraites dans les feature maps et les disposer en une seule ligne, pour les donner à un classificateur.”

Chaque valeur du vecteur final représente une **intensité d’activation** d’une caractéristique dans une région spécifique de l’image.

🧩 **Analogie** :
C’est comme si, après avoir détecté différents morceaux d’un visage (yeux, nez, bouche), tu rangeais toutes ces informations sur une seule ligne avant de décider si c’est un **chien**, un **chat**, ou un **humain**.

---

### ⚙️ 5.4.4 Exemple concret

Imaginons une **image 32×32×3 (RGB)**.
Après convolution et pooling, on obtient :

```
Feature maps = (8, 8, 32)
```

➡️ Le flattening transforme ce tenseur 3D en un **vecteur 1D de longueur 8×8×32 = 2048**.

Ce vecteur devient alors l’**entrée de la première couche fully connected (Dense)**, qui prendra ces 2048 valeurs comme **features globales** de l’image.

---

### 💡 5.4.5 Pourquoi c’est utile

✅ Il permet de connecter la partie **convolutionnelle** (apprentissage spatial) à la partie **dense** (apprentissage décisionnel).
✅ Il conserve **toutes les informations extraites** jusque-là.
✅ Il rend le réseau **compatible avec les couches de type Dense**.


![Flattening Structure](./images/Flattening_structure.png)

---

### ⚠️ 5.4.6 Points à retenir

| Étape      | Entrée                    | Sortie     | Rôle                                               |
| ---------- | ------------------------- | ---------- | -------------------------------------------------- |
| Flattening | Tenseur 3D (Feature Maps) | Vecteur 1D | Convertir les features en entrée d’un réseau dense |

---

### 🧱 5.4.7 Exemple en code (Keras)

```python
from tensorflow.keras.layers import Flatten

# Exemple après une convolution et un pooling
model.add(Conv2D(64, (3,3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

# Flatten : passage de 3D à 1D
model.add(Flatten())

# Puis couches fully connected
model.add(Dense(128, activation='relu'))
model.add(Dense(10, activation='softmax'))
```

---

### 🧮 5.4.8 Interprétation mathématique (facultative mais utile)

Le flattening est en réalité une **transformation linéaire** :
[
x' = \text{vec}(X)
]
où `vec` (vectorisation) empile les colonnes d’une matrice ou les valeurs d’un tenseur dans un seul vecteur.

Cela ne change **aucune valeur**, seulement leur **forme**.
Les poids du réseau dense qui suivent vont alors apprendre à pondérer chaque “feature activée” individuellement.

---

### 🧩 5.4.9 Métaphore visuelle

Imagine un **livre** :

* Les couches convolutionnelles et pooling représentent les **pages** (chaque page = un filtre qui détecte un motif).
* Le flattening consiste à **arracher toutes les pages, les découper en petits morceaux, et les mettre à plat sur une table**.
* Le réseau dense (fully connected) vient ensuite **analyser cette table complète** pour tirer une conclusion finale.

---

## 🔸 5.5 Étape 4 — Fully Connected Layer (FC)

Ces couches se comportent comme des **réseaux ANN classiques**.
Elles combinent toutes les features extraites pour prédire la classe finale.

![Fully Connected](./images/Fully_connected1.png)

📘 Exemple :

* Feature : “yeux”, “nez”, “oreilles”
* Classe : “chien”, “chat”, “lapin”

Le CNN apprend **quelles combinaisons de features** correspondent à quelle classe.

![Fully Connected Prediction](./images/FC_prediction.png)

---

## 🔸 5.6 Étape 5 — Couche de sortie

* Applique une **fonction Softmax** pour obtenir les **probabilités** de chaque classe :
  [
  P(y_i) = \frac{e^{z_i}}{\sum_j e^{z_j}}
  ]

* La **classe prédite** est celle avec la probabilité la plus élevée.

---

## 🔸 5.7 Étape 6 — Fonction de perte (Loss Function)

On utilise généralement la **Cross-Entropy** pour mesurer la performance du modèle :

[
L = -\sum y_i \log(\hat{y_i})
]

* Si la prédiction s’éloigne de la vérité → perte augmente.
* Objectif : **minimiser la perte** pour optimiser le réseau.

---

## 🔹 6. Résumé du pipeline CNN

| Étape | Nom de la couche        | Fonction principale           |
| ----- | ----------------------- | ----------------------------- |
| 1     | Convolution             | Extraire les features locales |
| 1’    | ReLU                    | Introduire la non-linéarité   |
| 2     | Pooling                 | Réduire la dimension spatiale |
| 3     | Flattening              | Convertir en vecteur 1D       |
| 4     | Fully Connected         | Combiner les features         |
| 5     | Softmax + Cross-Entropy | Prédire et évaluer la classe  |

![CNN Process](./images/CNN_Process.png)

---

## 🔹 7. Exemple en Keras

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# Création du modèle CNN
model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(64, 64, 3)),
    MaxPooling2D(pool_size=(2,2)),
    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D(pool_size=(2,2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=25, batch_size=32, validation_split=0.2)
```

---

## 🔹 8. Points forts et limites

✅ **Avantages :**

* Réduction du besoin d’extraction manuelle de features.
* Excellente performance en vision par ordinateur.
* Poids partagés → moins de paramètres à apprendre.

⚠️ **Limites :**

* Nécessite beaucoup de données d’entraînement.
* Très coûteux en calcul (GPU recommandé).
* Moins adapté aux données tabulaires classiques.

---

## 🔹 9. Applications réelles

* 🖼️ Reconnaissance faciale
* 🚗 Voitures autonomes (détection de piétons, feux, routes)
* 🩺 Imagerie médicale (IRM, radiographie)
* 📱 Reconnaissance d’objets sur smartphone
* 📷 Classification d’émotions sur visages