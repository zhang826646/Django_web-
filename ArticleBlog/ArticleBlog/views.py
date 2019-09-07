from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render_to_response


def index(request):
    return render_to_response('index.html',{})
def about(request):
    return render_to_response('about.html',{})
def newlist(request):
    return render_to_response('newlist.html',{})
def listpic(request):
    return render_to_response('listpic.html',{})