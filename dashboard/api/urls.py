from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet

customer_router = DefaultRouter()

customer_router.register(r'customers', CustomerViewSet)



# from django.urls import path
 
# urlpatterns = customer_router.urls + [
#     path("dashboard/", redirect_to_dashboard, name="redirect_to_dashboard"),
    
# ]