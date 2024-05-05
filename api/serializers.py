from rest_framework import serializers
from api.models import TodoList, Task

#create serializers here
class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model= TodoList
        fields="__all__"

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model= Task
        fields="__all__"