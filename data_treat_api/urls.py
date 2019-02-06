from django.urls import path, include
from rest_framework import routers

from .no_model.DataTreatViewSet import DataTreatViewSet


# Routes to the resources
router = routers.DefaultRouter()
router.register(r'data-treat', DataTreatViewSet, base_name='data-treat')

urlpatterns = [
    path('', include(router.urls))
]
