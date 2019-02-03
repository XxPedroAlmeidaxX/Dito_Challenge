from rest_framework import viewsets
from .models import User, EventData
from .serializers import UserSerializer, EventDataSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EventDataViewSet(viewsets.ModelViewSet):
    queryset = EventData.objects.all()
    serializer_class = EventDataSerializer
