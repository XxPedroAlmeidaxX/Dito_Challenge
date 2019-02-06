from django.urls import path, include
from rest_framework import routers

from .no_model.AutocompleteViewSet import AutocompleteViewSet
from .views import UserViewSet, EventDataViewSet

# Routes to the resources
router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'eventData', EventDataViewSet)
router.register(r'autocomplete', AutocompleteViewSet, base_name='autocomplete')

urlpatterns = [
    path('', include(router.urls))
]
