from django.db import models

# Create your models here.
class Userprofile(models.Model):

    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    contact=models.IntegerField()
