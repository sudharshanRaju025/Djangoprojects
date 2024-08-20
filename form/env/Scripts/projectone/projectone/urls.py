from django.contrib import admin
from django.urls import path
from appone import views as user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addUser/', user.addUser)
]