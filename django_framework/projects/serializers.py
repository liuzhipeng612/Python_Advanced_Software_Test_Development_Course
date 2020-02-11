from rest_framework import serializers

from .models import Projects


class ProjectModelSerializer(serializers.ModelSerializer):
    interfaces = serializers.StringRelatedField(many=True)

    class Meta:
        model = Projects
        exclude = ('create_time', 'update_time', 'desc')
