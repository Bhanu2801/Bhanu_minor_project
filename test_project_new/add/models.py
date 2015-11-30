from django.db import models

# Create your models here.
class SignUp(models.Model):
	email=models.EmailField()
	full_name=models.CharField(max_length=20,blank=True,null=True)
	timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)

	comments=models.CharField(max_length=20,blank=True,null=True)
    image = models.FileField(upload_to='profile/%Y/%m/%d')



	def __unicode__(self):
		return self.email


    