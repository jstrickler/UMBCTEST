"""
URL Configuration for superheroes
"""
from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # welcome page, no class-based views
    path(
        '',
        views.HomeView.as_view,
        name = 'home'
    ),

    # NO view -- don't do this:
    path(
        'noview',
        TemplateView.as_view(template_name='noview.html'),
        name="noview",
    ),

    # minimal views with models
    path(
        'minimallist',
        views.HeroListViewMinimal.as_view(),
        name="minimallist",
    ),
    url(
        r'(?i)minimaldetails/(?P<pk>\d+)$',
        views.HeroDetailViewMinimal.as_view(),
        name="minimaldetails",
    ),

    #
    url(
        r'(?i)genericcontext$',
        views.GenericContext.as_view(),
        name="genericcontext",
    ),
    url(
        r'(?i)genericlist$',
        views.HeroListView.as_view(),
        name="genericlist",
    ),
    url(
        r'(?i)genericdetail/(?P<pk>\d+)/$',
        views.HeroDetailView.as_view(),
        name="genericdetail",
    ),
    url(
        r'(?i)herocreate/$',
        views.HeroCreateView.as_view(),
        name="herocreate",
    ),
    url(
        r'(?i)heroupdate/(?P<pk>\d+)/$',
        views.HeroUpdateView.as_view(),
        name="heroupdate",
    ),
    path(
        'success', views.SuccessView.as_view(), name="success",
    )
]

