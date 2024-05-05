from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TodoList, Task
from .serializers import TodoListSerializer, TaskSerializer

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
                return Response({'message': 'Todo List not found'}, status=status.HTTP_404_NOT_FOUND)
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
            return Response({'message': 'Todo List not found'}, status=status.HTTP_404_NOT_FOUND)

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
            return Response({'message': 'Todo List not found'}, status=status.HTTP_404_NOT_FOUND)