from rest_framework import serializers

from .models import DebugTalks


class DebugTalkModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DebugTalks
        exclude = ('create_time', 'update_time')
