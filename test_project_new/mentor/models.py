import datetime
from django.db import models
from django.utils import timezone
# Create your models here.
from django.db import models
class Mentor(models.Model):
	mentor_name=models.CharField(max_length=200)
	mentor_email=models.EmailField(max_length=200)
	mentor_city=models.CharField(max_length=200)
	mentor_qualification=models.CharField(max_length=200)
	mentor_qualification1=models.CharField(max_length=200,blank=True)
	mentor_qualification2=models.CharField(max_length=200,blank=True)
	pub_date=models.DateTimeField('date published')
	def __unicode__(self):
		return self.mentor_name
class Student(models.Model):
	name=models.ForeignKey(Mentor)
	student_name=models.CharField(max_length=200)
	city=models.CharField(max_length=200)
	email=models.EmailField(max_length=200)
	course=models.CharField(max_length=200)
	def __unicode__(self):
		return self.student_name