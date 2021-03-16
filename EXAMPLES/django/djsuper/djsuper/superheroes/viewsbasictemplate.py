from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Superhero


def hero_basic_template(request, hero_name):
    hero =  get_object_or_404(Superhero, name=hero_name)
    context = {
        'hero_name': hero.name,
        'real_name': hero.real_name,
        'secret_identity': hero.secret_identity,
    }
    return render(request, 'hero_basic.html', context)
