__author__ = 'asafb'
from rest_framework import serializers

from todos.models import Todo


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = ('id', 'subject', 'body', 'date')