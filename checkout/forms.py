from django import forms
from .models import Order


class Orderform(forms.ModelForm):
    model = Order
    fields = ('full_name', 'email', 'phone_number',
             'street_address1', 'street_address2',
              'town_or_city', 'postcode', 'country',
               'county',)
    