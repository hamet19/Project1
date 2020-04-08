from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Contry)
admin.site.register(City)
admin.site.register(Airline)
admin.site.register(Aeroport)
admin.site.register(Ligne)
admin.site.register(Plane)



