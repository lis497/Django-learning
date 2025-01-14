from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
#tasks =["foo Meow", "bar Dog", "baz Nimo"]

class NewTaskForm(forms.Form):
	task = forms.CharField(label="Add Task")
	priority = forms.IntegerField(label="Priority", min_value=1, max_value=5)


def index(request):
	#print("at the beginning", dict(request.session))
	if 'todos' not in request.session:
		request.session["todos"] = []
		#print("in if", dict(request.session))
	return render(request, "todos/index.html", {
			"todos": request.session["todos"]
		})

def add(request):
	if request.method == "POST":
		form = NewTaskForm(request.POST)
		#print(type(form),form.is_valid(),form)
		#print(form.cleaned_data)
		if form.is_valid():
			task = form.cleaned_data["task"]
			#!!! request.session["todos"].append(task)
			request.session["todos"] += [task]
			# append not works here
			return HttpResponseRedirect(reverse("todos:index"))
		else:
			return render(request, "todos/add.html",{
					"form": form
				})

	return render(request, "todos/add.html",{
			"form":NewTaskForm()
		})