from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns =[
    path("gestion_cita/", views.gestion_cita),
    path("asignacion/", views.modulo, name="Modulo")
]