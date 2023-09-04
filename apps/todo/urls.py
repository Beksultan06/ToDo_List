from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TaskAPIViewSet

router = DefaultRouter()
router.register('tasks/', TaskAPIViewSet, basename='task')

urlpatterns = router.urls
