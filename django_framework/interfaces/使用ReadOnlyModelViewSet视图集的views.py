from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ReadOnlyModelViewSet
from interfaces import serializers
from interfaces.models import Interfaces

"""
使用ReadOnlyModelViewSet视图集，支持list、retrieve两张查询类方法
"""


class InterfaceList(ReadOnlyModelViewSet):
    queryset = Interfaces.objects.all()
    serializer_class = serializers.InterfaceModelSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['name', 'tester']
    ordering_fields = ['id', 'name']


class InterfaceDetail(ReadOnlyModelViewSet):
    queryset = Interfaces.objects.all()
    serializer_class = serializers.InterfaceModelSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['name', 'tester']
    ordering_fields = ['id', 'name']
