from django.db import models
from datetime import date

class Power(models.Model):
    name = models.CharField(max_length=32, unique=True)
    description = models.CharField(max_length=512)

    def __str__(self):
        return self.name


class DefaultDate(models.DateField):
    # predefined name "from_db_value"
    def from_db_value(self, value, expression, connection, context):
        if value is None:
            value = date.today()
        return value

class City(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name

class Enemy(models.Model):
    name = models.CharField(max_length=32, unique=True)
    powers = models.ManyToManyField(Power)

    class Meta:
        permissions = [('create_dataframe', 'Can Create Dataframe')]

    def __str__(self):
        return self.name

class Superhero(models.Model):
    name = models.CharField(max_length=32, unique=True)
    real_name = models.CharField(max_length=32)
    date_of_death = DefaultDate(null=True)
    height = models.IntegerField()
    weakness = models.CharField(max_length=32)
    date_of_birth = models.DateField(null=True)
    favorite_color = models.CharField(max_length=10, default='blue')
    secret_identity = models.CharField(max_length=32)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    powers = models.ManyToManyField(Power)
    enemies = models.ManyToManyField(Enemy)

    def __str__(self):
        return self.name


