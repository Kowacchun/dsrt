from django.conf.urls import url

from . import views

urlpatterns = [
	#ex: /users/
	url(r'^$', views.index, name='index'),
	#ex: /users/login/
	url(r'^login/$', views.login, name='login'),
	#ex: /users/signup/
	url(r'^signup/$', views.signup, name='signup'),
	#ex: /users/kowawakoala/
	url(r'^(?P<username>[\s\S]*)/$', views.display, name='display'),
]
