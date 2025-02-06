# 📚 Librairies Python pour la Data Science

## 🔧 Manipulation de Données

### Pandas
Manipulation de données tabulaires (format Excel/CSV)
```python
import pandas as pd

# Lire un CSV
df = pd.read_csv("donnees.csv")

# Filtrer et agréger
resultats = df.groupby("categorie").mean()
```

### NumPy
Calculs numériques et tableaux multidimensionnels
```python
import numpy as np

# Créer une matrice
matrice = np.array([[1, 2], [3, 4]])

# Opérations matricielles
inverse = np.linalg.inv(matrice)
```

### Polars
Alternative performante à Pandas pour les grands jeux de données
```python
import polars as pl

# Plus rapide que Pandas
df = pl.read_csv("large_file.csv")
resultat = df.groupby("colonne").agg(pl.sum("valeurs"))
```

### Vaex
Visualisation et analyse de données massives
```python
import vaex

# Traiter des millions de lignes
df = vaex.open("huge_dataset.hdf5")
stats = df.mean(["colonne1", "colonne2"])
```

## 📊 Visualisation

### Matplotlib & Seaborn
Visualisations statistiques standards
```python
import matplotlib.pyplot as plt
import seaborn as sns

# Créer un graphique
sns.scatterplot(data=df, x="x", y="y")
plt.title("Mon graphique")
```

### Plotly
Graphiques interactifs pour le web
```python
import plotly.express as px

# Créer un dashboard interactif
fig = px.scatter(df, x="x", y="y", color="categorie")
fig.show()
```

### Bokeh
Visualisations web avancées
```python
from bokeh.plotting import figure, show

# Créer un graphique interactif
p = figure(title="Visualisation")
p.line(x, y, line_width=2)
show(p)
```

## 🤖 Machine Learning

### Scikit-learn
Apprentissage automatique classique
```python
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Entraîner un modèle
model = RandomForestClassifier()
model.fit(X_train, y_train)
```

### TensorFlow/PyTorch
Deep Learning et réseaux de neurones
```python
import tensorflow as tf

# Créer un réseau de neurones
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])
```

### XGBoost
Algorithmes de boosting performants
```python
import xgboost as xgb

# Entraîner un modèle de boosting
model = xgb.XGBRegressor()
model.fit(X_train, y_train)
```

## 📈 Analyse Statistique

### SciPy
Calculs scientifiques et statistiques
```python
from scipy import stats

# Test statistique
t_stat, p_value = stats.ttest_ind(groupe1, groupe2)
```

### Statsmodels
Modèles statistiques avancés
```python
import statsmodels.api as sm

# Régression linéaire avec statistiques
model = sm.OLS(y, X).fit()
print(model.summary())
```

## 🔤 Traitement du Langage Naturel

### spaCy
Traitement linguistique avancé
```python
import spacy

# Analyse linguistique
nlp = spacy.load("fr_core_news_sm")
doc = nlp("Analysez cette phrase en français.")
```

### NLTK
Outils de base pour le NLP
```python
import nltk

# Tokenization et analyse
tokens = nltk.word_tokenize("Une phrase à analyser")
tags = nltk.pos_tag(tokens)
```

## 💾 Bases de Données & Big Data

### PySpark
Traitement distribué de données
```python
from pyspark.sql import SparkSession

# Créer une session Spark
spark = SparkSession.builder.getOrCreate()
df = spark.read.csv("big_data.csv")
```

### Dask
Calcul parallèle pour grands datasets
```python
import dask.dataframe as dd

# Traitement parallèle
df = dd.read_csv("*.csv")
resultat = df.groupby("colonne").mean().compute()
```

## ⏰ Séries Temporelles

### Prophet
Prévision de séries temporelles par Facebook
```python
from prophet import Prophet

# Créer des prévisions
model = Prophet()
model.fit(df)
future = model.make_future_dataframe(periods=365)
```

### Statsmodels (SARIMA)
Modèles classiques de séries temporelles
```python
from statsmodels.tsa.statespace.sarimax import SARIMAX

# Modèle SARIMA
model = SARIMAX(data, order=(1, 1, 1))
results = model.fit()
```

## 🌐 Web Scraping

### Beautiful Soup
Parser HTML/XML
```python
from bs4 import BeautifulSoup
import requests

# Extraire des données web
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
```

### Selenium
Automatisation de navigateur
```python
from selenium import webdriver

# Automatiser la navigation
driver = webdriver.Chrome()
driver.get(url)
element = driver.find_element_by_id("mon_id")
```

## 🎯 Cas d'Utilisation Courants

### Analyse de Données
- Pandas + Matplotlib pour l'exploration
- Seaborn pour les visualisations statistiques
- Scikit-learn pour la modélisation

### Big Data
- PySpark pour le traitement distribué
- Dask pour le parallélisme
- Vaex pour les visualisations grandes échelles

### Intelligence Artificielle
- TensorFlow/PyTorch pour le deep learning
- spaCy pour le NLP
- XGBoost pour les compétitions

### Finance
- Prophet pour les prévisions
- Statsmodels pour l'analyse technique
- Pandas pour les données financières