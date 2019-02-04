from rest_framework import viewsets
from .models import User, EventData
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, EventDataSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EventDataViewSet(viewsets.ModelViewSet):
    queryset = EventData.objects.all()
    serializer_class = EventDataSerializer


class Autocomplete(APIView):
    def get(self, request):
        event = request.data.get('event')
        return Response({"success": event})
