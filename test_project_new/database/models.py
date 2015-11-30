from django.db import models

# Create your models here.
class info(models.Model):
	cname=models.TextField()
	cabout=models.TextField()
	course=models.TextField()
	def __unicode__(self):
		return self.cname