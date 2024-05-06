from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TodoList, Task
from .serializers import TodoListSerializer, TaskSerializer, UserSerializer, UserLoginSerializer
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login , logout

# Create your views here.
class TodoListView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                todo_list = TodoList.objects.get(pk=pk)
                serializer = TodoListSerializer(todo_list)
                response_data = {
                    'message': 'Success',
                    'data': serializer.data
                }
                return Response(response_data, status=status.HTTP_200_OK)
            except TodoList.DoesNotExist:
                return Response({'message': 'Todo List not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            todo_lists = TodoList.objects.all()
            serializer = TodoListSerializer(todo_lists, many=True)
            response_data = {
                'message': 'Success',
                'data': serializer.data
            }
            return Response(response_data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TodoListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'message': 'Success',
                'data': serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            todo_list = TodoList.objects.get(pk=pk)
            todo_list.delete()
            response_data = {
                'message': 'Success',
                'data': {}
            }
            return Response(response_data, status=status.HTTP_200_OK)
        except TodoList.DoesNotExist:
            return Response({'message': 'Todo List not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            todo_list = TodoList.objects.get(pk=pk)
            serializer = TodoListSerializer(todo_list, data=request.data)
            if serializer.is_valid():
                serializer.save()
                response_data = {
                    'message': 'Success',
                    'data': serializer.data
                }
                return Response(response_data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except TodoList.DoesNotExist:
            return Response({'message': 'Todo List not found'}, status=status.HTTP_404_NOT_FOUND)

class TaskView(APIView):
    def get(self, request, id=None):
        if id:
            try:
                tasks = Task.objects.filter(todo_list=id)
                serializer = TaskSerializer(tasks, many=True)
                response_data = {
                    'message': 'Success',
                    'data': serializer.data
                }
                return Response(response_data, status=status.HTTP_200_OK)
            except Task.DoesNotExist:
                return Response({'message': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            tasks = Task.objects.all()
            serializer = TaskSerializer(tasks, many=True)
            response_data = {
                'message': 'Success',
                'data': serializer.data
            }
            return Response(response_data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'message': 'Success',
                'data': serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            task = Task.objects.get(pk=id)
            task.delete()
            response_data = {
                'message': 'Success',
                'data': {}
            }
            return Response(response_data, status=status.HTTP_200_OK)
        except Task.DoesNotExist:
            return Response({'message': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        try:
            task = Task.objects.get(pk=id)
            serializer = TaskSerializer(task, data=request.data)
            if serializer.is_valid():
                serializer.save()
                response_data = {
                    'message': 'Success',
                    'data': serializer.data
                }
                return Response(response_data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Task.DoesNotExist:
            return Response({'message': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')

            # Check if username already exists
            if get_user_model().objects.filter(username=username).exists():
                return Response({'message': 'Username is already taken'}, status=status.HTTP_400_BAD_REQUEST)
                
            # Create the user
            user = get_user_model().objects.create(
                username=username,
                password=make_password(password)  # Hash the password
            )

            # Obtain JWT token for the user
            refresh = RefreshToken.for_user(user)
            token = str(refresh.access_token)

            # Prepare response data
            response_data = {
                'message': 'User registered successfully',
                'data': UserSerializer(user).data,
                'token': token
            }

            return Response(response_data, status=status.HTTP_200_OK)
          
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView): 
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            # Authenticate user
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')
            user = authenticate(username=username, password=password)

            if user:
                # Generate JWT token
                refresh = RefreshToken.for_user(user)
                token = str(refresh.access_token)
            
                # Prepare response data with token
                response_data = {
                    'message': 'Login successful',
                    'token': token
                }
                return Response(response_data, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
