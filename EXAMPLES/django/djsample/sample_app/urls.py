"""
URL Configuration for sample_app
"""
from django.urls import path
from . import views   # import views from app

urlpatterns = [
    # add url patterns for the sample_app app here

    # Example:
    path('', views.home, name='home'),
]
