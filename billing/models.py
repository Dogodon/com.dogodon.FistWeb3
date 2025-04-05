from django.db import models

# Create your models here.


from django.db import models
# from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _



# from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
# from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from django.conf import settings
PARTICULIER = 'particulier'
PROFESSIONNEL = 'professionnel'

CUSTOMER_TYPE_CHOICES = [
    (PARTICULIER, 'Particulier'),
    (PROFESSIONNEL, 'Professionnel'),
]

SEX_TYPES = (
    ('M', _('Masculin')),
    ('F', _('Féminin')),
)
RURALE = 'rurale'
URBAINE = 'urbaine'

ZONE_TYPE_CHOICES = [
    (RURALE, 'rurale'),
    (URBAINE, 'urbaine'),
]
class Customer(models.Model):
    """
    Modèle Customer : gère les clients professionnels et particuliers.
    """

    PARTICULIER = 'particulier'
    PROFESSIONNEL = 'professionnel'

    CUSTOMER_TYPE_CHOICES = [
        (PARTICULIER, 'Particulier'),
        (PROFESSIONNEL, 'Professionnel'),
    ]

    SEX_TYPES = (
        ('M', _('Masculin')),
        ('F', _('Féminin')),
    )
    RURALE = 'rurale'
    URBAINE = 'urbaine'
    ZONE_TYPE_CHOICES = [
        (RURALE, 'rurale'),
        (URBAINE, 'urbaine'),
    ]

    # Champs communs à tous les clients
    customer_type = models.CharField(
        max_length=20, choices=CUSTOMER_TYPE_CHOICES, default=PARTICULIER
    )
    civilite = models.CharField(max_length=10, blank=True, null=True)  # M., Mme, Dr...
    nom = models.CharField(max_length=132)
    prenom = models.CharField(max_length=132, blank=True, null=True)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=1, choices=SEX_TYPES, default='M')
    zone = models.CharField(max_length=10, choices=ZONE_TYPE_CHOICES, default='RURALE')

    telephone = models.CharField(max_length=20, blank=True, null=True)
    adresse = models.CharField(max_length=255, blank=True, null=True)
    code_postal = models.CharField(max_length=16, blank=True, null=True)
    ville = models.CharField(max_length=50, blank=True, null=True)
    pays = models.CharField(max_length=50, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    save_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # save_by = models.ForeignKey(User, on_delete=models.PROTECT)

    # Champs spécifiques aux professionnels
    raison_sociale = models.CharField(max_length=255, blank=True, null=True)
    siret = models.PositiveIntegerField(blank=True, null=True, unique=True)
    num_tva_intracom = models.CharField(max_length=50, blank=True, null=True)
    fax = models.CharField(max_length=20, blank=True, null=True)
    fonction = models.CharField(max_length=100, blank=True, null=True)
    telephone_mobile = models.CharField(max_length=20, blank=True, null=True)
    telephone_fixe = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def __str__(self):
        if self.customer_type == self.PROFESSIONNEL:
            return f"{self.raison_sociale} ({self.nom} {self.prenom})"
        return f"{self.nom} {self.prenom or ''} - {self.pays}"


# class Customer(models.Model):
#     """
#     Modèle Customer : gère les clients professionnels et particuliers.
#     """

#     PARTICULIER = 'particulier'
#     PROFESSIONNEL = 'professionnel'

#     CUSTOMER_TYPE_CHOICES = [
#         (PARTICULIER, 'Particulier'),
#         (PROFESSIONNEL, 'Professionnel'),
#     ]

#     SEX_TYPES = (
#         ('M', _('Masculin')),
#         ('F', _('Féminin')),
#     )

#     # Champs communs à tous les clients
#     customer_type = models.CharField(
#         max_length=20, choices=CUSTOMER_TYPE_CHOICES, default=PARTICULIER
#     )
#     civilite = models.CharField(max_length=10, blank=True, null=True)  # M., Mme, Dr...
#     nom = models.CharField(max_length=132)
#     prenom = models.CharField(max_length=132, blank=True, null=True)
#     email = models.EmailField(unique=True)
#     telephone = models.CharField(max_length=20, blank=True, null=True)
#     adresse = models.CharField(max_length=255, blank=True, null=True)
#     code_postal = models.CharField(max_length=16, blank=True, null=True)
#     ville = models.CharField(max_length=50, blank=True, null=True)
#     pays = models.CharField(max_length=50, blank=True, null=True)
#     created_date = models.DateTimeField(auto_now_add=True)
#     save_by = models.ForeignKey(User, on_delete=models.PROTECT)

#     # Champs spécifiques aux professionnels
#     raison_sociale = models.CharField(max_length=255, blank=True, null=True)
#     siret = models.PositiveIntegerField(blank=True, null=True, unique=True)
#     num_tva_intracom = models.CharField(max_length=50, blank=True, null=True)
#     fax = models.CharField(max_length=20, blank=True, null=True)
#     fonction = models.CharField(max_length=100, blank=True, null=True)
#     telephone_mobile = models.CharField(max_length=20, blank=True, null=True)
#     telephone_fixe = models.CharField(max_length=20, blank=True, null=True)

#     class Meta:
#         verbose_name = "Client"
#         verbose_name_plural = "Clients"

#     def __str__(self):
#         if self.customer_type == self.PROFESSIONNEL:
#             return f"{self.raison_sociale} ({self.nom} {self.prenom})"
#         return f"{self.nom} {self.prenom or ''} - {self.pays}"
   







# Référence	Désignation	Quantité	PU Vente	TVA	Montant HT	Image
# class Invoice(models.Model):
#     """
#     Name: Invoice model definition
#     Description: 
#     author: dogodontraore@gmail.com
#     """

#     INVOICE_TYPE = (
#         ('R', _('RECEIPT')),
#         ('P', _('PROFORMA INVOICE')),
#         ('I', _('INVOICE'))
#     )

#     customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

#     save_by = models.ForeignKey(User, on_delete=models.PROTECT)

#     invoice_date_time = models.DateTimeField(auto_now_add=True)

#     total = models.DecimalField(max_digits=20, decimal_places=2)

#     last_updated_date = models.DateTimeField(null=True, blank=True)

#     paid  = models.BooleanField(default=False)

#     invoice_type = models.CharField(max_length=1, choices=INVOICE_TYPE)

#     comments = models.TextField(null=True, max_length=1000, blank=True)

    
#     class Meta:
#         verbose_name = "Invoice"
#         verbose_name_plural = "Invoices"

#     def __str__(self):
#            return f"{self.customer.name}_{self.invoice_date_time}"

#     @property
#     def get_total(self):
#         articles = self.article_set.all()   
#         total = sum(article.get_total for article in articles)
#         return total    

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# class Invoice(models.Model):
#     """
#     Name: Invoice model definition
#     Description: Model representing invoices.
#     author: dogodontraore@gmail.com
#     """

#     INVOICE_TYPE = (
#         ('R', _('RECEIPT')),
#         ('P', _('PROFORMA INVOICE')),
#         ('I', _('INVOICE'))
#     )

#     customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
#     save_by = models.ForeignKey(User, on_delete=models.PROTECT)
#     invoice_date_time = models.DateTimeField(auto_now_add=True)
#     total = models.DecimalField(max_digits=20, decimal_places=2)
#     last_updated_date = models.DateTimeField(null=True, blank=True)
#     paid = models.BooleanField(default=False)
#     invoice_type = models.CharField(max_length=1, choices=INVOICE_TYPE)
#     comments = models.TextField(null=True, max_length=1000, blank=True)

#     # Ajout des nouveaux champs
#     title = models.CharField(max_length=255, default="Facture")  # Titre du document
#     logo = models.ImageField(upload_to="invoices/logos/", null=True, blank=True)  # Logo de la facture

#     class Meta:
#         verbose_name = "Invoice"
#         verbose_name_plural = "Invoices"

#     def __str__(self):
#         return f"{self.customer.nom}_{self.invoice_date_time.strftime('%Y-%m-%d')}"

#     @property
#     def get_total(self):
#         articles = self.article_set.all()   
#         total = sum(article.get_total for article in articles)
#         return total

class Invoice(models.Model):
    """
    Name: Invoice model definition
    Description: 
    author: dogodontraore@gmail.com
    """

    INVOICE_TYPE = (
        ('R', _('RECEIPT')),
        ('P', _('PROFORMA INVOICE')),
        ('I', _('INVOICE'))
    )

    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    save_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # save_by = models.ForeignKey(User, on_delete=models.PROTECT)

    invoice_date_time = models.DateTimeField(auto_now_add=True)

    total = models.DecimalField(max_digits=20, decimal_places=2)

    last_updated_date = models.DateTimeField(null=True, blank=True)

    paid  = models.BooleanField(default=False)

    invoice_type = models.CharField(max_length=1, choices=INVOICE_TYPE)

    comments = models.TextField(null=True, max_length=1000, blank=True)

    logo = models.ImageField(upload_to="invoices/logos/", null=True, blank=True)

    class Meta:
        verbose_name = "Invoice"
        verbose_name_plural = "Invoices"

    def __str__(self):
        return f"{self.customer.nom}_{self.invoice_date_time}"

    @property
    def get_total(self):
        articles = self.article_set.all()   
        total = sum(article.get_total for article in articles)
        return total    















from django.db import models
from decimal import Decimal

# class Article(models.Model):
#     """
#     Name: Article model definition
#     Description: Model representing an article in an invoice.
#     Author: dogodontraore@gmail.com
#     """

#     PRODUCT = 'produit'
#     SERVICE = 'service'
#     ARTICLE_TYPE_CHOICES = [
#         (PRODUCT, 'Produit'),
#         (SERVICE, 'Service'),
#     ]

#     invoice = models.ForeignKey('Invoice', on_delete=models.CASCADE)

#     # Champs communs à tous les articles
#     designation = models.CharField(max_length=255, default="Article Inconnu")

#     quantity = models.IntegerField()
#     unite = models.CharField(max_length=50, blank=True, null=True)
#     unit_price = models.DecimalField(max_digits=20, decimal_places=2)
#     remise = models.DecimalField(max_digits=5, decimal_places=2, default=0)  # Remise en %
#     tva = models.DecimalField(max_digits=5, decimal_places=2, default=0)  # Taux de TVA en %
#     montant_ht = models.DecimalField(max_digits=20, decimal_places=2, default=0)  # Montant HT
#     reference = models.CharField(max_length=100, blank=True, null=True)
#     famille = models.CharField(max_length=50, choices=ARTICLE_TYPE_CHOICES)  # Produit ou Service
    
#     # Champs spécifiques aux produits
#     prix_achat_ht = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)  # Prix d'achat HT
#     taux_marge = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)  # Taux de marge en %
#     img = models.ImageField(upload_to="articles/imgs/", null=True, blank=True)  # Logo de la facture

#     class Meta:
#         verbose_name = 'Article'
#         verbose_name_plural = 'Articles'

#     @property
#     def get_total(self):
#         total = self.quantity * self.unit_price
#         return total

#     def save(self, *args, **kwargs):
#         # Calcul du montant HT en fonction du prix unitaire et de la quantité
#         self.montant_ht = self.unit_price * self.quantity

#         if self.famille == self.PRODUCT:
#             # Calcul du taux de marge si c'est un produit
#             if self.prix_achat_ht and self.unit_price:
#                 self.taux_marge = ((self.unit_price - self.prix_achat_ht) / self.prix_achat_ht) * 100
#         # Applique la remise et la TVA
#         self.total = self.montant_ht - (self.montant_ht * self.remise / 100)
#         self.total += self.total * self.tva / 100

#         super().save(*args, **kwargs)

#     def __str__(self):
#         return f"{self.designation} ({self.famille})"



class Article(models.Model):
    """
    Name: Article model definition
    Description: Model representing an article in an invoice.
    Author: dogodontraore@gmail.com
    """

    PRODUCT = 'produit'
    SERVICE = 'service'
    ARTICLE_TYPE_CHOICES = [
        (PRODUCT, 'Produit'),
        (SERVICE, 'Service'),
    ]

    invoice = models.ForeignKey('Invoice', on_delete=models.CASCADE, null=True, blank=True)  # Changer ici

    # Champs communs à tous les articles
    designation = models.CharField(max_length=255, default="Article Inconnu")
    quantity = models.IntegerField()
    unite = models.CharField(max_length=50, blank=True, null=True)
    unit_price = models.DecimalField(max_digits=20, decimal_places=2)
    remise = models.DecimalField(max_digits=5, decimal_places=2, default=0)  # Remise en %
    tva = models.DecimalField(max_digits=5, decimal_places=2, default=0)  # Taux de TVA en %
    montant_ht = models.DecimalField(max_digits=20, decimal_places=2, default=0)  # Montant HT
    reference = models.CharField(max_length=100, blank=True, null=True)
    famille = models.CharField(max_length=50, choices=ARTICLE_TYPE_CHOICES)  # Produit ou Service
    
    # Champs spécifiques aux produits
    prix_achat_ht = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)  # Prix d'achat HT
    taux_marge = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)  # Taux de marge en %
    img = models.ImageField(upload_to="articles/imgs/", null=True, blank=True)  # Logo de la facture

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    @property
    def get_total(self):
        total = self.quantity * self.unit_price
        return total

    def save(self, *args, **kwargs):
        # Calcul du montant HT en fonction du prix unitaire et de la quantité
        self.montant_ht = self.unit_price * self.quantity

        if self.famille == self.PRODUCT:
            # Calcul du taux de marge si c'est un produit
            if self.prix_achat_ht and self.unit_price:
                self.taux_marge = ((self.unit_price - self.prix_achat_ht) / self.prix_achat_ht) * 100
        # Applique la remise et la TVA
        self.total = self.montant_ht - (self.montant_ht * self.remise / 100)
        self.total += self.total * self.tva / 100

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.designation} ({self.famille})"











# class Article(models.Model):
#     """
#     Modèle représentant un article dans une facture.
#     """

#     PRODUCT = 'produit'
#     SERVICE = 'service'
#     ARTICLE_TYPE_CHOICES = [
#         (PRODUCT, 'Produit'),
#         (SERVICE, 'Service'),
#     ]

#     invoice = models.ForeignKey('Invoice', on_delete=models.CASCADE)

#     designation = models.CharField(max_length=255, default="Article Inconnu")
#     quantity = models.IntegerField()
#     unite = models.CharField(max_length=50, blank=True, null=True)
#     unit_price = models.DecimalField(max_digits=20, decimal_places=2)
#     remise = models.DecimalField(max_digits=5, decimal_places=2, default=0)  # En %
#     tva = models.DecimalField(max_digits=5, decimal_places=2, default=0)  # En %
#     montant_ht = models.DecimalField(max_digits=20, decimal_places=2, default=0)  # Calculé automatiquement
#     montant_ttc = models.DecimalField(max_digits=20, decimal_places=2, default=0)  # Montant TTC

#     reference = models.CharField(max_length=100, blank=True, null=True)
#     famille = models.CharField(max_length=10, choices=ARTICLE_TYPE_CHOICES)

#     # Champs spécifiques aux produits
#     prix_achat_ht = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
#     taux_marge = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
#     img = models.ImageField(upload_to="articles/imgs/", null=True, blank=True)

#     class Meta:
#         verbose_name = 'Article'
#         verbose_name_plural = 'Articles'

#     @property
#     def get_total(self):
#         return self.quantity * self.unit_price

#     def save(self, *args, **kwargs):
#         self.montant_ht = self.get_total()

#         if self.famille == self.PRODUCT:
#             if self.prix_achat_ht and self.unit_price:
#                 self.taux_marge = ((self.unit_price - self.prix_achat_ht) / self.prix_achat_ht) * 100
#             else:
#                 self.taux_marge = None  # Évite les erreurs si prix_achat_ht est null

#         # Appliquer remise et TVA
#         self.montant_ht -= self.montant_ht * (self.remise / 100)
#         self.montant_ttc = self.montant_ht + (self.montant_ht * (self.tva / 100))

#         super().save(*args, **kwargs)

#     def __str__(self):
#         return f"{self.designation} ({self.famille})"









# from django.db import models
# ###
# from django.contrib.auth.models import User
# # Create your models here.

# ###
# class Customer(models.Model):
#     """
#     Name: Customer model definition
#     """

#     SEX_TYPES = (
#         ('M', 'Masculin'),
#         ('F', 'Feminin') )

#     name = models.CharField(max_length=132)

#     email = models. EmailField()

#     phone = models.CharField(max_length=132)

#     address = models.CharField(max_length=64)

#     sex = models.CharField(max_length=1, choices=SEX_TYPES)
    
#     age = models.CharField(max_length=12)

#     city = models.CharField(max_length=32)

#     zip_code = models.CharField(max_length=16)

#     created_date = models.DateTimeField(auto_now_add=True)
    
#     save_by = models.ForeignKey(User, on_delete=models.PROTECT)

#     class Meta:
#         verbose_name = "Customer"
#         verbose_name_plural = "Customers"

#     def str_(self):
#         return self.name





# class Invoice(models.Model):
#     """
#     Name: Invoice model definition
#     Description:
#     author: dogodontraore@gmail.com
#     """
#     INVOICE_TYPE = (
#         ('R', 'RECU'),
#         ('P', 'PROFORMA FACTURE'),
#         ('R', 'FACTURE'),
#     )
#     customer = models.CharField(max_length=100) 

#     #un client peut avoir +sieurs factures
#     Customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    
#     #un administrateur peut enregistrer +sieurs factures
#     save_by = models.ForeignKey(User, on_delete=models.PROTECT)

#     invoice_date_time = models.DateTimeField(auto_now_add=True)

#     total = models.DecimalField(max_digits=10000, decimal_places=2)

#     last_updated_date = models.DateTimeField(null=True, blank=True)

#     paid = models.BooleanField(default=False)

#     invoice_type = models.CharField(max_length=1, choices=INVOICE_TYPE)

#     comments = models.TextField(null=True, max_length=1000, blank=True)



#     class Meta:
#             verbose_name = "Invoice"
#             verbose_name_plural = "Invoices"

#     def __str__(self):
#         return f"{self.customer.name}_{self.invoice_date_time}"

#     @property
#     def get_total(self):
#         articles = self.article_set.all()   
#         total = sum(article.get_total for article in articles)
#         return total    




# class Article(models.Model):
#     """
#     Name: Article model definiton
#     Descripiton: 
#     Author: dogodontraore@gmail.com
#     """

#     invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)

#     name = models.CharField(max_length=32)

#     quantity = models.IntegerField()

#     unit_price = models.DecimalField(max_digits=1000, decimal_places=2)

#     total = models.DecimalField(max_digits=1000, decimal_places=2)

#     class Meta:
#         verbose_name = 'Article'
#         verbose_name_plural = 'Articles'

#     @property
#     def get_total(self):
#         total = self.quantity * self.unit_price   
#         return total 
        

