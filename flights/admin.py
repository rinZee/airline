from django.contrib import admin
from django.contrib.admin.decorators import register
from django.db import models

from .models import Flight, Airport, Passengers

# Register your models here.
class FlightAdmin(admin.ModelAdmin):
	list_display = ("id", "origin", "destination", "duration")

class PassengerAdmin(admin.ModelAdmin):
	filter_horizontal = ("flights",)

admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passengers, PassengerAdmin)