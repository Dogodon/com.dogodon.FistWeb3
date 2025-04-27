from rest_framework import viewsets
from .serializers import CustomerSerializer
from billing.models import Customer,Article


from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse
from billing.models import Invoice  # adapte le chemin si besoin
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


# class CustomerViewSet(viewsets.ModelViewSet):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer


from rest_framework import viewsets
# from .models import Customer
from .serializers import CustomerSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def perform_create(self, serializer):
        serializer.save(save_by=self.request.user)

    # def get_queryset(self):
    #     return Customer.objects.filter(save_by=self.request.user)

    def get_queryset(self):
        save_by = self.request.user 
        if save_by.is_staff or save_by.is_superuser: 
            return Customer.objects.all()
        return Customer.objects.filter(save_by=self.request.user)




#     save_by=user
    # # invoices = Invoice.objects.filter(save_by=user)

    # def get_queryset(self):
    #     user = self.request.user
    #     return Customer.objects.filter(save_by=user) 


# @login_required
# def user_data(request):
#     user = request.user
#     invoices = Invoice.objects.filter(save_by=user)

#     data = {
#         "username": user.username,
#         "email": user.email,
#         "total_invoices": invoices.count(),
#         "paid_invoices": invoices.filter(paid=True).count(),
#         "unpaid_invoices": invoices.filter(paid=False).count(),
#         # Ajoute d'autres infos si tu veux
#     }

#     return JsonResponse(data)






# def check_session(request):
#     if request.user.is_authenticated:
#         return JsonResponse({'authenticated': True})
#     return JsonResponse({'authenticated': False}, status=401)


# from django.shortcuts import redirect

# def redirect_to_dashboard(request):
#     session_id = request.COOKIES.get('sessionid')
#     dashboard_url = f"http://localhost:8501/?sessionid={session_id}"
#     return redirect(dashboard_url)

