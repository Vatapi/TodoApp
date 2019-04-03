from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class ToDoList(models.Model):
    user = models.ForeignKey(to=User , on_delete=models.CASCADE)
    title = models.CharField(max_length = 100)
    content = models.TextField()
    todo_date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.title
