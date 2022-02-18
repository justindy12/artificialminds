from django.shortcuts import render, redirect
from django.http import Http404
from django.http import HttpResponse
from django.views.generic import View
from .forms import StudentForm
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login

# Create your views here.

class IndexView(View):
		def get(self, request):
			return render(request, 'index.html')

		# def post(self, request):
		# 	if 'login' in request.POST:
		# 		return redirect('sample:register')


class RegistrationView(View):
		def get(self, request):
			return render(request, 'register.html')

		def post(self, request):
			fname = request.POST['firstname']
			lname = request.POST['lastname']
			idnum = request.POST['idnum']
			email = request.POST['email']
			password = request.POST['password']
			cpassword = request.POST['cpassword']

			user = User.objects.create_user(username=email,first_name=fname, last_name=lname, password=password)
			user.save()
			print('user created')
			return redirect('sample:login')
		

def login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = auth.authenticate(username = username, password = password)

		if user is not None:
			auth.login(request, user)
			return redirect("sample:home")
		else:
			messages.error(request, 'Username and Password do not match!')
			return redirect('sample:login')

	else:
		return render(request,'login.html')

class HomeView(View):
	def get(self, request):
		return render(request, 'home.html')

class AboutView(View):
		def get(self, request):
			return render(request, 'about.html')

class ContactView(View):
		def get(self, request):
			return render(request, 'contact.html')
			
class SettingView(View):
		def get(self, request):
			return render(request, 'setting.html')
	
class LogoutView(View):
		def get(self, request):
			return render(request, 'logout.html')

class SetAppointmentView(View):
		def get(self, request):
			return render(request, 'setappointment.html')