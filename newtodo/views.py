from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Task
from .forms import TaskForm
import logging
# Create your views here.

def UserTaskList(request):
    if request.user.is_authenticated is True:
        user = request.user
    else:
        user = None
    user_task_list = Task.objects.filter(user=user)
    context = {
        'task_list': user_task_list,
        'task_form': TaskForm()
        }
    return render(request, 'newtodo/todolist.html', context)

def CreateTask(request):
    #check if the user is logged in
    if request.user.is_authenticated is True:
        # if this is a POST request we need to process the form data
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = TaskForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                t = Task(
                    user=request.user,
                    description=form.cleaned_data['description'],
                    duedate=form.cleaned_data['duedate'],
                    complete=False
                    )
                t.save()
                return HttpResponseRedirect('/')



    # if a GET (or any other method) we'll create a blank form
    else:
        return HttpResponseRedirect('/')

def DeleteTask(request, task_id):
    t = Task.objects.get(id=task_id)
    t.delete()
    return HttpResponseRedirect('/')

def CompleteTask(request, task_id):
    t = Task.objects.get(id=task_id)
    t.complete = True
    t.save()
    return HttpResponseRedirect('/')

def IncompleteTask(request, task_id):
    t = Task.objects.get(id=task_id)
    t.complete = False
    t.save()
    return HttpResponseRedirect('/')