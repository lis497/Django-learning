from django.shortcuts import render

# Create your views here.
tasks =["foo Meow", "bar Dog", "baz Nimo"]

def index(request):
	return render(request, "todos/index.html",
		{
			"todos": tasks
		})

def add(request):
	return render(request, "todos/add.html")