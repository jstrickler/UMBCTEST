from django.contrib import admin

# Register your models here.

from superheroes.models import Superhero, Power, Enemy, City # <1>

admin.site.register(Superhero)  # <2>
admin.site.register(City) # <2>
admin.site.register(Enemy) # <2>


class PowerAdmin(admin.ModelAdmin):  # <3>
    search_fields = ['name', 'description'] # <4>

admin.site.register(Power, PowerAdmin) # <5>
