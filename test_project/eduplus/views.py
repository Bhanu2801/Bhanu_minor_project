from django.http import Http404
from .forms import QuestionForm,ChoiceForm
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
#from django.template import RequestContext,loader
from .models import Question,Choice
from django.core.urlresolvers import reverse

# def search_titles(request):
#     questions=SearchQuerySet().autocomplete(content_auto=request.POST.get('search_text',''))
def home(request):
		title="question forum"
		form=QuestionForm(request.POST or None)

		if form.is_valid():
			instance=form.save(commit=False)
			instance.save()

		context={
			"title":title,
			"form":form
		}
		#	print instance.email

		return render(request,'eduplus/home.html',context)




def index(request):
	latest_question_list=Question.objects.order_by('-pub_date')[:500]
	#template=loader.get_template('eduplus/index.html')
	context={'latest_question_list':latest_question_list,}
	#check
	output=','.join([p.question_text for p in latest_question_list])
#	return HttpResponse(template.render(context))
	#return HttpResponse(output)
	return render(request,'eduplus/index.html',context)
def detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    title="choice forum"
    form=ChoiceForm(request.POST,request.FILES,initial={'question':question})
 
    if form.is_valid():
        # instance=form.save(choice_fill=request.FILES['choice_fill'])
        instance=form.save()
        instance.save()
    context={
            "title":title,
            "form":form,
            "question":question
        }
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    return render(request, 'eduplus/detail.html',context)

def vote(request, question_id):
    # import pdb;pdb.set_trace()
    #abc=request.form.get('choice')
    #print abc
    choice_id = request.POST.get('choice')
    choice = Choice.objects.get(pk=choice_id)
    choice.votes += 1
    print choice.votes
    choice.save()
    return HttpResponse("You are voting on question %s." %question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)
