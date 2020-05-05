from rest_framework import serializers

from projects.models import Projects
from .models import Interfaces


class InterfaceModelSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField(label='所属项目名称', help_text='所属项目名称')
    project_id = serializers.PrimaryKeyRelatedField(queryset=Projects.objects.all(), label='项目id', help_text='项目id',
                                                    write_only=True)

    class Meta:
        model = Interfaces
        fields = ('id', 'name', 'tester', 'create_time', 'desc', 'project', 'project_id')

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
