from django.urls import path
from .views import book_trip, booking_success, booking_history

urlpatterns = [
    path("book/<int:trip_id>/", book_trip, name="book_trip"),
    path("success/", booking_success, name="booking_success"),
    path("history/", booking_history, name="booking_history"),
]
