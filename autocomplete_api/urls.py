from django.urls import path, include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from .no_model.AutocompleteViewSet import AutocompleteViewSet
from .views import UserViewSet, EventDataViewSet

# Automatic swagger from django-rest-swagger
schema_view = get_swagger_view(title='Autocomplete')

# Routes to the resources
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'eventsData', EventDataViewSet)
router.register(r'autocomplete', AutocompleteViewSet, base_name='autocomplete')

urlpatterns = [
    path('swagger', schema_view),
    path('', include(router.urls))
]
