import requests
from rest_framework import viewsets, status
from rest_framework.response import Response


# Creates the Data Treat service
class DataTreatViewSet(viewsets.ViewSet):

    # Defines the GET behavior
    def list(self, request):
        """
           Accesses the endpoint https://storage.googleapis.com/dito-questions/events.json and manipulates the events to
           return a merged and sorted version
        """

        endpoint_url = 'https://storage.googleapis.com/dito-questions/events.json'
        request_result = requests.get(url=endpoint_url)

        if request_result.status_code == requests.codes.ok:
            return Response(get_treated_events(request_result.json()['events']))
        else:
            return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)


# Manipulates the events to return a merged and sorted version
def get_treated_events(events):

    timeline = list()
    buy_events = list()
    buy_product_events = list()

    # Separates the event kind
    for event in events:
        if event['event'] == 'comprou-produto':
            buy_product_events.append(event)
        elif event['event'] == 'comprou':
            event['products'] = []  # Add the key to be used on composition later
            buy_events.append(event)

    # Joins the buy-product event to its corresponding buy event
    for buy_product_event in buy_product_events:
        buy_event = next((buy_event for buy_event in iter(buy_events) if
                          get_event_transaction_id(buy_event) == get_event_transaction_id(buy_product_event)), None)

        if buy_event is not None:
            buy_event['products'].append({
                "name": get_event_custom_data_value(buy_product_event, 'product_name'),
                "price": get_event_custom_data_value(buy_product_event, 'product_price')
            })

    # Creates the timeline object
    for buy_event in buy_events:
        timeline.append({
            "timestamp": buy_event['timestamp'],
            "revenue": buy_event['revenue'],
            "transaction_id": get_event_transaction_id(buy_event),
            "store_name": get_event_custom_data_value(buy_event, 'store_name'),
            "products": buy_event['products']
        })

    # Sort the timeline by timestamp and return it
    return {"timeline": [sorted(timeline, key=lambda x: x['timestamp'], reverse=True)]}


# Returns the target_key's value inside custom_data from a event
def get_event_custom_data_value(event, target_key):
    for data in event['custom_data']:
        if data['key'] == target_key:
            return data['value']

    return None


# Returns the transaction_id from a event
def get_event_transaction_id(event):
    return get_event_custom_data_value(event, 'transaction_id')
