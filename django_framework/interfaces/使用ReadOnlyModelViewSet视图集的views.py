from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ReadOnlyModelViewSet
from interfaces import serializers
from interfaces.models import Interfaces

"""
使用GenericViewSet视图集，支持get_object()、get_serializer()、queryset、serializer_class等方法，
同时使url.py路由支持根据HTTP请求方法绑定对应的action动作
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
