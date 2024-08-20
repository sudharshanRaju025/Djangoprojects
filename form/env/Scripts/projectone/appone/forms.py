from django import forms
from appone.models import UserProfile
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError

class UserProfileForm(forms.ModelForm):

    class Meta:

        model = UserProfile  # hete UserProfile is a Model class
        fields = '__all__' # all the models fileds are included here

    first_name=forms.CharField(validators=[MinLengthValidator(3)])
    last_name=forms.CharField(validators=[MinLengthValidator(3)])


    def clean_first_name(self):
        first_name=self.cleaned_data.get("first_name")
        if first_name and first_name[0].islower():
            raise ValidationError("first letter must be uppercase")
        return first_name
    
    def clean_last_name(self):

        last_name=self.cleaned_data.get("last_name")
        if last_name and last_name[0].islower():
            raise ValidationError("first letter must be uppercase")
        return last_name
    
    # def clean_first_name(self):

    #     first_name = self.cleaned_data.get('first_name')
    #     if first_name and first_name[0].islower():
    #         raise ValidationError('First Letter Must be UpperCase')
    #     return first_name