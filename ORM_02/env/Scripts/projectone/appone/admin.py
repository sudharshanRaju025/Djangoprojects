from django.contrib import admin
from appone.models import UserProfile

# Register your models here.
class UserprofileAdmin(admin.ModelAdmin):
    list_display=("user_name","user_contact","user_email","product_name","product_cost")
    search_fields=("user_name","user_email")

admin.site.register(UserProfile,UserprofileAdmin)
