from django.http import Http404

from rest_framework.response import Response
from rest_framework.views import APIView

from projects.models import Projects
from . import serializers


class ProjectDetail(APIView):
    def get_object(self, pk):
        try:
            return Projects.objects.get(id=pk)
        except Projects.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """
        获取指定项目信息
        :param request: 
        :param pk: 
        :return: 
        """""
        one_project = self.get_object(pk)
        serializer = serializers.ProjectModelSerializer(instance=one_project)
        return Response(serializer.data)
