from django.urls import path
from . import views

app_name = 'titulos'

urlpatterns = [
    path('lista/', views.listar, name = 'listar' ),
]

