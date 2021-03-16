from django.contrib import admin
# Register your models here.

from .models import Person

admin.site.register(Person)

# admin user is sampleadmin
# admin p/w is SampleAdmin
