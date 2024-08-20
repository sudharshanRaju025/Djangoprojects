from django import forms
from .models import Car, CarImage

class CarForm(forms.ModelForm):

    class Meta:

        model = Car
        fields = ['engine', 'torque', 'power', 'seating_capacity']


class CarImageForm(forms.ModelForm):

    class Meta:

        model = CarImage
        fields = ['image']