from django.db import models

class Student(models.Model):
	firstname = models.CharField(max_length = 100)
	lastname = models.CharField(max_length = 100)
	idnum = models.CharField(max_length = 20)
	email = models.EmailField()
	password = models.CharField(max_length = 100)

	class Meta:
		db_table = "student"
