from django.conf.urls import url

from . import views

urlpatterns = [
	#ex: /users/
	url(r'^$', views.index, name='index'),
	#ex: /users/kowawakoala
	url(r'^(?P<username>[\s\S]*)/$', views.display, name='display'),
]
