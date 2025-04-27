from django.urls import path,include
from . import views
from .views import export_invoices_csv,AddArticleView
from .views import creer_facture_etape1, creer_facture_etape2,download_pdf,download_csv,client_list,services,load_content,formules, plus_loin,base_customers,CustomerListView,EditCustomerView,DeleteCustomerView,download_csv,download_pdf #,liste_avoirs

from .views import *






#SERIALIZERS DATASET!!
from .views import InvoiceDetailAPIView,InvoiceListAPIView ,redirect_to_dashboard #creer_avoir_etape1 ,creer_avoir_etape2 ,demarrer_avoir#,creer_avoir_etape2,detail_avoir , creer_avoir_etape2,toggle_paid ,creer_avoir_etape1 #creer_avoir_etape1 , creer_avoir, ,get_user_data#,dashboard_redirect   

# app_name = 'invoices'  # Très important pour le namespace


urlpatterns = [ 
    path('', views.HomeView.as_view(), name='home'),
    ###
    path('customer/add-customer', views.AddCustomerView.as_view(), name='add-customer'),  # Pas de préfixe fr/ ici

    # path('/customer/add-customer', views.AddCustomerView.as_view(), name='add-customer'),
    path('add-invoice', views.AddInvoiceView.as_view(), name='add-invoice'),
    path('view-invoice/<int:pk>', views.InvoiceVisualizationView.as_view(), name='view-invoice'),
    path('invoice-pdf/<int:pk>', views.get_invoice_pdf, name='invoice-pdf'),

    # path('add-article/', AddArticleView.as_view(), name='add_article'),
    path('add-article/',views.AddArticleToListView.as_view(), name='add_article'),


#vues client
    path('customer/add-customer', views.AddCustomerView.as_view(), name='add-customer'),  # Pas de préfixe fr/ ici
    path('customer/ajouter-client-professionnel/',views.AjouterClientProfessionnel.as_view(), name='ajouter_client_professionnel'),
    path('customer/ajouter-client-particulier/', views.AjouterClientParticulier.as_view(), name='ajouter_client_particulier'),



    # path('customers/', views.CustomerListView.as_view(), name='customer_list'),



    path('customer/edit/<int:pk>/', views.EditCustomerView.as_view(), name='edit_customer'),
    path('customer/delete/<int:pk>/', views.DeleteCustomerView.as_view(), name='delete_customer'),
    path('download/csv/', views.download_csv, name='download_csv'),
    path('download/pdf/', views.download_pdf, name='download_pdf'),
    # Page de la liste des clients
    path('customers/', views.client_list, name='client_list'),

    # Téléchargement CSV des clients
    path('clients/download/csv/', views.download_csv, name='download_csv'),

    # Téléchargement PDF des clients
    path('clients/download/pdf/', views.download_pdf, name='download_pdf'),





#vues factures:
    path("factures/", views.list_facture, name="list_facture"),
    path("factures/download/csv/", views.download_factures_csv, name="download_factures_csv"),
    path("factures/download/pdf/", views.download_factures_pdf, name="download_factures_pdf"),
    path('facture/<int:facture_id>/', views.voir_facture, name='voir_facture'),
    path('facture/<int:facture_id>/modifier/', views.modifier_facture, name='modifier_facture'),
    path('facture/<int:facture_id>/supprimer/', views.supprimer_facture, name='supprimer_facture'),




    path('export-csv/', export_invoices_csv, name='export_invoices_csv'),




    path("invoice/facture/etape1/", views.creer_facture_etape1, name="creer_facture_etape1"),
    path("invoice/facture/etape2/", views.creer_facture_etape2, name="creer_facture_etape2"),





    #last views
    path('services/', views.services, name='services'),
    path('formules/', views.formules, name='formules'),
    path('plus_loin/', views.plus_loin,name='plus_loin'),
    path('customers/base_customers/', views.base_customers,name='base_customers'),
    path('invoices/base_invoices/', views.base_invoices,name='base_invoices'),



    path('services/ajouter_client/', views.AjouterClient.as_view(), name='ajouter_client'),

    path('load-content/<str:page>/', views.load_content, name='load_content'),







































    path('invoice/<int:pk>/', InvoiceDetailAPIView.as_view(), name='invoice-detail'),
    path('invoices/', InvoiceListAPIView.as_view(), name='invoice-list'),  # <- Ajouté ici


    path('dashboard/', redirect_to_dashboard, name='redirect_to_dashboard'),
    # # path("user_data/", views.user_data, name="user_data"),
    # # path("dashboard/",  views.redirect_to_streamlit, name="go_to_dashboard"),
    # path("user_data/", user_data, name="user_data"),
    # path("dashboard/", dashboard_redirect, name="dash_board"),
    # path('user-data/', get_user_data, name='user-data'),



    path('view-invoice/<int:pk>', views.InvoiceVisualizationView.as_view(), name='view-invoice'),
    path('invoice-pdf/<int:pk>', views.get_invoice_pdf, name="invoice-pdf"),
    path('invoices/<int:pk>/toggle-paid/', views.toggle_paid, name='toggle-paid'),
    # path('facture/<int:facture_id>/creer-avoir/', views.creer_avoir, name='creer_avoir'),

# # urls.py
#     # path('avoirs/creer/etape1/', views.creer_avoir_etape1, name='creer_avoir_etape1'),


#     # path('facture/<int:facture_id>/creer-avoir/etape2/', views.creer_avoir_etape2, name='creer_avoir_etape2'),

#     # path('avoir/<int:avoir_id>/', views.detail_avoir, name='detail_avoir'),
#     path('avoirs/', views.liste_avoirs, name='liste_avoirs'),
#     # path('avoirs/<int:avoir_id>/', views.detail_avoir, name='detail_avoir'),
#     path('avoir/<int:avoir_id>/', views.detail_avoir, name='detail_avoir'),

#     # path('avoir/<int:facture_id>/etape1/', views.creer_avoir_etape1, name='creer_avoir_etape1'),
#     # path('avoir/<int:facture_id>/etape2/', views.creer_avoir_etape2, name='creer_avoir_etape2'),
#     path('creer-avoir/etape1/<int:facture_id>/', views.creer_avoir_etape1, name='creer_avoir_etape1'),
#     # path('creer-avoir/etape1/', views.creer_avoir_etape1, name='creer_avoir_simple_etape1'),
#     # path('creer-avoir/etape2/', views.creer_avoir_etape2, name='creer_avoir_etape2'),







#CREER AVOIRS

    # path('avoir/<int:avoir_id>/', views.voir_avoir, name='voir_avoir'),

    path("invoice/avoir/etape1/", views.creer_avoir_etape1, name="creer_avoir_etape1"),

    path("invoice/avoir/etape2/", views.creer_avoir_etape2, name="creer_avoir_etape2"),

    path('view-avoir/<int:pk>', views.AvoirVisualizationView.as_view(), name='view-avoir'),

    path('avoir-pdf/<int:pk>', views.get_avoir_pdf, name="avoir-pdf"),

    path("avoirs/", views.list_avoir, name="list_avoir"),

    path('api/invoices/', views.get_invoices_json, name='api_invoices'),
    path('api/invoices/', api_invoices, name='api_invoices'),

]

