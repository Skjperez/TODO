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

def UpdateTask(request, task_id):
    # get task by the id
    t = Task.objects.get(id=task_id)

    # generate form with task object data preloaded
    form = TaskForm(
        initial=
            {
                "description": t.description,
                "duedate": t.duedate,
            }
        )

    # preload context with form
    context = {
        'task_form': form,
        'username': request.user,
        'task_id': task_id
    }

    # save task with updated data and return to home page
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            t.description = form.cleaned_data["description"]
            t.duedate = form.cleaned_data["duedate"]
            t.save()
            return HttpResponseRedirect('/')
    
    #load update template with form
    return render(request, 'newtodo/update.html', context)