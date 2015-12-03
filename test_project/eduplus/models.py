import datetime
from django.db import models
from django.utils import timezone
# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    def __unicode__(self):
    	return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def get_absolute_url(self):
        return "/eduplus/%s/" % self.id
class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.TextField()
    choice_fill = models.FileField(upload_to='profile/%Y/%m/%d',blank=True,null=True)
    votes = models.IntegerField(default=0)
    def __unicode__(self):
    	return self.choice_text
