from django.contrib import admin
from .models import Userprofile

# Register your models here.

class UserprofileAdmin(Userprofile):
      
      list_display=("username","email","contact")
      search_fields=('username',"email","contact")

admin.site.register(Userprofile,UserprofileAdmin)