from django.shortcuts import get_object_or_404, render
from django.db.models import Min, Max, Count, FloatField, Q
from .models import Superhero

q_hulk = Q(name__icontains="hulk")
q_woman = Q(name__icontains="woman")

def hero_queries(request):

    queries = [
        'Superhero.objects.all()',
        'Superhero.objects.filter(name="Superman")',
        'Superhero.objects.filter(name="Superman").first()',
        'Superhero.objects.filter(name="Spider-Man").first()',
        'Superhero.objects.filter(name="Spider-Man").first().secret_identity',
        'Superhero.objects.filter(name="Superman").first().enemies.all',
        'Superhero.objects.filter(name="Spider-Man").first().powers.all',
        'Superhero.objects.filter(name="Batman").first().powers.all',
        'Superhero.objects.exclude(name="Batman")',
        'Superhero.objects.order_by("name")',
        'Superhero.objects.count()',
        'Superhero.objects.aggregate(Count("name"))',
        'Superhero.objects.aggregate(Min("name"))',
        'Superhero.objects.aggregate(Max("name"))',
        'Superhero.objects.aggregate(Min("name"),Max("name"))',
        'Superhero.objects.filter(name__contains="man").count()',
        '''Superhero.objects.filter(
                name__contains="man").exclude(name__contains="woman")''',
        '''Superhero.objects.filter(
                name__contains="man").exclude(
                name__contains="woman").count()''',
        'Superhero.objects.all()[:3]',
        'Superhero.objects.filter(name__contains="man")[:2]',
        '''Superhero.objects.filter(
            enemies__name__icontains="Luthor").first().name''',
        'Superhero.objects.filter(q_hulk | q_woman)',
    ]

    query_pairs = [
        (query, eval(query)) for query in queries
    ]
    context = {
        'page_title': 'Query Examples',
        'query_pairs': query_pairs,
    }
    return render(request, 'hero_queries.html', context)

