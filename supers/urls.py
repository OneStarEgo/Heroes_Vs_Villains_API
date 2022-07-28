from django.urls import path
from . import views


urlpatterns = [
    path('', views.supers_list),
    path('<int:pk>/', views.super_details),
    path('?type=', views.super_heroes),
    path('?type=', views.super_villains),
]