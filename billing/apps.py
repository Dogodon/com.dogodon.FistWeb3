from django.apps import AppConfig


class BillingConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "billing"




# #token django rest
# class UsersConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'users'  # ou 'accounts' selon ton projet

#     def ready(self):
#         import  authentication.signals  # ou accounts.signals selon ton app
