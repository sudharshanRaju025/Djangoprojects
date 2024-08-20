from django.shortcuts import render, redirect
from .models import Car, CarImage
from .forms import CarForm, CarImageForm
# Create your views here.
def car_list(request):

    cars = Car.objects.all()
    return render(request, 'car_list.html', {'cars': cars})

def car_create(request):

    if request.method == 'POST':
        car_form = CarForm(request.POST)
        if car_form.is_valid():
            c = car_form.save()
        for file in request.FILES.getlist('images'):
            CarImage.objects.create(car = c, image = file)
        return redirect('car_list')
    
    else:
        car_form = CarForm()
    return render(request, 'car_form.html', {'car_form': car_form})