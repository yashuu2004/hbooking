# trips/models.py
from django.db import models

class State(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}, {self.state.name}"


class Trip(models.Model):
    TRANSPORT_CHOICES = [
        ("BUS", "Bus"),
        ("TRAIN", "Train"),
        ("FLIGHT", "Flight"),
    ]

    transport_type = models.CharField(max_length=10, choices=TRANSPORT_CHOICES)
    source = models.ForeignKey(City, related_name="source_trips", on_delete=models.CASCADE)
    destination = models.ForeignKey(City, related_name="destination_trips", on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    total_seats = models.IntegerField()
    available_seats = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
