from django.urls import path

from . import views

urlpatterns = [
    path('services/', views.services, name='services'),
    path('services/oil-change-packages/', views.oil_change_packages, name='oil-change-packages'),
    path('services/brake-services/', views.brake_services, name='brake-services'),
    path('', views.home, name='home'),
]