from django.db import models

# Create your models here.
class Ticket(models.Model):

    INDIAN_CITIES=[
        ("hyderabad","hyderabad"),
        ("bangalore","bangalore"),
        ("chennai","chennai"),
        ("mumbai","mumbai"),
        ("kadapa","kadapa"),
    ]

    Purpose=[
        ("Vacation","Vacation"),
        ("Tovisit Temples","Tovisit Temples"),
        ("Short-term stay","Short-term stay"),
        ("Long-term stay","Long-term stay"),
        ("studies","Studies"),
        ("others","others"),
    ]
    
    
    from_location=models.CharField(max_length=100,choices=INDIAN_CITIES)
    to_location=models.CharField(max_length=100,choices=INDIAN_CITIES)
    date=models.DateField()
    time=models.TimeField()

    user_name=models.CharField(max_length=100)
    email=models.EmailField()
    contact_number=models.CharField(max_length=10)
    purpose=models.CharField(max_length=100,choices=Purpose,default=None)




