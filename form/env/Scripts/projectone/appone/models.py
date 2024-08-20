from django.db import models

# Create your models here.
class UserProfile(models.Model):

    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    course_name = models.CharField(max_length=25)
    email = models.EmailField()
    joining_date = models.DateField() # Month/Date/Year
    contact_number = models.CharField(max_length=15)