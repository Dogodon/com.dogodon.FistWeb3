"""
URL configuration for facturation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
###
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from .views import DashboardView
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),

    #api POUR DASHBOARD!!
    path("api/", include('facturation.api.urls')),
    path('api/', include('billing.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

###
urlpatterns += i18n_patterns(
    #...
    path('', include('landing.urls')),  # landing page à la racine
    # path('billing/', include('billing.urls', namespace='invoices')),  # Inclure les URLs de l'application billing

    path('billing/', include('billing.urls')),  # Inclure les URLs de l'application billing
    path('payments/', include('payments.urls')),    # Inclure les URLs de l'application payment

    path('education/', include('education.urls')),  # Cours d'éducation financière
    path('subscription/', include('subscription.urls')),  # Cours d'éducation financière
        
    # path('auth/', include('authentication.urls')),
    path('auth/', include('authentication.urls', namespace='authentication')),
    # path("echeance/", include("echeance.urls")),
    path("calendarapp/", include("calendarapp.urls")),

    path("dashboard/", DashboardView.as_view(), name="dashboard"),

    
)


###
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)

