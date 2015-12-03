from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Feedback
from .forms import FeedbackForm
def home(request):
	title="Feedback form"
	form=FeedbackForm(request.POST or None)

	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()

	context={
		"title":title,
		"form":form
	}
		#	print instance.email

	return render(request,'feedback/home.html',context)
	