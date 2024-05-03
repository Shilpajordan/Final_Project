from django.contrib import admin
from django.urls import path
from .views import appointment_add, appointment_list

urlpatterns = [
    path('appointment/add/', appointment_add, name='appointment_add'),
    path('appointments/', appointment_list, name='appointment_list'),
]
