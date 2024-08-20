from django.contrib import admin
from django.urls import path
from djangoapp import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("admin/", admin.site.urls),
    path('UserProfiledetails/', login_required(views.UserProfiledetails))
]
