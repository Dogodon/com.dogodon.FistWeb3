from django.shortcuts import render

# Create your views here.
# landing/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'landing/index.html')
