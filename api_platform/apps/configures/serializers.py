from rest_framework import serializers

from .models import Configures


class ConfigureModelSerializer(serializers.ModelSerializer):
    interfaces = serializers.StringRelatedField(many=True)

    class Meta:
        model = Configures
        exclude = ('create_time', 'update_time')


class ConfigureNamesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configures
        fields = ('id', 'name')
