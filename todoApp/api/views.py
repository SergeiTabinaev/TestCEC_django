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

# class TaskViewSet(viewsets.ViewSet):
#     """вывод удаление редактирование создание тасок"""
#
#     def list(self, request):
#         tasks = Task.objects.all()
#         serializer = TaskSerializer(tasks, many=True)
#         return Response(serializer.data)
#
#     def create(self, request, *args, **kwargs):
#         serializer = TaskSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#     def retrieve(self, request, pk=None):
#         task = Task.objects.get(id=pk)
#         serializer = TaskSerializer(task)
#         return Response(serializer.data)
#
#     def update(self, request, pk=None):
#         product = Task.objects.get(id=pk)
#         serializer = TaskSerializer(instance=product, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
#
#     def destroy(self, request, pk=None):
#         product = Task.objects.get(id=pk)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
