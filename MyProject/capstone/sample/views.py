from django.shortcuts import render, redirect
from django.http import Http404
from django.http import HttpResponse
from django.views.generic import View
from .forms import *
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
					#messages.success(request, 'Your account has been successfully registered!')
					return redirect('sample:login')


class AdviserRegistrationView(View):
		def get(self, request):
			return render(request, 'registerAdviser.html')

		def post(self,request):
			form = AdviserForm(request.POST)

			if form.is_valid():
				firstname = request.POST['firstname']
				lastname = request.POST['lastname']
				idnum = request.POST['idnum']
				email = request.POST['email']
				contact = request.POST['contact']
				password = request.POST['password']
				cpassword = request.POST['cpassword']

				if password != cpassword:
					messages.error(request, 'Password do not match')
					return redirect('sample:aregister')

				elif password == cpassword:
					form = Adviser(firstname=firstname, lastname=lastname, idnum = idnum, email = email, contact = contact, password = password)	
					form.save()
					print('adviser created')
					return redirect('sample:login')

def login(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')
		students = Student.objects.all()

		if Student.objects.filter(email=email).count() != 0 :
			account = Student.objects.get(email=email)
			print('account')
			if account.password == password:
				print('login successful')
				Student.objects.filter(email=email).update(isLoggedIn = True)
				return redirect('sample:home')

			elif account.password != password: 
				messages.error(request, 'Incorrect Password')
				return render(request,'login.html')

		else:
			messages.error(request, 'Username does not exist!')
			return render(request,'login.html')
	else:
		return render(request,'login.html')

def alogin(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')
		adviser = Adviser.objects.all()

		if Adviser.objects.filter(email=email).count() != 0:
			account = Adviser.objects.get(email=email)
			print('adviser account')
			if account.password == password:
				print('adviser login successful')
				Adviser.objects.filter(email=email).update(isLoggedIn = True)
				return redirect('sample:ahome')

			elif account.password != password:
				messages.error(request,'Incorrect Password')
				return render(request,'alogin.html')

		else:
			messages.error(request,'Username does not exist!')
			return render(request,'alogin.html')
	else:
		return render(request,'alogin.html')

class HomeView(View):
	def get(self, request):
		students = Student.objects.all()
		
		for student in students:
			if(student.isLoggedIn == True):
				return render(request, 'home.html', {'student':student})
	
		return redirect('sample:login')

class AdviserHomeView(View):
	def get(self, request):
		advisers = Adviser.objects.all()

		for adviser in advisers:
			if(adviser.isLoggedIn == True):
				return render(request, 'homeAdviser.html', {'adviser':adviser})

		return redirect('sample:alogin')

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
		students = Student.objects.all()
		advisers = Adviser.objects.all()

		for student in students:
			if(student.isLoggedIn == True):
				Student.objects.update(isLoggedIn = False)
		

		for adviser in advisers:
			if(adviser.isLoggedIn == True):
				Adviser.objects.update(isLoggedIn = False)

		print('user successfully log out')
		return redirect('sample:index')

class SetAppointmentView(View):
		def get(self, request):
			advisers = Adviser.objects.all()
			students = Student.objects.all()

			for student in students:
				if(student.isLoggedIn == True):
					context ={
						'adviser':advisers,
						'student':students,
					}
					return render(request, 'setappointment.html', {'student':student, 'adviser':advisers})

		def post(seld, request):
			form = AppointmentForm(request.POST)

			if form.is_valid():
				student_id = request.POST['student_id']
				meeting_type = request.POST['meeting_type']
				meeting_urgency = request.POST['meeting_urgency']
				meeting_counselor = request.POST['meeting_counselor']
				meeting_date = request.POST['meeting_date']
				meeting_time = request.POST['meeting_time']

				form = Appointment(meeting_type=meeting_type, meeting_urgency=meeting_urgency, meeting_counselor=meeting_counselor, meeting_date=meeting_date, meeting_time=meeting_time, student_id=student_id)
				form.save()
				print('appointment saved')
				return redirect('sample:home')
			
			else:
				return redirect('sample:setappointment ')
class ViewAppointmentView(View):
		def get(self, request):
			return render(request, 'viewappointment.html')

class AdviserLoginView(View):
		def get(self, request):
			return render(request, 'loginAdviser.html')
