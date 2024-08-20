from django.shortcuts import render
from django.template import loader
from .models import Userprofile
from django.http import HttpResponse



# Create your views here.
def UserProfiledetails(requests):

    template=loader.get_template("UserProfiledetails.html")
    details=Userprofile.objects.all()

    d={"details":details}
    return HttpResponse(template.render(context=d))

