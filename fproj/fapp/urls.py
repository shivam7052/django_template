from django.contrib import admin
from django.urls import path, include
from fapp import views

urlpatterns = [
    path('', views.home, name='home'),
]