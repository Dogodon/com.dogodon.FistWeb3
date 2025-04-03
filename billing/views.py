from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin




from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Customer, Invoice, Article
from django.contrib import messages
from django.db import transaction
from django.contrib.auth.mixins import LoginRequiredMixin
from .utils import pagination, get_invoice
import pdfkit
import datetime
from django.template.loader import get_template #recupérer un fichier html
from .decorators import *
from django.utils.translation import gettext as _


class HomeView(LoginRequiredSuperuserMixin, View):
    """ Main view """

    template_name = 'base.html'
            
    invoices = Invoice.objects.select_related('customer', 'save_by').all().order_by('-invoice_date_time')

    context = {'invoices': invoices}

    def get(self, request, *args, **kwargs):

        items =pagination(request,self.invoices)
        self.context['invoices'] = items

        return render(request, self.template_name, self.context)
    

            
    def post(self, request, *args, **kwargs):
            # Vérifier si une modification est demandée
            invoice_id = request.POST.get("id_modified")

            if invoice_id:
                paid = request.POST.get("modified")

                try:
                    obj = get_object_or_404(Invoice, id=invoice_id)
                    obj.paid = True if paid == "True" else False
                    obj.save()
                    messages.success(request, _("Change made successfully."))

                except Exception as e:
                    messages.error(request, _(f"Sorry, an error occurred: {e}"))

            # Appliquer la pagination après modification
            # items = pagination(request, self.invoices)
            # context = {'invoices': items}

            # return render(request, self.template_name, context)



            if request.POST.get("id_supprimer"):
                try:
                    obj = Invoice.objects.get(pk=request.POST.get("id_supprimer"))
                    obj.delete()
                    messages.success(request, _("The deletion was successful."))
                except Exception as e:
                    messages.error(request, _(f"Sorry, the following error has occurred: {e}"))
            
            
            # Appliquer la pagination après modification

            items = pagination(request, self.invoices)
            self.context['invoices'] = items  # Correction de l'affectation (utilisation de "=" au lieu de "-")

            return render(request, self.template_name, self.context)






from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.utils.translation import gettext as _
from .models import Customer

class AddCustomerView(LoginRequiredSuperuserMixin, View):
    """ Ajouter un nouveau client (particulier ou professionnel) """

    template_name = "customers/add_customer.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        try:
            # Récupération des données du formulaire
            customer_type = request.POST.get('customer_type', 'particulier')  # Valeur par défaut 'particulier'
            # customer_type = request.POST.get('customer_type_hidden', 'particulier')

            # customer_type = request.POST.get('customer_type', Customer.PARTICULIER)
            civilite = request.POST.get('civilite', '').strip()
            nom = request.POST.get('nom', '').strip()
            prenom = request.POST.get('prenom', '').strip()
            email = request.POST.get('email', '').strip()
            sex = request.POST.get('sex', '')
            telephone = request.POST.get('telephone', '').strip()
            adresse = request.POST.get('adresse', '').strip()
            code_postal = request.POST.get('code_postal', '').strip()
            ville = request.POST.get('ville', '').strip()
            pays = request.POST.get('pays', '').strip()
            raison_sociale = request.POST.get('raison_sociale', '').strip()
            siret = request.POST.get('siret', None)
            num_tva_intracom = request.POST.get('num_tva_intracom', '').strip()
            fax = request.POST.get('fax', '').strip()
            fonction = request.POST.get('fonction', '').strip()
            telephone_mobile = request.POST.get('telephone_mobile', '').strip()
            telephone_fixe = request.POST.get('telephone_fixe', '').strip()

            # Vérification des champs obligatoires
            if not nom or not email:
                messages.error(request, _("Le nom et l'email sont obligatoires."))
                return render(request, self.template_name)

            # Création de l'objet Customer
            customer = Customer.objects.create(
                customer_type=customer_type,
                civilite=civilite,
                nom=nom,
                prenom=prenom,
                email=email,
                sex=sex,
                telephone=telephone,
                adresse=adresse,
                code_postal=code_postal,
                ville=ville,
                pays=pays,
                raison_sociale=raison_sociale if customer_type == Customer.PROFESSIONNEL else None,
                siret=int(siret) if siret and customer_type == Customer.PROFESSIONNEL else None,
                num_tva_intracom=num_tva_intracom if customer_type == Customer.PROFESSIONNEL else None,
                fax=fax if customer_type == Customer.PROFESSIONNEL else None,
                fonction=fonction if customer_type == Customer.PROFESSIONNEL else None,
                telephone_mobile=telephone_mobile if customer_type == Customer.PROFESSIONNEL else None,
                telephone_fixe=telephone_fixe if customer_type == Customer.PROFESSIONNEL else None,
                save_by=request.user
            )

            messages.success(request, _("Client enregistré avec succès."))
            return redirect('home')  # Redirection après ajout

        except Exception as e:
            messages.error(request, _(f"Erreur lors de l'enregistrement : {e}"))
            return render(request, "customers/add_customer.html")



# class AddCustomerView(LoginRequiredSuperuserMixin, View):
#     """ Add a new customer """

#     template_name = 'add_customer.html'

#     def get(self, request, *args, **kwargs):
#         return render(request, self.template_name)

#     def post(self, request, *args, **kwargs):
#         data = {
#             'name': request.POST.get('name'),
#             'email': request.POST.get('email'),
#             'phone': request.POST.get('phone'),
#             'address': request.POST.get('address'),
#             'sex': request.POST.get('sex'),
#             'age': request.POST.get('age'),
#             'city': request.POST.get('city'),
#             'zip_code': request.POST.get('zip'),
#             'save_by': request.user
#         }

#         try:
#             customer = Customer.objects.create(**data)
#             messages.success(request, _("Client enregistré avec succès."))
#             return redirect('home')  # Redirection après ajout
#         except Exception as e:
#             messages.error(request, _(f"Erreur lors de l'enregistrement : {e}"))
#             return render(request, self.template_name)








class InvoiceVisualizationView(LoginRequiredSuperuserMixin, View):
    """ This view helps to visualize the invoice """

    template_name = 'invoice.html'

    def get(self, request, *args, **kwargs):

        pk=kwargs.get('pk')
        context = get_invoice(pk)

        return render(request, self.template_name, context)



@superuser_required
def get_invoice_pdf(request, *args, **kwargs):
    """ generate pdf file from html file """

    pk = kwargs.get('pk')

    context = get_invoice(pk)

    context['date'] = datetime.datetime.today()

    #get html file
    template = get_template('invoice-pdf.html')

    #render html with  context variables
    html = template.render(context)

    #options of pdf format
    options ={
        'page-size' :'Letter',
        'encoding' : 'UTF-8',
        # 'enable-local-file-acces' : ''
    }
    # options = {
    #     'page-size': 'A4',  # Corrigé: '--page-size' au lieu de '--page_size'
    #     'encoding': 'UTF-8',
    #     'enable-local-file-access': ''
    # }

    # config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
    # pdf = pdfkit.from_string(html, False, options=options, configuration=config)


    #generate pdf
    pdf =pdfkit.from_string(html, False, options)
    response=HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = "attachement"
    return response





from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Invoice, Customer


from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.utils.translation import gettext as _
from django.db import transaction
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Invoice, Article, Customer, User

# @login_required
# def register_invoice(request):
#     if request.method == 'POST':
#         customer_id = request.POST.get('customer')
#         invoice_type = request.POST.get('invoice_type')
#         comments = request.POST.get('comment')
#         total = request.POST.get('total')
#         title = request.POST.get('title', 'Facture')  # Nouveau champ
#         logo = request.FILES.get('logo')  # Nouveau champ

#         articles = request.POST.getlist('article[]')
#         quantities = request.POST.getlist('qty[]')
#         unit_prices = request.POST.getlist('unit[]')
#         total_prices = request.POST.getlist('total-a[]')
#         remises = request.POST.getlist('remise[]')
#         tvas = request.POST.getlist('tva[]')
#         familles = request.POST.getlist('famille[]')

#         if not all([customer_id, invoice_type, articles, quantities, unit_prices, total_prices]):
#             return HttpResponse(_("Missing required fields"), status=400)

#         customer = get_object_or_404(Customer, id=customer_id)
#         invoice = Invoice.objects.create(
#             customer=customer,
#             save_by=request.user,
#             invoice_type=invoice_type,
#             total=total,
#             comments=comments,
#             title=title,
#             logo=logo
#         )

#         for i in range(len(articles)):
#             Article.objects.create(
#                 invoice=invoice,
#                 designation=articles[i],
#                 quantity=int(quantities[i]),
#                 unit_price=float(unit_prices[i]),
#                 remise=float(remises[i]) if remises[i] else 0,
#                 tva=float(tvas[i]) if tvas[i] else 0,
#                 famille=familles[i]
#             )

#         return redirect('invoice_success')

#     return render(request, 'register_invoice.html', {'customers': Customer.objects.all()})




from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Invoice, Customer, Article
from django.db import transaction

class AddInvoiceView(View):
    template_name = 'add_invoice.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        context = {'customers': Customer.objects.all()}
        return render(request, self.template_name, context)

    @method_decorator(login_required)
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        try:

            # Récupérer les données du formulaire
            customer_id = request.POST.get('customer')
            invoice_type = request.POST.get('invoice_type')
            title = request.POST.get('title', 'Facture')
            logo = request.FILES.get('logo')
            comment = request.POST.get('comment')
            total = request.POST.get('total')

            # Traiter les articles
            articles = request.POST.getlist('article')
            qties = request.POST.getlist('qty')
            units = request.POST.getlist('unit')
            total_a = request.POST.getlist('total-a')
            remises = request.POST.getlist('remise')
            tvas = request.POST.getlist('tva')
            familles = request.POST.getlist('famille')

            customer = get_object_or_404(Customer, id=customer_id)
            invoice = Invoice.objects.create(
                customer=customer,
                save_by=request.user,
                invoice_type=invoice_type,
                total=total,
                comments=comment,
                title=title,
                logo=logo
            )

            items = [
                Article(
                    invoice=invoice,
                    designation=articles[i],
                    quantity=int(qties[i]),
                    unit_price=float(units[i]),
                    remise=float(remises[i]) if remises[i] else 0,
                    tva=float(tvas[i]) if tvas[i] else 0,
                    famille=familles[i]
                )
                for i in range(len(articles))
            ]
            Article.objects.bulk_create(items)

            messages.success(request, _("Invoice saved successfully."))
            return redirect('home')  # Ou toute autre page après la création de la facture
        except Exception as e:
            messages.error(request, _(f"An error occurred: {e}"))
            return render(request, self.template_name, {'customers': Customer.objects.all()})




# @superuser_required
# def register_invoice(request):
#     if request.method == 'POST':
#         # Récupérer les données envoyées
#         customer_id = request.POST.get('customer')
#         invoice_type = request.POST.get('invoice_type')
#         comments = request.POST.get('comment')
#         total = request.POST.get('total')

#         # Récupérer les articles et leurs informations
#         articles = request.POST.getlist('article[]')
#         quantities = request.POST.getlist('qty[]')
#         unit_prices = request.POST.getlist('unit[]')
#         total_prices = request.POST.getlist('total-a[]')

#         # Assurez-vous que toutes les informations sont présentes et valides
#         if not all([customer_id, invoice_type, articles, quantities, unit_prices, total_prices]):
#             return HttpResponse(_("Missing required fields"), status=400)

#         # Créer l'objet facture
#         customer = Customer.objects.get(id=customer_id)
#         invoice = Invoice.objects.create(
#             customer=customer,
#             invoice_type=invoice_type,
#             total=total,
#             comments=comments
#         )

#         # Créer les articles associés à la facture
#         for i in range(len(articles)):
#             article = articles[i]
#             qty = float(quantities[i])
#             unit_price = float(unit_prices[i])
#             total_price = float(total_prices[i])

#             # Assurez-vous que chaque article a des données valides
#             if article and qty > 0 and unit_price > 0:
#                 invoice.items.create(
#                     name=article,
#                     quantity=qty,
#                     unit_price=unit_price,
#                     total=total_price
#                 )

#         return redirect('invoice_success')  # Rediriger vers une page de succès ou de confirmation

#     return render(request, 'register_invoice.html', {'customers': Customer.objects.all()})




# class AddInvoiceView(LoginRequiredSuperuserMixin, View):
#     """ add a new invoice view """

#     template_name = 'add_invoice.html'

#     customers = Customer.objects.select_related('save_by').all()

#     context = {
#         'customers': customers
#     }

#     def get(self, request, *args, ** kwargs):
#         return render(request, self.template_name, self.context)


#     @transaction.atomic()
#     def post(self, request, *args, ** kwargs):

#         items = []

#         try:
#             customer = request.POST.get('customer')
#             type = request.POST.get('invoice_type')
#             articles = request.POST.getlist('article')

#             qties = request.POST.getlist('qty')
#             units = request.POST.getlist('unit')
#             total_a =request.POST.getlist('total-a')
#             total = request.POST.get('total')

#             comment = request.POST.get('comment')

#             invoice_object = {
#                 'customer_id': customer,
#                 'save_by': request.user,
#                 'total': total,
#                 'invoice_type': type,
#                 'comments': comment
#             }
#             invoice = Invoice.objects.create(**invoice_object)
    
#             for index, article in enumerate(articles):

#                 data = Article(
#                     invoice_id = invoice.id,
#                     name = article,
#                     quantity=qties[index],
#                     unit_price = units[index],
#                     total = total_a[index],
#                 )
#                 items.append(data)

#             created = Article.objects.bulk_create(items)

#             if created:
#                 # Si tout se passe bien
#                 messages.success(request, _("Data saved successfully."))
#                 return redirect('home')  # Redirection vers une autre page après la soumission
#             else:
#                 messages.error(request, _("Sorry, please try again the sent data is corrupt."))

#         except Exception as e:
#             messages.error(request, _(f"Sorry the following error has occured {e}."))

#         return render(request, self.template_name, self.context)

from django.db import transaction
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _

# class AddInvoiceView(LoginRequiredSuperuserMixin, View):
#     """ Add a new invoice view """

#     template_name = 'add_invoice.html'

#     def get(self, request, *args, **kwargs):
#         customers = Customer.objects.all()
#         return render(request, self.template_name, {'customers': customers})

#     @transaction.atomic
#     def post(self, request, *args, **kwargs):
#         try:
#             # Récupérer les données envoyées
#             customer_id = request.POST.get('customer')
#             invoice_type = request.POST.get('invoice_type')
#             articles = request.POST.getlist('article')
#             quantities = request.POST.getlist('qty')
#             unit_prices = request.POST.getlist('unit')
#             total_prices = request.POST.getlist('total-a')
#             total = request.POST.get('total')
#             comment = request.POST.get('comment')

#             # Créer la facture
#             customer = Customer.objects.get(id=customer_id)
#             invoice = Invoice.objects.create(
#                 customer=customer,
#                 save_by=request.user,
#                 total=total,
#                 invoice_type=invoice_type,
#                 comments=comment
#             )

#             # Créer les articles associés à la facture
#             items = []
#             for i in range(len(articles)):
#                 article = articles[i]
#                 qty = float(quantities[i])
#                 unit_price = float(unit_prices[i])
#                 total_price = float(total_prices[i])

#                 if article and qty > 0 and unit_price > 0:
#                     item = Article(
#                         invoice=invoice,
#                         designation=article,
#                         quantity=qty,
#                         unit_price=unit_price,
#                         total=total_price
#                     )
#                     items.append(item)

#             # Sauvegarder les articles
#             if items:
#                 Article.objects.bulk_create(items)

#             messages.success(request, _("Data saved successfully."))

#             return redirect('home')  # Vous pouvez rediriger vers une autre page après la soumission

#         except Exception as e:
#             transaction.rollback()  # Annuler la transaction en cas d'erreur
#             messages.error(request, _(f"Sorry the following error has occurred: {e}."))
#             return render(request, self.template_name, {'customers': Customer.objects.all()})



from django.utils.translation import get_language_info

def my_view(request):
    languages = [
        get_language_info('en'),
        get_language_info('fr'),
        get_language_info('ar'),
    ]
    return render(request, 'home', {'languages': languages})










# import csv
# from django.http import HttpResponse
# from .models import Invoice  # Assurez-vous d'importer votre modèle Invoice
# import csv
# from django.http import HttpResponse
# from .models import Invoice

# def export_invoices_csv(request):
#     # Récupérer toutes les factures, triées par date d'émission décroissante
#     invoices = Invoice.objects.all().order_by('-invoice_date_time')

#     # Créer une réponse HTTP avec le type CSV
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="invoices.csv"'

#     writer = csv.writer(response)
#     # Écrire la ligne d'en-tête avec les champs disponibles
#     writer.writerow([
#         'ID', 'Customer', 'Saved By', 'Invoice Date Time', 
#         'Total', 'Last Updated Date', 'Paid', 'Invoice Type', 'Comments'
#     ])

#     # Écrire les données pour chaque facture
#     for invoice in invoices:
#         writer.writerow([
#             invoice.id,
#             invoice.customer.name,           # Supposons que Customer possède un attribut 'name'
#             invoice.save_by.username,        # Ou utilisez .get_full_name() selon votre modèle User
#             invoice.invoice_date_time,
#             invoice.total,
#             invoice.last_updated_date,
#             invoice.paid,
#             invoice.get_invoice_type_display(),  # Affiche la valeur lisible de l'option invoice_type
#             invoice.comments,
#         ])

#     return response

import csv
from django.http import HttpResponse
from django.utils.translation import gettext as _
from django.utils.translation import activate
from .models import Invoice

def export_invoices_csv(request):
    # Détecter la langue depuis la requête (ex: 'fr', 'ar', 'en')
    language = request.GET.get('lang', 'en')  # 'en' par défaut
    activate(language)  # Activer la langue choisie

    # Récupérer toutes les factures
    invoices = Invoice.objects.all().order_by('-invoice_date_time')

    # Créer une réponse HTTP avec type CSV
    response = HttpResponse(content_type='text/csv; charset=utf-8-sig')
    response['Content-Disposition'] = f'attachment; filename="invoices_{language}.csv"'

    writer = csv.writer(response)

    # Traduire les en-têtes selon la langue choisie
    writer.writerow([
        _('ID'), _('Customer'), _('Saved By'), _('Invoice Date Time'),
        _('Total'), _('Last Updated Date'), _('Paid'), _('Invoice Type'), _('Comments')
    ])

    # Écrire les données en respectant la langue
    for invoice in invoices:
        writer.writerow([
            invoice.id,
            invoice.customer.name if invoice.customer else _('Unknown'),  # Gestion si `customer` est None
            invoice.save_by.get_full_name() if invoice.save_by else _('Unknown'),  # Gestion si `save_by` est None
            invoice.invoice_date_time.strftime('%Y-%m-%d %H:%M:%S') if invoice.invoice_date_time else _('N/A'),
            invoice.total,
            invoice.last_updated_date.strftime('%Y-%m-%d %H:%M:%S') if invoice.last_updated_date else _('N/A'),
            _('Yes') if invoice.paid else _('No'),  # Traduction de "Paid" en "Oui/Non"
            invoice.get_invoice_type_display(),  # Option traduite automatiquement
            invoice.comments if invoice.comments else _('No comments'),
        ])

    return response













#ARTICLE
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .models import Article, Invoice  # Assurez-vous d'importer vos modèles

# class AddArticleView(View):
#     """ Vue permettant d'ajouter un article à une facture """

#     template_name = 'add_article.html'  # Fichier HTML contenant le formulaire

#     def get(self, request, *args, **kwargs):
#         invoices = Invoice.objects.all()  # Récupérer les factures disponibles
#         return render(request, self.template_name, {'invoices': invoices})

#     def post(self, request, *args, **kwargs):
#         try:
#             invoice_id = request.POST.get('invoice')
#             invoice = Invoice.objects.get(id=invoice_id)  # Récupérer la facture associée

#             data = {
#                 'invoice': invoice,
#                 'designation': request.POST.get('designation'),
#                 'quantity': int(request.POST.get('quantity', 1)),  # Valeur par défaut : 1
#                 'unite': request.POST.get('unite'),
#                 'unit_price': float(request.POST.get('unit_price')),
#                 'remise': float(request.POST.get('remise', 0)),  # Valeur par défaut : 0
#                 'tva': float(request.POST.get('tva', 0)),  # Valeur par défaut : 0
#                 'reference': request.POST.get('reference'),
#                 'famille': request.POST.get('famille'),
#                 'prix_achat_ht': request.POST.get('prix_achat_ht'),
#             }

#             article = Article.objects.create(**data)
#             messages.success(request, "Article ajouté avec succès.")
#             return redirect('home')  # Redirection après l'ajout

#         except Invoice.DoesNotExist:
#             messages.error(request, "Facture introuvable.")
#         except Exception as e:
#             messages.error(request, f"Erreur lors de l'ajout de l'article : {e}")

#         return render(request, self.template_name)


from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .models import Invoice, Article

class AddArticleView(View):
    """ Vue permettant d'ajouter un article à une facture """
    
    template_name = 'add_article.html'  # Template contenant le formulaire

    def get(self, request, *args, **kwargs):
        invoices = Invoice.objects.all()  # Récupérer toutes les factures
        return render(request, self.template_name, {'invoices': invoices})

    def post(self, request, *args, **kwargs):
        try:
            invoice_id = request.POST.get('invoice')
            invoice = Invoice.objects.get(id=invoice_id)  # Récupérer la facture associée

            quantity = int(request.POST.get('quantity', 1))
            unit_price = float(request.POST.get('unit_price', 0))
            remise = float(request.POST.get('remise', 0))
            tva = float(request.POST.get('tva', 0))
            famille = request.POST.get('famille')

            # Vérifications
            if quantity <= 0 or unit_price < 0:
                messages.error(request, "La quantité et le prix unitaire doivent être positifs.")
                return render(request, self.template_name)

            if famille not in [Article.PRODUCT, Article.SERVICE]:
                messages.error(request, "Type d'article invalide.")
                return render(request, self.template_name)

            # Gestion du prix d'achat (peut être vide)
            prix_achat_ht = request.POST.get('prix_achat_ht')
            prix_achat_ht = float(prix_achat_ht) if prix_achat_ht else None

            # Gestion de l'image (si fournie)
            img = request.FILES.get('img')

            # Création de l'article
            article = Article.objects.create(
                invoice=invoice,
                designation=request.POST.get('designation'),
                quantity=quantity,
                unite=request.POST.get('unite'),
                unit_price=unit_price,
                remise=remise,
                tva=tva,
                reference=request.POST.get('reference'),
                famille=famille,
                prix_achat_ht=prix_achat_ht,
                img=img,
            )

            messages.success(request, "Article ajouté avec succès.")
            return redirect('home')  # Redirection après succès

        except Invoice.DoesNotExist:
            messages.error(request, "Facture introuvable.")
        except ValueError:
            messages.error(request, "Veuillez entrer des valeurs numériques valides.")
        except Exception as e:
            messages.error(request, f"Erreur lors de l'ajout de l'article : {e}")

        return render(request, self.template_name)





from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .models import Article

class AddArticleToListView(View):
    """ Vue permettant d'ajouter un article à la liste des articles """
    
    template_name = 'add_article.html'  # Nom du fichier HTML du formulaire

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)  # Afficher le formulaire

    def post(self, request, *args, **kwargs):
        try:
            # Récupération et validation des données
            try:
                quantity = int(request.POST.get('quantity', 1))
                unit_price = float(request.POST.get('unit_price', 0))
                remise = float(request.POST.get('remise', 0))
                tva = float(request.POST.get('tva', 0))
                prix_achat_ht = request.POST.get('prix_achat_ht')
                prix_achat_ht = float(prix_achat_ht) if prix_achat_ht else None
            except ValueError:
                messages.error(request, "Valeurs numériques invalides.")
                return render(request, self.template_name)

            img = request.FILES.get('img')  # Gestion de l’image

            # Création de l'article
            Article.objects.create(
                designation=request.POST.get('designation'),
                quantity=quantity,
                unite=request.POST.get('unite'),
                unit_price=unit_price,
                remise=remise,
                tva=tva,
                reference=request.POST.get('reference'),
                famille=request.POST.get('famille'),
                prix_achat_ht=prix_achat_ht,
                img=img  # Ajout de l'image si présente
            )

            messages.success(request, "Article ajouté avec succès.")
            return redirect('base')  # Redirection vers la liste des articles

        except Exception as e:
            messages.error(request, f"Erreur lors de l'ajout de l'article : {e}")
            return render(request, self.template_name)























from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Invoice, Article
from django.contrib.auth.models import User




from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Article, Invoice
from django.db import transaction

def add_article(request):
    if request.method == 'POST':
        # Si l'article n'est pas lié à une facture, on peut omettre le champ 'invoice'
        try:
            # Si l'ID de facture est présent, associer l'article à cette facture
            invoice_id = request.POST.get('invoice')
            invoice = Invoice.objects.get(id=invoice_id) if invoice_id else None
        except Invoice.DoesNotExist:
            invoice = None

        try:
            with transaction.atomic():  # Démarre une transaction atomique pour les articles
                # Récupérer les données de l'article
                designation = request.POST.get('designation')
                quantity = int(request.POST.get('quantity'))
                unite = request.POST.get('unite', '')
                unit_price = float(request.POST.get('unit_price'))
                remise = float(request.POST.get('remise', 0))
                tva = float(request.POST.get('tva', 0))
                montant_ht = float(request.POST.get('montant_ht', 0))
                reference = request.POST.get('reference', '')
                famille = request.POST.get('famille')
                prix_achat_ht = float(request.POST.get('prix_achat_ht', 0) or 0)
                taux_marge = float(request.POST.get('taux_marge', 0) or 0)

                # Création de l'article sans être lié à une facture (si invoice est None)
                article = Article(
                    invoice=invoice,
                    designation=designation,
                    quantity=quantity,
                    unite=unite,
                    unit_price=unit_price,
                    remise=remise,
                    tva=tva,
                    montant_ht=montant_ht,
                    reference=reference,
                    famille=famille,
                    prix_achat_ht=prix_achat_ht,
                    taux_marge=taux_marge,
                )

                # Sauvegarder l'article
                article.save()

                # Retourner une réponse JSON pour l'API ou redirection pour un formulaire classique
                return JsonResponse({"success": "Article ajouté avec succès", "article_id": article.id})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    else:
        invoices = Invoice.objects.all()  # Récupérer toutes les factures pour afficher dans le formulaire
        return render(request, 'add_article.html', {'invoices': invoices})

















from django.shortcuts import render, redirect, get_object_or_404
from .models import Invoice, Customer, Article
from django.http import JsonResponse
from django.core.files.storage import default_storage

# def creer_facture_etape1(request):
#     if request.method == "POST":
#         titre = request.POST.get("titre")
#         logo = request.FILES.get("logo")
#         customer_id = request.POST.get("customer")

#         customer = get_object_or_404(Customer, id=customer_id)
#         facture = Invoice.objects.create(
#             customer=customer,
#             total=0,  # Initialisation
#             comments=titre
#         )
        
#         # Stocker l'ID de la facture temporairement en session
#         request.session["facture_id"] = facture.id

#         return redirect("creer_facture_etape2")

#     customers = Customer.objects.all()
#     return render(request, "facture_etape1.html", {"customers": customers})


from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Invoice, Customer

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Invoice, Article, Customer
from django.contrib import messages
# @login_required
# def creer_facture_etape1(request):
#     user = request.user
#     customers = Customer.objects.filter(save_by=user)

#     # Récupération des données de session
#     facture_id = request.session.get("facture_id", None)
#     articles = request.session.get("articles", [])
#     customer_id = request.session.get("customer_id", None)
#     logo = request.session.get("logo", None)

#     if request.method == "POST":
#         customer_id = request.POST.get("customer")
#         logo = request.FILES.get("logo")

#         if not customer_id:
#             messages.error(request, "Veuillez sélectionner un client.")
#             return redirect("creer_facture_etape1")

#         # Stocker les données en session
#         request.session["customer_id"] = customer_id  
#         if logo:
#             request.session["logo"] = logo.name  # Stocke seulement le nom du fichier logo

#         return redirect("creer_facture_etape2")  # Rediriger vers l'étape 2

#     return render(request, "facture_etape1.html", {
#         "customers": customers,
#         "articles": articles,
#         "selected_customer_id": customer_id,  # Renvoyer l'ID du client sélectionné
#         "logo": logo  # Renvoyer le logo stocké
#     })





@login_required
def creer_facture_etape1(request):
    user = request.user
    customers = Customer.objects.filter(save_by=user)  # Filtrer les clients de l'utilisateur connecté

    # Récupération des données de session
    invoice_id = request.session.get("invoice_id", None)
    articles = request.session.get("articles", [])
    customer_id = request.session.get("customer_id", None)
    logo = request.session.get("logo", None)

    if request.method == "POST":
        
        customer_id = request.POST.get("customer")
        logo = request.FILES.get("logo")

        if not customer_id:
            messages.error(request, "Veuillez sélectionner un client.")
            return redirect("creer_facture_etape1")

        request.session["customer_id"] = customer_id  # Stocke le client sélectionné
        request.session["logo"] = logo.name if logo else None  # Stocke le nom du fichier logo

        # Création de la facture
        customer = get_object_or_404(Customer, id=customer_id)
        invoice = Invoice.objects.create(
            customer=customer,
            save_by=user,
            logo=logo,
            total=sum(article["total"] for article in articles),
            invoice_type="I"
        )
    

        # Ajout des articles à la base de données
        for article in articles:
            Article.objects.create(
                invoice=invoice,
                designation=article["designation"],
                quantity=article["quantite"],
                unit_price=article["prix_unitaire"],
                famille = article["famille"]
            )

        # Nettoyer la session après validation
        request.session.pop("invoice_id", None)
        request.session.pop("articles", None)
        request.session.pop("customer_id", None)
        request.session.pop("logo", None)

        request.session.modified = True  # ✅ Force Django à enregistrer les changements
        # request.session.flush()  # ❌ Ne l'utilise que si tu veux TOUT effacer, y compris l'auth utilisateur

        messages.success(request, "Facture créée avec succès.")
        return redirect("home")


        # Nettoyer la session après validation
        # request.session.pop("invoice_id", None)
        # request.session.pop("articles", None)
        # request.session.pop("customer_id", None)
        # request.session.pop("logo", None)

        # messages.success(request, "Facture créée avec succès.")
        # return redirect("home")

    return render(request, "invoices/facture_etape1.html", {
        "customers": customers,
        "articles": articles,
        "selected_customer_id": customer_id,
        "logo": logo
    })





# @login_required
# def creer_facture_etape1(request):
#     user = request.user
#     customers = Customer.objects.filter(save_by=user)  # Filtrer les clients de l'utilisateur connecté
#     facture_id = request.session.get("facture_id", None)

#     articles = request.session.get("articles", [])  # Récupérer les articles temporairement stockés en session

#     if request.method == "POST":
#         customer_id = request.POST.get("customer")
#         logo = request.FILES.get("logo")

#         if not customer_id:
#             messages.error(request, "Veuillez sélectionner un client.")
#             return redirect("creer_facture_etape1")

#         customer = get_object_or_404(Customer, id=customer_id)

#         # Création de la facture
#         facture = Invoice.objects.create(
#             customer=customer,
#             save_by=user,
#             logo=logo,
#             total=sum(article["total"] for article in articles),  # Calcul du total
#             invoice_type="I"  # Type de facture par défaut
#         )

#         # Ajout des articles à la base de données
#         for article in articles:
#             Article.objects.create(
#                 invoice=facture,
#                 designation=article["designation"],
#                 quantite=article["quantite"],
#                 prix_unitaire=article["prix_unitaire"],
#                 total=article["total"]
#             )

#         # Nettoyer la session après création
#         request.session.pop("facture_id", None)
#         request.session.pop("articles", None)

#         messages.success(request, "Facture créée avec succès.")
#         return redirect("base")  # Redirection vers la page principale

#     return render(request, "facture_etape1.html", {"customers": customers, "articles": articles})


# def creer_facture_etape2(request):
#     facture_id = request.session.get("facture_id")
#     if not facture_id:
#         return redirect("creer_facture_etape1")

#     facture = get_object_or_404(Invoice, id=facture_id)

#     if request.method == "POST":
#         designation = request.POST.get("designation")
#         quantity = int(request.POST.get("quantity"))
#         unit_price = float(request.POST.get("unit_price"))
#         remise = float(request.POST.get("remise", 0))
#         tva = float(request.POST.get("tva", 0))

#         # Calcul du total HT
#         montant_ht = quantity * unit_price
#         total = montant_ht - (montant_ht * remise / 100)
#         total += total * tva / 100

#         Article.objects.create(
#             invoice=facture,
#             designation=designation,
#             quantity=quantity,
#             unit_price=unit_price,
#             remise=remise,
#             tva=tva,
#             montant_ht=montant_ht,
#         )

#         # Mise à jour du total de la facture
#         facture.total += total
#         facture.save()

#         return JsonResponse({"success": True, "total": facture.total})

#     articles = facture.article_set.all()
#     return render(request, "facture_etape2.html", {"facture": facture, "articles": articles})













@login_required
def creer_facture_etape2(request):


    if "articles" not in request.session:
        request.session["articles"] = []

    articles = request.session["articles"]
    customer_id = request.session.get("customer_id", None)  # 🔥 Récupère le client stocké
    selected_customer = None

    if customer_id:
        selected_customer = get_object_or_404(Customer, id=customer_id)  # 🔥 Retrouver l'objet Customer

    # return render(request, "facture_etape2.html", {
    #     "selected_customer": selected_customer  # On envoie à la template
    # })

    if request.method == "POST":
        designation = request.POST.get("designation")
        quantite = request.POST.get("quantite")
        prix_unitaire = request.POST.get("prix_unitaire")
        famille = request.POST.get("famille")


        if designation and quantite and prix_unitaire:
            quantite = int(quantite)
            prix_unitaire = float(prix_unitaire)
            total = quantite * prix_unitaire

            articles.append({
                "designation": designation,
                "quantite": quantite,
                "prix_unitaire": prix_unitaire,
                "famille" : famille,

                "total": total
            })

            request.session["articles"] = articles  # Mise à jour de la session
            request.session.modified = True  # Marquer la session comme modifiée

            messages.success(request, "Article ajouté avec succès.")

    return render(request, "invoices/facture_etape2.html", {"articles": articles})


# @login_required
# def creer_facture_etape2(request):
#     if "articles" not in request.session:
#         request.session["articles"] = []

#     articles = request.session["articles"]

#     if request.method == "POST":
#         designation = request.POST.get("designation")
#         quantite = request.POST.get("quantite")
#         prix_unitaire = request.POST.get("prix_unitaire")

#         if designation and quantite and prix_unitaire:
#             quantite = int(quantite)
#             prix_unitaire = float(prix_unitaire)
#             total = quantite * prix_unitaire

#             articles.append({
#                 "designation": designation,
#                 "quantite": quantite,
#                 "prix_unitaire": prix_unitaire,
#                 "total": total
#             })

#             request.session["articles"] = articles  # Mise à jour de la session
#             request.session.modified = True  # Marquer la session comme modifiée

#             messages.success(request, "Article ajouté avec succès.")

#     return render(request, "facture_etape2.html", {"articles": articles})

















#LAST VIEWS
from django.shortcuts import render

def services(request):
    return render(request, "services.html")


def formules(request):
    return render(request, "formules.html")


def plus_loin(request):
    return render(request, "plus_loin.html")

def base_customers(request):
    return render(request, 'customers/base_customers.html')

def base_invoices(request):
    return render(request, 'invoices/base_invoices.html')






#Ajouter clients professionnel
class AjouterClientProfessionnel(LoginRequiredSuperuserMixin, View):
    """ Ajouter un nouveau client (particulier ou professionnel) """

    template_name = 'customers/add_customer_professional.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        try:
            # Récupération des données du formulaire
            customer_type = "professionnel"
            # customer_type = request.POST.get('customer_type', 'professionnel')  # Valeur par défaut 'particulier'
            # customer_type = request.POST.get('customer_type_hidden', 'particulier')

            # customer_type = request.POST.get('customer_type', Customer.PARTICULIER)
            civilite = request.POST.get('civilite', '').strip()
            nom = request.POST.get('nom', '').strip()
            prenom = request.POST.get('prenom', '').strip()
            email = request.POST.get('email', '').strip()
            sex = request.POST.get('sex', '')
            telephone = request.POST.get('telephone', '').strip()
            adresse = request.POST.get('adresse', '').strip()
            code_postal = request.POST.get('code_postal', '').strip()
            ville = request.POST.get('ville', '').strip()
            pays = request.POST.get('pays', '').strip()
            raison_sociale = request.POST.get('raison_sociale', '').strip()
            siret = request.POST.get('siret', None)
            num_tva_intracom = request.POST.get('num_tva_intracom', '').strip()
            fax = request.POST.get('fax', '').strip()
            fonction = request.POST.get('fonction', '').strip()
            telephone_mobile = request.POST.get('telephone_mobile', '').strip()
            telephone_fixe = request.POST.get('telephone_fixe', '').strip()

            # Vérification des champs obligatoires
            if not nom or not email:
                messages.error(request, _("Le nom et l'email sont obligatoires."))
                return render(request, self.template_name)

            # Création de l'objet Customer
            customer = Customer.objects.create(
                customer_type=customer_type,
                civilite=civilite,
                nom=nom,
                prenom=prenom,
                email=email,
                sex=sex,
                telephone=telephone,
                adresse=adresse,
                code_postal=code_postal,
                ville=ville,
                pays=pays,
                raison_sociale=raison_sociale,
                siret=int(siret),
                num_tva_intracom=num_tva_intracom  ,
                fax=fax  ,
                fonction=fonction,
                telephone_mobile=telephone_mobile,
                telephone_fixe=telephone_fixe ,
                save_by=request.user
            )

            messages.success(request, _("Client enregistré avec succès."))
            return redirect('home')  # Redirection après ajout

        except Exception as e:
            messages.error(request, _(f"Erreur lors de l'enregistrement : {e}"))
            return render(request, self.template_name)
        


#Ajouter clients particulier
class AjouterClientParticulier(LoginRequiredSuperuserMixin, View):
    """ Ajouter un nouveau client (particulier ou professionnel) """

    template_name = 'customers/add_customer_particular.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        try:
            # Récupération des données du formulaire
            # customer_type = request.POST.get('customer_type', 'particulier')  # Valeur par défaut 'particulier'
            customer_type = "particulier"
            # customer_type = request.POST.get('customer_type_hidden', 'particulier')

            # customer_type = request.POST.get('customer_type', Customer.PARTICULIER)
            civilite = request.POST.get('civilite', '').strip()
            nom = request.POST.get('nom', '').strip()
            prenom = request.POST.get('prenom', '').strip()
            email = request.POST.get('email', '').strip()
            sex = request.POST.get('sex', '')
            telephone = request.POST.get('telephone', '').strip()
            adresse = request.POST.get('adresse', '').strip()
            code_postal = request.POST.get('code_postal', '').strip()
            ville = request.POST.get('ville', '').strip()
            pays = request.POST.get('pays', '').strip()


            # Vérification des champs obligatoires
            if not nom or not email:
                messages.error(request, _("Le nom et l'email sont obligatoires."))
                return render(request, self.template_name)

            # Création de l'objet Customer
            customer = Customer.objects.create(
                customer_type=customer_type,
                civilite=civilite,
                nom=nom,
                prenom=prenom,
                email=email,
                sex=sex,
                telephone=telephone,
                adresse=adresse,
                code_postal=code_postal,
                ville=ville,
                pays=pays,

                save_by=request.user
            )

            messages.success(request, _("Client enregistré avec succès."))
            return redirect('home')  # Redirection après ajout

        except Exception as e:
            messages.error(request, _(f"Erreur lors de l'enregistrement : {e}"))
            return render(request, self.template_name)



#Ajouter clients
class AjouterClient(LoginRequiredSuperuserMixin, View):
    """ Ajouter un nouveau client (particulier ou professionnel) """

    template_name = 'ajouter_client.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        try:
            # Récupération des données du formulaire
            customer_type = request.POST.get('customer_type', 'particulier')  # Valeur par défaut 'particulier'
            # customer_type = request.POST.get('customer_type_hidden', 'particulier')

            # customer_type = request.POST.get('customer_type', Customer.PARTICULIER)
            civilite = request.POST.get('civilite', '').strip()
            nom = request.POST.get('nom', '').strip()
            prenom = request.POST.get('prenom', '').strip()
            email = request.POST.get('email', '').strip()
            sex = request.POST.get('sex', '')
            telephone = request.POST.get('telephone', '').strip()
            adresse = request.POST.get('adresse', '').strip()
            code_postal = request.POST.get('code_postal', '').strip()
            ville = request.POST.get('ville', '').strip()
            pays = request.POST.get('pays', '').strip()
            raison_sociale = request.POST.get('raison_sociale', '').strip()
            siret = request.POST.get('siret', None)
            num_tva_intracom = request.POST.get('num_tva_intracom', '').strip()
            fax = request.POST.get('fax', '').strip()
            fonction = request.POST.get('fonction', '').strip()
            telephone_mobile = request.POST.get('telephone_mobile', '').strip()
            telephone_fixe = request.POST.get('telephone_fixe', '').strip()

            # Vérification des champs obligatoires
            if not nom or not email:
                messages.error(request, _("Le nom et l'email sont obligatoires."))
                return render(request, self.template_name)

            # Création de l'objet Customer
            customer = Customer.objects.create(
                customer_type=customer_type,
                civilite=civilite,
                nom=nom,
                prenom=prenom,
                email=email,
                sex=sex,
                telephone=telephone,
                adresse=adresse,
                code_postal=code_postal,
                ville=ville,
                pays=pays,
                raison_sociale=raison_sociale if customer_type == Customer.PROFESSIONNEL else None,
                siret=int(siret) if siret and customer_type == Customer.PROFESSIONNEL else None,
                num_tva_intracom=num_tva_intracom if customer_type == Customer.PROFESSIONNEL else None,
                fax=fax if customer_type == Customer.PROFESSIONNEL else None,
                fonction=fonction if customer_type == Customer.PROFESSIONNEL else None,
                telephone_mobile=telephone_mobile if customer_type == Customer.PROFESSIONNEL else None,
                telephone_fixe=telephone_fixe if customer_type == Customer.PROFESSIONNEL else None,
                save_by=request.user
            )

            messages.success(request, _("Client enregistré avec succès."))
            return redirect('home')  # Redirection après ajout

        except Exception as e:
            messages.error(request, _(f"Erreur lors de l'enregistrement : {e}"))
            return render(request, self.template_name)






#Ajouter factures
class AjouterFacture(LoginRequiredSuperuserMixin, View):
    """ add a new invoice view """

    template_name = 'ajouter_facture.html'

    customers = Customer.objects.select_related('save_by').all()

    context = {
        'customers': customers
    }

    def get(self, request, *args, ** kwargs):
        return render(request, self.template_name, self.context)


    @transaction.atomic()
    def post(self, request, *args, ** kwargs):

        items = []

        try:
            customer = request.POST.get('customer')
            type = request.POST.get('invoice_type')
            articles = request.POST.getlist('article')

            qties = request.POST.getlist('qty')
            units = request.POST.getlist('unit')
            total_a =request.POST.getlist('total-a')
            total = request.POST.get('total')

            comment = request.POST.get('comment')

            invoice_object = {
                'customer_id': customer,
                'save_by': request.user,
                'total': total,
                'invoice_type': type,
                'comments': comment
            }
            invoice = Invoice.objects.create(**invoice_object)
    
            for index, article in enumerate(articles):

                data = Article(
                    invoice_id = invoice.id,
                    name = article,
                    quantity=qties[index],
                    unit_price = units[index],
                    total = total_a[index],
                )
                items.append(data)

            created = Article.objects.bulk_create(items)

            if created:
                # Si tout se passe bien
                messages.success(request, _("Data saved successfully."))
                return redirect('home')  # Redirection vers une autre page après la soumission
            else:
                messages.error(request, _("Sorry, please try again the sent data is corrupt."))

        except Exception as e:
            messages.error(request, _(f"Sorry the following error has occured {e}."))

        return render(request, self.template_name, self.context)
    













# load content
from django.shortcuts import render
from django.http import JsonResponse

def load_content(request, page):
    templates = {
        'ajouter_client': 'partials/ajouter_client.html',
        'ajouter_facture': 'partials/ajouter_facture.html',
    }
    
    template_name = templates.get(page, None)
    
    if template_name:
        html_content = render(request, template_name).content.decode('utf-8')
        return JsonResponse({'html': html_content})
    
    return JsonResponse({'error': 'Page non trouvée'}, status=404)





from django.core.paginator import Paginator
from django.utils.translation import gettext as _
from django.contrib import messages
from django.shortcuts import render
from django.views import View
from .models import Customer
from .mixins import LoginRequiredSuperuserMixin

class CustomerListView(View):
    """ Afficher la liste des clients (particuliers et professionnels) """
    
    template_name = "customers/customer_list.html"
    
    def get(self, request, *args, **kwargs):
        customers = Customer.objects.all().order_by('-id')  # Trier du plus récent au plus ancien
        
        # Pagination (10 clients par page)
        paginator = Paginator(customers, 10)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        
        return render(request, self.template_name, {"page_obj": page_obj})


class EditCustomerView(LoginRequiredSuperuserMixin, View):
    """ Modifier un client existant """

    template_name = "customers/edit_customer.html"

    def get(self, request, pk, *args, **kwargs):
        customer = get_object_or_404(Customer, pk=pk)
        return render(request, self.template_name, {'customer': customer})

    def post(self, request, pk, *args, **kwargs):
        try:
            customer = get_object_or_404(Customer, pk=pk)

            # Mise à jour des informations du client
            customer.nom = request.POST.get('nom', customer.nom).strip()
            customer.prenom = request.POST.get('prenom', customer.prenom).strip()
            customer.email = request.POST.get('email', customer.email).strip()
            customer.telephone = request.POST.get('telephone', customer.telephone).strip()
            customer.adresse = request.POST.get('adresse', customer.adresse).strip()
            customer.ville = request.POST.get('ville', customer.ville).strip()
            customer.pays = request.POST.get('pays', customer.pays).strip()

            customer.save()

            messages.success(request, "Client modifié avec succès.")
            return redirect('home')  # Redirection après modification

        except Exception as e:
            messages.error(request, f"Erreur lors de la modification : {e}")
            return render(request, self.template_name, {'customer': customer})


class DeleteCustomerView(LoginRequiredSuperuserMixin, View):
    """ Supprimer un client """

    template_name = "customers/delete_customer.html"

    def get(self, request, pk, *args, **kwargs):
        customer = get_object_or_404(Customer, pk=pk)
        return render(request, self.template_name, {'customer': customer})

    def post(self, request, pk, *args, **kwargs):
        try:
            customer = get_object_or_404(Customer, pk=pk)
            customer.delete()
            messages.success(request, "Client supprimé avec succès.")
            return redirect('home')  # Redirection après suppression

        except Exception as e:
            messages.error(request, f"Erreur lors de la suppression : {e}")
            return render(request, self.template_name, {'customer': customer})


import csv
# from django.http import HttpResponse
# from .models import Customer

# def download_csv(request):
#     # Récupère tous les clients
#     customers = Customer.objects.all()

#     # Crée une réponse HTTP pour envoyer le fichier CSV
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename=clients.csv'
    
#     # Crée un writer CSV
#     writer = csv.writer(response)
    
#     # Écrire les en-têtes du CSV
#     writer.writerow(['ID', 'Nom', 'Email', 'Type', 'Ville', 'Pays'])
    
#     # Écrire les données des clients
#     for customer in customers:
#         writer.writerow([customer.id, customer.nom, customer.email, customer.get_customer_type_display(), customer.ville, customer.pays])
    
#     return response



# import reportlab

# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
# from django.http import HttpResponse
# from .models import Customer

# def download_pdf(request):
#     # Crée une réponse HTTP pour envoyer le fichier PDF
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename=clients.pdf'
    
#     # Crée un objet canvas pour dessiner le PDF
#     pdf = canvas.Canvas(response, pagesize=letter)
    
#     # Ajouter du texte dans le PDF
#     pdf.drawString(100, 750, "Liste des Clients")
    
#     customers = Customer.objects.all()
#     y_position = 730
#     for customer in customers:
#         pdf.drawString(100, y_position, f"{customer.id} - {customer.nom} {customer.prenom} - {customer.email}")
#         y_position -= 20  # Déplacer vers le bas pour chaque client
    
#     # Terminer le PDF et le renvoyer
#     pdf.showPage()
#     pdf.save()
    
#     return response



# import reportlab
# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
# from reportlab.lib import colors
# from django.http import HttpResponse
# from .models import Customer

# def download_pdf(request):
#     # Crée une réponse HTTP pour envoyer le fichier PDF
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename=clients.pdf'
    
#     # Crée un objet canvas pour dessiner le PDF
#     pdf = canvas.Canvas(response, pagesize=letter)
    
#     # Définir des styles de police et de couleur
#     pdf.setFont("Helvetica-Bold", 16)
#     pdf.setFillColor(colors.darkblue)
#     pdf.drawString(100, 750, "Liste des Clients")  # Titre de la page
    
#     # Revenir à une police normale pour la liste des clients
#     pdf.setFont("Helvetica", 10)
#     pdf.setFillColor(colors.black)
    
#     customers = Customer.objects.all()
#     y_position = 730  # Position initiale pour le premier client
    
#     # Ajouter les entêtes de colonnes
#     pdf.setFont("Helvetica-Bold", 12)
#     pdf.setFillColor(colors.grey)
#     pdf.drawString(100, y_position, "ID - Nom - Prénom - Email")
#     y_position -= 20  # Espacement entre l'entête et les données
    
#     # Remettre la police normale pour les données
#     pdf.setFont("Helvetica", 10)
#     pdf.setFillColor(colors.black)
    
#     # Remplir le PDF avec les données des clients
#     for customer in customers:
#         # Ajouter chaque client
#         pdf.drawString(100, y_position, f"{customer.id} - {customer.nom} {customer.prenom} - {customer.email}")
#         y_position -= 20  # Déplacer vers le bas pour chaque client
        
#         # Si le texte dépasse la page, ajouter une nouvelle page
#         if y_position < 100:
#             pdf.showPage()  # Crée une nouvelle page
#             pdf.setFont("Helvetica", 10)  # Reprend la même police pour la nouvelle page
#             pdf.setFillColor(colors.black)
#             y_position = 750  # Réinitialise la position Y en haut de la page
#             pdf.drawString(100, y_position, "ID - Nom - Prénom - Email")
#             y_position -= 20  # Espacement après l'entête
    
#     # Terminer le PDF et le renvoyer
#     pdf.showPage()
#     pdf.save()
    
#     return response


import reportlab
# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
# from reportlab.lib import colors
# from django.http import HttpResponse
# from .models import Customer

# def download_pdf(request):
#     # Crée une réponse HTTP pour envoyer le fichier PDF
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename=clients.pdf'
    
#     # Crée un objet canvas pour dessiner le PDF
#     pdf = canvas.Canvas(response, pagesize=letter)
    
#     # Définir des styles de police et de couleur
#     pdf.setFont("Helvetica-Bold", 16)
#     pdf.setFillColor(colors.darkblue)
#     pdf.drawString(100, 750, "Liste des Clients")  # Titre de la page
    
#     # Revenir à une police normale pour la table des clients
#     pdf.setFont("Helvetica", 10)
#     pdf.setFillColor(colors.black)
    
#     # Données des clients
#     customers = Customer.objects.all()
    
#     # Position initiale pour commencer à dessiner le tableau
#     y_position = 720
    
#     # Dessiner l'en-tête du tableau
#     pdf.setFont("Helvetica-Bold", 10)
#     pdf.setFillColor(colors.grey)
#     pdf.drawString(100, y_position, "ID")
#     pdf.drawString(150, y_position, "Nom")
#     pdf.drawString(250, y_position, "Prénom")
#     pdf.drawString(350, y_position, "Email")
#     y_position -= 20  # Réduire la position pour la ligne suivante
    
#     # Dessiner les données du tableau
#     pdf.setFont("Helvetica", 10)
#     pdf.setFillColor(colors.black)
    
#     for customer in customers:
#         pdf.drawString(100, y_position, str(customer.id))
#         pdf.drawString(150, y_position, customer.nom)
#         pdf.drawString(250, y_position, customer.prenom)
#         pdf.drawString(350, y_position, customer.email)
#         y_position -= 20  # Réduire la position pour la ligne suivante
        
#         # Si la position Y est trop basse, ajouter une nouvelle page
#         if y_position < 100:
#             pdf.showPage()  # Crée une nouvelle page
#             pdf.setFont("Helvetica", 10)  # Reprend la même police pour la nouvelle page
#             pdf.setFillColor(colors.black)
#             y_position = 750  # Réinitialise la position Y en haut de la page
#             # Redessiner l'en-tête sur la nouvelle page
#             pdf.drawString(100, y_position, "ID")
#             pdf.drawString(150, y_position, "Nom")
#             pdf.drawString(250, y_position, "Prénom")
#             pdf.drawString(350, y_position, "Email")
#             y_position -= 20  # Réduire la position après l'en-tête
    
#     # Dessiner des lignes pour délimiter les cellules du tableau
#     pdf.setStrokeColor(colors.black)
#     pdf.setLineWidth(0.5)
    
#     # Lignes horizontales
#     pdf.line(100, y_position + 10, 450, y_position + 10)  # Ligne après l'en-tête
    
#     # Lignes verticales
#     pdf.line(130, 720, 130, y_position + 10)  # Après "ID"
#     pdf.line(230, 720, 230, y_position + 10)  # Après "Nom"
#     pdf.line(330, 720, 330, y_position + 10)  # Après "Prénom"
    
#     # Terminer le PDF et le renvoyer
#     pdf.showPage()
#     pdf.save()
    
#     return response





from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer
from django.core.paginator import Paginator
import csv
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# def client_list(request):
#     search_query = request.GET.get('search', '')
#     customer_type = request.GET.get('customer_type', '')  # 'particulier' ou 'professionnel'
#     customers = Customer.objects.all()

#     # Filtrage des clients en fonction du type
#     if customer_type:
#         customers = customers.filter(customer_type=customer_type)

#     # Recherche par nom ou email si le champ de recherche est rempli
#     if search_query:
#         customers = customers.filter(
#             nom__icontains=search_query
#         ) | customers.filter(
#             email__icontains=search_query
#         )

#     # Pagination
#     page = request.GET.get('page', 1)
#     paginator = Paginator(customers, 10)  # Affiche 10 clients par page
#     page_obj = paginator.get_page(page)

#     return render(request, 'customers/client_list.html', {
#         'customers': page_obj,
#         'search_query': search_query,
#         'customer_type': customer_type
#     })

# # Vue pour télécharger la liste des clients en CSV
# def download_csv(request):
#     customer_type = request.GET.get('customer_type', '')
#     customers = Customer.objects.all()

#     if customer_type:
#         customers = customers.filter(customer_type=customer_type)

#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename=clients.csv'
    
#     writer = csv.writer(response)
#     writer.writerow(['ID', 'Nom', 'Email', 'Type', 'Ville', 'Pays'])
    
#     for customer in customers:
#         writer.writerow([customer.id, customer.nom, customer.email, customer.get_customer_type_display(), customer.ville, customer.pays])

#     return response

# # Vue pour télécharger la liste des clients en PDF
# def download_pdf(request):
#     customer_type = request.GET.get('customer_type', '')
#     customers = Customer.objects.all()

#     if customer_type:
#         customers = customers.filter(customer_type=customer_type)

#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename=clients.pdf'
    
#     pdf = canvas.Canvas(response, pagesize=letter)
#     pdf.drawString(100, 750, "Liste des Clients")

#     y_position = 730
#     for customer in customers:
#         pdf.drawString(100, y_position, f"{customer.id} - {customer.nom} {customer.prenom} - {customer.email}")
#         y_position -= 20
    
#     pdf.showPage()
#     pdf.save()

#     return response


from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Customer

def client_list(request):
    search_query = request.GET.get('search', '').strip()
    customer_type = request.GET.get('customer_type', '')  # 'particulier' ou 'professionnel'
    
    # Filtrer les clients selon les critères de recherche
    customers = Customer.objects.all()
    
    if customer_type:
        customers = customers.filter(customer_type=customer_type)
    
    if search_query:
        customers = customers.filter(
            Q(nom__icontains=search_query) | 
            Q(email__icontains=search_query) |
            Q(ville__icontains=search_query)|
            Q(pays__icontains=search_query)

        )

    # Pagination
    paginator = Paginator(customers, 10)  # 10 clients par page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'customers/client_list.html', {
        'customers': page_obj,
        'search_query': search_query,
        'customer_type': customer_type
    })


import csv
from django.http import HttpResponse

def download_csv(request):
    search_query = request.GET.get('search', '').strip()
    customer_type = request.GET.get('customer_type', '')

    customers = Customer.objects.all()

    if customer_type:
        customers = customers.filter(customer_type=customer_type)
    
    if search_query:
        customers = customers.filter(
            Q(nom__icontains=search_query) | 
            Q(email__icontains=search_query) |
            Q(ville__icontains=search_query)|
            Q(pays__icontains=search_query)
        )

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=clients.csv'

    writer = csv.writer(response)
    writer.writerow(['ID', 'Nom', 'Email', 'Type', 'Ville', 'Pays'])  # En-têtes du fichier CSV

    for customer in customers:
        writer.writerow([customer.id, customer.nom, customer.email, customer.customer_type, customer.ville, customer.pays])

    return response


from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def download_pdf(request):
    search_query = request.GET.get('search', '').strip()
    customer_type = request.GET.get('customer_type', '')

    customers = Customer.objects.all()

    if customer_type:
        customers = customers.filter(customer_type=customer_type)
    
    if search_query:
        customers = customers.filter(
            Q(nom__icontains=search_query) | 
            Q(email__icontains=search_query) |
            Q(ville__icontains=search_query)|
            Q(pays__icontains=search_query)            
        )

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=clients.pdf'

    pdf = canvas.Canvas(response, pagesize=letter)
    pdf.drawString(200, 750, "Liste des Clients Filtrés")
    
    y_position = 730
    for customer in customers:
        pdf.drawString(100, y_position, f"{customer.id} - {customer.nom} {customer.email} - {customer.customer_type}")
        y_position -= 20  # Espacement entre les lignes

    pdf.showPage()
    pdf.save()

    return response






#Liste factures reliée a creer_facture_etape1
from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Invoice, Customer
from django.http import HttpResponse
import csv
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

@login_required
def list_facture(request):
    search_query = request.GET.get("search", "").strip()
    montant_filter = request.GET.get("montant_filter", "").strip()
    montant_value = request.GET.get("montant_value", "").strip()

    factures = Invoice.objects.filter(save_by=request.user)  # Filtrer par utilisateur connecté

    # Filtrage par nom du client
    if search_query:
        factures = factures.filter(
            Q(customer__nom__icontains=search_query) | 
            Q(customer__email__icontains=search_query)
        )

    # Filtrage par montant
    if montant_filter and montant_value.isdigit():
        montant_value = float(montant_value)
        if montant_filter == "greater":
            factures = factures.filter(total__gt=montant_value)
        elif montant_filter == "less":
            factures = factures.filter(total__lt=montant_value)
        elif montant_filter == "equal":
            factures = factures.filter(total=montant_value)

    # Pagination (10 factures par page)
    paginator = Paginator(factures, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "invoices/facture_list.html", {
        "factures": page_obj,
        "search_query": search_query,
        "montant_filter": montant_filter,
        "montant_value": montant_value
    })


#telecharger factures csv:
@login_required
def download_factures_csv(request):
    search_query = request.GET.get("search", "").strip()
    montant_filter = request.GET.get("montant_filter", "").strip()
    montant_value = request.GET.get("montant_value", "").strip()

    factures = Invoice.objects.filter(save_by=request.user)

    if search_query:
        factures = factures.filter(
            Q(customer__nom__icontains=search_query) | 
            Q(customer__email__icontains=search_query)
        )

    if montant_filter and montant_value.isdigit():
        montant_value = float(montant_value)
        if montant_filter == "greater":
            factures = factures.filter(total__gt=montant_value)
        elif montant_filter == "less":
            factures = factures.filter(total__lt=montant_value)
        elif montant_filter == "equal":
            factures = factures.filter(total=montant_value)

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = "attachment; filename=factures.csv"

    writer = csv.writer(response)
    writer.writerow(["ID", "Client", "Total", "Date de Création"])

    for facture in factures:
        # writer.writerow([facture.id, facture.customer.nom, facture.total, facture.created_at])
        writer.writerow([facture.id, facture.customer.nom, facture.total, facture.invoice_date_time.strftime('%d-%m-%Y %H:%M')])


    return response


#telecharger factures pdf:
@login_required
def download_factures_pdf(request):
    search_query = request.GET.get("search", "").strip()
    montant_filter = request.GET.get("montant_filter", "").strip()
    montant_value = request.GET.get("montant_value", "").strip()

    factures = Invoice.objects.filter(save_by=request.user)

    if search_query:
        factures = factures.filter(
            Q(customer__nom__icontains=search_query) | 
            Q(customer__email__icontains=search_query)
        )

    if montant_filter and montant_value.isdigit():
        montant_value = float(montant_value)
        if montant_filter == "greater":
            factures = factures.filter(total__gt=montant_value)
        elif montant_filter == "less":
            factures = factures.filter(total__lt=montant_value)
        elif montant_filter == "equal":
            factures = factures.filter(total=montant_value)

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = "attachment; filename=factures.pdf"

    pdf = canvas.Canvas(response, pagesize=letter)
    pdf.drawString(200, 750, "Liste des Factures Filtrées")

    y_position = 730
    for facture in factures:
        # pdf.drawString(100, y_position, f"{facture.id} - {facture.customer.nom} - {facture.total} € - {facture.invoice_date_time}")
        #date et heure formatée: 
        pdf.drawString(100, y_position, f"{facture.id} - {facture.customer.nom} - {facture.total} DT - {facture.invoice_date_time.strftime('%d-%m-%Y %H:%M')}")

        y_position -= 20  # Espacement entre les lignes

    pdf.showPage()
    pdf.save()

    return response


#voir facture
from django.shortcuts import get_object_or_404, render
from .models import Invoice

@login_required
def voir_facture(request, facture_id):
    facture = get_object_or_404(Invoice, id=facture_id)
    return render(request, 'invoices/voir_facture.html', {'facture': facture})


#modifier_facture: VUE SANS FORM
# from django.shortcuts import get_object_or_404, redirect
# from django.contrib import messages
# from .forms import InvoiceForm  # À créer si nécessaire
# from .models import Invoice

# @login_required
# def modifier_facture(request, facture_id):
#     facture = get_object_or_404(Invoice, id=facture_id)
    
#     if request.method == 'POST':
#         form = InvoiceForm(request.POST, instance=facture)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Facture modifiée avec succès.')
#             return redirect('voir_facture', facture_id=facture.id)
#     else:
#         form = InvoiceForm(instance=facture)
    
#     return render(request, 'invoices/modifier_facture.html', {'form': form, 'facture': facture})
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Invoice

@login_required
def modifier_facture(request, facture_id):
    facture = get_object_or_404(Invoice, id=facture_id)
    
    if request.method == 'POST':
        # Modifier les champs spécifiques sans formulaire
        facture.customer = request.POST.get('customer', facture.customer)
        facture.total = request.POST.get('total', facture.total)
        facture.invoice_date_time = request.POST.get('invoice_date_time', facture.invoice_date_time)
        # Ajoutez d'autres champs que vous souhaitez permettre de modifier
        
        # Sauvegarder les modifications
        facture.save()
        
        messages.success(request, 'Facture modifiée avec succès.')
        return redirect('voir_facture', facture_id=facture.id)
    
    return render(request, 'invoices/modifier_facture.html', {'facture': facture})



#supprimer_facture
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Invoice

@login_required
def supprimer_facture(request, facture_id):
    facture = get_object_or_404(Invoice, id=facture_id)
    
    if request.method == 'POST':
        facture.delete()
        messages.success(request, 'Facture supprimée avec succès.')
        return redirect('list_facture')
    
    return render(request, 'invoices/supprimer_facture.html', {'facture': facture})

