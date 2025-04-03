# from django.urls import path

# from . import views
# from .views import Register, Login
# from authentication.views import signin, home
# # urlpatterns = [
# # 	url(r'^$', views.home, name='index'),
# # 	url(r'^login/$', views.signin, name='login'),
# # 	url(r'^home/$', views.index, name='home'),
# #     url(r'^check-mail-ajax/$', views.check_mail_ajax, name='check_mail_ajax'),
# #     url(r'^register/$', Register.as_view(), name='register'),
# #     url(r'login-req', Login.as_view(), name='login_ajax'),

# #     url(r'^subscription/', views.subscription, name='subscription'),
# #     url(r'^subscribe/', views.subscribe, name='subscribe'),
# #     url(r'^subscribed/', views.subscribed, name='subscribed'),
# #     url(r'^sub/', views.end_sub, name='sub'),

# #     url(r'^payment/$', views.call_back_url, name='payment'),
# # ]

# urlpatterns = [
# 	# path('login/', views.signin, name='login'),
# 	# path('', views.home, name='index'),
# 	# path('home/', views.index, name='home'),
#     # path('check-mail-ajax/', views.check_mail_ajax, name='check_mail_ajax'),
#     # path('register/', Register.as_view(), name='register'),
#     # path('login-req', Login.as_view(), name='login_ajax'),



#     path('register/', Register.as_view(), name='register'),


#     path('subscription/', views.subscription, name='subscription'),
#     path('subscribe/', views.subscribe, name='subscribe'),
#     path('subscribed/', views.subscribed, name='subscribed'),
#     path('sub/', views.end_sub, name='sub'),

#     path('payment/', views.call_back_url, name='payment'),

# ]


# urls.py de l'application subscription

from django.urls import path
from . import views
from subscription.views import *

# from authentication.views import signin, home
# from subscription.views import Register, Login

# Définir les URLs pour la gestion des abonnements
urlpatterns = [
    # path('register/', Register.as_view(), name='register'),
    path('subscription/', views.subscription, name='subscription'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('subscribed/', views.subscribed, name='subscribed'),
    path('sub/', views.end_sub, name='sub'),
    path('payment/', views.call_back_url, name='payment'),
    



    # path('subscription/', views.subscription, name='subscription'),
    # path('subscribe/', views.subscribe, name='subscribe'),
    # path('payment/callback/', views.call_back_url, name='callback_url'),
    # path('subscribed/', views.subscribed, name='subscribed'),
]