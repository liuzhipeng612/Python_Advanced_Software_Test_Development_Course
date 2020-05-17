from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response

from . import serializers
from .models import Testcases
from .utils import get_count_by_testcase


class TestcaseViewSet(viewsets.ModelViewSet):
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
    queryset = Testcases.objects.all()
    serializer_class = serializers.TestcaseModelSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['name']
    ordering_fields = ['id', 'name', ]

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data['results'] = get_count_by_testcase(response.data['results'])
        return response

    @action(detail=False)
    def run(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
