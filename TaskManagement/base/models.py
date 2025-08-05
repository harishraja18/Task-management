from django.db import models

# Create your models here.

class TaskManagement(models.Model):
    name = models.CharField(max_length=100)
    task_name = models.CharField(max_length=100)
    contact = models.IntegerField()
    description = models.TextField()
    priority = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    due_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name