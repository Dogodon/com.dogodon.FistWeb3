from django.contrib import admin

# Register your models here.
from django.contrib import admin
###
from .models import * 
from django.utils.translation import gettext_lazy as _


# Register your models here.


class AdminCustomer(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email', 'customer_type', 'telephone', 'pays', 'ville', 'code_postal')

# admin.site.register(Customer, AdminCustomer)

class AdminInvoice(admin.ModelAdmin):
    list_display = ('customer', 'save_by', 'invoice_date_time', 'total', 'last_updated_date', 'paid', 'invoice_type')    

admin.site.register(Customer, AdminCustomer)
admin.site.register(Invoice, AdminInvoice)
admin.site.register(Article)

admin.site.site_title = _("NG-SmartFact")
admin.site.site_header = _("NG-SmartFact")
admin.site.index_title = _("NG-SmartFact")

class AdminAvoir(admin.ModelAdmin):
    list_display = ('customer', 'save_by', 'avoir_date_time', 'total', 'last_updated_date')    
admin.site.register(Avoir, AdminAvoir)
