from django.shortcuts import render, redirect
from .models import TodoApp, Category

# Create your views here.

def index(request): #the index view
    todos = TodoApp.objects.all() #quering all todos with the object manager
    categories = Category.objects.all() #getting all categories with object manager
    if request.method == "POST": #checking if the request method is a POST 
        if "taskAdd" in request.POST: #checking if there is a request to add a todo
            title = request.POST["description"] #title
            content = title

            Todo = TodoApp(title=title, content=content) 
            Todo.save() #saving the todo 
            return redirect("/") #reloading the page 

        if "taskDelete" in request.POST: #checking if there is a request to delete a todo
            checkedlist = request.POST["checkedbox"] #checked todos to be deleted
            for todo_id in checkedlist:
                todo = TodoApp.objects.get(id=int(todo_id)) #getting todo id
                todo.delete() #deleting todo
    return render(request, "index.html", {"todos": todos, "categories":categories})