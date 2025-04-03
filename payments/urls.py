from django.urls import path
from . import views  # Assurez-vous que les vues sont bien importées

urlpatterns = [
    path('', views.some_view, name='some_view'),
]
