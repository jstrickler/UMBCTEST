"""
URL Configuration for apiv1
"""
from django.urls import path
from . import views   # import views from app

app_name = 'apiv1'

urlpatterns = [
    # add url patterns for the apiv1 app here

    # Example:
    path('heroes', views.heroes, name='heroes'),
    path('heroes/<int:pk>', views.heroes_detail, name='heroesdetail'),
    path('cities', views.cities, name='cities'),
    path('cities/<int:pk>', views.cities_detail, name='citiesdetail'),
    path('powers', views.powers, name='powers'),
    path('powers/<int:pk>', views.powers_detail, name='powersdetail'),
    path('enemies', views.EnemyList.as_view(), name='enemies'),
    path('enemies/<int:pk>', views.EnemyDetail.as_view(), name='enemiesdetail'),
]
