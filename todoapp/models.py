from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model): # The Category table name that inherits models.Model
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True) # <--- added
    name = models.CharField(max_length=100) #Like a varchar 
    
    
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")    
    
    def __str__(self):
        return self.name #name to be shown when called

class TodoItem(models.Model): #TodoApp able name that inherits models.Model
    todolist = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=250) # a varchar
    content = models.TextField(blank=True) # a text field
    
        
    def __str__(self):
        return self.title #name to be shown when called