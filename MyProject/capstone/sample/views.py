from django.shortcuts import render, redirect
from django.http import Http404
from django.http import HttpResponse
from django.views.generic import View
from .forms import StudentForm
from django.contrib import messages
from .models import *
# Create your views here.

class IndexView(View):
		def get(self, request):
			return render(request, 'index.html')

		# def post(self, request):
		# 	if 'login' in request.POST:
		# 		return redirect('sample:register')


class RegistrationView(View):
		def get(self, request):
			return render(request,'register.html')

		def post(self,request):
			form = StudentForm(request.POST)

			if form.is_valid():
				fname = request.POST.get("firstname")
				lname = request.POST.get("lastname")
				idnum = request.POST.get("idnum")
				email = request.POST.get("email")
				password = request.POST.get("password")
				cpassword = request.POST.get("cpassword")

				if password != cpassword:
					messages.info(request, 'Passwords do not match!')
					return redirect('sample:register')

				elif password == cpassword:
					form = Student(firstname = fname, lastname = lname, idnum = idnum, email = email, password = password)
					form.save()
					return render(request,'login.html')

			else:
				print(form.errors)
				return HttpResponse('not valid')


class LoginView(View):
		def get(self, request):
			return render(request, 'login.html')