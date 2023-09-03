from django.shortcuts import render

from apps.todo.models import Task
from apps.todo.serializers import TaskSerializer
# Create your views here.
class TodoAPI():
    queruset = Task.objects.all()
    serialaizers_class = TaskSerializer

    
