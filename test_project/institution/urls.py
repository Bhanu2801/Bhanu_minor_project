from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns=[
		url(r'^(?P<institute_id>[0-9]+)/$', views.detail, name='detailed'),
		url(r'^(?P<institute_id>[0-9]+)/update$', views.detail2, name='detailed2'),
		]