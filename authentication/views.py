# from django.shortcuts import render

# # Create your views here.


# from django.shortcuts import render, redirect
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.http import JsonResponse
# from .models import *
# from .serializers import RegisterSerializer
# from django.contrib.auth.hashers import make_password
# from django.contrib import auth
# import datetime
# from datetime import timedelta
# from datetime import datetime as dt
# import requests
# import json
# from django.http import HttpResponseRedirect


# today = datetime.date.today()


# def home(request):
# 	return render(request, 'index.html')


	

# def signin(request):
# 	return render(request, 'login.html')

# def check_mail_ajax(request):
# 	if request.is_ajax():
# 		email = request.GET.get('email', None)
# 		check_email = User.objects.filter(email=email).exists()
# 		if check_email == True:
# 			response = {'error': 'Email already exists.'}
# 			return JsonResponse(response)
# 		else:
# 			response = {'success': 'Cool'}
# 			return JsonResponse(response)
# 	else:
# 		response = {'error': 'Error Email Checking.'}
# 		return JsonResponse(response)





# class Login(APIView):
# 	def post(self, request):
# 		email = request.data.get('email')
# 		password = request.data.get('password')

# 		# Let us check if the user exists or not...
# 		check_email = User.objects.filter(email=email).exists()
# 		if check_email == False:
# 			return Response({'error': 'No account with such email'})
# 		# We need to check if the user password is correct
# 		user = User.objects.get(email=email)
# 		if user.check_password(password) == False:
# 			return Response({'error': 'Password is not correct. Try again'})
# 		# Now let us log the user in
# 		log_user = auth.authenticate(email=email, password=password)
# 		if user is not None:
# 			auth.login(request, log_user)
# 			return Response({'success': 'Login successful'})
# 		else:
# 			return Response({'error': 'Invalid email/password. Try again later.'})






from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from .models import *
from .serializers import RegisterSerializer
from django.contrib.auth.hashers import make_password
from django.contrib import auth
import datetime
from datetime import timedelta
from datetime import datetime as dt
import requests
import json
from django.http import HttpResponseRedirect

from subscription.models import UserMembership, PayHistory, Membership

today = datetime.date.today()
def signin(request):
	return render(request, 'login.html')

def check_mail_ajax(request):
	if request.is_ajax():
		email = request.GET.get('email', None)
		check_email = User.objects.filter(email=email).exists()
		if check_email == True:
			response = {'error': 'Email already exists.'}
			return JsonResponse(response)
		else:
			response = {'success': 'Cool'}
			return JsonResponse(response)
	else:
		response = {'error': 'Error Email Checking.'}
		return JsonResponse(response)


class Register(APIView):
	def post(self, request):
		serializer = RegisterSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			obj = serializer.save()
			password = make_password(serializer.data['password'])
			User.objects.filter(email=serializer.data['email']).update(password=password)
			get_membership = Membership.objects.get(membership_type='Free')
			instance = UserMembership.objects.create(user=obj, membership=get_membership)
			return Response({'success': 'Registration successful.'})
		else:
			return Response({'error': 'Error. Try again'})


def home(request):
	return render(request, 'index.html')

def index(request):
	user_membership = UserMembership.objects.get(user=request.user)
	subscriptions = Subscription.objects.filter(user_membership=user_membership).exists()
	if subscriptions == False:
		return redirect('sub')
	else:
		subscription = Subscription.objects.filter(user_membership=user_membership).last()
		return render(request, 'home.html', {'sub': subscription})
	



class Login(APIView):
	def post(self, request):
		email = request.data.get('email')
		password = request.data.get('password')

		# Let us check if the user exists or not...
		check_email = User.objects.filter(email=email).exists()
		if check_email == False:
			return Response({'error': 'No account with such email'})
		# We need to check if the user password is correct
		user = User.objects.get(email=email)
		if user.check_password(password) == False:
			return Response({'error': 'Password is not correct. Try again'})
		# Now let us log the user in
		log_user = auth.authenticate(email=email, password=password)
		if user is not None:
			auth.login(request, log_user)
			return Response({'success': 'Login successful'})
		else:
			return Response({'error': 'Invalid email/password. Try again later.'})











from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

# class Login(APIView):
#     def post(self, request):
#         email = request.data.get('email')
#         password = request.data.get('password')

#         # Vérifier si l'email existe
#         if not User.objects.filter(email=email).exists():
#             return Response({'error': 'Aucun compte trouvé avec cet email.'}, status=400)

#         # Vérifier si le mot de passe est correct
#         user = authenticate(request, username=email, password=password)
#         if user is None:
#             return Response({'error': 'Mot de passe incorrect. Réessayez.'}, status=400)

#         # Authentification réussie
#         # Générer ou récupérer le token pour l'utilisateur
#         token, created = Token.objects.get_or_create(user=user)

#         # Enregistrer l'utilisateur et son token dans la session
#         request.session['user_id'] = user.id
#         request.session['token'] = token.key

#         # Retourner une réponse de succès avec le token
#         return Response({'success': 'Connexion réussie', 'token': token.key}, status=200)




# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token

# class Login(APIView):
#     def post(self, request):
#         email = request.data.get('email')
#         password = request.data.get('password')

#         if not User.objects.filter(email=email).exists():
#             return Response({'error': 'Aucun compte trouvé avec cet email.'}, status=400)

#         user = authenticate(request, username=email, password=password)
#         if user is None:
#             return Response({'error': 'Mot de passe incorrect. Réessayez.'}, status=400)

#         login(request, user)  # ← Création de session

#         token, created = Token.objects.get_or_create(user=user)

#         # Récupération du sessionid après login
#         sessionid = request.session.session_key

#         return Response({
#             'success': 'Connexion réussie',
#             'token': token.key,
#             'sessionid': sessionid,
#             'dashboardurl': f"http://localhost:8501/?sessionid={sessionid}"
#         }, status=200)


# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login
# from rest_framework.authtoken.models import Token
# from django.contrib.sessions.models import Session

# def login_view(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         user = authenticate(request, username=email, password=password)
        
#         if user is not None:
#             login(request, user)
#             token, created = Token.objects.get_or_create(user=user)
            
#             # Enregistrement du token dans la session
#             request.session['user_id'] = user.id
#             request.session['token'] = token.key
#             return redirect('dashboard_redirect')
#         else:
#             # Erreur d'authentification
#             return render(request, 'login.html', {'error': 'Identifiants invalides'})
    
#     return render(request, 'login.html')






#LOGIN
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # ou tableau de bord
        else:
            return render(request, 'auth/login.html', {'error': 'Identifiants invalides'})
    return render(request, 'auth/login.html')



#SIGN UP
from django.contrib.auth import get_user_model
User = get_user_model()

def signup_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        if User.objects.filter(email=email).exists():
            return render(request, 'auth/signup.html', {'error': 'Email déjà utilisé'})
        
        user = User.objects.create_user(
            email=email,
            password=password,
            username=username,
            first_name=first_name,
            last_name=last_name
        )
        return redirect('authentication:login')
    
    return render(request, 'auth/signup.html')




# #LOG OUT
# from django.contrib.auth.views import LogoutView

# # Déjà inclus dans urls.py
# path('logout/', LogoutView.as_view(next_page='login'), name='logout'),



from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import json
from django.contrib.auth import get_user_model
User = get_user_model()


@login_required
def user_data(request):
    user = request.user
    data = {
        'email': user.email,
        'username': user.username,
        'invoices': list(user.invoices.values())  # Adaptez à votre modèle
    }
    return JsonResponse(data)

def check_session(request):
    if request.user.is_authenticated:
        return JsonResponse({'authenticated': True})
    return JsonResponse({'authenticated': False}, status=401)





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


