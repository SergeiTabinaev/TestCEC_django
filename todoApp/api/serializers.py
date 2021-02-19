from rest_framework import serializers
from ..models import *
# from djoser.serializers import UserCreateSerializer
# from django.contrib.auth import get_user_model

# User = get_user_model()
#
# class UserCreateSerializer(UserCreateSerializer):
#
#     class Meta(UserCreateSerializer.Meta):
#         model = User
#         fields = ('id', 'email', 'first_name', 'last_name', 'password')

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class CategoryDetailSerializer(serializers.ModelSerializer):

    tasks = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = '__all__'

    @staticmethod
    def get_tasks(obj):
        return TaskSerializer(Task.objects.filter(category=obj), many=True).data


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'

