from django.shortcuts import render
from django.http import JsonResponse
from .models import Trip, City, State


# AJAX: Load cities based on selected state
def cities_by_state(request, state_id):
    cities = City.objects.filter(state_id=state_id).values("id", "name")
    return JsonResponse(list(cities), safe=False)


# MAIN SEARCH PAGE (like RedBus home)
def search_trips(request):
    trips = None
    states = State.objects.all()

    if request.method == "POST":
        transport = request.POST.get("transport_type")
        source = request.POST.get("source")
        destination = request.POST.get("destination")
        date = request.POST.get("date")

        trips = Trip.objects.filter(
            transport_type=transport,
            source_id=source,
            destination_id=destination,
            date=date
        )

    return render(
        request,
        "trips/search.html",
        {
            "states": states,
            "trips": trips,
        }
    )


# OPTIONAL: View all trips (admin-style / testing)
def trip_list(request):
    trips = Trip.objects.all()
    return render(
        request,
        "trips/trip_list.html",
        {
            "trips": trips
        }
    )


def home(request):
    trips = Trip.objects.all()
    return render(request, "trips/home.html", {"trips": trips})

def bus_page(request):
    return render(request, "trips/bus.html")

def train_page(request):
    return render(request, "trips/train.html")

def flight_page(request):
    return render(request, "trips/flight.html")