import subprocess
import time
import webbrowser
import os

# --- Configuration des chemins ---
django_path = "python manage.py runserver"
streamlit_path = "streamlit run dashboard.py"  # remplace dashboard.py par ton fichier réel

# --- Lancer le serveur Django ---
print("🚀 Démarrage du serveur Django...")
django_process = subprocess.Popen(django_path, shell=True)

# --- Attente que Django soit prêt ---
time.sleep(3)  # ajuste si besoin (augmente à 5 si c'est lent)

# --- Lancer Streamlit dans un nouvel onglet du navigateur ---
print("📊 Lancement de Streamlit...")
streamlit_process = subprocess.Popen(streamlit_path, shell=True)

# --- Ouvrir automatiquement le dashboard dans le navigateur (optionnel) ---
time.sleep(2)
webbrowser.open("http://localhost:8501")

# --- Laisser tourner les deux processus ---
try:
    django_process.wait()
    streamlit_process.wait()
except KeyboardInterrupt:
    print("🛑 Arrêt des serveurs...")
    django_process.terminate()
    streamlit_process.terminate()
