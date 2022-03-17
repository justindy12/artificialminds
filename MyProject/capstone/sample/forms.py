from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class StudentForm(forms.ModelForm):

	class Meta:
		model = Student
		fields = ('firstname','lastname','idnum','email','course','year','gender','contact','password')

class AdviserForm(forms.ModelForm):

	class Meta:
		model = Adviser
		fields = ('firstname','lastname','idnum','email','contact','password')


class AppointmentForm(forms.ModelForm):

	class Meta:
		model = Appointment
		fields = ('meeting_type','meeting_date','meeting_time','meeting_counselor')