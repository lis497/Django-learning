
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
	return HttpResponse("Hello, <h1 style='color:orange'>Meow!</h1>")

def greet(request, name):
	#return HttpResponse(f"Hello, {name}!")
	print(type(request))
	print(request)
	#request is a dictionary_like object, return a key
	print(dict(request).keys())
	return render(request, "hello/greet.html",{
			"name": name
		})

