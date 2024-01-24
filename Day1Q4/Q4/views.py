from django.template.response import TemplateResponse
from django.shortcuts import render

def vehicle_list(request):
    vehicles = [
        {'make': 'Toyota', 'model': 'Camry', 'year': 2022},
        {'make': 'Ford', 'model': 'Mustang', 'year': 2021},
        {'make': 'Honda', 'model': 'Civic', 'year': 2023},
    ]
    return TemplateResponse(request, 'vehicle_list.html', {'vehicles': vehicles})
