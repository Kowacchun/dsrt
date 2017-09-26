# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse

from .models import User

# Create your views here.

def index(request):
	userList = User.objects.all()
	context = {'userList': userList}
	return render(request, 'users/index.html', context)

def display(request, username):
	user = get_object_or_404(User, username=username)
	return render(request, 'users/display.html', {'user': user})
