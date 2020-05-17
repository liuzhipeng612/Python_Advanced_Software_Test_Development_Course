from rest_framework import serializers

from .models import Envs


class EnvModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Envs
        fields = ('id', 'name', 'base_url', 'create_time', 'desc')

# class EnvNamesModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Envs
#         fields = ('id', 'name')
