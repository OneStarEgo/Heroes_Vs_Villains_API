from django.urls import path
from . import views


urlpatterns = [
    path('', views.supers_list),
    path('<int:pk>/', views.super_details),
    path('heroes/', views.super_heroes),
    path('villains/', views.super_villains),
]