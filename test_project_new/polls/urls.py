from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='indexp'),
    url(r'^index2/$', views.index2, name='index2p'),
	url(r'^(?P<college_id>[0-9]+)/$', views.detail, name='detailp'),
	url(r'^(?P<college_id>[0-9]+)/comments/$', views.comments, name='comments'),
    url(r'^home/$', views.home, name='homep'),
    url(r'^home2/$', views.home2, name='home2p'),

]