from api.Requests.requestbase import RequestBase
from api.serializers import TaskSerializer
from todos.models import Todo

__author__ = 'asafb'
from rest_framework.response import Response


class Update(RequestBase):
    def __init__(self, todo_id, data):
        self._tid = todo_id
        self._data = data

    def _populate(self):
        todo_obj = Todo.objects.get(id=self._tid)
        serializer = TaskSerializer(todo_obj, data=self._data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, 400)
