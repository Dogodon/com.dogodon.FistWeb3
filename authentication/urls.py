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




app_name = 'authentication'  # Très important pour le namespace
 
from django.urls import path
from . import views
from authentication.views import Register, Login
from django.contrib.auth.views import LogoutView




# from .views import user_data_view, user_data



# urlpatterns = [
#     path('', views.home, name='index'),
#     # path('check-mail-ajax/', views.check_mail_ajax, name='check_mail_ajax'),
#     # path('login-req', Login.as_view(), name='login_ajax'),
#     # path('login/', views.signin, name='login'),



# #LOG
#     path('login/', views.login_view, name='login'),
#     path('signup/', views.signup_view, name='signup'),
#     path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
# ]










urlpatterns = [
    path('', views.home, name='index'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', LogoutView.as_view(next_page='authentication:login'), name='logout'),
    
    # API endpoints pour Streamlit
    path('api/check-session/', views.check_session, name='check_session'),
    path('api/user-data/', views.user_data, name='user_data'),

    # path("user_data/", user_data_view, name="user_data"),
    # path('dashboard/', views.redirect_to_dashboard, name='redirect_to_dashboard'),
    # path("user_data/", user_data, name="user_data"),


]