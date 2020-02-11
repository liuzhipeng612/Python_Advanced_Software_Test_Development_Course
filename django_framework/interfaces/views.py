from django.http import Http404, JsonResponse
from django.views import View

from interfaces import serializers
from interfaces.models import Interfaces


class InterfaceDetail(View):

    def get_object(self, pk):
        try:
            return Interfaces.objects.get(id=pk)
        except Interfaces.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """
        查询操作
        获取指定项目信息
        :param pk:
        :param request:
        :return:
        """
        one_interface = self.get_object(pk)
        serializer = serializers.InterfacesModelSerializer(instance=one_interface)
        return JsonResponse(data=serializer.data)
