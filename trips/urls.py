from django.urls import path
from .views import search_trips, cities_by_state
from . import views

urlpatterns = [
    path("", search_trips, name="search_trips"),
    path("cities/<int:state_id>/", cities_by_state, name="cities_by_state"),
    path("bus/", views.bus_page, name="bus_page"),
]
