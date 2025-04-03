# from django.urls import path
# from . import views

# from subscription.views import Register
# from subscription.views import  Login

# urlpatterns = [
#     # path('register/', Register.as_view(), name='register'),
#     # path('login/', Login.as_view(), name='login'),



#     path('', views.home, name='index'),

# 	# path('home/', views.index, name='home'),

#     path('check-mail-ajax/', views.check_mail_ajax, name='check_mail_ajax'),

#     # path('register/', Register.as_view(), name='register'),

#     path('login-req', Login.as_view(), name='login_ajax'),


#     path('login/', views.signin, name='login'),

# ]


# # from django.urls import path

# # from . import views
# # from .views import Register, Login


# # urlpatterns = [

# #     path('subscription/', views.subscription, name='subscription'),
# #     path('subscribe/', views.subscribe, name='subscribe'),
# #     path('subscribed/', views.subscribed, name='subscribed'),
# #     path('sub/', views.end_sub, name='sub'),

# #     path('payment/', views.call_back_url, name='payment'),

# # ]


# urls.py de l'application authentication

from django.urls import path
from . import views
from authentication.views import Register, Login

urlpatterns = [
    path('', views.home, name='index'),
    path('check-mail-ajax/', views.check_mail_ajax, name='check_mail_ajax'),
    path('login-req', Login.as_view(), name='login_ajax'),
    path('login/', views.signin, name='login'),
]