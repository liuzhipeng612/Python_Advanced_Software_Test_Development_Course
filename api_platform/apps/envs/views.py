from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response

from . import serializers
from .models import Envs


class EnvViewSet(viewsets.ModelViewSet):
    queryset = Envs.objects.all()
    serializer_class = serializers.EnvModelSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['name']
    ordering_fields = ['id', 'name']

    @action(methods=['get'], detail=False)
    def names(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(instance=queryset, many=True)
        return Response(data=serializer.data)
