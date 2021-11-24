from django.urls import path
from . import views


urlpatterns = [
    path('',views.index_medico, name='index_medico'),
]
