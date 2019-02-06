from rest_framework import viewsets
from rest_framework.response import Response


# Creates the Data Treat service
class DataTreatViewSet(viewsets.ViewSet):

    # Defines the GET behavior
    def list(self, request):

        return Response('')
