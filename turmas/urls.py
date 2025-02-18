from django.urls import path, include
from . import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('lista/', views.listar, name='listar')
]