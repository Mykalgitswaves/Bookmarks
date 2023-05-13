from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    t = loader.get_template("login/form.html")
    context = { 'name': 'Cash Money' }
    return HttpResponse(t.render(context, request))