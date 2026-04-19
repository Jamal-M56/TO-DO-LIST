from django import forms
from .models import Task

class TaskForms(forms.ModelForm):

    class Meta:

        model = Task
        fields = [
            'title',
            'discription',
            'status',
            'deadline',
            'user',
        ]
        widgets = {
            'title':forms.TextInput(),
            'discription':forms.Textarea(),
            'status':forms.Select(),
            'deadline':forms.DateTimeInput(attrs={'type':'datetime-local'})

        }
