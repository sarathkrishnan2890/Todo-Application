from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Tasks(models.Model):
    task = models.CharField(max_length=500, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null = True, blank=True)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(default='')

    def __str__(self):
        return self.task

    class meta:
        ordering = ['completed']
