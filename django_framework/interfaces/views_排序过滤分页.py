from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import OrderingFilter
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from interfaces import serializers
from interfaces.models import Interfaces


class InterfaceList(GenericAPIView):
    queryset = Interfaces.objects.all()  # 指定queryset查询集类属性
    serializer_class = serializers.InterfaceModelSerializer  # 指定serializers_class序列化器类
    filter_backends = [DjangoFilterBackend, OrderingFilter]  # 指定过滤和排序引擎
    filterset_fields = ['name', 'project', 'tester']  # 指定过滤字段
    ordering_fields = ['id', 'name', 'project']  # 指定允许排序字段，在查询字符串传参使用ordering=-id格式进行排序操作

    def get(self, request):
        """
        get_queryset()方法的使用
        get_serializer()方法的使用
        filter_queryset()方法的使用，将所有项目查询集使用filter_queryset方法按照filterset_fields过滤字段进行过滤处理
        paginate_queryset()方法的使用
        :param request:
        :return:
        """
        interface_qs = self.get_queryset()  # get_queryset()方法的使用
        interface_qs = self.filter_queryset(interface_qs)  # filter_queryset()方法的使用
        page = self.paginate_queryset(interface_qs)  # paginate_queryset()方法的使用
        if page is not None:
            serializer = self.get_serializer(instance=page, many=True)
            return self.get_paginated_response(serializer.data)  # 如果查询字符串传参page不为空，直接返回分页内容
        serializer = self.get_serializer(instance=interface_qs, many=True)  # get_serializer()方法的使用
        return Response(data=serializer, status=status.HTTP_200_OK)


class InterfaceDetail(GenericAPIView):
    queryset = Interfaces.objects.all()
    serializer_class = serializers.InterfaceModelSerializer

    def get(self, request, pk):
        """
        get_object()方法的使用
        查询操作
        获取指定项目信息
        :param pk:
        :param request:
        :return:
        """
        one_interface = self.get_object()  # get_object()方法的使用
        serializer = serializers.InterfaceModelSerializer(instance=one_interface)
        return Response(data=serializer.data)
