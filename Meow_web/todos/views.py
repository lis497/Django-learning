from django import forms
from django.shortcuts import render

# Create your views here.
tasks =["foo Meow", "bar Dog", "baz Nimo"]

class NewTaskForm(forms.Form):
	task = forms.CharField(label="Add Task")
	priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)


def index(request):
	return render(request, "todos/index.html", {
			"todos": tasks
		})

def add(request):
	return render(request, "todos/add.html",{
			"form":NewTaskForm()
		})