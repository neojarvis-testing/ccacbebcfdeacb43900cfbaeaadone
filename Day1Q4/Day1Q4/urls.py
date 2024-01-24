# In Day1Q4/urls.py
from django.contrib import admin
from django.urls import include, path
from Q4.views import vehicle_list
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vehicle_list, name='vehicle_list'),  # Handle the root URL
    path('vehicle-list/', include('Q4.urls')),
]
