# 🐍 Workshop Python - Démarrage

## 🌐 Environnement Virtuel

### Qu'est-ce qu'un environnement virtuel ?
Un environnement virtuel est un espace isolé où vous pouvez installer des packages Python sans affecter votre système ou d'autres projets.

### Création et utilisation
```bash
# Création
python3 -m venv env

# Activation
## Windows
env\Scripts\activate
## macOS/Linux
source env/bin/activate

# Installation des dépendances du projet
pip3 install -r requirements.txt
```

### Commandes utiles
```bash
# Lancer un script
python3 script.py

# Mode interactif
python3
# Pour quitter
exit

# Installer un package
pip3 install nom_package

# Sauvegarder les dépendances
pip3 freeze > requirements.txt
```

## 📚 Notions de Base

### Types de données
```python
# Nombres
entier = 42          # int
decimal = 3.14       # float

# Chaînes
texte = "Python"     # str

# Booléens
vrai = True         # bool
faux = False        # bool

# Listes (mutables)
liste = [1, 2, 3]   # list

# Tuples (immutables)
tuple = (1, 2, 3)   # tuple

# Dictionnaires
dico = {"nom": "Jérémy", "age": 20}  # dict
```

### Opérateurs
```python
# Arithmétiques
+    # Addition
-    # Soustraction
*    # Multiplication
/    # Division
//   # Division entière
%    # Modulo
**   # Puissance

# Comparaison
==   # Égal à
!=   # Différent de
<    # Inférieur à
>    # Supérieur à
<=   # Inférieur ou égal
>=   # Supérieur ou égal

# Logiques
and  # ET
or   # OU
not  # NON
```

### Structures de contrôle
```python
# Conditions
if condition:
    # code
elif autre_condition:
    # code
else:
    # code

# Boucles
for i in range(5):
    # code

while condition:
    # code
```

## 🎯 Pourquoi Python ?

### Applications Principales
- **IA & Machine Learning**: TensorFlow, PyTorch
- **Web**: Django, Flask, FastAPI
- **Data Science**: Pandas, NumPy
- **Automatisation**: Scripts, Tests
- **Cybersécurité**: Analyse, Tests d'intrusion

### Avantages
- Syntaxe claire
- Grande communauté
- Multi-plateformes
- Gratuit et open source