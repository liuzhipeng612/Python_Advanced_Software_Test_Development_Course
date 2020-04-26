from rest_framework import serializers

from .models import Interfaces


class InterfaceModelSerializer(serializers.ModelSerializer):
    interfaces = serializers.StringRelatedField(many=True)

    class Meta:
        model = Interfaces
        exclude = ('create_time', 'update_time')


class InterfaceNamesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interfaces
        fields = ('id', 'name')
