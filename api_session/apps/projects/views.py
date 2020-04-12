from rest_framework import viewsets
from .models import Projects
from . import serializers


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = serializers.ProjectModelSerializer
