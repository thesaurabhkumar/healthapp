# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return render(request, 'homeapp/home.html',{'login_status': request.user.is_authenticated(),
                                                'username': request.user.username
												})