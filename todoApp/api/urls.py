from django.urls import path
from rest_framework import routers
from .views import CategoryViewSet, TaskViewSet

router = routers.SimpleRouter()
router.register('category', CategoryViewSet, basename='category')  # категории тасок
router.register('task', TaskViewSet, basename='task')  # таски

urlpatterns = [

]

urlpatterns += router.urls
