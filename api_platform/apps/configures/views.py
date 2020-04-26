from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response

from . import serializers
from .models import Configures


class ConfigureViewSet(viewsets.ModelViewSet):
    """
    create:
    创建项目

    retrieve:
    获取项目详情数据

    update:
    完整更新项目

    partial_update:
    部分更新项目

    list:
    获取项目列表信息

    destroy:
    删除项目

    names:
    获取所有的项目名和项目ID

    interfaces:
    获取某个项目下的所有接口信息

    """
    queryset = Configures.objects.all()
    serializer_class = serializers.ConfigureModelSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    @action(methods=['get'], detail=False)
    def names(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        serializer = self.get_serializer(instance=queryset, many=True)
        return Response(data=serializer.data)

    @action(detail=True)
    def interfaces(self, request, *args, **kwargs):
        pass

    def get_serializer_class(self):
        return serializers.ConfigureNamesModelSerializer if self.action == 'names' else self.serializer_class
