from rest_framework import viewsets

from .models import User, EventData
from .serializers import UserSerializer, EventDataSerializer


# Creates the RESTful 'CRUD' behavior to Model User
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Creates the RESTful 'CRUD' behavior to Model EventData
class EventDataViewSet(viewsets.ModelViewSet):
    queryset = EventData.objects.all()
    serializer_class = EventDataSerializer



