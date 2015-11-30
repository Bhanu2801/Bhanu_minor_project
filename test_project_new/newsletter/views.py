from django.shortcuts import render
from .forms import ContactForm,SignUpForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home(request):
	title='welcome'
	#title="MY TITLE %s" %(request.user)
	#if request.method=="POST":
	#	print request.POST
	form=SignUpForm(request.POST)
	context = {
		"template_title": title,
		"form": form
	}
	if form.is_valid():
		instance=form.save(commit="False")
		instance.save()
		context = {
			"template_title": "thank you"
		}
	return render(request,"rage2.html",context)




def profile(request):
	return render(request,"profile.html",{})

def about(request):
	return render(request,"rondon.html",{})




def contact(request):
	form=ContactForm(request.POST or None)
	if form.is_valid():
		form_email = form.cleaned_data.get("email")
		full_name = form.cleaned_data.get("full_name")
		subject ='verification mail'
		from_email= settings.EMAIL_HOST_USER
		to_email = [from_email,'meharfzr@gmail.com']
		contact_message = '%s, we are happy that you now are part of the EduCamp community.We hope you would like being a part of it'%(full_name)
		send_mail(subject, contact_message,from_email,to_email,fail_silently=False)
		#for key,value in form.cleaned_data.iteritems():
		#	print key,value
			#print form.cleaned_data
	context={
		"form":form
	}
	return render(request,"forms.html",context)
	