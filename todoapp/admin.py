from django.contrib import admin
from . import models

# Register your models here.

class TodoAppAdmin(admin.ModelAdmin):
    list_display = ("title")
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    
admin.site.register(models.TodoApp)
admin.site.register(models.Category, CategoryAdmin)
