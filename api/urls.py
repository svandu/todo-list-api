from django.urls import path, include
from api.views import TodoListView, TaskView

urlpatterns = [
    path('todolist/', TodoListView.as_view(), name='todo-list'),
    path('todolist/<int:pk>/', TodoListView.as_view(), name='todo-list-details'),

    path('task/', TaskView.as_view(), name='task'),
    path('task/<int:id>/', TaskView.as_view(), name='task-details'),
]