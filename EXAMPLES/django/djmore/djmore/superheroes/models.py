from django.db import models
import logging

logging.basicConfig(
    filename='superheroes.log',
    level=logging.INFO,
)

class LoggingMixin():
    def save(self, *args, **kwargs):
        logging.info("Created record")
        super().save(*args, **kwargs)
        # type(self).mro()
        # do something else here as needed


class SuperheroManager(models.Manager):
    def get_fliers(self):
        return self.filter(powers__name__icontains="fly")


class Power(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=512)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Enemy(models.Model):
    name = models.CharField(max_length=32)
    powers = models.ManyToManyField(Power)

    def __str__(self):
        return self.name


class Superhero(LoggingMixin, models.Model):
    name = models.CharField(max_length=32)
    real_name = models.CharField(max_length=32)
    secret_identity = models.CharField(max_length=32)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    powers = models.ManyToManyField(Power)
    enemies = models.ManyToManyField(Enemy)
    objects = SuperheroManager()

    def __str__(self):
        return self.name

    # must use "Meta"
    class Meta():
        ordering = ['secret_identity']
        verbose_name = 'superhero'
        verbose_name_plural = 'superheroes'
        man

    def get_brief_enemies(self):
        enemies = [e.name.split()[-1] for e in self.enemies.all()]
        return '/'.join(enemies)

    # def save(self, *args, **kwargs):
    #     logging.info("Created superhero {}".format(self.name))
    #     super().save(*args, **kwargs)
    #     # do something else here as needed

