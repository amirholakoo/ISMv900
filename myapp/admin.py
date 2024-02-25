from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Truck)
class TruckAdmin(admin.ModelAdmin):
    list_display = ('license_number', 'driver_name', 'phone', 'status', 'location')
    search_fields = ('license_number', 'driver_name')
    list_filter = ('status', 'location')  # Add filters
    ordering = ['-license_number']  # Sort by license number in descending order

