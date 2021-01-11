from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
	tasks = Task.objects.all() #grabs all tasks from database

	form = TaskForm()

	if request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save() #saves to db
		return redirect('/')

	context = {'tasks':tasks, 'form':form}
	return render(request, 'list.html', context)

def updateTask(request, primary_key):
	task = Task.objects.get(id=primary_key)
	return render(request, 'update_task.html')