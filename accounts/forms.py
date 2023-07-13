from django import forms
from django.contrib.auth import get_user_model
from . import models
from dashboard.models import Customer
from django.contrib.auth.forms import UserCreationForm


# User = get_user_model()

# class LoginForm(forms.Form):
#     email = forms.CharField()
#     password = forms.CharField(widget = forms.PasswordInput)

#     class Meta:
#         fields = ['email', 'password']

#     def clean(self):
#         email = self.cleaned_data.get('email')
#         password = self.cleaned_data.get('password')

#         error = forms.ValidationError({
#             'email' : 'Email or Password didn\'t match.'
#         })

#         user_queryset = User.objects.filter(email=email)
#         if not user_queryset.exists():
#             raise error

#         user = user_queryset.first()
#         if not user.check_password(password):
#             raise error
        
#         self.instance = user

# class CustomerRegistrationForm(forms.ModelForm):
#     username = forms.CharField(widget=forms.TextInput())
#     email = forms.CharField(widget=forms.EmailInput())
#     password = forms.CharField(widget=forms.PasswordInput())

#     class Meta:
#         model = Customer
#         exclude= []


User = get_user_model()

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

class CreateUserForm(UserCreationForm):
    class Meta:
        model = Customer
        exclude =[]


class CustomerRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.CharField(widget=forms.EmailInput())
    full_name = forms.CharField(widget=forms.TextInput())
    address = forms.CharField(widget=forms.TextInput())
    contact = forms.IntegerField(widget = forms.NumberInput)

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

