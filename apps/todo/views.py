from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated  # Добавим импорт разрешения IsAuthenticated
from rest_framework.generics import DestroyAPIView
from rest_framework.response import Response


from apps.todo.models import Task
from apps.todo.serializers import TaskSerializer

class TaskAPIViewSet(GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]  # Добавим разрешение IsAuthenticated
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
class ToDoAllDeleteAPIViewSet(DestroyAPIView):
    queryset = Task.objects.all()
    
    def delete(self, request, *args, **kwargs):
        todo = Task.objects.filter(user=request.user)
        todo = [t for t in todo.delete()]
        return Response({'delete' : 'Все задания удалены'})

    