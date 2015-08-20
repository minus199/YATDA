__author__ = 'asafb'

from api.Requests.requestbase import RequestBase
from api.serializers import TaskSerializer
from todos.models import Todo
from rest_framework.response import Response


class GetOne(RequestBase):
    def __init__(self, tid):
        self._tid = tid

    def _populate(self):
        todo_obj = Todo.objects.get(id=self._tid)
        serializer = TaskSerializer(instance=todo_obj)

        return Response(data=serializer.data, status=200)
