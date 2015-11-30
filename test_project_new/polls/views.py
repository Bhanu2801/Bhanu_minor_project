from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import Http404
from django.shortcuts import render
from .models import College,Rating
from .forms import CollegeForm,RatingForm


def home(request):
        title="College forum"
        form=CollegeForm(request.POST or None)

        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()

        context={
            "title":title,
            "form":form
        }
        #   print instance.email

        return render(request,'polls/college.html',context)

def home2(request):
        title="Rating forum"
        form=RatingForm(request.POST or None)

        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()

        context={
            "title":title,
            "form":form
        }
        #   print instance.email

        return render(request,'polls/rating.html',context)




def index(request):
    latest_college_list = College.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    context = {'latest_college_list': latest_college_list,
    }
    return render(request,'polls/index.html',context)
    #return HttpResponse(template.render(context))
def index2(request):
    latest_college_list = College.objects.order_by('-pub_date')[:5]
    
    #template = loader.get_template('polls/index2.html')
    context = {'latest_college_list': latest_college_list,
    }
    return render(request,'polls/index2.html',context)
    #return HttpResponse(template.render(context))
def detail(request, college_id):
    college=College.objects.get(pk=college_id)

    # print college
    # for clg in college:
    # print college.rating_set.all()
    sm_avg = 0.0
    for rating in college.rating_set.all():
        sm_avg += rating.rating

    avg = float(sm_avg)/len(college.rating_set.all())
    #template=loader.get_template('polls/detail.html')
    context={'college':college, 'avg': avg}

    # context={'college':college, 'avg': avg}
    return render(request,'polls/detail.html',context)
    #return HttpResponse(template.render(context))
def comments(request,college_id):
    college=College.objects.get(pk=college_id)
    
    
    #template=loader.get_template('polls/comments.html')
    context={'college':college}
    #return HttpResponse(template.render(context))
    return render(request,'polls/comments.html',context)




   # return HttpResponse("You're looking at question %s." % question_id)