from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TaskAPIViewSet

from rest_framework_simplejwt.views import TokenObtainPairView


router = DefaultRouter()
router.register('tasks/', TaskAPIViewSet, basename='task')

urlspatterns = [
    path("task", TokenObtainPairView.as_view(), name='task'),
]

urlpatterns = router.urls
