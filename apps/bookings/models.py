from django.db import models


class Guest_booking(models.Model):
    BOOKING_METHODS = (("PH", "PHONE"), ("BK", "BOOKING"), ("RE", "LOBBY"))
    arriving_date = models.DateTimeField(auto_now_add=True)
    check_out_date = models.DateTimeField(auto_now=True)
    booking_method = models.CharField(max_length=15, default="PH", choices=BOOKING_METHODS)
    name= models.CharField(max_length=40, default='')
    last_name=models.CharField(max_length=40, default='')
    adults = models.IntegerField(default=1)
    childs = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    room = models.IntegerField(null=True)

    def __str__(self):
        return "Huesped " + self.name


class Guest_registration(models.Model):
    PAYMENT_TYPE = (("CS", "CASH"), ("CR", "CARD"), ("MT", "MONEY TRANSFER"))
    booking = models.ForeignKey(Guest_booking, on_delete=models.CASCADE)
    registration_date = models.DateField()
    # towels = models.IntegerField(default=2)
    payment_type = models.CharField(max_length=15, default="CS", choices=PAYMENT_TYPE)
    # employee = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL)
    car_plates = models.CharField(max_length=15)
    debt = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    hasDebt = models.BooleanField(default=False)
    vehicle = models.CharField(max_length=30)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

# class Guest(models.Model):
#     name= models.CharField(max_length=60)
#     last_name=models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
#     updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)