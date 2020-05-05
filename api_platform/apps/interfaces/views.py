from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response

from utils.pagination import InterfacePageNumberPagination
from . import serializers
from .models import Interfaces
from .utils import get_count_by_project


# logger = logging.getLogger(name="test")
# logger.error("这里有一个严重的错误")


# 1.要实现过滤、排序、分页功能，需要继承DRF中的GennericAPIView
# 2.要指定queryset查询集类属性
# 3.需要使用serializers_class序列化器类
# 4.使用get_queryset方法获取查询集对象
# 5.以后获取需要使用的序列化器类，不要使用serializer_class
# 5.1而是使用get_serializer方法获取
# 6.filter_backends来指定过滤引擎,如果在全局配置settyings.py中定义了，就不需要再每个类中重新定义
# 7.filterset_fields来指定过滤字段，只能为模型类中的对象
# 8.指定排序字段,如果在全局配置settyings.py中定义了，就不需要再每个类中重新定义,排序只对于get获取详情接口
# 默认前端只需要使用ordering作为key，指定的字段名作为value
# 默认会以升序来排序，如果要降序，加-号
# 9.分页操作
# page为分页之后的查询集对象
class InterfaceViewSet(viewsets.ModelViewSet):
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
    queryset = Interfaces.objects.all()
    serializer_class = serializers.InterfaceModelSerializer
    pagination_class = InterfacePageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['name', 'tester']
    ordering_fields = ['id', 'name', ]

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data['results'] = get_count_by_project(response.data['results'])
        return response

    @action(detail=False)
    def names(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True)
    def interfaces(self, request, pk=None):
        interface_obj = Interfaces.objects.filter(project_id=pk)
        one_list = []
        for item in interface_obj:
            one_list.append({
                'id': item.id,
                'name': item.name
            })
        return Response(data=one_list)
