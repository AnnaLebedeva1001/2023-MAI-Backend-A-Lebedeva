from django.urls import path
from . import views

urlpatterns = [
    path('pharmacy', views.pharmacy, name='pharmacy'),
    path('pharmacist', views.pharmacist, name='pharmacist'),
    path('product', views.product, name='product'),
]
