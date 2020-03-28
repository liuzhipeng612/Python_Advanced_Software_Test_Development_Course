import logging
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework import viewsets
from rest_framework.response import Response

from projects.models import Projects
from . import serializers

logger = logging.Logger(name="test")


class ProjectViewSet(viewsets.ModelViewSet):
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
    queryset = Projects.objects.all()
    serializer_class = serializers.ProjectModelSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['name', 'leader', 'tester']
    ordering_fields = ['id', 'name', 'leader']

    # 1. 使用action装饰器来声明自定义动作
    # 默认方法名就是动作名
    # methods参数来指定该动作支持的请求方法，默认为get
    # detail参数用于指定该动作，要处理的是否为详情资源对象（url是否需要传递pk主键）
    # 如果获取详情数据，那么需要指定detail为True，否则为False
    # url_name为路由别名
    # url_path为路由路径
    # 绝大多数情况是不需要指定路由别名和路径
    # @action(methods=['get'], detail=False, url_name='nn', url_path='mm')
    @action(methods=['get'], detail=False)
    def names(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        # serializer = serializers.ProjectNamesModelSerializer(instance=queryset, many=True)
        serializer = self.get_serializer(instance=queryset, many=True)
        logger.error("这里有一个严重的错误")
        return Response(data=serializer.data)

    @action(detail=True)
    def interfaces(self, request, *args, **kwargs):
        pass

    def get_serializer_class(self):
        # if self.action == 'names':
        #     return serializers.ProjectNamesModelSerializer
        # return self.serializer_class
        return serializers.ProjectNamesModelSerializer if self.action == 'names' else self.serializer_class
