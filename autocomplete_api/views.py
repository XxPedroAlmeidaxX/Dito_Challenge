from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.schemas import SchemaGenerator
from rest_framework.views import APIView
from rest_framework_swagger import renderers

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


# Sets up the Autocomplete API Swagger
class AutocompleteSwaggerSchemaView(APIView):
    renderer_classes = [
        renderers.OpenAPIRenderer,
        renderers.SwaggerUIRenderer
    ]

    def get(self, request):
        generator = SchemaGenerator(title='Autocomplete API', url='/autocomplete/api/', urlconf='autocomplete_api.urls')
        schema = generator.get_schema(request=request)
        return Response(schema)

