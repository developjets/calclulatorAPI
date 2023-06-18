from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    template = loader.get_template('home/index.html')
    page_title = "Home"
    context = {
        'page_title' : page_title,
    }
    return HttpResponse(template.render(context, request))