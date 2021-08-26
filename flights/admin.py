from django.contrib import admin
from django.contrib.admin.decorators import register

from .models import Flight, Airport
# Register your models here.
admin.site.register(Airport)
admin.site.register(Flight)