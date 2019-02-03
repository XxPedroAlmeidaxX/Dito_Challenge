from rest_framework import serializers
from .models import User, EventData


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email')


class EventDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventData
        fields = ('id', 'event', 'dateTime', 'user')
