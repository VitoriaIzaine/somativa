from django.urls import path
from paciente import views

urlpatterns = [
    path("",views.index),
]
