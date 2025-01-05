
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
	return HttpResponse("Hello, <h1 style='color:orange'>Meow!</h1>")

def greet(request, name):
	return HttpResponse(f"Hello, {name}!")
