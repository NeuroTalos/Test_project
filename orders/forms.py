from django import forms
from .models import *

class CheckoutContactFrom(forms.Form):
    name = forms.CharField(required = True)
    phone= forms.CharField(required = True)
