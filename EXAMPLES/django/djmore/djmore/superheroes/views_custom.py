from django.shortcuts import render, get_object_or_404
from .models import Superhero


def hero_custom(request, hero_name):
    hero = get_object_or_404(Superhero, name=hero_name)
    context = {
        'page_title': "Custom Function",
        'hero': hero,
        'enemies': hero.get_brief_enemies
    }
    return render(request, 'hero_custom.html', context)
