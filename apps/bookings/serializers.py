from rest_framework import serializers
from .models import Guest_booking, Guest_registration

class GuestBookingSerializer(serializers.ModelSerializer):
  class Meta: 
    model = Guest_booking
    fields = '__all__'

class GuestRegistrationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Guest_registration
    fields = '__all__'
