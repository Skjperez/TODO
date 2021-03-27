from django.urls import path
from .views import UserTaskList

urlpatterns = [
    path('', UserTaskList, name='user_task_list')
]