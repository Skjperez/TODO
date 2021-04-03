from django.contrib import admin
from .models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'description', 'complete',
        'duedate', 'created_date', 'modified_date'
        )
admin.site.register(Task, TaskAdmin)