__author__ = 'asafb'

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from todos.models import Todo

from abc import ABCMeta, abstractmethod
from rest_framework.response import Response


class RequestBase(object):
    __metaclass__ = ABCMeta

    def populate(self):
        try:
            return self._populate()
        except ObjectDoesNotExist:
            return Response(data={"error": "was not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response(data={"error": "something went wrong or bad request."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @abstractmethod
    def _populate(self):
        pass
