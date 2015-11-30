from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns=[
	url(r'^$', views.index, name='indexe'),
   url(r'^home/$', views.home, name='homee'),
   url(r'^home2/$', views.home2, name='home2e'),


    # ex: /eduplus/5/
   url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detaile'),
    # ex: /eduplus/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /eduplus/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]

