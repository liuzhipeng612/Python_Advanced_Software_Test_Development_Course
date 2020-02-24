from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import OrderingFilter
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from interfaces import serializers
from interfaces.models import Interfaces


class InterfaceList(ViewSet):

    def post(self, request):
        """
        创建接口
        :param request:
        :return:
        """
        serializer = serializers.InterfaceModelSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class InterfaceDetail(ViewSet):
    def get_object(self, pk):
        try:
            return Interfaces.objects.get(id=pk)
        except Interfaces.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        """
        完整更新接口
        :param request:
        :param pk:
        :return:
        """
        one_project = self.get_object(pk)
        serializer=serializers.InterfaceModelSerializer(data=request.data)

    def delete(self, request, pk):
        pass
