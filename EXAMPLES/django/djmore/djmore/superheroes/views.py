from django.shortcuts import get_object_or_404, render
from django.db.models import Min, Max, Count, FloatField, Q
from .models import Superhero


def home(request):
    data = {
        'message': 'Welcome to the superheroes app',
    }
    return render(request, 'home.html', data)

