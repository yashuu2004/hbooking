from django.contrib import admin
from .models import State, City, Trip


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'state')
    list_filter = ('state',)
    search_fields = ('name',)


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = (
        'transport_type',
        'source',
        'destination',
        'date',
        'time',
        'price',
        'available_seats'
    )
    list_filter = ('transport_type', 'date')
    search_fields = ('source__name', 'destination__name')
