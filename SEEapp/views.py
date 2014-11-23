from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader, Context, Template

from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.core.mail import send_mail
from django.db import IntegrityError

import json
import string
import random

# Create your views here.


def root(request):
	if request.method == "GET":
		template = loader.get_template("SEEapp/index.html")
		context = Context()
		return HttpResponse(template.render(context))


def about(request):
	return HttpResponse(loader.get_template("SEEapp/aboutUs.html").render(Context()))

def videos(request):
	return HttpResponse(loader.get_template("SEEapp/videos.html").render(Context()))

def getinvolved(request):
	return HttpResponse(loader.get_template("SEEapp/getinvolved.html").render(Context()))

def team(request):
	return HttpResponse(loader.get_template("SEEapp/page-typography.html").render(Context()))
