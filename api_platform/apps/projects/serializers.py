from rest_framework import serializers

from interfaces.models import Interfaces
from .models import Projects


class ProjectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        exclude = ('update_time',)
        extra_kwargs = {
            'create_time': {
                'read_only': True
            }
        }


class ProjectNamesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('id', 'name')


class InterfaceNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interfaces
        fields = ('id', 'name')


class InterfaceByProjectIdSerializer(serializers.ModelSerializer):
    interfaces = InterfaceNameSerializer(read_only=True, many=True)

    class Meta:
        model = Projects
        fields = ('id', 'interfaces')
