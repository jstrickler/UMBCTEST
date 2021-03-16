from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.generics import ListAPIView, RetrieveAPIView, get_object_or_404


from superheroes.models import Superhero, Enemy, Power, City

from .serializers import (
    SuperheroSerializer, PowerSerializer, EnemySerializer, CitySerializer
)

# hero endpoints
@api_view(['GET', 'POST'])
def heroes(request):
    if request.method == 'GET':
        heroes = Superhero.objects.all()
        serialized = SuperheroSerializer(heroes, many=True)
        return Response(serialized.data)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SuperheroSerializer(data=data)
        if serializer.is_valid():
            serializer.save() # ADD TO DATABASE
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def heroes_detail(request, pk):
    if request.method == 'GET':
        hero_obj = get_object_or_404(Superhero, pk=pk)
        serialized = SuperheroSerializer(hero_obj)

        return Response(serialized.data)

    if request.method == 'PUT':
        return Response("PUT REQUEST")

    if request.method == 'DELETE':
        return Response("DELETE REQUEST")


# power endpoints
@api_view(['GET'])
def powers(request):
    powers = Power.objects.all()
    serialized = PowerSerializer(powers, many=True)

    return Response(serialized.data)


@api_view(['GET'])
def powers_detail(request, pk):
    if request.method == 'GET':
        power_obj = Power.objects.get(pk=pk)
        serialized = PowerSerializer(power_obj)

        return Response(serialized.data)

# city endpoints
@api_view(['GET', 'POST'])
def cities(request):
    if request.method == 'GET':
        all_cities = City.objects.all()
        serialized = CitySerializer(all_cities, many=True)
        return Response(serialized.data)


@api_view(['GET'])
def cities_detail(request, pk):
    if request.method == 'GET':
        city = City.objects.get(pk=pk)
        serialized = CitySerializer(city)

        return Response(serialized.data)


# enemy endpoints
class EnemyList(ListAPIView):
    queryset = Enemy.objects.all()
    model = Enemy
    serializer_class = EnemySerializer


class EnemyDetail(RetrieveAPIView):
    queryset = Enemy.objects.all()
    model = Enemy
    serializer_class = EnemySerializer


