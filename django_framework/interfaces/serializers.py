from rest_framework import serializers

from .models import Interfaces
from projects.models import Projects


class ProjectsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        exclude = ('create_time', 'update_time', 'desc')


class InterfacesModelSerializer(serializers.ModelSerializer):
    project = ProjectsModelSerializer(read_only=True)

    class Meta:
        model = Interfaces
        exclude = ('create_time', 'update_time', 'desc')
