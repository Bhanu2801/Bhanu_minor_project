from django.http import Http404
from .forms import QuestionForm,ChoiceForm
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
#from django.template import RequestContext,loader
from .models import Question,Choice
from django.core.urlresolvers import reverse
# Create your views here.
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


def home2(request):
    title="choice forum"
    form=ChoiceForm(request.POST or None)

    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
    context={
            "title":title,
            "form":form
        }
    return render(request,'eduplus/home2.html',context)


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
    try:
        question = Question.objects.get(pk=question_id)

    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'eduplus/detail.html', {'question': question})
#def details(request,question_id):
#	try:
#		question=Question.objects.get(pk=question_id)
#	except Question.DoesNotExist:
#		raise Http404("Question doesnot exist")
#	return render(request,'eduplus/detail.html',{'question':question})
	#question=get_object_or_404(Question,pk=question_id)
	#return render(request,'eduplus/detail.html',{'question':question})
#	return HttpResponse("You are looking at question %s."%question_id)
#def results(request,question_id):
#	response="you are looking at results of question %s."
#	return HttpResponse(response % question_id)
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
#def index(request):
 #   return HttpResponse("Hello, world. You're at the polls index.")
#def detail(request, question_id):
 #   return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)
#def vote(request, question_id):
    #p = get_object_or_404(Question, pk=question_id)
    #try:
    #    selected_choice = p.choice_set.get(pk=request.POST['choice'])
    #except (KeyError, Choice.DoesNotExist):
    #    # Redisplay the question voting form.
    #    return render(request, 'polls/detail.html', {
    #       'question': p,
    #        'error_message': "You didn't select a choice.",
    #    })
    #else:
    #    selected_choice.votes += 1
    #    selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
    #    return HttpResponseRedirect(reverse('/eduplus/(?P<question_id>[0-9]+)/results/', args=(p.id,)))






    #return HttpResponse("You're voting on question %s." % question_id)