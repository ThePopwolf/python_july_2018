from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register/', views.register),
    path('verify/', views.verify),
    path('success/', views.success),
    path('log_out/', views.log_out),
]
