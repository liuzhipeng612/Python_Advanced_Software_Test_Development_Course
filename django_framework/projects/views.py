from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import generics

from projects.models import Projects
from . import serializers


# class Foo(mixins.ListModelMixin,
#           mixins.CreateModelMixin,
#           GenericAPIView):
#     def get(self, request, *args, **kwargs):
#         """
#         获取项目
#         :param request:
#         :return:
#         """
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         """
#         新增项目
#         :param request:
#         :return:
#         """
#         return self.create(request, *args, **kwargs)


# 继承DRF中的Mixin拓展类，需要在GennericAPIView前面继承
class ProjectList(generics.ListCreateAPIView):
    queryset = Projects.objects.all()
    serializer_class = serializers.ProjectModelSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['name', 'leader', 'tester']
    ordering_fields = ['id', 'name', 'leader']


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Projects.objects.all()
    serializer_class = serializers.ProjectModelSerializer
