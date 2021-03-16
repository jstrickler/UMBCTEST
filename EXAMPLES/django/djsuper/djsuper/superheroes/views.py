from django.http import HttpResponse, Http404
from .models import Superhero

def home(request):
    return HttpResponse("Welcome to my app")

def hero(request, hero_city='Petaluma', hero_name=""):
    if hero_city == '':
        hero_city = 'Corning, NY'
    print("hero_city:", hero_city, repr(hero_city), type(hero_city))
    # if hero_city is None:
    #     print('wahhhhh')
    s = Superhero.objects.get(name=hero_name)
    return HttpResponse(
        "{} is really {} from {}".format(s.secret_identity, s.name, hero_city)
    )

def hero2(request, hero_name):
    return HttpResponse(
        "I'm {}!".format(hero_name)
    )

def heroerror(request):
    raise Http404("Oops")
