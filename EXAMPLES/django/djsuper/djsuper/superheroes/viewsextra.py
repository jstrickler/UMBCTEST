from django.shortcuts import get_object_or_404, render
from django.db.models import Count, Sum, Case, When, IntegerField
from .models import Superhero

def hero_extra(request):
    heroes = Superhero.objects.all().annotate(
        num_enemies=Count('enemies')
    )

    fliers = Superhero.objects.all().aggregate(
        num_fliers=Sum(
            Case(
                When(powers__name__contains="flying", then=1),
            ),
            output_field=IntegerField(),
        )
    )

    context = {
        'page_title': 'aggregate() and annotate()',
        'heroes': heroes,
        'fliers': fliers,
    }
    return render(request, 'hero_extra.html', context)

