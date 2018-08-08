from django.urls import path

from . import views

urlpatterns = [
    # path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('services/oil-change-packages/', views.oil_change_packages, name='oil-change-packages'),
    path('', views.home, name='home'),
]