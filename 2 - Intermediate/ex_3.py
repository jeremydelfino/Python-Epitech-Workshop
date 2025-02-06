# Créez un moniteur système en ligne de commande qui:
# 1. Affiche en temps réel dans le terminal:
#    - Utilisation CPU (avec barre de progression ASCII)
#    - Utilisation RAM (avec barre de progression ASCII) 
#    - Top 5 des processus les plus consommateurs
# 2. Rafraîchit l'affichage toutes les secondes
# 3. Permet de quitter proprement avec Ctrl+C
# 4. Affiche des alertes colorées si surchage
# 5. Mode debug avec plus de détails (-v)

# Librairies: psutil, time, sys
# Bonus: Utilisez curses pour une interface plus sophistiquée

import psutil
import time
import os
import sys
from datetime import datetime

def main():
   # Code à compléter...