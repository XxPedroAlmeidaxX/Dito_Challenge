from rest_framework import serializers

from .models import User, EventData


# Serializer to Model User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email')


# Serializer to Model EventData
class EventDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventData
        fields = ('id', 'event', 'dateTime', 'user')
