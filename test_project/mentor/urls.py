from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='indexm'),
    url(r'^(?P<mentor_id>[0-9]+)/$', views.detail, name='detailm'),
    url(r'^home/$', views.home, name='homem'),
    url(r'^home2/$', views.home2, name='home2m'),




]