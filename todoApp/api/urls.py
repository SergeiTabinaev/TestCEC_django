from django.urls import path
from rest_framework import routers
from .views import CategoryViewSet, TaskViewSet

router = routers.SimpleRouter()
router.register('category', CategoryViewSet, basename='category')  # категории тасок
router.register('task', TaskViewSet, basename='task')  # таски

urlpatterns = [
    # path('tasks/', TaskViewSet.as_view({   # список всех тасок
    #     'get': 'list',
    #     'post': 'create',
    # })),
    # path('task/<str:pk>', TaskViewSet.as_view({  # эндпоинты для работы с тасками
    #     'get': 'retrieve',
    #     'put': 'update',
    #     'delete': 'destroy'
    # })),
]

urlpatterns += router.urls
