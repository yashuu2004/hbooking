from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.db import transaction

from trips.models import Trip
from .models import Booking


@login_required
def book_trip(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id)

    if request.method == "POST":
        try:
            seats = int(request.POST.get("seats", 1))
        except ValueError:
            seats = 1

        if seats <= 0:
            seats = 1

        # 🔐 ATOMIC TRANSACTION (prevents overbooking)
        with transaction.atomic():
            trip.refresh_from_db()

            if trip.available_seats < seats:
                return render(request, "bookings/book_trip.html", {
                    "trip": trip,
                    "error": "Not enough seats available"
                })

            total_price = trip.price * seats

            booking = Booking.objects.create(
                user=request.user,
                trip=trip,
                seats_booked=seats,
                total_price=total_price
            )

            trip.available_seats -= seats
            trip.save()

        # 📧 EMAIL CONFIRMATION
        if request.user.email:
            send_mail(
                subject="Booking Confirmation",
                message=(
                    f"Hello {request.user.username},\n\n"
                    f"Your booking is confirmed!\n\n"
                    f"Route: {trip.source} → {trip.destination}\n"
                    f"Date: {trip.date}\n"
                    f"Seats Booked: {seats}\n"
                    f"Price per seat: ₹{trip.price}\n"
                    f"Total Price: ₹{total_price}\n\n"
                    "Thank you for booking with us."
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[request.user.email],
                fail_silently=False,
            )

        return redirect("booking_success")

    return render(request, "bookings/book_trip.html", {
        "trip": trip
    })


@login_required
def booking_success(request):
    return render(request, "bookings/booking_success.html")


@login_required
def booking_history(request):
    bookings = Booking.objects.filter(
        user=request.user
    ).order_by("-booking_date")

    return render(request, "bookings/history.html", {
        "bookings": bookings
    })
