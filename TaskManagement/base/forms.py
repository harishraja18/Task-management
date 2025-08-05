from django import forms
from .models import TaskManagement

class TaskRead(forms.ModelForm):
    class Meta:
        model = TaskManagement
        fields = ['name','task_name','contact','description','priority','status','due_date']
