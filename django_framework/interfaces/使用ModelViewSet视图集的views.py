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
    queryset = Interfaces.objects.all()
    serializer_class = serializers.InterfaceModelSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['name', 'tester']
    ordering_fields = ['id', 'name']


class InterfaceDetail(ModelViewSet):
    queryset = Interfaces.objects.all()
    serializer_class = serializers.InterfaceModelSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['name', 'tester']
    ordering_fields = ['id', 'name']
