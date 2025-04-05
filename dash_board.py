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





import plotly.express as px
import pandas as pd
import streamlit as st

data = fetch_data(api_url)
# Assure-toi que df est bien défini
if data:
    expanded_data = []  # Liste pour stocker toutes les lignes étendues(depuis les superlignes INVOICE)

    for item in data:
        # Accède aux informations du 'customer'
        zone = item['customer']['zone']
        pays = item['customer']['pays']
        customer_type = item['customer']['customer_type']
        creator_name = item['customer']['creator_name']

        # Accède aux informations de la liste 'articles'
        for article in item['articles']: 
            article_details = {
                'zone': zone,  # Ajoute l'information sur la zone
                'pays': pays,  # Ajoute l'information sur le pays
                'customer_type': customer_type,  # Ajoute le type de client
                'creator_name': creator_name,  # Ajoute le nom du créateur
                'designation': article['designation'],
                'quantity': article['quantity'],
                'unite': article['unite'],
                'unit_price': article['unit_price'],
                'famille': article['famille'],
                'remise': article['remise'],
                'tva': article['tva']
            }
            expanded_data.append(article_details)  # Ajoute chaque article à la liste

    # Crée un DataFrame à partir de la liste 'expanded_data'
    df_selection = pd.DataFrame(expanded_data)

    # # Vérifie les données dans le DataFrame
    # st.write(df_selection.head())  # Affiche les premières lignes pour vérifier les données

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



#   df = pd.DataFrame(data)

#   st.dataframe(df)
  












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
