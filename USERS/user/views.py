from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.

def index(request):
    return HttpResponse(f"<h1>Main page</h1>")
