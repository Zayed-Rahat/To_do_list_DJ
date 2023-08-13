from django.db import models
from django.utils import timezone
from django.utils.text import slugify

class TaskModel(models.Model):
    id = models.IntegerField(primary_key=True)
    task_title = models.CharField(max_length=100)
    task_description = models.TextField()
    is_completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.task_title