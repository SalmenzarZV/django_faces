from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Im at the faces index!")

# Create your views here.
