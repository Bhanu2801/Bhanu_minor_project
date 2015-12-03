from .models import Institute,Rating
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from .forms import RatingForm
# Create your views here.
def detail(request, institute_id):
    # try:
    institute = Institute.objects.get(pk=institute_id)

    # except Institute.DoesNotExist:
    #     raise Http404("Institute does not exist")
    form=RatingForm(request.POST or None)
    if form.is_valid():
		instance=form.save(commit="False")
		instance.save()
    context = {
		"form": form,
		"institute": institute
	}

    return render(request, 'institution/detail.html',context)


def detail2(request, institute_id):
    institute=Institute.objects.get(pk=institute_id)

    # print college
    # for clg in college:
    # print college.rating_set.all()
    sm_avg = 0.0
    for rating in institute.rating_set.all():
        sm_avg += rating.rating

    avg = float(sm_avg)/len(institute.rating_set.all())
    #template=loader.get_template('polls/detail.html')
    context={'institute':institute, 'avg': avg}

    # context={'college':college, 'avg': avg}
    return render(request,'institution/detail2.html',context)