from django.urls import path, include
from django.contrib import admin
from autocomplete_api.views import AutocompleteSwaggerSchemaView
from data_treat_api.views import DataTreatSwaggerSchemaView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('autocomplete/api/', include('autocomplete_api.urls')),
    path('data-treat/api/', include('data_treat_api.urls')),
    path('autocomplete/api/swagger', AutocompleteSwaggerSchemaView.as_view(), name='swagger'),
    path('data-treat/api/swagger', DataTreatSwaggerSchemaView.as_view(), name='swagger'),
]
