from django.shortcuts import render, get_object_or_404
from .models import Superhero


def hero_manager(request):
    fliers = Superhero.objects.get_fliers()
    context = { 'page_title': "Fliers", 'fliers': fliers }
    return render(request, 'hero_manager.html', context)

def hero_details(request, hero_name):
    hero =  get_object_or_404(Superhero, name=hero_name)
    data = {
        'hero': hero
    }
    return render(request, 'hero_details.html', data)
