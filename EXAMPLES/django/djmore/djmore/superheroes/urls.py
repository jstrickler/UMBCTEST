"""
URL Configuration for superheroes
"""
from django.conf.urls import url
from . import views
from . import views_meta
from . import views_custom
from . import views_manager

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^herosort$', views_meta.hero_sort, name='herosort'),
    url(
        r'^herodetails/(?P<hero_name>.*)',
        views_meta.hero_details,
        name="herodetails",
    ),
    url(
        r'^flyerdetails/(?P<hero_name>.*)',
        views_manager.hero_details,
        name="flyerdetails",
    ),
    url(
        r'^herocustom/(?P<hero_name>.*)',
        views_custom.hero_custom,
        name="herocustom",
    ),
    url(
        r'^heromanager/',
        views_manager.hero_manager,
        name="heromanager",
    ),
]

