from django.db import models
from django.contrib.auth.models import User


class Flight(models.Model):
    flight_number = models.CharField(max_length=100)
    departure_city = models.CharField(max_length=50)
    arrival_city = models.CharField(max_length=50)
    departure_date = models.DateField()
    arrival_date = models.DateField()
    avialable_seats = models.PositiveIntegerField()

    def __str__(self):
        return 


class Passenger(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    passport_number = models.CharField(max_length=20)


class Booking(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    booking_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    # hotel = models.ForeignKey()



class Review(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comments = models.TextField()


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    read_is = models.BooleanField(default=False)


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    description = models.TextField()
    room_capacity = models.PositiveIntegerField()
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    

class CarRental(models.Model):
    name_company = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    description = models.TextField()
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name_company
    

class Discount(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

    


