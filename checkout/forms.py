from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    model = Order
    fields = ('full_name', 'email', 'phone_number', 'street_address1',
                'street_address2', 'town_or_city', 'postcode', 'country', 'county',)


    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        # dict of placeholders
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'country' : 'Country',
            'postcode': 'Post Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County',
        }
        # Start form with user full name and setting other placeholders
        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            # placeholders set so removing form field labels
            self.fields[field].label = False