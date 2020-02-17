from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import mixins, viewsets

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
