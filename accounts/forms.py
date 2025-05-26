from django import forms
from django.contrib.auth import get_user_model
from . import models
# from accounts.models import CustomUser
from dashboard.models import Customer
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.core import validators

# def starts_with_address(value):
#     if value != '\d+\s+([A-Za-z]+\s?)+,\s*\w+,\s*\w+\s*\d*$':
#         raise forms.ValidationError('Address must contain 5 letters')
    

# def starts_with_98(value):
#     if value != '98':
#         raise forms.ValidationError('Number must start with 98')


class CustomerRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.CharField(widget=forms.EmailInput())
    # full_name = forms.CharField(widget=forms.TextInput())
    # address = forms.CharField(validators=[starts_with_address])
    # contact = forms.IntegerField(validators=[starts_with_98])

    class Meta:
        model = Customer
        fields = ["username", "password", "email", "full_name", "address","contact"]

    def clean_username(self):
        uname = self.cleaned_data.get("username")
        if User.objects.filter(username=uname).exists():
            raise forms.ValidationError(
                "Customer with this username already exists.")

        return uname
    
class CustomerLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())



class AdminLoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)

    class Meta:
        fields = ['email','password']

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        error = forms.ValidationError({
            'email' : 'Email or Password didn\'t match.'
        })

        user_queryset = User.objects.filter(email=email)
        if not user_queryset.exists():
            raise error
        
        user = user_queryset.first()
        if not user.check_password(password):
            raise error
        
        self.instance = user

# class AdminLoginForm(UserCreationForm):
#     username= forms.CharField()
#     password= forms.CharField(widget=forms.PasswordInput)




# class CustomUserCreationForm(UserCreationForm):

#     class Meta(UserCreationForm):
#         model = CustomUser
#         fields = ('email',)


# class CustomUserChangeForm(UserChangeForm):

#     class Meta:
#         model = CustomUser
#         fields = ('email',)

