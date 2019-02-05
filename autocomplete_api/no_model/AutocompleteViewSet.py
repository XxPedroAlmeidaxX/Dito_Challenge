import coreapi
from rest_framework import viewsets, status
from rest_framework.filters import BaseFilterBackend
from rest_framework.response import Response

from autocomplete_api.models import EventData


# Defines custom Query String Parameters working accordingly with the Django Rest Swagger
class AutocompleteFilterBackend(BaseFilterBackend):
    def get_schema_fields(self, view):
        return [
            coreapi.Field(
                name='event',
                location='query',
                required=True,
                description='String utilizada para completar os eventos'
            ),
            coreapi.Field(
                name='limit',
                location='query',
                required=False,
                description='Quantidade de eventos a serem sugeridos. Default: 5'
            ),
        ]


# Creates the Autocomplete service
class AutocompleteViewSet(viewsets.ViewSet):

    limit_default_value = 5

    # id must be included in raw query - Django requirement -
    event_raw_query = ("SELECT id, event FROM autocomplete_api_eventdata " +
                       "WHERE event LIKE '{event_part}%' " +
                       "GROUP BY event ORDER BY count(id) DESC LIMIT {limit} ")

    # Apply the custom Query String Parameters
    filter_backends = (AutocompleteFilterBackend,)

    # Defines the GET behavior
    def list(self, request):

        # Get and treat the parameters
        event_part = request.GET.get('event')
        if event_part is None or len(event_part) < 2:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        limit = request.GET.get('limit')
        if limit is None:
            limit = self.limit_default_value

        # Executes the raw query
        events = EventData.objects.raw(self.event_raw_query.format(event_part=event_part, limit=limit))

        # Creates events list to be returned
        events_return = list()
        for row in events:
            events_return.append(getattr(row, 'event'))

        return Response(events_return)
