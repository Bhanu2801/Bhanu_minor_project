from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.calc, name='calc'),
    url(r'^([0-9]+)/$', views.test, name='teste')
    ]