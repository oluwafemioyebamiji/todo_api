from rest_framework import generics
from .models import Todo
# from .serializers import TodoSerializer
from todo import serializers

class TodoListView(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = serializers.TodoFewSerializer


class TodoCreateView(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = serializers.TodoFewSerializer


class AdminTodoListCreateView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = serializers.TodoSerializer


class AdminTodoEditView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = serializers.TodoSerializer

