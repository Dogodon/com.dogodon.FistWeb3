from django.urls import path
from .views import get_articles, save_articles,redirect_to_dashboard,user_data

urlpatterns = [
    path('articles/', get_articles, name='get_articles'),
    path('articles/save/', save_articles, name='save_articles'),

    
    # path("user_data/", user_data, name="user_data"),  # ✅ celle-là uniquement
    # path('dashboard/', redirect_to_dashboard, name='redirect_to_dashboard'),
]
