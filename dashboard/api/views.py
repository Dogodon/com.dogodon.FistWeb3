from rest_framework import viewsets
from .serializers import CustomerSerializer
from billing.models import Customer,Article

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer