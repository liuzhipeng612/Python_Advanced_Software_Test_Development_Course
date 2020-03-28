from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet
from interfaces import serializers
from interfaces.models import Interfaces
"""
使用ModelViewSet视图集，继承了CreateModelMixin、ListModelMixin、
RetrieveModelMixin、UpdateModelMixin、DestroyModelMixin、GenericViewSet视图集，
拥有create、list、retrieve、update、destroy方法，简化程序调用
"""


class InterfaceList(ModelViewSet):
    """
        create:
        创建接口

        retrieve:
        获取接口详情数据

        update:
        完整更新接口

        partial_update:
        部分更新接口

        list:
        获取接口列表信息

        destroy:
        删除接口
        """
    queryset = Interfaces.objects.all()
    serializer_class = serializers.InterfaceModelSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['name', 'tester']
    ordering_fields = ['id', 'name']
