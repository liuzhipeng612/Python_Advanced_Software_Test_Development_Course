from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, mixins
from rest_framework.filters import OrderingFilter
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from projects.models import Projects
from . import serializers


# 继承DRF中的Mixin拓展类，需要在GennericAPIView前面继承
class ProjectList(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericAPIView):
    queryset = Projects.objects.all()
    serializer_class = serializers.ProjectModelSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['name', 'leader', 'tester']
    ordering_fields = ['id', 'name', 'leader']

    def get(self, request, *args, **kwargs):
        """
        获取项目
        :param request:
        :return:
        """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        新增项目
        :param request:
        :return:
        """
        return self.create(request, *args, **kwargs)


class ProjectDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    GenericAPIView):
    queryset = Projects.objects.all()
    serializer_class = serializers.ProjectModelSerializer

    def get(self, request, *args, **kwargs):
        """
        获取指定项目
        :param request: 
        :return: 
        """""
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        更新指定的项目
        :param request:
        :return:
        """

        return self.update(request, *args, **kwargs)

    def patch(self, request, pk):
        project_list = []
        return Response(data=project_list)

    def delete(self, request, *args, **kwargs):
        """
        删除指定的数据
        :param request:
        :param pk:
        :return:
        """
        return self.destroy(request, *args, **kwargs)
