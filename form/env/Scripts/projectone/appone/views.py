from django.shortcuts import render
from django.http import HttpResponse
from . import forms


# Create your views here.
# def addUser(request):

#     form = forms.UserProfileForm()
#     if request.method == 'POST':
#         f = forms.UserProfileForm(request.POST)
#         print(f)
#     return render(request, 'addUser.html', {'form' : form})
from .forms import UserProfileForm
def addUser(request):

    f = forms.UserProfileForm()
    if request.method == 'POST':
        f = UserProfileForm(request.POST)
        if f.is_valid():
            f.save()
            print(f.is_valid())
            # print(f.cleaned_data)#{'first_name': 'Sudharshan Raju', 'last_name': 'Battala', 'course_name': 'python course', 'email': 'bsudharshan404@gmail.com', 'joining_date': datetime.date(2011, 11, 11), 'contact_number': '09392486441'}
            return HttpResponse("Data submitted")
        else:
            print(f.is_valid())
            print(f.errors)
    else:
        f=UserProfileForm()
    return render(request, 'addUser.html', {'form' : f})

