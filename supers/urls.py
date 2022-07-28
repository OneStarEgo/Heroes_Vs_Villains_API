from django.urls import path
from . import views


urlpatterns = [
    path('', views.supers_list),
    path('<int:pk>/', views.super_details),
    path('', views.super_heroes),
    path('', views.super_villains),
]