from django.db import models
from django import forms
from datetime import datetime


class Student(models.Model):
	studentID = models.AutoField(primary_key = True)
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
	adviserID = models.AutoField(primary_key = True)
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
	appointmentID = models.AutoField(primary_key = True)
	student = models.ForeignKey(Student, null = False, blank = False, on_delete = models.CASCADE, related_name = "Student")
	meeting_counselor = models.ForeignKey(Adviser, null = False, blank = False, on_delete = models.CASCADE, related_name = "Adviser")
	meeting_type = models.CharField(max_length = 100)
	meeting_status = models.CharField(max_length = 100, default = "pending")
	meeting_date = models.DateField(default = datetime.now()) 
	meeting_time = models.TimeField(null = False)
	is_Approved = models.IntegerField(default = 0)

	class Meta:
		db_table = "appointment"


class RoomMember(models.Model):
	name = models.CharField(max_length=200)
	uid = models.CharField(max_length=200)
	room_name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Room(models.Model):
	name = models.CharField(max_length=1000)

class Message(models.Model):
	value = models.CharField(max_length=1000)
	date = models.DateTimeField(default=datetime.now, blank=True)
	user = models.CharField(max_length=1000)
	room = models.CharField(max_length=1000)