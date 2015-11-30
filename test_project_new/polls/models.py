import datetime
from django.db import models
from django.utils import timezone
# Create your models here.
class College(models.Model):
	college_text=models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	def __unicode__(self):
		return self.college_text

class Rating(models.Model):
	college=models.ForeignKey(College)
	rating=models.BigIntegerField()
	views=models.CharField(max_length=200)
	def __unicode__(self):
		return self.views


