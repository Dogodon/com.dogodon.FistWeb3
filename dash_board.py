# import streamlit as st
# import matplotlib.pyplot as plt
# import numpy as np



# st.title("Analiytics Dashboard")
# st.write("v.0.0.1")


# #Test chart





import streamlit as st
import pandas as pd 
import streamlit.components.v1 as stc
import plotly.express as px
import time
from streamlit_option_menu import option_menu
from numerize.numerize import numerize
import plotly.express as px
import plotly.subplots as sp
import plotly.graph_objects as go






###IMPORTER LES DONNEES DEPUIS NOTRE API *DASHBOARD*
import requests
import altair as alt
# import pandas as pd





#page behaviour
st.set_page_config(page_title="Descriptive Analytics ", page_icon="🌎", layout="wide")  


###IMPORTER LES DONNEES DEPUIS NOTRE API *DASHBOARD*

#functions
def fetch_data(endpoint):
   response = requests.get(endpoint)
   data = response.json()
   return data

# #data from SWAPI API
# swapi_endpoint = 'https://swapi.dev/api/people/1' 

# #store return data from fetch here
# swapi_data = fetch_data(swapi_endpoint)  

# #display data
# st.write('Data from the SWAPI API')
# st.json('swapi_data')

#fetch data from our api
# api_url = 'http://127.0.0.1:8000/api/customers/'
api_url = 'http://127.0.0.1:8000/api/invoices/'





# data = fetch_data(api_url)
# if data:
#   if data:
#     # Si 'zone' se trouve dans un sous-objet 'customer', tu devras l'extraire
#     for item in data:
#         item['zone'] = item['customer']['zone']  # Ajoute 'zone' à l'objet principal
#         item['pays'] = item['customer']['pays']  # Ajoute 'pays' à l'objet principal
#         item['customer_type'] = item['customer']['customer_type']  # Ajoute 'customer_type' à l'objet principal 
#         item['creator_name'] = item['customer']['creator_name']  # Ajoute 'creator_name' à l'objet principal 
    
#     for item in data:
#         item['designation'] = item['articles']['designation']  # Ajoute 'designation' à l'objet principal
#         item['quantity'] = item['articles']['quantity']  # Ajoute 'quantity' à l'objet principal
#         item['unite'] = item['articles']['unite']  # Ajoute 'unite' à l'objet principal
#         item['unit_price'] = item['articles']['unit_price']  # Ajoute 'unit_price' à l'objet principal
#         item['famille'] = item['articles']['famille']  # Ajoute 'famille' à l'objet principal
#         item['remise'] = item['articles']['remise']  # Ajoute 'remise' à l'objet principal
#         item['tva'] = item['articles']['tva']  # Ajoute 'tva' à l'objet principal


#     df = pd.DataFrame(data)
#     print(df.columns)  # Vérifie les colonnes après ajout de 'zone'

#     st.dataframe(df)

# data = fetch_data(api_url)
# if data:
#     for item in data:
#         # Accède aux informations du 'customer'
#         item['zone'] = item['customer']['zone']  # Ajoute 'zone' à l'objet principal
#         item['pays'] = item['customer']['pays']  # Ajoute 'pays' à l'objet principal
#         item['customer_type'] = item['customer']['customer_type']  # Ajoute 'customer_type' à l'objet principal
#         item['creator_name'] = item['customer']['creator_name']  # Ajoute 'creator_name' à l'objet principal

#         # Accède aux informations de la liste 'articles'
#         for article in item['articles']:  # Assure-toi que 'articles' est une liste
#             item['designation'] = article['designation']  # Ajoute 'designation' à l'objet principal
#             item['quantity'] = article['quantity']  # Ajoute 'quantity' à l'objet principal
#             item['unite'] = article['unite']  # Ajoute 'unite' à l'objet principal
#             item['unit_price'] = article['unit_price']  # Ajoute 'unit_price' à l'objet principal
#             item['famille'] = article['famille']  # Ajoute 'famille' à l'objet principal
#             item['remise'] = article['remise']  # Ajoute 'remise' à l'objet principal
#             item['tva'] = article['tva']  # Ajoute 'tva' à l'objet principal

#     df = pd.DataFrame(data)
#     print(df.columns)  # Vérifie les colonnes après ajout de 'zone'

#     st.dataframe(df)


# import streamlit as st
# import pandas as pd
# import requests



# import streamlit as st
# import requests
# import pandas as pd

# DJANGO_URL = "http://localhost:8000"
# SESSION_COOKIE_NAME = "sessionid"

# # Récupération de l’ID de session depuis les query params
# def get_django_session():
#     query_params = st.query_params
#     return query_params.get(SESSION_COOKIE_NAME, [None])[0]

# # Requête à l'API Django
# def fetch_user_data(session_id):
#     cookies = {SESSION_COOKIE_NAME: session_id}
#     try:
#         response = requests.get(f"{DJANGO_URL}/api/invoices/", cookies=cookies)
#         if response.status_code == 200:
#             return response.json()
#         else:
#             st.error(f"⚠️ Erreur ({response.status_code}) : {response.text}")
#             return None
#     except Exception as e:
#         st.error(f"❌ Erreur réseau : {str(e)}")
#         return None


# # Exécution principale
# session_id = get_django_session()

# if not session_id:
#     st.warning("⚠️ Aucun identifiant de session trouvé dans l'URL.")
#     st.stop()

# data = fetch_user_data(session_id)

# if not data:
#     st.warning("⚠️ Aucune donnée reçue de l'API.")
#     st.stop()

# # Expand les données
# expanded_data = []
# for item in data:
#     zone = item['customer']['zone']
#     pays = item['customer']['pays']
#     customer_type = item['customer']['customer_type']
#     creator_name = item['customer']['creator_name']
#     for article in item['articles']:
#         article_details = {
#             'zone': zone,
#             'pays': pays,
#             'customer_type': customer_type,
#             'creator_name': creator_name,
#             'designation': article['designation'],
#             'quantity': article['quantity'],
#             'unite': article['unite'],
#             'unit_price': article['unit_price'],
#             'famille': article['famille'],
#             'remise': article['remise'],
#             'tva': article['tva']
#         }
#         expanded_data.append(article_details)

# df_selection = pd.DataFrame(expanded_data)

# # 🔒 Sécurité : si DataFrame est vide
# if df_selection.empty:
#     st.warning("⚠️ Données vides.")
#     st.stop()






# DJANGO_URL = "http://localhost:8000"
# SESSION_COOKIE_NAME = "sessionid"

# # Récupération de l’ID de session depuis les query params
# def get_django_session():
#     query_params = st.query_params
#     return query_params.get(SESSION_COOKIE_NAME, [None])[0]

# # Requête à l'API Django
# def fetch_user_data(session_id):
#     cookies = {SESSION_COOKIE_NAME: session_id}
#     try:
#         response = requests.get(f"{DJANGO_URL}/api/invoices/", cookies=cookies)
#         if response.status_code == 200:
#             return response.json()
#         else:
#             st.error(f"⚠️ Erreur ({response.status_code}) : {response.text}")
#             return None
#     except Exception as e:
#         st.error(f"❌ Erreur réseau : {str(e)}")
#         return None

# # Exécution principale
# session_id = get_django_session()
# if not session_id:
#     st.warning("⚠️ Aucun identifiant de session trouvé dans l'URL.")
# else:
#     data = fetch_user_data(session_id)
#     if data:
#         expanded_data = []
#         for item in data:
#             zone = item['customer']['zone']
#             pays = item['customer']['pays']
#             customer_type = item['customer']['customer_type']
#             creator_name = item['customer']['creator_name']
#             for article in item['articles']:
#                 article_details = {
#                     'zone': zone,
#                     'pays': pays,
#                     'customer_type': customer_type,
#                     'creator_name': creator_name,
#                     'designation': article['designation'],
#                     'quantity': article['quantity'],
#                     'unite': article['unite'],
#                     'unit_price': article['unit_price'],
#                     'famille': article['famille'],
#                     'remise': article['remise'],
#                     'tva': article['tva']
#                 }
#                 expanded_data.append(article_details)

#             # Crée un DataFrame à partir de la liste 'expanded_data'
#             df_selection = pd.DataFrame(expanded_data)


# data = fetch_data(api_url)
# if data:
#     expanded_data = []  # Liste pour stocker toutes les lignes étendues(depuis les superlignes INVOICE)

#     for item in data:
#         # Accède aux informations du 'customer'
#         zone = item['customer']['zone']
#         pays = item['customer']['pays']
#         customer_type = item['customer']['customer_type']
#         creator_name = item['customer']['creator_name']

#         # Accède aux informations de la liste 'articles'
#         for article in item['articles']: 
#             article_details = {
#                 'zone': zone,  # Ajoute l'information sur la zone
#                 'pays': pays,  # Ajoute l'information sur le pays
#                 'customer_type': customer_type,  # Ajoute le type de client
#                 'creator_name': creator_name,  # Ajoute le nom du créateur
#                 'designation': article['designation'],
#                 'quantity': article['quantity'],
#                 'unite': article['unite'],
#                 'unit_price': article['unit_price'],
#                 'famille': article['famille'],
#                 'remise': article['remise'],
#                 'tva': article['tva']
#             }
#             expanded_data.append(article_details)  # Ajoute chaque article à la liste

#     # Crée un DataFrame à partir de la liste 'expanded_data'
#     df = pd.DataFrame(expanded_data)

#     # Affiche le DataFrame avec Streamlit
#     st.dataframe(df)



import requests
import pandas as pd
import streamlit as st

# def fetch_data(endpoint, token=None):
#     try:
#         headers = {"Authorization": f"Bearer {token}"} if token else {}
#         response = requests.get(endpoint, headers=headers)
#         response.raise_for_status()
#         return response.json()
#     except requests.exceptions.HTTPError as e:
#         st.error(f"HTTP Error: {str(e)}")
#     except Exception as e:
#         st.error(f"Error fetching data: {str(e)}")
#     return None

# # API Configuration
# api_url = "http://127.0.0.1:8000/api/invoices/"
# # api_token = "your_api_token_here"  # 🔑 Replace with your token

# # If using Token Auth:
# # token = "your_api_token_here"  # Replace with your actual token
# # data = fetch_data(api_url, token=token)

# # If using Basic Auth:
# # data = fetch_data(api_url, username="your_username", password="your_password")
# # Fetch data
# # data = fetch_data(api_url, token=api_token)
# data = fetch_data(api_url, email="dogodontraore@gmail.com", password="d*") 

# if data is None:
#     st.error("❌ Failed to fetch data. Check authentication and API URL.")
#     st.stop()






































#################################3GOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOD  2222222222222222222222222222



# from urllib.parse import urlparse, parse_qs

# query_params = st.experimental_get_query_params()
# email = query_params.get("email", [None])[0]
# token = query_params.get("token", [None])[0]

# if email and token:
#     headers = {"Authorization": f"Token {token}"}
#     response = requests.get(api_url, headers=headers)
#     data = response.json()

import streamlit as st
import requests
from urllib.parse import urlparse, parse_qs
import pandas as pd
import plotly.express as px

# # 🧠 Récupération des paramètres dans l'URL
# query_params = st.query_params

query_params = st.query_params
session_id = query_params.get("sessionid")  # Pas besoin de [0]

# query_params = st.experimental_get_query_params()
# session_id = query_params.get("sessionid", [None])[0]

if not session_id:
    st.warning("🔐 Session non trouvée. Veuillez vous connecter via l'application principale.")
    st.stop()

# query_params = st.experimental_get_query_params()
# email = query_params.get("email", [None])[0]
# token = query_params.get("token", [None])[0]


# URL de ton API
api_url = "http://127.0.0.1:8000/api/invoices/"

# 🛰️ Requête API avec token d'authentification

def fetch_data_with_session(url, session_id):
    try:
        cookies = {'sessionid': session_id}
        response = requests.get(url, cookies=cookies)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        st.error(f"Erreur HTTP : {e.response.status_code} - {e.response.text}")
    except Exception as e:
        st.error(f"Erreur lors de la récupération des données : {str(e)}")
    return None

# def fetch_data_with_token(url, token):
#     try:
#         headers = {"Authorization": f"Token {token}"}
#         response = requests.get(url, headers=headers)
#         response.raise_for_status()
#         return response.json()
#     except requests.exceptions.HTTPError as e:
#         st.error(f"HTTP Error: {e.response.status_code} - {e.response.text}")
#     except Exception as e:
#         st.error(f"Erreur lors de la récupération des données : {str(e)}")
#     return None


# # ✅ Affichage conditionnel
data = fetch_data_with_session("http://127.0.0.1:8000/api/invoices/", session_id)

# if email and token:
#     st.success(f"✅ Connecté en tant que : {email}")
#     data = fetch_data_with_token(api_url, token)
# else:
#     st.warning("🔐 Aucun utilisateur connecté. Lien mal formé ou utilisateur non authentifié.")
#     st.stop()



# Gestion du retour de l'API
if isinstance(data, dict) and "results" in data:
    data = data["results"]

if not isinstance(data, list):
    st.error(f"❌ Format de données inattendu. Liste attendue, reçu : {type(data)}")
    st.stop()

# 🔄 Transformation des données
expanded_data = []

for item in data:
    if not isinstance(item, dict):
        continue

    customer = item.get("customer", {})
    articles = item.get("articles", [])

    if not isinstance(customer, dict) or not isinstance(articles, list):
        continue

    zone = customer.get("zone", "Unknown")
    pays = customer.get("pays", "Unknown")
    customer_type = customer.get("customer_type", "Unknown")
    creator_name = customer.get("creator_name", "Unknown")

    for article in articles:
        if not isinstance(article, dict):
            continue

        expanded_data.append({
            "zone": zone,
            "pays": pays,
            "customer_type": customer_type,
            "creator_name": creator_name,
            "designation": article.get("designation", "Unknown"),
            "quantity": article.get("quantity", 0),
            "unit_price": article.get("unit_price", 0.0),
            "famille": article.get("famille", "Inconnue")
        })

# 📊 Affichage des données
if expanded_data:
    df_selection = pd.DataFrame(expanded_data)
    st.dataframe(df_selection)  # Display in StreamliT


    # df = pd.DataFrame(expanded_data)
    # st.dataframe(df)
else:
    st.warning("Aucune donnée à afficher.")

# # 🧪 Vérifications et visualisations
# if "customer_type" in df.columns and "unit_price" in df.columns:
#     unit_price_by_customer_type = (
#         df.groupby("customer_type").count()[["unit_price"]].sort_values(by="unit_price")
#     )

#     fig = px.bar(
#         unit_price_by_customer_type,
#         x="unit_price",
#         y=unit_price_by_customer_type.index,
#         orientation="h",
#         title="Unit Price par Customer Type",
#         color_discrete_sequence=["#0083B8"] * len(unit_price_by_customer_type),
#         template="plotly_white",
#     )

#     fig.update_layout(
#         plot_bgcolor="rgba(0,0,0,0)",
#         xaxis=dict(showgrid=False)
#     )

#     st.plotly_chart(fig)
# else:
#     st.error("Les colonnes 'customer_type' ou 'unit_price' sont absentes.")


import streamlit as st
import requests
import pandas as pd
import plotly.express as px



import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# Vérifier que l'utilisateur est bien connecté
# email = st.experimental_get_query_params().get('email', [None])[0]
# token = st.experimental_get_query_params().get('token', [None])[0]
# Récupération des paramètres dans l'URL avec st.query_params
# query_params = st.query_params
# email = query_params.get("email", [None])[0]
# token = query_params.get("token", [None])[0]

# # Affichage du contenu brut de la réponse pour débogage
# if email and token:
#     st.success(f"✅ Connecté en tant que : {email}")
#     data = fetch_data_with_token(api_url, token)
#     if data is not None:
#         st.write("Données récupérées : ", data)
#     else:
#         st.warning("Aucune donnée n'a été récupérée.")
# else:
#     st.warning("🔐 Aucun utilisateur connecté. Lien mal formé ou utilisateur non authentifié.")
#     st.stop()

#     # URL de ton API
#     api_url = "http://127.0.0.1:8000/api/invoices/"

#     # Requête API avec token d'authentification
#     def fetch_data_with_token(url, token):
#         try:
#             headers = {"Authorization": f"Token {token}"}
#             response = requests.get(url, headers=headers)
#             response.raise_for_status()
#             return response.json()  # Assure-toi que la réponse est au format JSON
#         except requests.exceptions.HTTPError as e:
#             st.error(f"HTTP Error: {e.response.status_code} - {e.response.text}")
#         except Exception as e:
#             st.error(f"Erreur lors de la récupération des données : {str(e)}")
#         return None

    
#     data = fetch_data_with_token(api_url, token)
    
#     if isinstance(data, dict) and "results" in data:
#         data = data["results"]
#     else:
#         st.warning("Aucune donnée à afficher.")
#         st.stop()

#     expanded_data = []

#     for item in data:
#         if not isinstance(item, dict):
#             continue

#         customer = item.get("customer", {})
#         articles = item.get("articles", [])

#         if not isinstance(customer, dict) or not isinstance(articles, list):
#             continue

#         zone = customer.get("zone", "Unknown")
#         pays = customer.get("pays", "Unknown")
#         customer_type = customer.get("customer_type", "Unknown")
#         creator_name = customer.get("creator_name", "Unknown")

#         for article in articles:
#             if not isinstance(article, dict):
#                 continue

#             expanded_data.append({
#                 "zone": zone,
#                 "pays": pays,
#                 "customer_type": customer_type,
#                 "creator_name": creator_name,
#                 "designation": article.get("designation", "Unknown"),
#                 "quantity": article.get("quantity", 0),
#                 "unit_price": article.get("unit_price", 0.0),
#                 "famille": article.get("famille", "Inconnue")
#             })
    
#     # Affichage des données
#     if expanded_data:
#         df = pd.DataFrame(expanded_data)
#         st.dataframe(df)

#         # Visualisation des données
#         if "customer_type" in df.columns and "unit_price" in df.columns:
#             unit_price_by_customer_type = (
#                 df.groupby("customer_type").count()[["unit_price"]].sort_values(by="unit_price")
#             )

#             fig = px.bar(
#                 unit_price_by_customer_type,
#                 x="unit_price",
#                 y=unit_price_by_customer_type.index,
#                 orientation="h",
#                 title="Unit Price par Customer Type",
#                 color_discrete_sequence=["#0083B8"] * len(unit_price_by_customer_type),
#                 template="plotly_white",
#             )

#             fig.update_layout(
#                 plot_bgcolor="rgba(0,0,0,0)",
#                 xaxis=dict(showgrid=False)
#             )

# #             st.plotly_chart(fig)













############################################################################################LAST
# import streamlit as st
# import requests
# import pandas as pd
# import plotly.express as px

# # Récupérer les paramètres d'URL (email, token)
# query_params = st.query_params
# email = query_params.get("email", [None])[0]
# token = query_params.get("token", [None])[0]

# # URL de l'API
# api_url = "http://127.0.0.1:8000/api/invoices/"

# # Requête API avec token d'authentification
# def fetch_data_with_token(url, token):
#     try:
#         headers = {"Authorization": f"Token {token}"}
#         response = requests.get(url, headers=headers)
#         response.raise_for_status()
#         return response.json()  # Assure-toi que la réponse est au format JSON
#     except requests.exceptions.HTTPError as e:
#         st.error(f"HTTP Error: {e.response.status_code} - {e.response.text}")
#     except Exception as e:
#         st.error(f"Erreur lors de la récupération des données : {str(e)}")
#     return None

# # Vérification des paramètres email et token
# if email and token:
#     st.success(f"✅ Connecté en tant que : {email}")
#     data = fetch_data_with_token(api_url, token)

#     if data is not None:
#         st.write("Données récupérées : ", data)
#     else:
#         st.warning("Aucune donnée n'a été récupérée.")
# else:
#     st.warning("🔐 Aucun utilisateur connecté. Lien mal formé ou utilisateur non authentifié.")
#     st.stop()

# # Vérification du format des données
# if isinstance(data, dict) and "results" in data:
#     data = data["results"]
# else:
#     st.warning("Aucune donnée à afficher.")
#     st.stop()

# # Transformation des données pour affichage
# expanded_data = []
# for item in data:
#     if not isinstance(item, dict):
#         continue

#     customer = item.get("customer", {})
#     articles = item.get("articles", [])

#     if not isinstance(customer, dict) or not isinstance(articles, list):
#         continue

#     zone = customer.get("zone", "Unknown")
#     pays = customer.get("pays", "Unknown")
#     customer_type = customer.get("customer_type", "Unknown")
#     creator_name = customer.get("creator_name", "Unknown")

#     for article in articles:
#         if not isinstance(article, dict):
#             continue

#         expanded_data.append({
#             "zone": zone,
#             "pays": pays,
#             "customer_type": customer_type,
#             "creator_name": creator_name,
#             "designation": article.get("designation", "Unknown"),
#             "quantity": article.get("quantity", 0),
#             "unit_price": article.get("unit_price", 0.0),
#             "famille": article.get("famille", "Inconnue")
#         })

# # Affichage des données dans un dataframe
# if expanded_data:
#     df = pd.DataFrame(expanded_data)
#     st.dataframe(df)

#     # Visualisation des données si les colonnes sont présentes
#     if "customer_type" in df.columns and "unit_price" in df.columns:
#         unit_price_by_customer_type = (
#             df.groupby("customer_type").count()[["unit_price"]].sort_values(by="unit_price")
#         )

#         fig = px.bar(
#             unit_price_by_customer_type,
#             x="unit_price",
#             y=unit_price_by_customer_type.index,
#             orientation="h",
#             title="Unit Price par Customer Type",
#             color_discrete_sequence=["#0083B8"] * len(unit_price_by_customer_type),
#             template="plotly_white",
#         )

#         fig.update_layout(
#             plot_bgcolor="rgba(0,0,0,0)",
#             xaxis=dict(showgrid=False)
#         )

#         st.plotly_chart(fig)
# else:
#     st.warning("Aucune donnée à afficher.")



# # 🧠 Récupération des paramètres dans l'URL avec st.query_params
# query_params = st.query_params
# email = query_params.get("email", [None])[0]
# token = query_params.get("token", [None])[0]

# # URL de ton API
# api_url = "http://127.0.0.1:8000/api/invoices/"

# # 🛰️ Requête API avec token d'authentification
# def fetch_data_with_token(url, token):
#     try:
#         headers = {"Authorization": f"Token {token}"}
#         response = requests.get(url, headers=headers)
#         response.raise_for_status()
#         return response.json()
#     except requests.exceptions.HTTPError as e:
#         st.error(f"HTTP Error: {e.response.status_code} - {e.response.text}")
#     except Exception as e:
#         st.error(f"Erreur lors de la récupération des données : {str(e)}")
#     return None

# # ✅ Affichage conditionnel
# if email and token:
#     st.success(f"✅ Connecté en tant que : {email}")
#     data = fetch_data_with_token(api_url, token)
# else:
#     st.warning("🔐 Aucun utilisateur connecté. Lien mal formé ou utilisateur non authentifié.")
#     st.stop()

# # Gestion du retour de l'API
# if isinstance(data, dict) and "results" in data:
#     data = data["results"]

# if not isinstance(data, list):
#     st.error(f"❌ Format de données inattendu. Liste attendue, reçu : {type(data)}")
#     st.stop()

# # 🔄 Transformation des données
# expanded_data = []

# for item in data:
#     if not isinstance(item, dict):
#         continue

#     customer = item.get("customer", {})
#     articles = item.get("articles", [])

#     if not isinstance(customer, dict) or not isinstance(articles, list):
#         continue

#     zone = customer.get("zone", "Unknown")
#     pays = customer.get("pays", "Unknown")
#     customer_type = customer.get("customer_type", "Unknown")
#     creator_name = customer.get("creator_name", "Unknown")

#     for article in articles:
#         if not isinstance(article, dict):
#             continue

#         expanded_data.append({
#             "zone": zone,
#             "pays": pays,
#             "customer_type": customer_type,
#             "creator_name": creator_name,
#             "designation": article.get("designation", "Unknown"),
#             "quantity": article.get("quantity", 0),
#             "unit_price": article.get("unit_price", 0.0),
#             "famille": article.get("famille", "Inconnue")
#         })

# # 📊 Affichage des données
# if expanded_data:
#     df = pd.DataFrame(expanded_data)
#     st.dataframe(df)
# else:
#     st.warning("Aucune donnée à afficher.")

# # 🧪 Vérifications et visualisations
# if "customer_type" in df.columns and "unit_price" in df.columns:
#     unit_price_by_customer_type = (
#         df.groupby("customer_type").count()[["unit_price"]].sort_values(by="unit_price")
#     )

#     fig = px.bar(
#         unit_price_by_customer_type,
#         x="unit_price",
#         y=unit_price_by_customer_type.index,
#         orientation="h",
#         title="Unit Price par Customer Type",
#         color_discrete_sequence=["#0083B8"] * len(unit_price_by_customer_type),
#         template="plotly_white",
#     )

#     fig.update_layout(
#         plot_bgcolor="rgba(0,0,0,0)",
#         xaxis=dict(showgrid=False)
#     )

#     st.plotly_chart(fig)
# else:
#     st.error("Les colonnes 'customer_type' ou 'unit_price' sont absentes.")












################################3GOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOD
# import requests
# from requests.auth import HTTPBasicAuth
# import pandas as pd
# import streamlit as st

# def fetch_data(endpoint, email=None, password=None):
#     try:
#         auth = HTTPBasicAuth(email, password) if (email and password) else None
#         response = requests.get(endpoint, auth=auth)
#         response.raise_for_status()  # Raises error for 4xx/5xx responses
#         return response.json()
#     except requests.exceptions.HTTPError as e:
#         st.error(f"HTTP Error: {e.response.status_code} - {e.response.text}")
#     except Exception as e:
#         st.error(f"Failed to fetch data: {str(e)}")
#     return None

# # API Configuration
# api_url = "http://127.0.0.1:8000/api/invoices/"

# # Fetch data with email/password authentication
# data = fetch_data(
#     api_url,
#     email="dogodontraore@gmail.com",
#     password="d*"
# )

# if data is None:
#     st.error("❌ Failed to fetch data. Check credentials and API URL.")
#     st.stop()

# # Rest of your processing code remains the same...
# # Handle case where API returns a dict (e.g., {"results": [...]})
# if isinstance(data, dict) and "results" in data:
#     data = data["results"]

# if not isinstance(data, list):
#     st.error(f"Unexpected data format. Expected a list, got {type(data)}")
#     st.stop()

# # Process data into DataFrame
# expanded_data = []

# for item in data:
#     if not isinstance(item, dict):
#         continue

#     customer = item.get("customer", {})
#     articles = item.get("articles", [])

#     if not isinstance(customer, dict) or not isinstance(articles, list):
#         continue

#     zone = customer.get("zone", "Unknown")
#     pays = customer.get("pays", "Unknown")
#     customer_type = customer.get("customer_type", "Unknown")
#     creator_name = customer.get("creator_name", "Unknown")

#     for article in articles:
#         if not isinstance(article, dict):
#             continue

#         expanded_data.append({
#             "zone": zone,
#             "pays": pays,
#             "customer_type": customer_type,
#             "creator_name": creator_name,
#             "designation": article.get("designation", "Unknown"),
#             "quantity": article.get("quantity", 0),
#             "unit_price": article.get("unit_price", 0.0),
#             # Add other fields as needed
#             "famille": article.get("famille", "Inconnue")  # <-- AJOUT ICI

#         })

# if expanded_data:
#     df_selection = pd.DataFrame(expanded_data)
#     st.dataframe(df_selection)  # Display in StreamliT
# else:
#     st.warning("No data available after processing.")


#     # Vérifie les données dans le DataFrame
#     st.write(df_selection.head())  # Affiche les premières lignes pour vérifier les données

#     # Vérifie si les colonnes existent
#     if "customer_type" in df_selection.columns and "unit_price" in df_selection.columns:
#         # Graphique à barres simple pour afficher le 'unit_price' par 'customer_type'
#         unit_price_by_Customer_type = (
#             df_selection.groupby(by=["customer_type"]).count()[["unit_price"]].sort_values(by="unit_price")
#         )
        
#         fig_unit_price = px.bar(
#             unit_price_by_Customer_type,
#             x="unit_price",
#             y=unit_price_by_Customer_type.index,
#             orientation="h",
#             title="unit_price by Customer Type",
#             color_discrete_sequence=["#0083B8"] * len(unit_price_by_Customer_type),
#             template="plotly_white",
#         )

#         fig_unit_price.update_layout(
#             plot_bgcolor="rgba(0,0,0,0)",
#             xaxis=dict(showgrid=False)
#         )

#         # Afficher le graphique dans Streamlit
#         st.plotly_chart(fig_unit_price)
#     else:
#         st.error("Les colonnes 'customer_type' ou 'unit_price' sont manquantes dans les données.")



#   df = pd.DataFrame(data)

#   st.dataframe(df)
import streamlit as st
import requests


import requests
from requests.auth import HTTPBasicAuth
import pandas as pd
import streamlit as st
import requests
import pandas as pd
import streamlit as st
import plotly.express as px

# # # 🔑 Récupérer le sessionid depuis les query params
# # session_id = st.query_params.get("sessionid", [None])[0]

# # if not session_id:
# #     st.warning("Aucun sessionid fourni dans l'URL.")
# #     st.stop()

# # # ✅ Affichage session
# # st.success("Session active")

# # # 🔗 URL de l’API Django avec sessionid
# # api_url = f"http://127.0.0.1:8000/api/user-data/?sessionid={session_id}"

# # # 🔄 Requête vers l’API Django
# # response = requests.get(api_url)

# # if response.status_code != 200:
# #     st.error(f"Erreur API : {response.status_code} - {response.text}")
# #     st.stop()

# # # ✅ Traitement de la réponse
# # data = response.json()

# # # 📌 Vérifie si les données sont dans un champ "invoices" ou directement une liste
# # if isinstance(data, dict) and "invoices" in data:
# #     data = data["invoices"]

# # if not isinstance(data, list):
# #     st.error(f"❌ Format de données inattendu. Liste attendue, reçu : {type(data)}")
# #     st.stop()

# # # 🧩 Transformation en DataFrame
# # expanded_data = []

# # for item in data:
# #     if not isinstance(item, dict):
# #         continue

# #     customer = item.get("customer", {})
# #     articles = item.get("articles", [])

# #     if not isinstance(customer, dict) or not isinstance(articles, list):
# #         continue

# #     zone = customer.get("zone", "Unknown")
# #     pays = customer.get("pays", "Unknown")
# #     customer_type = customer.get("customer_type", "Unknown")
# #     creator_name = customer.get("creator_name", "Unknown")

# #     for article in articles:
# #         if not isinstance(article, dict):
# #             continue

# #         expanded_data.append({
# #             "zone": zone,
# #             "pays": pays,
# #             "customer_type": customer_type,
# #             "creator_name": creator_name,
# #             "designation": article.get("designation", "Unknown"),
# #             "quantity": article.get("quantity", 0),
# #             "unit_price": article.get("unit_price", 0.0),
# #             "famille": article.get("famille", "Inconnue")
# #         })
# import streamlit as st
# import requests
# import pandas as pd
# import plotly.express as px

# # 🔑 1. Récupération automatique du sessionid depuis les paramètres de l'URL
# # query_params = st.query_params
# # session_id = query_params.get("sessionid", [None])[0]

# sessionid = st.query_params.get("sessionid", [None])[0]

# if not sessionid:
#     st.error("❌ Aucun sessionid fourni. Veuillez vous connecter.")
#     st.stop()

# api_url = f"http://127.0.0.1:8000/api/user-data/?sessionid={sessionid}"
# response = requests.get(api_url)

# if response.status_code == 200:
#     st.success("✅ Données récupérées avec succès")
#     st.write(response.json())
# else:
#     st.error("🚫 Échec de la récupération des données utilisateur.")
# # # 🧠 2. Vérification
# # if not session_id:
# #     st.warning("❌ Aucun sessionid fourni dans l'URL.")
# #     st.stop()

# # # 🌐 3. Construction automatique de l'URL d'API avec sessionid
# # api_url = f"http://127.0.0.1:8000/api/user-data/?sessionid={session_id}"
# # st.write(f"🔗 URL de l'API : `{api_url}`")  # Affichage à des fins de debug

# # # 📦 4. Appel API
# # response = requests.get(api_url)

# # if response.status_code == 200:
# #     data = response.json()
# #     invoices = data.get("invoices", [])
# #     st.success(f"✅ {len(invoices)} factures récupérées")
# # else:
# #     st.error(f"Erreur {response.status_code} : {response.text}")
# #     st.stop()

# # 🔄 5. Transformation en DataFrame
# expanded_data = []

# for invoice in invoices:
#     customer = invoice.get("customer", {})
#     articles = invoice.get("articles", [])

#     for article in articles:
#         expanded_data.append({
#             "zone": customer.get("zone"),
#             "pays": customer.get("pays"),
#             "customer_type": customer.get("customer_type"),
#             "creator_name": customer.get("creator_name"),
#             "designation": article.get("designation"),
#             "quantity": article.get("quantity"),
#             "unit_price": article.get("unit_price"),
#             "famille": article.get("famille"),
#         })

# # 📊 6. Affichage et visualisation
# if expanded_data:
#     df = pd.DataFrame(expanded_data)
#     st.dataframe(df)

#     if "customer_type" in df.columns and "unit_price" in df.columns:
#         chart_data = df.groupby("customer_type")["unit_price"].count().reset_index(name="count")
#         fig = px.bar(chart_data, x="count", y="customer_type", orientation="h", title="Factures par type de client")
#         st.plotly_chart(fig)
# else:
#     st.warning("Aucune donnée à afficher.")


# # # 🖼️ Affichage
# # if expanded_data:
# #     df_selection = pd.DataFrame(expanded_data)
# #     st.dataframe(df_selection)

# #     if "customer_type" in df_selection.columns and "unit_price" in df_selection.columns:
# #         unit_price_by_Customer_type = (
# #             df_selection.groupby(by=["customer_type"]).count()[["unit_price"]].sort_values(by="unit_price")
# #         )

# #         fig_unit_price = px.bar(
# #             unit_price_by_Customer_type,
# #             x="unit_price",
# #             y=unit_price_by_Customer_type.index,
# #             orientation="h",
# #             title="unit_price by Customer Type",
# #             color_discrete_sequence=["#0083B8"] * len(unit_price_by_Customer_type),
# #             template="plotly_white",
# #         )

# #         fig_unit_price.update_layout(
# #             plot_bgcolor="rgba(0,0,0,0)",
# #             xaxis=dict(showgrid=False)
# #         )

# #         st.plotly_chart(fig_unit_price)
# #     else:
# #         st.warning("Colonnes manquantes pour la visualisation.")
# # else:
# #     st.warning("Aucune donnée disponible après traitement.")














# def fetch_data(endpoint, email=None, password=None):
#     try:
#         auth = HTTPBasicAuth(email, password) if (email and password) else None
#         response = requests.get(endpoint, auth=auth)
#         response.raise_for_status()  # Raises error for 4xx/5xx responses
#         return response.json()
#     except requests.exceptions.HTTPError as e:
#         st.error(f"HTTP Error: {e.response.status_code} - {e.response.text}")
#     except Exception as e:
#         st.error(f"Failed to fetch data: {str(e)}")
#     return None

# # API Configuration
# api_url = "http://127.0.0.1:8000/api/invoices/"
# # 🔑 Récupérer le sessionid depuis les query params
# session_id = st.query_params.get("sessionid", [None])[0]

# if session_id:
#     st.success("Session active")
#     # 🛰️ Requête vers ton API Django
#     api_url = f"http://127.0.0.1:8000/api/user-data/?sessionid={session_id}"
#     response = requests.get(api_url)
    
#     if response.status_code == 200:
#         data = response.json()
#         st.write("📦 Données récupérées :", data)
#     else:
#         st.error(f"Erreur API : {response.status_code} - {response.text}")
# else:
#     st.warning("Aucun sessionid fourni dans l'URL.")
# # Fetch data with email/password authentication
# data = fetch_data(
#     api_url,
#     email="dogodontraore@gmail.com",
#     password="d*"
# )

# if data is None:
#     st.error("❌ Failed to fetch data. Check credentials and API URL.")
#     st.stop()

# # Rest of your processing code remains the same...
# # Handle case where API returns a dict (e.g., {"results": [...]})
# if isinstance(data, dict) and "results" in data:
#     data = data["results"]

# if not isinstance(data, list):
#     st.error(f"Unexpected data format. Expected a list, got {type(data)}")
#     st.stop()

# # Process data into DataFrame
# expanded_data = []

# for item in data:
#     if not isinstance(item, dict):
#         continue

#     customer = item.get("customer", {})
#     articles = item.get("articles", [])

#     if not isinstance(customer, dict) or not isinstance(articles, list):
#         continue

#     zone = customer.get("zone", "Unknown")
#     pays = customer.get("pays", "Unknown")
#     customer_type = customer.get("customer_type", "Unknown")
#     creator_name = customer.get("creator_name", "Unknown")

#     for article in articles:
#         if not isinstance(article, dict):
#             continue

#         expanded_data.append({
#             "zone": zone,
#             "pays": pays,
#             "customer_type": customer_type,
#             "creator_name": creator_name,
#             "designation": article.get("designation", "Unknown"),
#             "quantity": article.get("quantity", 0),
#             "unit_price": article.get("unit_price", 0.0),
#             # Add other fields as needed
#             "famille": article.get("famille", "Inconnue")  # <-- AJOUT ICI

#         })

# if expanded_data:
#     df_selection = pd.DataFrame(expanded_data)
#     st.dataframe(df_selection)  # Display in StreamliT
# else:
#     st.warning("No data available after processing.")


#     # Vérifie les données dans le DataFrame
#     st.write(df_selection.head())  # Affiche les premières lignes pour vérifier les données

#     # Vérifie si les colonnes existent
#     if "customer_type" in df_selection.columns and "unit_price" in df_selection.columns:
#         # Graphique à barres simple pour afficher le 'unit_price' par 'customer_type'
#         unit_price_by_Customer_type = (
#             df_selection.groupby(by=["customer_type"]).count()[["unit_price"]].sort_values(by="unit_price")
#         )
        
#         fig_unit_price = px.bar(
#             unit_price_by_Customer_type,
#             x="unit_price",
#             y=unit_price_by_Customer_type.index,
#             orientation="h",
#             title="unit_price by Customer Type",
#             color_discrete_sequence=["#0083B8"] * len(unit_price_by_Customer_type),
#             template="plotly_white",
#         )

#         fig_unit_price.update_layout(
#             plot_bgcolor="rgba(0,0,0,0)",
#             xaxis=dict(showgrid=False)
#         )

#         # Afficher le graphique dans Streamlit
#         st.plotly_chart(fig_unit_price)
#     else:
#         st.error("Les colonnes 'customer_type' ou 'unit_price' sont manquantes dans les données.")




#########################################################################################################################

# import requests
# from requests.auth import HTTPBasicAuth
# import pandas as pd
# import streamlit as st

# def fetch_data(endpoint, email=None, password=None):
#     try:
#         auth = HTTPBasicAuth(email, password) if (email and password) else None
#         response = requests.get(endpoint, auth=auth)
#         response.raise_for_status()  # Raises error for 4xx/5xx responses
#         return response.json()
#     except requests.exceptions.HTTPError as e:
#         st.error(f"HTTP Error: {e.response.status_code} - {e.response.text}")
#     except Exception as e:
#         st.error(f"Failed to fetch data: {str(e)}")
#     return None

# # API Configuration
# api_url = "http://127.0.0.1:8000/api/invoices/"

# # Fetch data with email/password authentication
# data = fetch_data(
#     api_url,
#     email="dogodontraore@gmail.com",
#     password="d*"
# )

# if data is None:
#     st.error("❌ Failed to fetch data. Check credentials and API URL.")
#     st.stop()

# # Process the API data into a DataFrame
# expanded_data = []

# for item in data:
#     if not isinstance(item, dict):
#         continue
    
#     customer = item.get("customer", {})
#     articles = item.get("articles", [])
    
#     if not isinstance(customer, dict) or not isinstance(articles, list):
#         continue
    
#     zone = customer.get("zone", "Unknown")
#     pays = customer.get("pays", "Unknown")
#     customer_type = customer.get("customer_type", "Unknown")
#     creator_name = customer.get("creator_name", "Unknown")
    
#     for article in articles:
#         if not isinstance(article, dict):
#             continue
        
#         expanded_data.append({
#             "zone": zone,
#             "pays": pays,
#             "customer_type": customer_type,
#             "creator_name": creator_name,
#             "designation": article.get("designation", "Unknown"),
#             "quantity": article.get("quantity", 0),
#             "unite": article.get("unite", "Unknown"),
#             "unit_price": article.get("unit_price", 0.0),
#             "famille": article.get("famille", "Unknown"),
#             "remise": article.get("remise", 0.0),
#             "tva": article.get("tva", 0.0)
#         })

# # Create DataFrame
# if expanded_data:
#     df_selection = pd.DataFrame(expanded_data)
# else:
#     st.error("No data available after processing.")
#     st.stop()

# # Now you can use df_selection safely
# st.title("Invoice Data Dashboard")
# st.dataframe(df_selection)

# # Example usage of df_selection
# zone_filter = st.selectbox(
#     "Select Zone:",
#     options=df_selection["zone"].unique()
# )

# filtered_data = df_selection[df_selection["zone"] == zone_filter]
# st.write(f"Showing data for zone: {zone_filter}")
# st.dataframe(filtered_data)



import streamlit as st
import requests
import pandas as pd
from datetime import datetime, timedelta

# # Configuration
# DJANGO_AUTH_URL = "http://localhost:8000/api/auth/login/"  # Votre endpoint Django
# API_DATA_URL = "http://localhost:8000/api/invoices/"  # Endpoint des données

# # Gestion de l'authentification
# def django_login(email, password):
#     """Authentification via Django REST"""
#     try:
#         response = requests.post(
#             DJANGO_AUTH_URL,
#             json={"email": email, "password": password}
#         )
#         if response.status_code == 200:
#             return response.json().get('token')  # JWT token
#         return None
#     except Exception as e:
#         st.error(f"Erreur de connexion: {str(e)}")
#         return None

# # Récupération des données sécurisée
# def fetch_user_data(token):
#     """Récupère les données avec le token JWT"""
#     headers = {"Authorization": f"Bearer {token}"}
#     try:
#         response = requests.get(API_DATA_URL, headers=headers)
#         response.raise_for_status()
#         return response.json()
#     except Exception as e:
#         st.error(f"Erreur de récupération: {str(e)}")
#         return None

# # Interface Streamlit
# def main():
#     st.title("Tableau de Bord Intelligent")

#     # Gestion de session
#     if 'auth_token' not in st.session_state:
#         st.session_state.auth_token = None
#         st.session_state.user_email = None

#     # Formulaire de connexion
#     if not st.session_state.auth_token:
#         with st.form("Connexion"):
#             email = st.text_input("Email")
#             password = st.text_input("Mot de passe", type="password")
            
#             if st.form_submit_button("Se connecter"):
#                 token = django_login(email, password)
#                 if token:
#                     st.session_state.auth_token = token
#                     st.session_state.user_email = email
#                     st.success("Connexion réussie!")
#                     st.experimental_rerun()
#                 else:
#                     st.error("Identifiants incorrects")
#         return

#     # Interface utilisateur connecté
#     st.sidebar.markdown(f"**Connecté:** {st.session_state.user_email}")
#     if st.sidebar.button("Déconnexion"):
#         st.session_state.clear()
#         st.experimental_rerun()
#         return

#     # Actualisation automatique
#     refresh_interval = timedelta(minutes=5)
#     last_refresh = st.session_state.get('last_refresh', datetime.min)
    
#     if datetime.now() - last_refresh > refresh_interval:
#         st.session_state.last_refresh = datetime.now()
#         st.rerun()

#     # Récupération des données
#     data = fetch_user_data(st.session_state.auth_token)
    
#     if not data:
#         st.warning("Aucune donnée disponible")
#         return

#     # Traitement des données (exemple)
#     df = pd.DataFrame(data)
#     st.dataframe(df)

#     # Filtres dynamiques
#     if 'zone' in df.columns:
#         selected_zone = st.selectbox(
#             "Filtrer par zone:",
#             options=df['zone'].unique()
#         )
#         st.dataframe(df[df['zone'] == selected_zone])

# if __name__ == "__main__":
#     main()

import streamlit as st
import requests
import pandas as pd
from datetime import datetime
import streamlit as st
import requests
import pandas as pd
from datetime import datetime

# # Configuration
# DJANGO_URL = "http://localhost:8000"
# SESSION_COOKIE_NAME = "sessionid"

# def get_django_session():
#     """Récupère le cookie de session depuis les paramètres de requête"""
#     query_params = st.query_params
#     return query_params.get(SESSION_COOKIE_NAME, [None])[0]
# st.write("🔐 Session ID reçue :", session_id)

# def fetch_user_data(session_id):
#     """Récupère les données utilisateur avec la session Django"""
#     cookies = {SESSION_COOKIE_NAME: session_id}
#     try:
#         response = requests.get(
#             f"{DJANGO_URL}/api/user_data/",
#             cookies=cookies
#         )
#         if response.status_code == 200:
#             return response.json()
#         return None
#     except Exception as e:
#         st.error(f"Erreur: {str(e)}")
#         return None

# def process_user_data(user_data):
#     """Transforme les données utilisateur en DataFrame"""
#     if not user_data or 'invoices' not in user_data:
#         return None
    
#     df = pd.DataFrame(user_data['invoices'])
    
#     # Assure que toutes les colonnes nécessaires existent
#     required_columns = ['zone', 'pays', 'customer_type', 'designation', 'quantity']
#     for col in required_columns:
#         if col not in df.columns:
#             df[col] = None  # ou une valeur par défaut appropriée
    
#     return df

# def main():
#         # Actualisation automatique toutes les 5 minutes
#     if 'last_update' not in st.session_state:
#         st.session_state.last_update = datetime.now()

#     if (datetime.now() - st.session_state.last_update).seconds > 300:
#         st.session_state.last_update = datetime.now()
#         st.rerun()
#     st.title("Tableau de Bord Personnel")

#     # Vérification de session
#     session_id = get_django_session()

#     # Récupération des données
#     user_data = fetch_user_data(session_id)

#     # Traitement des données
#     df_selection = process_user_data(user_data)
    
#     if df_selection is None:
#         st.warning("Aucune donnée disponible")
#         return

#     # Affichage des données
#     st.sidebar.markdown(f"""
#     **Utilisateur connecté:**  
#     {user_data.get('email')}  
#     {user_data.get('username')}
#     """)

#     # Vérification que la colonne 'zone' existe avant de l'utiliser
#     if 'zone' in df_selection.columns:
#         zones = df_selection['zone'].unique()
#         selected_zone = st.selectbox(
#             "Filtrer par zone:",
#             options=zones
#         )
#         filtered_data = df_selection[df_selection['zone'] == selected_zone]
#         st.dataframe(filtered_data)
#     else:
#         st.dataframe(df_selection)
#         st.warning("La colonne 'zone' n'est pas disponible dans les données")

# if __name__ == "__main__":
#     main()












# import streamlit as st
# import pandas as pd
# import requests

# DJANGO_URL = "http://localhost:8000"
# SESSION_COOKIE_NAME = "sessionid"

# def get_django_session():
#     """Récupère la session depuis l'URL"""
#     query_params = st.query_params
#     return query_params.get(SESSION_COOKIE_NAME, [None])[0]

# def fetch_user_data(session_id):
#     """Appelle l’API Django avec la session"""
#     cookies = {SESSION_COOKIE_NAME: session_id}
#     try:
#         response = requests.get(f"{DJANGO_URL}/api/invoices/", cookies=cookies)
#         if response.status_code == 200:
#             return response.json()
#         else:
#             st.error(f"⚠️ Erreur de session ({response.status_code}) : {response.text}")
#             return None
#     except Exception as e:
#         st.error(f"❌ Exception : {str(e)}")
#         return None

# def main():
#     st.title("📊 Dashboard de Facturation")

#     # Étape 1 : récupérer sessionid
#     session_id = get_django_session()
#     if not session_id:
#         st.warning("🔒 Session non détectée. Veuillez accéder via Django.")
#         st.stop()

#     # Étape 2 : récupérer les données utilisateur
#     user_data = fetch_user_data(session_id)
#     if not user_data:
#         st.warning("Impossible de récupérer les données utilisateur.")
#         st.stop()

#     # Étape 3 : construire un DataFrame
#     df = pd.DataFrame(user_data["invoices"])
#     st.success(f"Bienvenue {user_data['username']} !")

#     # Étape 4 : affichage
#     st.subheader("Aperçu des factures")
#     st.dataframe(df)

#     # Graphe exemple
#     if "designation" in df.columns:
#         st.subheader("Total par produit")
#         chart = df.groupby("designation")["quantity"].sum().plot(kind="bar", title="Total des quantités par produit")
#         st.pyplot(chart.figure)

# if __name__ == "__main__":
#     main()













































#remove default theme
theme_plotly = None # None or streamlit

 
# CSS Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

# #load excel file
# df=pd.read_excel('data.xlsx', sheet_name='Sheet1')


#2. switcher
st.sidebar.header("Please Filter Here:")
zone= st.sidebar.multiselect(
    "Select the zone:",
    options=df_selection["zone"].unique(),
    default=df_selection["zone"].unique()
)
pays = st.sidebar.multiselect(
    "Select the pays:",
    options=df_selection["pays"].unique(),
    default=df_selection["pays"].unique(),
)
customer_type= st.sidebar.multiselect(
    "Select the customer_type:",
    options=df_selection["customer_type"].unique(),
    default=df_selection["customer_type"].unique()
     
    
)
df_selection = df_selection.query(
    "zone == @zone & pays ==@pays & customer_type == @customer_type"
)

#method/function

def HomePage():
  #1. print dataframe
 with st.expander("🧭 My database"):
  #st.dataframe(df_selection,use_container_width=True)
  shwdata = st.multiselect('Filter :', df_selection.columns, default=[])
  st.dataframe(df_selection[shwdata],use_container_width=True)

#  #2. compute top Analytics
 
#  total_unit_price = float(df_selection.columns['unit_price'].sum())
#  unit_price_mode = float(df_selection.columns['unit_price'].mode())
#  unit_price_mean = float(df_selection.columns['unit_price'].mean())
#  unit_price_median= float(df_selection.columns['unit_price'].median()) 
#  rating = float(df_selection.columns['Rating'].sum())

#  #3. columns
#  total1,total2,total3,total4,total5 = st.columns(5,gap='large')
#  with total1:

#     st.info('Total unit_price', icon="🔍")
#     st.metric(label = 'sum TZS', value= f"{total_unit_price:,.0f}")
    
#  with total2:
#     st.info('Most frequently', icon="🔍")
#     st.metric(label='Mode TZS', value=f"{unit_price_mode:,.0f}")

#  with total3:
#     st.info('unit_price Average', icon="🔍")
#     st.metric(label= 'Mean TZS',value=f"{unit_price_mean:,.0f}")

#  with total4:
#     st.info('unit_price Marging', icon="🔍")
#     st.metric(label='Median TZS',value=f"{unit_price_median:,.0f}")

#  with total5:
#     st.info('Ratings', icon="🔍")
#     st.metric(label='Rating',value=numerize(rating),help=f"""Total rating: {rating}""")
    
#  st.markdown("""---""")


# Assurez-vous que df_selection est bien défini, sinon ça pourrait entraîner une erreur
# Par exemple, vous pouvez le récupérer d'une API ou d'un fichier, comme dans votre code précédent


# # Vérifie si les colonnes existent
# if "customer_type" in df_selection.columns and "unit_price" in df_selection.columns:
#     # Graphique à barres simple pour afficher le 'unit_price' par 'customer_type'
#     unit_price_by_Customer_type = (
#         df_selection.groupby(by=["customer_type"]).count()[["unit_price"]].sort_values(by="unit_price")
#     )
    
#     fig_unit_price = px.bar(
#         unit_price_by_Customer_type,
#         x="unit_price",
#         y=unit_price_by_Customer_type.index,
#         orientation="h",
#         title="unit_price by Customer Type",
#         color_discrete_sequence=["#0083B8"] * len(unit_price_by_Customer_type),
#         template="plotly_white",
#     )

#     fig_unit_price.update_layout(
#         plot_bgcolor="rgba(0,0,0,0)",
#         xaxis=dict(showgrid=False)
#     )

#     # Afficher le graphique dans Streamlit
#     st.plotly_chart(fig_unit_price)
# else:
#     st.error("Les colonnes 'customer_type' ou 'unit_price' sont manquantes dans les données.")


# 2. Compute top Analytics
# Nettoyer la colonne 'unit_price' pour remplacer les caractères non numériques et convertir en float
df_selection['unit_price'] = pd.to_numeric(df_selection['unit_price'], errors='coerce')
# Nettoyer la colonne 'remise' pour remplacer les caractères non numériques et convertir en float
# df_selection['remise'] = pd.to_numeric(df_selection['remise'], errors='coerce')

# Maintenant, vous pouvez calculer la somme, la moyenne, la médiane, etc.
total_unit_price = float(df_selection['unit_price'].sum())  # Correct: accédez directement à la colonne 'unit_price'
unit_price_mode = float(df_selection['unit_price'].mode()[0])  # Correct: accédez à la première valeur de la mode
unit_price_mean = float(df_selection['unit_price'].mean())  # Correct: calcul de la moyenne
unit_price_median = float(df_selection['unit_price'].median())  # Correct: calcul de la médiane
# remise = float(df_selection['remise'].sum())  # Correct: somme des évaluations

# Affichage des résultats
# total1, total2, total3, total4, total5 = st.columns(5, gap='large')
total1, total2, total3, total4 = st.columns(4, gap='large')

with total1:
    st.info('Total unit_price', icon="🔍")
    st.metric(label='sum TZS', value=f"{total_unit_price:,.0f}")

with total2:
    st.info('Most frequently', icon="🔍")
    st.metric(label='Mode TZS', value=f"{unit_price_mode:,.0f}")

with total3:
    st.info('unit_price Average', icon="🔍")
    st.metric(label='Mean TZS', value=f"{unit_price_mean:,.0f}")

with total4:
    st.info('unit_price Margin', icon="🔍")
    st.metric(label='Median TZS', value=f"{unit_price_median:,.0f}")

# with total5:
#     st.info('remises', icon="🔍")
#     st.metric(label='remise', value=numerize(remise), help=f"Total remise: {remise}")

st.markdown("""---""")

# # 3. Columns for displaying the metrics
# total1, total2, total3, total4, total5 = st.columns(5, gap='large')

# with total1:
#     st.info('Total unit_price', icon="🔍")
#     st.metric(label='sum TZS', value=f"{total_unit_price:,.0f}")

# with total2:
#     st.info('Most frequently', icon="🔍")
#     st.metric(label='Mode TZS', value=f"{unit_price_mode:,.0f}")

# with total3:
#     st.info('unit_price Average', icon="🔍")
#     st.metric(label='Mean TZS', value=f"{unit_price_mean:,.0f}")

# with total4:
#     st.info('unit_price Margin', icon="🔍")
#     st.metric(label='Median TZS', value=f"{unit_price_median:,.0f}")

# # with total5:
# #     st.info('remises', icon="🔍")
# #     st.metric(label='remise', value=numerize(remise), help=f"Total remise: {remise}")

# st.markdown("""---""")


 #graphs
 
def Graphs():
 total_unit_prices = int(df_selection["unit_price"].sum())
#  average_rating = round(df_selection["Rating"].mean(), 1)
#  star_rating = ":star:" * int(round(average_rating, 0))
 average_unit_price = round(df_selection["unit_price"].mean(), 2)

# #1. simple bar graph
#  Price_by_ArticleType = (
#     df_selection.groupby(by=["ArticleType"]).count()[["Price"]].sort_values(by="Price")
#  )
#  fig_Price = px.bar(
#     Price_by_ArticleType,
#     x="Price",
#     y=Price_by_ArticleType.index,
#     orientation="h",
#     title="Price by Business Type",
#     color_discrete_sequence=["#0083B8"] * len(Price_by_ArticleType),
#     template="plotly_white",
#  )

#  fig_Price.update_layout(
#     plot_bgcolor="rgba(0,0,0,0)",
#     xaxis=(dict(showgrid=False))
#  )

# import plotly.express as px
# import streamlit as st

# # Graphique à barres pour afficher le 'Price' par 'customer_type'
# if "customer_type" in df_selection.columns and "unit_price" in df_selection.columns:
#     Price_by_Customer_type = (
#         df_selection.groupby(by=["customer_type"]).count()[["unit_price"]].sort_values(by="unit_price")
#     )
    
#     fig_Price = px.bar(
#         Price_by_Customer_type,
#         x="unit_price",
#         y=Price_by_Customer_type.index,
#         orientation="h",
#         title="Price by Customer Type",
#         color_discrete_sequence=["#0083B8"] * len(Price_by_Customer_type),
#         template="plotly_white",
#     )
    
#     fig_Price.update_layout(
#         plot_bgcolor="rgba(0,0,0,0)",  # Fond transparent
#         xaxis=dict(showgrid=False)  # Masquer les grilles de l'axe X
#     )
    
#     st.plotly_chart(fig_Price)  # Afficher le graphique dans Streamlit


# # Graphique linéaire pour afficher le 'unit_price' par 'pays'
# if "pays" in df_selection.columns and "unit_price" in df_selection.columns:
#     Price_by_state = df_selection.groupby(by=["pays"]).count()[["unit_price"]]
    
#     fig_state = px.line(
#         Price_by_state,
#         x=Price_by_state.index,
#         y="unit_price",
#         title="unit_price by Region",
#         color_discrete_sequence=["#0083B8"] * len(Price_by_state),
#         template="plotly_white",
#     )
    
#     fig_state.update_layout(
#         xaxis=dict(tickmode="linear"),
#         plot_bgcolor="rgba(0,0,0,0)",  # Fond transparent
#         yaxis=dict(showgrid=False),  # Masquer les grilles de l'axe Y
#     )
    
#     st.plotly_chart(fig_state)  # Afficher le graphique dans Streamlit

#  #pie chart

# left_column, right_column,center = st.columns(3)
# left_column.plotly_chart(fig_state, use_container_width=True)
# right_column.plotly_chart(fig_Price, use_container_width=True)
# with center:
#   fig = px.pie(df_selection, values='famille', names='pays', title='Regions by Ratings')
#   fig.update_layout(legend_title="Famille", legend_y=0.9)
#   fig.update_traces(textinfo='percent+label', textposition='inside')
#   st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# Graphique linéaire pour afficher le 'unit_price' par 'pays'
if "pays" in df_selection.columns and "unit_price" in df_selection.columns:
    Price_by_state = df_selection.groupby(by=["pays"]).count()[["unit_price"]]
    
    fig_state = px.line(
        Price_by_state,
        x=Price_by_state.index,
        y="unit_price",
        title="unit_price by Region",
        color_discrete_sequence=["#0083B8"] * len(Price_by_state),
        template="plotly_white",
    )
    
    fig_state.update_layout(
        xaxis=dict(tickmode="linear"),
        plot_bgcolor="rgba(0,0,0,0)",  # Fond transparent
        yaxis=dict(showgrid=False),  # Masquer les grilles de l'axe Y
    )
    

# Graphique à barres pour afficher le 'Price' par 'customer_type'
if "customer_type" in df_selection.columns and "unit_price" in df_selection.columns:
    Price_by_Customer_type = (
        df_selection.groupby(by=["customer_type"]).count()[["unit_price"]].sort_values(by="unit_price")
    )
    
    fig_Price = px.bar(
        Price_by_Customer_type,
        x="unit_price",
        y=Price_by_Customer_type.index,
        orientation="h",
        title="Price by Customer Type",
        color_discrete_sequence=["#0083B8"] * len(Price_by_Customer_type),
        template="plotly_white",
    )
    
    fig_Price.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",  # Fond transparent
        xaxis=dict(showgrid=False)  # Masquer les grilles de l'axe X
    )
    

left_column, right_column,center = st.columns(3)
left_column.plotly_chart(fig_state, use_container_width=True)
right_column.plotly_chart(fig_Price, use_container_width=True)
# Graphique circulaire (pie chart)
# with center:
#     if "pays" in df_selection.columns and "famille" in df_selection.columns:

#         fig = px.pie(df_selection, values='famille', names='pays', title='Regions by Ratings')
#         fig.update_layout(legend_title="Regions", legend_y=0.9)
#         fig.update_traces(textinfo='percent+label', textposition='inside')
#         st.plotly_chart(fig, use_container_width=True, theme=theme_plotly, key="fig_pie_1")  # Ajout d'un key unique

with center:
    if "pays" in df_selection.columns and "famille" in df_selection.columns:
        # Compter les occurrences de chaque 'famille' par 'pays'
        famille_count = df_selection.groupby('pays')['famille'].count().reset_index()

        # Créer le graphique circulaire avec les valeurs comptées
        fig = px.pie(famille_count, values='famille', names='pays', title='Regions by Ratings')
        fig.update_layout(legend_title="Regions", legend_y=0.9)
        fig.update_traces(textinfo='percent+label', textposition='inside')
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly, key="fig_pie_1")





















# #2. simple line graph------------------
#  unit_price_by_state = df.groupby(by=["pays"]).count()[["unit_price"]]
#  fig_state = px.line(
#     unit_price_by_state,
#     x=unit_price_by_state.index,
#      orientation="v",
#     y="unit_price",
#     title="unit_price by Region ",
#     color_discrete_sequence=["#0083B8"] * len(unit_price_by_state),
#     template="plotly_white",
#  )
#  fig_state.update_layout(
#     xaxis=dict(tickmode="linear"),
#     plot_bgcolor="rgba(0,0,0,0)",
#     yaxis=(dict(showgrid=False)),
#  )

#  left_column, right_column,center = st.columns(3)
#  left_column.plotly_chart(fig_state, use_container_width=True)
#  right_column.plotly_chart(fig_unit_price, use_container_width=True)

#  #pie chart
#  with center:
#   fig = px.pie(df_selection, values='Rating', names='State', title='Regions by Ratings')
#   fig.update_layout(legend_title="Regions", legend_y=0.9)
#   fig.update_traces(textinfo='percent+label', textposition='inside')
#   st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)





#################################################################################################################################

# #1. simple bar graph
#  Price_by_Customer_type = (
#     df_selection.groupby(by=["customer_type"]).count()[["Price"]].sort_values(by="Price")
#  )
#  fig_Price = px.bar(
#     Price_by_Customer_type,
#     x="Price",
#     y=Price_by_Customer_type.index,
#     orientation="h",
#     title="Price by Customer Type",
#     color_discrete_sequence=["#0083B8"] * len(Price_by_Customer_type),
#     template="plotly_white",
#  )

#  fig_Price.update_layout(
#     plot_bgcolor="rgba(0,0,0,0)",
#     xaxis=(dict(showgrid=False))
#  )

# #2. simple line graph------------------
#  Price_by_state = df_selection.groupby(by=["State"]).count()[["Price"]]
#  fig_state = px.line(
#     Price_by_state,
#     x=Price_by_state.index,
#      orientation="v",
#     y="Price",
#     title="Price by Region ",
#     color_discrete_sequence=["#0083B8"] * len(Price_by_state),
#     template="plotly_white",
#  )
#  fig_state.update_layout(
#     xaxis=dict(tickmode="linear"),
#     plot_bgcolor="rgba(0,0,0,0)",
#     yaxis=(dict(showgrid=False)),
#  )

#  left_column, right_column,center = st.columns(3)
#  left_column.plotly_chart(fig_state, use_container_width=True)
#  right_column.plotly_chart(fig_Price, use_container_width=True)

#  #pie chart
#  with center:
#   fig = px.pie(df_selection, values='Rating', names='State', title='Regions by Ratings')
#   fig.update_layout(legend_title="Regions", legend_y=0.9)
#   fig.update_traces(textinfo='percent+label', textposition='inside')
#   st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
#################################################################################################################################













#-----PROGRESS BAR-----

def ProgressBar():
  st.markdown("""<style>.stProgress > div > div > div > div { background-image: linear-gradient(to right, #99ff99 , #FFFF00)}</style>""",unsafe_allow_html=True,)
  target=3000000000
  current=df_selection['unit_price'].sum()
  percent=round((current/target*100))
  my_bar = st.progress(0)

  if percent>100:
    st.subheader("Target 100 complited")
  else:
   st.write("you have ", percent, " % " ," of ", (format(target, ',d')), " TZS")
   for percent_complete in range(percent):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1,text="Target percentage")

#-----SIDE BAR-----
 
def sideBar():
 with st.sidebar:
    selected=option_menu(
        menu_title="Menu",
         #menu_title=None,
        options=["Home","Progress"],
        icons=["house","eye"],
        menu_icon="cast", #option
        default_index=0, #option
        )
 if selected=="Home":   
    try:
     HomePage()
     Graphs()
    except:
        st.warning("one or more options are mandatory ! ")
     
    
 if selected=="Progress":
   try:
    ProgressBar()
    Graphs()
   except:
    st.warning("one or more options are mandatory ! ")
 
#print side bar
sideBar()

footer="""<style>
 

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
height:5%;
bottom: 0;
width: 100%;
background-color: #243946;
color: white;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with  ❤ by <a style='display: block; text-align: center;' href="https://www.heflin.dev/" target="_blank">Samir.s.s</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)




















































# Location	State	Region	Price	Billing	ArticleType	Payment_a_time	Flood	Rating	Location	State	Region	Price	Billing	ArticleName	Payment_a_time	Flood	Rating	Location	State	Region	Price	Billing	ArticleType
