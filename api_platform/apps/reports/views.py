from api_platform.utils.utils import get_dict_time_formatting
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from . import serializers
from .models import Reports


class ReportViewSet(mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):
    queryset = Reports.objects.all()
    serializer_class = serializers.ReportModelSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data['results'] = get_dict_time_formatting(response.data['results'])

        return response
