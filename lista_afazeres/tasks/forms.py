from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    city = forms.CharField(max_length=100, required=False, help_text="Enter city for weather info")

    class Meta:
        model = Task
        fields = ['title', 'description', 'completed', 'due_date', 'category']
