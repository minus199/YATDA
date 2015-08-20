from api.Requests.requestbase import RequestBase

__author__ = 'asafb'

from api.serializers import TaskSerializer
from todos.models import Todo
from rest_framework.response import Response


class GetAll(RequestBase):

    def _populate(self):
        todos = Todo.objects.all()
        serializer = TaskSerializer(todos, many=True)
        return Response(serializer.data)
