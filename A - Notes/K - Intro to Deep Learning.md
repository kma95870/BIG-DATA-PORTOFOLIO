# 🧠 INTRO : Réseaux de Neurones & Deep Learning

---

## 🔹 1. Introduction à l’IA, ML et DL

* **IA (Intelligence Artificielle)** : créer des machines intelligentes.
* **ML (Machine Learning)** : apprentissage automatique à partir des données.
* **DL (Deep Learning)** : sous-domaine du ML basé sur les **réseaux de neurones profonds**, capables d’apprendre **automatiquement les features**.

➡️ Le Deep Learning s’inspire du cerveau humain (neurones, synapses, propagation d’un signal).

---

## 🔹 2. Le Neurone Artificiel

### Fonctionnement :

[
z = \sum w_i x_i + b
]
[
a = f(z)
]

* **$w_i$** : poids, importance de chaque feature.
* **$b$** : biais, ajuste le seuil de déclenchement.
* **$f(z)$** : fonction d’activation (sigmoid, tanh, ReLU, softmax).

### Fonctions d’activation :

* **Sigmoid** : probabilité entre 0 et 1.
* **tanh** : sortie entre -1 et 1.
* **ReLU** : $max(0,z)$, rapide, évite vanishing gradient.
* **Softmax** : classification multi-classes.

---

## 🔹 3. Architecture des Réseaux de Neurones

* **Input layer** : variables d’entrée.
* **Hidden layers** : transformations non-linéaires.
* **Output layer** : prédiction finale.

➡️ Les modèles **profonds** = plusieurs couches cachées.

---

## 🔹 4. Apprentissage d’un Réseau

1. **Forward pass** : calcul des sorties $\hat{y}$.
2. **Fonction de coût** : ex. MSE (régression), Cross-Entropy (classification).
3. **Backpropagation** : calcul des gradients par dérivation en chaîne.
4. **Optimisation** : mise à jour des poids via descente de gradient (SGD, Adam, RMSprop…).

---

## 🔹 5. Types de Réseaux de Neurones

### 🔸 5.1 ANN (Perceptron multicouche)

* Réseau de neurones dense (**Fully Connected**).
* Base de tout le deep learning.
* Utilisé pour données tabulaires, classification simple.

### 🔸 5.2 CNN (Convolutional Neural Networks)

* Adaptés aux **images, audio, vidéos**.
* **Convolution** : détection de motifs (bords, textures, objets).
* **ReLU** : non-linéarité.
* **Pooling** : réduction dimensionnelle (max pooling).
* **Flattening + Fully connected** : classification.
* **Softmax + Cross-Entropy** : sortie probabiliste.
  ➡️ Applications : reconnaissance faciale, détection d’objets, vision autonome.

### 🔸 5.3 RNN (Recurrent Neural Networks)

* Gèrent les **séquences temporelles** (texte, séries financières, audio).
* Chaque état dépend de l’état précédent (mémoire courte).
* Problème : **vanishing gradient**.

#### Améliorations :

* **LSTM (Long Short-Term Memory)** : mémoire longue grâce à des **portes** (input, forget, output).
* **GRU (Gated Recurrent Unit)** : plus simple et rapide.

➡️ Applications : traduction automatique, prévision boursière, analyse de sentiments.

### 🔸 5.4 Transformers

* Basés sur le mécanisme **d’attention**.
* Permettent de traiter de longues séquences efficacement.
* Exemples : **BERT, GPT (ChatGPT), T5, ViT**.
  ➡️ Applications : NLP, résumé de texte, vision par ordinateur, multimodalité.

---

## 🔹 6. Problèmes & Solutions

* **Overfitting** : régularisation (Dropout, L2, BatchNorm, Early Stopping).
* **Vanishing gradient** : ReLU, LSTM, normalisation des poids.
* **Besoin massif en données** : Data Augmentation, Transfer Learning.

---

## 🔹 7. Optimisation & Hyperparamètres

* **Learning rate** : vitesse d’apprentissage.
* **Batch size** : nombre d’exemples par mise à jour.
* **Epochs** : nombre de passages sur l’ensemble des données.
* **Optimizers** : SGD, Adam, RMSprop.

---

## 🔹 8. Cas pratiques

* **ANN** → prédire si un client quitte une banque (churn).
* **CNN** → reconnaître un chiffre manuscrit (MNIST).
* **RNN/LSTM** → prédire le cours d’une action boursière.
* **Transformers** → traduire un texte ou générer du langage naturel.

---

## 🔹 9. Exemple pratique (CNN avec Keras)

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),
    MaxPooling2D(2,2),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.fit(X_train, y_train, epochs=10, batch_size=64, validation_split=0.2)
```

---

## 🔹 10. Conclusion

* **ANN** = base.
* **CNN** = vision et perception.
* **RNN/LSTM** = séquences.
* **Transformers** = état de l’art en NLP et multimodalité.

👉 Le Deep Learning permet de résoudre des problèmes **complexes, multidimensionnels, séquentiels et perceptuels** en imitant l’intelligence humaine.

