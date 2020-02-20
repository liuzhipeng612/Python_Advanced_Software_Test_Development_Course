from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework import mixins, viewsets
from rest_framework.response import Response

from projects.models import Projects
from . import serializers


# class ProjectList(generics.ListCreateAPIView):
#     queryset = Projects.objects.all()
#     serializer_class = serializers.ProjectModelSerializer
#     filter_backends = [DjangoFilterBackend, OrderingFilter]
#     filterset_fields = ['name', 'leader', 'tester']
#     ordering_fields = ['id', 'name', 'leader']
#
#
# class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Projects.objects.all()
#     serializer_class = serializers.ProjectModelSerializer


# class ProjectViewSet(mixins.CreateModelMixin,
#                      mixins.ListModelMixin,
#                      mixins.RetrieveModelMixin,
#                      mixins.UpdateModelMixin,
#                      mixins.DestroyModelMixin,
#                      viewsets.GenericViewSet):

class ProjectViewSet(viewsets.ModelViewSet):
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
    @action(methods=['get'], detail=False)
    def names(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = serializers.ProjectNamesModelSerializer(instance=queryset, many=True)
        return Response(data=serializer.data)
