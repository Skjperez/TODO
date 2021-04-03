from django.urls import path
from .views import UserTaskList, CreateTask, DeleteTask, CompleteTask, IncompleteTask

urlpatterns = [
    path('', UserTaskList, name='user_task_list'),
    path('create-task', CreateTask, name='create_task'),
    path('delete-task/<int:task_id>', DeleteTask, name='delete_task'),
    path('complete-task/<int:task_id>', CompleteTask, name='complete_task'),
    path('incomplete-task/<int:task_id>', IncompleteTask, name='incomplete_task')

]