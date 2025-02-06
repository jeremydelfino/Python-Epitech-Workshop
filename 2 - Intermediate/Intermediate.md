# 🚀 Workshop Python Intermédiaire

## 📝 Prérequis

### Création d'un environnement virtuel
```bash
# Création
python3 -m venv venv

# Activation
## Linux/MacOS
source venv/bin/activate
## Windows
venv\Scripts\activate

# Installation des dépendances
pip3 install -r requirements.txt
```

## 📚 Concepts Clés

### 1. Classes et Objets

Une classe est un plan pour créer des objets. Elle définit :
- Attributs (données)
- Méthodes (fonctions)
- Constructeur (__init__)

```python
# Exemple avec l'exercice EncoderDecoder
class EncoderDecoder:
    def __init__(self):
        self.key = self._generate_key()
    
    def encode(self, message):
        return ''.join([chr(ord(c) + self.key) for c in message])
    
    def decode(self, encoded_message):
        return ''.join([chr(ord(c) - self.key) for c in encoded_message])
```

### 2. Interfaces Graphiques (GUI)
```python
# Exemple avec CustomTkinter (Cookie Clicker)
class CookieClicker:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("Cookie Clicker")
        self.setup_ui()
    
    def setup_ui(self):
        self.cookie_button = ctk.CTkButton(
            self.window,
            text="🍪",
            command=self.click_cookie
        )
```

### 3. Gestion des Systèmes
```python
# Exemple avec le moniteur système
def get_system_info():
    cpu_percent = psutil.cpu_percent()
    memory = psutil.virtual_memory()
    processes = sorted(
        psutil.process_iter(['pid', 'name', 'cpu_percent']),
        key=lambda p: p.info['cpu_percent'],
        reverse=True
    )[:5]
```

### 4. Base de Données (SQLite)
```python
# Exemple avec le système de blog
class BlogManager:
    def __init__(self):
        self.conn = sqlite3.connect('blog.db')
        self.cursor = self.conn.cursor()
    
    def create_article(self, title, content):
        self.cursor.execute('''
            INSERT INTO articles (title, content, date)
            VALUES (?, ?, ?)
        ''', (title, content, datetime.now()))
        self.conn.commit()
```

## 🛠️ Librairies Essentielles

- **customtkinter**: Interfaces graphiques modernes
- **PIL (Pillow)**: Manipulation d'images
- **psutil**: Informations système
- **sqlite3**: Base de données SQL
- **datetime**: Gestion des dates
- **json**: Stockage/lecture de données

## 📝 Concepts Avancés Appliqués

### Gestion des Ressources
```python
# Context managers (with)
with open('save.json', 'w') as f:
    json.dump(game_state, f)
```

### Programmation Événementielle
```python
# Exemple du Cookie Clicker
def on_cookie_click():
    self.cookies += self.click_power
    self.update_display()
```

### Multithreading
```python
# Pour le moniteur système
import threading

update_thread = threading.Thread(target=update_display)
update_thread.daemon = True
update_thread.start()
```

### Design Patterns
- Singleton (gestionnaire de base de données)
- Observer (mise à jour d'interface)
- Factory (création d'objets)

## 🎯 Bonnes Pratiques

1. **Structure du Code**
   - Organisation modulaire
   - Séparation des responsabilités
   - Documentation des classes et méthodes

2. **Gestion des Erreurs**
   ```python
   try:
       self.conn.execute(query)
   except sqlite3.Error as e:
       logging.error(f"Database error: {e}")
       raise
   ```

3. **Persistance des Données**
   - Sauvegarde/chargement JSON
   - Transactions SQLite
   - Gestion des fichiers