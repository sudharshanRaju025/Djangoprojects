from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from appone.models import UserProfile

# Create your views here.
def UserProfileDetails(request):
    template=loader.get_template('UserProfileDetails.html')
    details=UserProfile.objects.all()
    d={"details":details}

    return HttpResponse(template.render(context=d))
