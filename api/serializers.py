from rest_framework import serializers
from django.contrib.auth import authenticate
from api.models import TodoList, Task
from django.contrib.auth.models import User

#create serializers here
class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model= TodoList
        fields="__all__"

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model= Task
        fields="__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']  # You might want to include more fields here
        extra_kwargs = {'password': {'write_only': True}}  # Ensure password is write-only

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        # Authenticate user
        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError('Invalid credentials')

        return data