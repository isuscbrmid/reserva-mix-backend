from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .guest_booking_views import GuestBookingView, GuestBookingListView

app_name = "bookings"

urlpatterns = [
    path("", GuestBookingListView.as_view(), name="bookings_list"),
    path("/<int:pk>", GuestBookingView.as_view(), name="booking_details"),
]
