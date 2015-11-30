from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Mentor,Student
from .forms import MentorForm,StudentForm

def home(request):
		title="Mentor form"
		form=MentorForm(request.POST or None)

		if form.is_valid():
			instance=form.save(commit=False)
			instance.save()

		context={
			"title":title,
			"form":form
		}
		#	print instance.email

		return render(request,'mentor/home.html',context)

def home2(request):
    title="Student form"
    form=StudentForm(request.POST or None)

    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
    context={
            "title":title,
            "form":form
        }
    return render(request,'mentor/home2.html',context)


# Create your views here.
def index(request):
	latest_mentor_list=Mentor.objects.order_by('-pub_date')[:100]
	template=loader.get_template('mentor/index.html')
	context=RequestContext(request,{'latest_mentor_list':latest_mentor_list,})
	return HttpResponse(template.render(context))





	return HttpResponse(output)
def detail(request, mentor_id):
    try:
        mentor = Mentor.objects.get(pk=mentor_id)
    except Mentor.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'mentor/detail.html', {'mentor': mentor})