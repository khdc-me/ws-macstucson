from django.urls import path

from . import views

urlpatterns = [
    path('services/', views.services, name='services'),
    path('services/oil-change-packages/', views.oil_change_packages, name='oil-change-packages'),
    path('services/brake-services/', views.brake_services, name='brake-services'),
    path('services/suspension-services/', views.suspension_services, name='suspension-services'),
    path('services/tires-wheels/', views.tires_wheels, name='tires-wheels'),
    path('services/road-trip/', views.road_trip, name='road-trip'),
    path('services/prepurchase-ins/', views.prepurchase_ins, name='prepurchase-ins'),
    path('services/major-service/', views.major_service, name='major-service'),
    path('', views.home, name='home'),
]