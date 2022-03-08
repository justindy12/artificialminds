from django.db import models
from django import forms
from datetime import datetime

class Student(models.Model):
	firstname = models.CharField(max_length = 100)
	lastname = models.CharField(max_length = 100)
	idnum = models.CharField(max_length = 20)
	email = models.EmailField()
	course = models.CharField(max_length = 100)
	year = models.CharField(max_length = 100)
	gender = models.CharField(max_length = 100)
	contact = models.CharField(max_length = 100)
	password = models.CharField(max_length = 100)
	isLoggedIn = models.BooleanField(default = False)
	isDeleted = models.IntegerField(default = 0)


	class Meta:
		db_table = "student"


class Adviser(models.Model):
    firstname = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    idnum = models.CharField(max_length = 20)
    email = models.EmailField()
    contact = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    available_anytime = models.IntegerField(default = 0)
    schedule_date = models.DateField(null=True)
    schedule_time = models.TimeField(null=True)
    isLoggedIn = models.BooleanField(default = False)
    isDeleted = models.IntegerField(default = 0)

    class Meta:
        db_table = "adviser" 

class Appointment(models.Model):
	student = models.ForeignKey(Student, null = False, blank = False, on_delete = models.CASCADE, related_name = "Student")
	meeting_type = models.CharField(max_length = 100)
	meeting_urgency = models.CharField(max_length = 100)
	meeting_status = models.IntegerField(default = 0)
	meeting_counselor = models.CharField(max_length = 100)
	meeting_date = models.DateField(null=False) 
	meeting_time = models.CharField(max_length = 100)

	class Meta:
		db_table = "appointment"