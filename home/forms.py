from django import forms
from django.contrib.auth import get_user_model
from . import models
from dashboard.models import Customer,Order
from django.contrib.auth.models import User

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["ordered_by", "shipping_address",
                  "mobile", "email", "payment_method"]
        

    


