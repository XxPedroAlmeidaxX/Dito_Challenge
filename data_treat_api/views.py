from rest_framework.response import Response
from rest_framework.schemas import SchemaGenerator
from rest_framework.views import APIView
from rest_framework_swagger import renderers


# Sets up the Data Treat API Swagger
class DataTreatSwaggerSchemaView(APIView):
    renderer_classes = [
        renderers.OpenAPIRenderer,
        renderers.SwaggerUIRenderer
    ]

    def get(self, request):
        generator = SchemaGenerator(title='Data Treat API', url='/data-treat/api/', urlconf='data_treat_api.urls')
        schema = generator.get_schema(request=request)
        return Response(schema)
