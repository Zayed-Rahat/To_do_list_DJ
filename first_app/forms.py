from django import forms
from .models import TaskModel

class TaskStoreForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['task_title','task_description']
       
        