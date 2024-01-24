from django.urls import path
from .views import vehicle_list

urlpatterns = [
    path('vehicle-list/', vehicle_list, name='vehicle_list'),
    # Add other URL patterns as needed
]
