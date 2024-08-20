from django.db import models

# Create your models here.
class UserProfile(models.Model):

    user_name=models.CharField(max_length=100)
    user_contact=models.CharField(max_length=100)
    user_email=models.EmailField()
    product_name=models.CharField(max_length=100)
    product_cost=models.DecimalField(max_digits=12,decimal_places=2,default=0.0)
    product_image=models.ImageField(upload_to='product_images/',default='default_product.jpg',null=True,blank=True)
