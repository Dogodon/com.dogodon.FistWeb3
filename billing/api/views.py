from django.http import JsonResponse

def get_articles(request):
    data = {"message": "Liste des articles"}
    return JsonResponse(data)




from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from ..models import Article, Invoice
from django.http import JsonResponse


# @csrf_exempt
# def save_articles(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             invoice = Invoice.objects.first()  # Remplace par la logique d'identification de la facture
#             articles = data.get('articles', [])

#             for item in articles:
#                 Article.objects.create(
#                     invoice=invoice,
#                     designation=item['designation'],
#                     quantity=int(item['quantity']),
#                     unite=item.get('unite', ''),
#                     unit_price=float(item['unit_price']),
#                     remise=float(item['remise']),
#                     tva=float(item['tva']),
#                     montant_ht=float(item['montant_ht']),
#                     reference=item.get('reference', ''),
#                     famille=item['famille'],
#                     prix_achat_ht=float(item['prix_achat_ht']) if item['prix_achat_ht'] else None,
#                     taux_marge=float(item['taux_marge']) if item['taux_marge'] else None
#                 )

#             return JsonResponse({'message': 'Articles enregistrés avec succès'}, status=201)

#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=400)

#     return JsonResponse({'error': 'Méthode non autorisée'}, status=405)


@csrf_exempt
def save_articles(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            invoice_id = data.get('invoice_id')

            if not invoice_id:
                return JsonResponse({'error': 'ID de facture manquant'}, status=400)

            invoice = get_object_or_404(Invoice, id=invoice_id)
            articles = data.get('articles', [])

            if not articles:
                return JsonResponse({'error': 'Aucun article fourni'}, status=400)

            items = []
            for item in articles:
                article = Article(
                    invoice=invoice,
                    designation=item['designation'],
                    quantity=int(item['quantity']),
                    unite=item.get('unite', ''),
                    unit_price=float(item['unit_price']),
                    remise=float(item['remise']),
                    tva=float(item['tva']),
                    montant_ht=float(item['montant_ht']),
                    reference=item.get('reference', ''),
                    famille=item['famille'],
                    prix_achat_ht=float(item['prix_achat_ht']) if item.get('prix_achat_ht') else None,
                    taux_marge=float(item['taux_marge']) if item.get('taux_marge') else None
                )

                # Vérification et ajout de l'image
                if 'img' in request.FILES:
                    article.img = request.FILES['img']  # Corriger le nom de la clé
                    article.save()

                items.append(article)

            Article.objects.bulk_create(items)

            return JsonResponse({'message': 'Articles enregistrés avec succès'}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Format JSON invalide'}, status=400)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Méthode non autorisée'}, status=405)













# ✅ Vue Étape 1 - Création de la facture
from django.shortcuts import render, redirect, get_object_or_404
from models import Invoice, Customer, Article
from django.http import JsonResponse
from django.core.files.storage import default_storage

def creer_facture_etape1(request):
    if request.method == "POST":
        titre = request.POST.get("titre")
        logo = request.FILES.get("logo")
        customer_id = request.POST.get("customer")

        customer = get_object_or_404(Customer, id=customer_id)
        facture = Invoice.objects.create(
            customer=customer,
            total=0,  # Initialisation
            comments=titre
        )
        
        # Stocker l'ID de la facture temporairement en session
        request.session["facture_id"] = facture.id

        return redirect("creer_facture_etape2")

    customers = Customer.objects.all()
    return render(request, "facture_etape1.html", {"customers": customers})



# ✅ Vue Étape 2 - Ajout des articles
def creer_facture_etape2(request):
    facture_id = request.session.get("facture_id")
    if not facture_id:
        return redirect("creer_facture_etape1")

    facture = get_object_or_404(Invoice, id=facture_id)

    if request.method == "POST":
        designation = request.POST.get("designation")
        quantity = int(request.POST.get("quantity"))
        unit_price = float(request.POST.get("unit_price"))
        remise = float(request.POST.get("remise", 0))
        tva = float(request.POST.get("tva", 0))

        # Calcul du total HT
        montant_ht = quantity * unit_price
        total = montant_ht - (montant_ht * remise / 100)
        total += total * tva / 100

        Article.objects.create(
            invoice=facture,
            designation=designation,
            quantity=quantity,
            unit_price=unit_price,
            remise=remise,
            tva=tva,
            montant_ht=montant_ht,
        )

        # Mise à jour du total de la facture
        facture.total += total
        facture.save()

        return JsonResponse({"success": True, "total": facture.total})

    articles = facture.article_set.all()
    return render(request, "facture_etape2.html", {"facture": facture, "articles": articles})
















# # views.py
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import SessionAuthentication

# @api_view(['GET'])
# def user_data_view(request):
#     if request.user.is_authenticated:
#         return Response({
#             "username": request.user.username,
#             "email": request.user.email,
#             "invoices": list(Invoice.objects.filter(user=request.user).values())
#         })
#     return Response({"detail": "Non authentifié"}, status=401)


# from django.shortcuts import redirect

# def redirect_to_dashboard(request):
#     session_id = request.COOKIES.get('sessionid')
#     dashboard_url = f"http://localhost:8501/?sessionid={session_id}"
#     return redirect(dashboard_url)


# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def user_data(request):
#     user = request.user
#     invoices = user.invoices.all().values()  # adapter selon ton modèle
#     return Response({
#         "username": user.username,
#         "email": user.email,
#         "invoices": list(invoices),
#     })


