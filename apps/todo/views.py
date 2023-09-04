from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated  # Добавим импорт разрешения IsAuthenticated


from apps.todo.models import Task
from apps.todo.serializers import TaskSerializer
# Create your views here.
class TaskAPIViewSet(GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]  # Добавим разрешение IsAuthenticated


    