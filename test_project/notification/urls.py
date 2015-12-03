from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^show/(?P<notification_id>[0-9]+)/$', 'views.show_notification'),
	url(r'^delete/(?P<notification_id>[0-9]+)/$', 'views.delete_notification'),
	]