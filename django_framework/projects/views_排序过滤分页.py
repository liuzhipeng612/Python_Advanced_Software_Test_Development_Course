from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import OrderingFilter
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from projects.models import Projects
from . import serializers


# 1.要实现过滤、排序、分页功能，需要继承DRF中的GennericAPIView
class ProjectList(GenericAPIView):
    # 2.要指定queryset查询集类属性
    queryset = Projects.objects.all()
    # 3.需要使用serializers_class序列化器类
    serializer_class = serializers.ProjectModelSerializer
    # 6.filter_backends来指定过滤引擎,如果在全局配置settyings.py中定义了，就不需要再每个类中重新定义
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    # 7.filterset_fields来指定过滤字段，只能为模型类中的对象
    filterset_fields = ['name', 'leader', 'tester']
    # 8.指定排序字段,如果在全局配置settyings.py中定义了，就不需要再每个类中重新定义,排序只对于get获取详情接口
    # 默认前端只需要使用ordering作为key，指定的字段名作为value
    # 默认会以升序来排序，如果要降序，加-号
    ordering_fields = ['id', 'name', 'leader']

    def get(self, request):
        """

        :param request:
        :return:
        """
        # 4.使用get_queryset方法获取查询集对象
        project_qs = self.get_queryset()  # 查询集对象中，有100条项目模型对象
        # name = request.query_params.get('name')
        # project_qs = project_qs.filter(name__contains=name)
        project_qs = self.filter_queryset(project_qs)  # 过滤之后可能只有20条
        # 9.分页操作
        # page为分页之后的查询集对象
        page = self.paginate_queryset(project_qs)
        if page is not None:
            serializer = self.get_serializer(instance=page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(instance=project_qs, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        """

        :param request:
        :return:
        """
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=201)


class ProjectDetail(GenericAPIView):
    queryset = Projects.objects.all()
    serializer_class = serializers.ProjectModelSerializer

    # # 实例方法别名（路径参数别名）
    # lookup_field = 'pk'
    # # url定义时指定的别名，默认的值与lookup_field一致，如果不一致，需要指定对应别名lookup_url_kwarg = 对应的别名
    # lookup_url_kwarg = None

    def get(self, request, pk):
        """
        获取指定项目信息
        :param request: 
        :return: 
        """""
        # self.get_object方法自动读取传入的pk值，调用时不需要再次指定，他会将对应pk值的项目返回
        one_project = self.get_object()
        # 5.以后获取需要使用的序列化器类，不要使用serializer_class
        # serializer = self.serializer_class(instance=one_project)
        # 5.1而是使用get_serializer方法获取
        serializer = self.get_serializer(instance=one_project)
        return Response(serializer.data)

    def put(self, request, pk):
        """
        更新指定的项目
        :param request:
        :param pk:
        :return:
        """

        one_project = self.get_object()
        serializer = self.get_serializer(instance=one_project, data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request, pk):
        project_list = []
        return Response(data=project_list)

    def delete(self, request, pk):
        """
        删除指定的数据
        :param request:
        :param pk:
        :return:
        """
        # one_project = Projects.objects.get(id=pk)
        one_project = self.get_object()
        one_project.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
