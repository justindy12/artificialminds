from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class StudentForm(forms.ModelForm):

	class Meta:
		model = Student
		fields = ('firstname','lastname','idnum','email','password')
	