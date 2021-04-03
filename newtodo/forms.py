from django import forms

class TaskForm(forms.Form):
    description = forms.CharField(label='Task Description', max_length=100)
    duedate = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'date'})
        )