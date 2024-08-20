from django.db import models

# Create your models here.
class Car(models.Model):

    engine = models.CharField(max_length=100)
    torque = models.CharField(max_length=100)
    power = models.CharField(max_length=100)
    seating_capacity = models.IntegerField()

class CarImage(models.Model):

    car = models.ForeignKey(Car, related_name='imgs', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='car_images/')