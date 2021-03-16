from django.shortcuts import get_object_or_404, get_list_or_404, render
from .models import Superhero

def hero_sort(request):
    heroes = get_list_or_404(Superhero)
    data = {
        'heroes': heroes
    }
    return render(request, 'hero_meta.html', data)

def hero_details(request, hero_name):
    hero =  get_object_or_404(Superhero, name=hero_name)
    data = {
        'hero': hero
    }
    return render(request, 'hero_details.html', data)
