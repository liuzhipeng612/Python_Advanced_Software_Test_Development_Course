from rest_framework import serializers

from projects.models import Projects
from .models import Testsuites


class TestsuiteModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testsuites
        fields = ('id', 'name', 'project', 'project_id', 'include', 'create_time', 'update_time')

        extra_kwargs = {
            'create_time': {
                'read_only': True
            },
            'update_time': {
                'read_only': True
            },
            'include': {
                'write_only': True
            },
        }

    def validate(self, attrs):
        include = attrs.get('include')
        project_id = attrs.get('project_id')
        Projects.objects.filter(interfaces__id__in=include)
        pass
        return attrs

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
