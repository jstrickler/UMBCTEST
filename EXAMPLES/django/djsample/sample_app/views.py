from django.http import HttpResponse
from django.shortcuts import render
from .models import Person

# Create your views here.

# example without template (you probably won't be doing this):
# def home(request):
#     return HttpResponse("Hello Django world")

# example with template (normal Django approach)
def home(request):
    person = Person.objects.get(pk=1)
    context = {
        'message': 'Hello from the sample Application',
        'person': person,
    }
    return render(request, 'sample_app/home.html', context)
