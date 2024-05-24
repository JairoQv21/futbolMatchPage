from django.urls import path
from .views import home,reservar, planes,registro,login

urlpatterns = [
    path('',home),
    path('reservar',reservar),
    path('planes', planes ),
    path('registro', registro),
    path('login', login),
    path('registro', registro)
]
