import datetime
from django.db import models
from django.utils import timezone
# Create your models here.
class Feedback(models.Model):
	email=models.EmailField(max_length=200)
	feedback=models.CharField(max_length=500)
	pub_date = models.DateTimeField('date published')
	def __unicode__(self):
		return self.feedback