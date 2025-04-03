from django.urls import path
from .views import get_articles, save_articles

urlpatterns = [
    path('articles/', get_articles, name='get_articles'),
    path('articles/save/', save_articles, name='save_articles'),
]
