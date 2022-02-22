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
			form = StudentForm(request.POST)

			if form.is_valid():
				firstname = request.POST['firstname']
				lastname = request.POST['lastname']
				idnum = request.POST['idnum']
				email = request.POST['email']
				course = request.POST['course'] 
				year = request.POST['year']
				gender = request.POST['gender']
				contact = request.POST['contact']
				password = request.POST['password']
				cpassword = request.POST['cpassword']

				if password != cpassword:
					messages.error(request, 'Password do not match!')
					return redirect('sample:register')

				elif password == cpassword:
					form = Student(firstname=firstname, lastname=lastname, idnum = idnum, email = email,  course = course, year = year, gender = gender, contact = contact, password = password)
					form.save()
					print('student created')
					return redirect('sample:login')


def login(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')

		if Student.objects.filter(email=email).count() != 0 :
			account = Student.objects.get(email=email)
			print('account')
			if account.password == password:
				print('login successful')
				return redirect('sample:home')

			else: 
				messages.error(request, 'Incorrect Password')

		else:
			messages.error(request, 'Username does not exist!')
			return render(request,'login.html')
	else:
		return render(request,'login.html')


class HomeView(View):
	def get(self, request):
		student_list = Student.objects.all()
		for student in student_list:
				print(student)
		print(student_list)

		context ={
				'qs' : student_list
			}
	
		return render(request, 'home.html', context)


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

class ViewAppointmentView(View):
		def get(self, request):
			return render(request, 'viewappointment.html')