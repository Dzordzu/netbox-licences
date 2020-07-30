from django.urls import path
from . import views


urlpatterns = [
    path('software-providers/', views.SoftwareProviderListView.as_view(), name='software_providers_list'),
    path("software-providers/add/", views.SoftwareProviderCreateView.as_view(), name="software_providers_add"),
    path("software-providers/delete/", views.SoftwareProviderBulkDeleteView.as_view(), name="software_providers_delete"),
    path('licences/', views.LicenceListView.as_view(), name='licences_list'),
]
