from django.http.response import HttpResponseNotFound
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.Requests.create import Create
from api.Requests.delete import Delete
from api.Requests.get import GetOne
from api.Requests.get_all import GetAll
from api.Requests.update import Update

from todos.models import Todo
from api.serializers import TaskSerializer


def home_action(request):
    return HttpResponseNotFound('<h1>Page not found</h1>')


@api_view(['GET'])
def get_all(request):
    method = GetAll()
    return method.populate()


@api_view(['POST'])
def create_new(request):
    method = Create(data=request.data)
    return method.populate()


@api_view(['GET', 'DELETE', 'POST', 'PUT'])
def update_create_delete_get(request, tid=0):
    # We have somewhat of a problem here which i need more time to investigate
    # All of these methods, RESTfully, should be same routing
    # However, one of them should not get ID as an argument.
    # There for, I've given tid the default value of 0 to be used whenever POST is requested
    # This way, I can encapsulate all this methods and use same routing without getting wrong number of args exception
    if request.method == "PUT":
        method = Update(todo_id=tid, data=request.data)
    elif request.method == "DELETE":
        method = Delete(tid=tid)
    elif request.method == "GET":
        method = GetOne(tid=tid)
    else:
        return Response({"error": "request not supported"}, status.HTTP_400_BAD_REQUEST)

    return method.populate()
