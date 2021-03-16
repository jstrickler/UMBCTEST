#!/usr/bin/env python
# (c) 2017 CJ Associates
#
from rest_framework import serializers
from superheroes.models import Superhero, City, Power, Enemy

class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ('id', 'name')


class PowerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Power
        fields = ('id', 'name', 'description')


class EnemySerializer(serializers.ModelSerializer):
    powers = PowerSerializer(many=True)

    class Meta:
        model = Enemy
        fields = ('id', 'name', 'powers')


class SuperheroSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    enemies = EnemySerializer(many=True)
    powers = PowerSerializer(many=True)

    class Meta:
        model = Superhero
        fields = (
            'id', 'name', 'secret_identity', 'real_name',
            'city', 'enemies', 'powers'
        )


