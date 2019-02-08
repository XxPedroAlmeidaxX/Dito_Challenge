import coreapi
from rest_framework import viewsets, status
from rest_framework.filters import BaseFilterBackend
from rest_framework.response import Response
from django.db.models import Count

from autocomplete_api.models import EventData


# Defines custom Query String Parameters working accordingly with the Django Rest Swagger
class AutocompleteFilterBackend(BaseFilterBackend):
    def get_schema_fields(self, view):
        return [
            coreapi.Field(
                name='event',
                location='query',
                required=True,
                description='String used to complete the events'
            ),
            coreapi.Field(
                name='limit',
                location='query',
                required=False,
                description='Number of events to be suggested. Default: 5'
            ),
        ]


# Creates the Autocomplete service
class AutocompleteViewSet(viewsets.ViewSet):
    """
       Tries to find an event inserted on Event Data that completes the string passed. If the amount of returns is
       superior to the 'limit' the most used events are retrieve
    """

    limit_default_value = 5

    # Apply the custom Query String Parameters
    filter_backends = (AutocompleteFilterBackend,)

    # Defines the GET behavior
    def list(self, request):

        # Get and treat the parameters
        event_part = request.GET.get('event')
        if event_part is None or len(event_part) < 2:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        limit = request.GET.get('limit')
        limit = self.limit_default_value if limit is None else int(limit)

        # Gets the most repeated events that starts with the event_part sliced by the passed limit 
        events = EventData.objects.values('event').filter(event__startswith=event_part).annotate(num_events=Count('event')).order_by('-num_events')[:limit]
 
        # Creates events list to be returned
        events_return = list()
        for row in events:
            events_return.append(row['event'])

        return Response(events_return)

