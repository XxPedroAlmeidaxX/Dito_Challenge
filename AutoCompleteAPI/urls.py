from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'eventsData', views.EventDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('autocomplete/', views.Autocomplete.as_view())
]
