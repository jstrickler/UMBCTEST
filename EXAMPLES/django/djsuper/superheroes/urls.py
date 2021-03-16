"""
URL Configuration for superheroes
"""
from django.conf.urls import url
from . import views   # import views from app
from . import views404
from . import viewsbasictemplate
from . import viewstemplate
from . import viewsqueries

urlpatterns = [
    url('', views.home, name='home'),
    url('hero/<str:hero_name>/', views.hero, name="hero"),
    url('hero404x/<str:hero_name>/', views404.hero404, name="hero404"),
    url('hero404sc/<str:hero_name>/', views404.hero404sc, name="hero404sc"),
    url(
        'herotemplate101/<str:hero_name>/',
        viewsbasictemplate.hero_basic_template,
        name="herobasictemplate",
    ),
    url(
        'herohardway/<str:hero_name>/',
        viewstemplate.hero_hard_way,
        name="herohardway",
    ),
    url(
        'heroeasyway/<str:hero_name>/',
        viewstemplate.hero_easy_way,
        name="heroeasyway",
    ),
    url(
        'herolookups/<str:hero_name>/',
        viewstemplate.hero_lookups,
        name="herolookups",
    ),
    url(
        'herofilters/<str:hero_name>/',
        viewstemplate.hero_filters,
        name="herofilters",
    ),
    url(
        'herotags/<str:hero_name>/',
        viewstemplate.hero_tags,
        name="herotags",
    ),
    url(
        'herodetails/<str:hero_name>/',
        viewstemplate.hero_details,
        name="herodetails",
    ),
    url(
        'heroescape/<str:hero_name>/',
        viewstemplate.hero_escape,
        name="heroescape",
    ),
    url(
        'herourls/',
        viewstemplate.hero_urls,
        name="herourls",
    ),
    url(
        'herostatic/<str:hero_name>/',
        viewstemplate.hero_static,
        name="herostatic",
    ),
    url(
        'heroqueries/',
        viewsqueries.hero_queries,
        name="heroqueries",
    ),
]

