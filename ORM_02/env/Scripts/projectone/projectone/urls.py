from django.contrib import admin
from django.urls import path
from appone import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("UserProfileDetails/",views.UserProfileDetails)

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
