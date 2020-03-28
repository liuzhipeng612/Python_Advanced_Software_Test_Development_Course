from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from interfaces import serializers
from interfaces.models import Interfaces

"""
使用GenericViewSet视图集，支持get_object()、get_serializer()、queryset、serializer_class等方法，
同时使url.py路由支持根据HTTP请求方法绑定对应的action动作
"""


class InterfaceList(GenericViewSet):
    queryset = Interfaces.objects.all()
    serializer_class = serializers.InterfaceModelSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['name', 'tester']
    ordering_fields = ['id', 'name']

    def list(self, request):
        """
        获取接口数据列表
        :param request:
        :return:
        """
        project_qs = self.get_queryset()
        project_qs = self.filter_queryset(project_qs)
        page = self.paginate_queryset(project_qs)
        if page is not None:
            serializer = self.get_serializer(instance=page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(instance=project_qs, many=True)
        return Response(data=serializer.data)

    def create(self, request):
        """
        创建接口
        :param request:
        :return:
        """
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class InterfaceDetail(GenericViewSet):
    queryset = Interfaces.objects.all()
    serializer_class = serializers.InterfaceModelSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['name', 'tester']
    ordering_fields = ['id', 'name']

    def retrieve(self, request, pk):
        """
        获取指定接口数据
        :param request:
        :param pk:
        :return:
        """
        serializer = self.get_serializer(instance=self.get_object())
        return Response(data=serializer.data)

    def update(self, request, pk):
        """
        完整更新接口
        :param request:
        :param pk:
        :return:
        """
        serializer = self.get_serializer(instance=self.get_object(), data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response(data=serializer.errors)
        serializer.save()
        return Response(data=serializer.data)

    def destroy(self, request, pk):
        """
        删除指定接口
        :param request:
        :param pk:
        :return:
        """
        one_interface = self.get_object()
        one_interface.delete()
        return Response(data='指定接口删除成功', status=status.HTTP_204_NO_CONTENT)
