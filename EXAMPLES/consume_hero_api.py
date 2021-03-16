#!/usr/bin/env python
#
from pprint import pprint
import requests


def print_if_ok(response, message):
    print("** {} **".format(message))
    print(response.status_code)
    if response.status_code == requests.codes.OK:
        pprint(response.json())
    else:
        print("Oops:")  # , response.status_code)


hero_response = requests.get('http://localhost:8000/api/v1/herolist')
print_if_ok(hero_response, 'all heroes')
print('-' * 60)

hero_response = requests.get('http://localhost:8000/api/v1/hero/1')
print_if_ok(hero_response, 'hero #1')
print('-' * 60)

hero_response = requests.get('http://localhost:8000/api/v1/hero/2')
print_if_ok(hero_response, 'hero #2')

print('=' * 60)
hero_response = requests.get('http://localhost:8000/api/v1/enemylist')
print_if_ok(hero_response, 'all enemies')

print('-' * 60)
hero_response = requests.get('http://localhost:8000/api/v1/enemy/1')
print_if_ok(hero_response, 'enemy #1')

print('-' * 60)
hero_response = requests.get('http://localhost:8000/api/v1/enemy/5')
print_if_ok(hero_response, 'enemy #5')
