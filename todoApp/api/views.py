from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import (
    TaskSerializer,
    CategorySerializer,
    CategoryDetailSerializer)

from ..models import *


class CategoryViewSet(viewsets.ModelViewSet):
    """ вывод списка тасков в категории """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    action_to_serializer = {
            'list': CategorySerializer,
            'create': CategorySerializer,
            'retrieve': CategoryDetailSerializer,
            'update': CategorySerializer,
            'destroy': CategorySerializer
        }

    def get_serializer_class(self):
        return self.action_to_serializer.get(
            self.action,
            self.serializer_class
        )


class TaskViewSet(viewsets.ModelViewSet):
    """ вывод списка тасков в категории """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    action_to_serializer = {
            'list': TaskSerializer,
            'create': TaskSerializer,
            'retrieve': TaskSerializer,
            'update': TaskSerializer,
            'destroy': TaskSerializer
        }

    def get_serializer_class(self):
        return self.action_to_serializer.get(
            self.action,
            self.serializer_class
        )
