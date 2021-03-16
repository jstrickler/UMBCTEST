"""
URL Configuration for superheroes
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^demoform', views.demoform, name='demoform'),
    url(r'^heroform', views.heroform, name='heroform'),
    url(r'^heromodel', views.heromodel, name='heromodel'),
]

