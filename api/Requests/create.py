__author__ = 'asafb'

from api.Requests.requestbase import RequestBase
from api.serializers import TaskSerializer
from rest_framework.response import Response


class Create(RequestBase):
    def __init__(self, data):
        self._data = data
        pass

    def _populate(self):
        serializer = TaskSerializer(data=self._data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)

        return Response(serializer.errors, status=500)
