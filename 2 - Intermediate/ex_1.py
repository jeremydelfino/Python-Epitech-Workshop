
# Créez un système de blog qui:
# 1. Utilise SQLite pour stocker les articles
# 2. Permet CreateReadUpdateDelete (CRUD) complet sur les articles
# 3. Supporte la recherche full-text
# 4. Gère les dates automatiquement
# 5. Intègre une interface console

# Si jamais vous avez des difficultés, n'hésitez pas à regarder l'exercice 5:begginer pour avoir une base sur le projet. 
# Il vous restera à ajouter SQLite et les fonctionnalités demandées.

# La database vide est déjà créée pour vous dans le dossier utils, vous n'avez qu'à la remplir.

# Librairies: sqlite3
# Concepts: SQL, bases de données, CRUD

import sqlite3
from datetime import datetime

class BlogManager:
    def __init__(self):
        # Connexion à la base de données
        pass
    
    def setup_database(self):
        # Création des tables
        pass

if __name__ == "__main__":
    blog = BlogManager()
