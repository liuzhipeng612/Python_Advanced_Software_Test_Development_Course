from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from interfaces import serializers
from interfaces.models import Interfaces

"""
使用ViewSet视图集，使url.py路由支持根据HTTP请求方法绑定对应的action动作
"""


class InterfaceList(ViewSet):
    def list(self, request):
        """
        获取接口数据列表
        :param request:
        :return:
        """
        interface_qs = Interfaces.objects.all()
        serializer = serializers.InterfaceModelSerializer(instance=interface_qs, many=True)
        return Response(data=serializer.data)

    def create(self, request):
        """
        创建接口
        :param request:
        :return:
        """
        serializer = serializers.InterfaceModelSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class InterfaceDetail(ViewSet):
    def get_object(self, pk):
        try:
            return Interfaces.objects.get(id=pk)
        except Interfaces.DoesNotExist:
            raise Http404

    def retrieve(self, request, pk):
        """
        获取指定接口数据
        :param request:
        :param pk:
        :return:
        """
        one_interface = self.get_object(pk)
        serializer = serializers.InterfaceModelSerializer(instance=one_interface)
        return Response(data=serializer.data)

    def update(self, request, pk):
        """
        完整更新接口
        :param request:
        :param pk:
        :return:
        """
        one_interface = self.get_object(pk)
        serializer = serializers.InterfaceModelSerializer(instance=one_interface, data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response(data=serializer.errors)
        serializer.save()
        return Response(data=serializer.data)

    def destroy(self, request, pk):
        """
        删除指定接口
        :param request:
        :param pk:
        :return:
        """
        one_interface = Interfaces.objects.get(id=pk)
        one_interface.delete()
        return Response(data='指定接口删除成功', status=status.HTTP_204_NO_CONTENT)
