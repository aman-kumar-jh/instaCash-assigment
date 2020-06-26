from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

class Task(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(null=False,)
    date = models.DateField(null=False,)
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,)
    completed_task = models.BooleanField(default=False)
    
    def complete_task(self):
        self.completed_task = True
        self.save()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('task_detail', args=[str(self.id)])
    

