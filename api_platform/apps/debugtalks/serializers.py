from rest_framework import serializers

from .models import DebugTalks


class DebugTalkModelSerializer(serializers.ModelSerializer):
    interfaces = serializers.StringRelatedField(many=True)

    class Meta:
        model = DebugTalks
        exclude = ('create_time', 'update_time')


class DebugTalkNamesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DebugTalks
        fields = ('id', 'name')
