from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Guest_booking
from .serializers import GuestBookingSerializer


class GuestBookingView(APIView):
    def get_object(self, pk):
        try:
            return Guest_booking.objects.get(pk=pk)
        except Guest_booking.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        guest_booking = self.get_object(pk)
        serializer = GuestBookingSerializer(guest_booking)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        guest_booking = self.get_object(pk)
        serializer = GuestBookingSerializer(guest_booking, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        guest_booking = self.get_object(pk)
        guest_booking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GuestRegistrationListView(APIView):
    def get(self, request):
        guest_bookings = Guest_booking.objects.all()
        serializer = GuestBookingSerializer(guest_bookings, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GuestBookingSerializer(data=request.data)
        form = request.POST
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
