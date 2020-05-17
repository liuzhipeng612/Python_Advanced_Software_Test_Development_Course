from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response

from . import serializers
from .models import Testsuites
from .utils import get_count_by_testsuite


class TestsuiteViewSet(viewsets.ModelViewSet):
    queryset = Testsuites.objects.all()
    serializer_class = serializers.TestsuiteModelSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data['results'] = get_count_by_testsuite(response.data['results'])

        return response

    def retrieve(self, request, *args, **kwargs):
        testsuite_obj = self.get_object()
        datas = {
            "name": testsuite_obj.name,
            "project_id": testsuite_obj.project_id,
            "include": testsuite_obj.include
        }

        return Response(datas)

    @action(detail=True)
    def run(self):
        pass
