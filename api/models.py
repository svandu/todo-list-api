from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# Todolist model
class TodoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Task(models.Model):
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE, null=True)
    task = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task
