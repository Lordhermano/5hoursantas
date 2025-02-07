from django.urls import path
from santas import views

urlpatterns = [
    path('',views.home,name=''),
    path('Travel',views.Travel,name='Travel'),
    path('Things',views.Things,name='Things')
]