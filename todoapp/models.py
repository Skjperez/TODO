from django.db import models
from django.utils import timezone

class Category(models.Model): # The Category table name that inherits models.Model
    name = models.CharField(max_length=100) #Like a varchar    
    
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")    
    
    def __str__(self):
        return self.name #name to be shown when called

class TodoApp(models.Model): #TodoApp able name that inherits models.Model
    title = models.CharField(max_length=250) # a varchar
    content = models.TextField(blank=True) # a text field
    
        
    def __str__(self):
        return self.title #name to be shown when called