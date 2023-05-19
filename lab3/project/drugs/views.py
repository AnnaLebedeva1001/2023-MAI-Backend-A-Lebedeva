from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET", "POST"])
def pharmacy(request):
    pharmacy_info = {
        'id': 1,
        'name': 'Sample Pharmacy',
        'address': '456 Elm St',
        'city': 'Los Angeles',
        'country': 'USA',
    }
    return JsonResponse(pharmacy_info)


@require_http_methods(["GET", "POST"])
def pharmacist(request):
    pharmacist_info = {
        'id': 1,
        'first_name': 'Jane',
        'last_name': 'Smith',
        'gender': 'F',
        'age': 35,
    }
    return JsonResponse(pharmacist_info)


@require_http_methods(["GET", "POST"])
def product(request):
    product_info = {
        'id': 1,
        'name': 'Sample Product',
        'price': 9.99,
        'description': 'Lorem ipsum dolor sit amet.',
    }
    return JsonResponse(product_info)
