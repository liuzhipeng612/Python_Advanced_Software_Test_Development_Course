from rest_framework import serializers

from .models import Interfaces
# from projects.models import Projects

# class ProjectModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Projects
#         exclude = ('create_time', 'update_time', 'desc')


class InterfaceModelSerializer(serializers.ModelSerializer):
    # project = ProjectModelSerializer(read_wonly=True)

    class Meta:
        model = Interfaces
        exclude = ('create_time', 'update_time', 'desc')
