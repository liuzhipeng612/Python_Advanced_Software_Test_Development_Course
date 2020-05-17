from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from . import serializers
from .models import DebugTalks


class DebugTalkViewSet(mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.ListModelMixin,
                       GenericViewSet):
    queryset = DebugTalks.objects.all()
    serializer_class = serializers.DebugTalkModelSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
