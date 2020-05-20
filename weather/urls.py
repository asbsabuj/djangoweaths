from django.urls import path
from . import views

urlpatterns = [
    path('hello', views.first, name = 'hello'),
    path('locations', views.second, name='locations'),
]
