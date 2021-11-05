from django.urls import path
from . import views
from product import views

import product

urlpatterns = [
    path('json', views.json, name='json')
]
