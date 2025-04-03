from django.shortcuts import render

# Create your views here.


def some_view(request):
    from .models import Payment  # Import à l'intérieur pour éviter une boucle
    ...
