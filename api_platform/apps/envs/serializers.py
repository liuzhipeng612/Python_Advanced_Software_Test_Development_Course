from rest_framework import serializers

from .models import Envs


class EnvModelSerializer(serializers.ModelSerializer):
    interfaces = serializers.StringRelatedField(many=True)

    class Meta:
        model = Envs
        exclude = ('create_time', 'update_time')


class EnvNamesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Envs
        fields = ('id', 'name')
