from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):

    class Meta:

        model = Ticket
        fields = ['from_location', 'to_location', 'date', 'time', 'user_name', 'email', 'contact_number',"purpose"]

        def clean_contact_number(self):

            contact_number = self.cleaned_data.get('contact_number')
            if not contact_number.isdigit():
                raise forms.ValidationError('Contact Number must contain only digits')
            if len(contact_number) != 10:
                raise forms.ValidationError('Contact Number must be exactly 10 digits only')
            return contact_number

class SearchForm(forms.Form):
    query=forms.CharField(label="search",max_length=100)