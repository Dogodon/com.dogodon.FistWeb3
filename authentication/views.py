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