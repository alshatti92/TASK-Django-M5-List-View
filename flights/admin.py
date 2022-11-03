from django.contrib import admin

# Register your models here.
from .models import Booking, Flight

admin.site.register(Flight)

admin.site.register(Booking)