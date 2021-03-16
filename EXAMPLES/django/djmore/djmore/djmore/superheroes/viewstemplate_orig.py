#!/usr/bin/env python
# (c) 2016 John Strickler
#
from django.shortcuts import get_object_or_404, render
from .models import Superhero
from django.http import HttpResponse
from django.template.loader import get_template
from django.template.context import Context

def hero_hard_way(request, hero_name):
    hero =  get_object_or_404(Superhero, name=hero_name)
    data = {
        'hero_name': hero.name,
        'real_name': hero.real_name,
        'secret_identity': hero.secret_identity,
    }
    t = get_template('hero_basic.html')
    page = t.render(data)
    return HttpResponse(page)

def hero_easy_way(request, hero_name):
    hero =  get_object_or_404(Superhero, name=hero_name)
    data = {
        'hero_name': hero.name,
        'real_name': hero.real_name,
        'secret_identity': hero.secret_identity,
    }
    t = get_template('hero_basic.html')
    page = t.render(data)
    return HttpResponse(page)

def super_basic(request, hero_name):
    hero =  get_object_or_404(Superhero, name=hero_name)
    context = {
        'hero_name': hero.name,
        'real_name': hero.real_name,
        'secret_identity': hero.secret_identity,
    }
    return render(request, 'registry/reg_hero.html', context)




def super_lookups(request, hero_name):
    hero =  get_object_or_404(Superhero, name=hero_name)
    context = {'hero': hero}
    return render(request, 'registry/reg_lookups.html', context)


def super_filters(request, hero_name):
    hero =  get_object_or_404(Superhero, name=hero_name)
    context = {'hero': hero}
    return render(request, 'registry/reg_filter.html', context)


def super_escape(request, hero_name):
    hero =  get_object_or_404(Superhero, name=hero_name)
    context = {
        'hero': hero,
        'html_fragment': '<i>Some HTML</i>'
    }
    return render(request, 'registry/reg_escape.html', context)


def super_tags(request, hero_name):
    hero =  get_object_or_404(Superhero, name=hero_name)
    context = {'hero': hero}
    return render(request, 'registry/reg_tags.html', context)


def super_details(request, hero_name):
    hero =  get_object_or_404(Superhero, name=hero_name)
    context = {'page_title': hero.name, 'hero': hero}
    return render(request, 'registry/reg_hero_details.html', context)


def super_details_boot(request, hero_name):
    hero =  get_object_or_404(Superhero, name=hero_name)
    context = {'page_title': hero.name, 'hero': hero}
    return render(request, 'registry/reg_hero_details_boot.html', context)


def super_static(request, hero_name):
    hero =  get_object_or_404(Superhero, name=hero_name)
    context = {
        'page_title': hero.name,
        'hero': hero,
    }
    return render(request, 'registry/reg_hero_static.html', context)


def super_list(request):
    context = {
        'page_title': 'Superheroes',
        'superheroes': Superhero.objects.all()
    }
    return render(request, 'registry/reg_hero_list.html', context)


def super_list_boot(request):
    context = {
        'page_title': 'Superheroes',
        'superheroes': Superhero.objects.all()
    }
    return render(request, 'registry/reg_hero_list_boot.html', context)


def super_urls(request):
    context = {
        'page_title': 'Superheroes',
        'superheroes': Superhero.objects.all()
    }
    return render(request, 'registry/reg_hero_urls.html', context)

def boot_grid(request):
    context = {
        'heros': [
            'Batman', 'Aquaman', 'Spiderman',
            'Superman', 'The Hulk', 'Iron Man',
            'Black Widow', 'Green Arrow',
            'Daredevil'
        ],
        'page_title': 'Grid Demo',
    }
    return render(request, 'registry/reg_boot_grid.html', context)
