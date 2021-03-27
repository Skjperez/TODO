from django.shortcuts import render
from .models import Task
# Create your views here.

def UserTaskList(request):
    if request.user.is_authenticated is True:
        user = request.user
    else:
        user = None
    user_task_list = Task.objects.filter(user=user)
    context = {'user_task_list': user_task_list}
    return render(request, 'newtodo/todolist.html', context)