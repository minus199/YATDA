from api.Requests.requestbase import RequestBase
from todos.models import Todo

__author__ = 'asafb'
from rest_framework.response import Response


class Delete(RequestBase):
    def __init__(self, tid):
        self._tid = tid

    def _populate(self):
        todo_obj = Todo.objects.get(id=self._tid)
        todo_obj.delete()
        return Response(data={}, status=200)
