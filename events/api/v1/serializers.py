import uuid
from django.utils import timezone

from rest_framework import serializers

from events.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ("session", "category", "name", "data", "timestamp")

    def validate_session_id(self, value):
        if not isinstance(uuid, value):
            raise serializers.ValidationError("This session id is not valid")
        return value

    def validate_data(self, value):
        if not "host" or "path" in value:
            raise serializers.ValidationError("This data is not valid")
        return value

    def validate_timestamp(self, value):
        if value > timezone.now():
            raise serializers.ValidationError("Invalid Timestamp")
        return value
