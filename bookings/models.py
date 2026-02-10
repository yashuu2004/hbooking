from django.db import models
from django.contrib.auth.models import User
from trips.models import Trip


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    seats_booked = models.IntegerField(default=1)
    total_price = models.PositiveIntegerField() 
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
     return f"{self.user.username} - {self.trip}"
