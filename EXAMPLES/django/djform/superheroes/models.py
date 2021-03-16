"""
Models for superhero project

Blahdy-blahdy-blah
"""
from django.db import models
import logging

logging.basicConfig(
    filename='superheroes.log',
    level=logging.INFO,
)

class SuperheroManager(models.Manager):
    """
    Custom manager for the Superhero model
    """
    def get_fliers(self):
        return self.filter(powers__name__icontains="fly")

class Power(models.Model):
    """
    Special ability. Used by both Superhero and Enemy
    """
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=512)

    def __str__(self):
        return self.name

class City(models.Model):
    """
    Primary city where Superhero lives/works.
    """
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class Enemy(models.Model):
    """
    Superhero antagonist. Has powers.
    """
    name = models.CharField(max_length=32)
    powers = models.ManyToManyField(Power)

    def __str__(self):
        return self.name

class Superhero(models.Model):
    """
    Weirdly enhanced person who tries to save the world with ridiculous
    collateral damage.
    """
    name = models.CharField(max_length=32)
    real_name = models.CharField(max_length=32)
    secret_identity = models.CharField(max_length=32)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    powers = models.ManyToManyField(Power)
    enemies = models.ManyToManyField(Enemy)
    objects = SuperheroManager()

    def __str__(self):
        return self.name

    class Meta():
        ordering = ['secret_identity']

    def get_brief_enemies(self):
        enemies = [e.name.split()[-1] for e in self.enemies.all()]
        return '/'.join(enemies)

    def save(self, *args, **kwargs):
        logging.info("Created superhero {}".format(self.name))
        super().save(*args, **kwargs)
        # do something else here as needed

