import datetime
from django.db import models
from django.utils import timezone

class Institute(models.Model):
	name=models.TextField()
	about=models.TextField()
	courses=models.TextField()
	pub_date=models.DateTimeField(default=datetime.datetime.now)

	def __unicode__(self):
		return self.name

	def get_absolute_url(self):
  		return "/institution/%s/" % self.id

class Rating(models.Model):
	institute=models.ForeignKey(Institute)
	rating=models.BigIntegerField()
	views=models.CharField(max_length=200)
	def __unicode__(self):
		return self.views
