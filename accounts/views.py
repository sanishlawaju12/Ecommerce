from django.shortcuts import render,redirect,reverse
from django.views.generic import View, TemplateView, CreateView, FormView, DetailView, ListView
from django.http import HttpResponseRedirect,HttpResponse
from django.core.mail import send_mail
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from .models import *
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth import login,logout,authenticate
from .forms import AdminLoginForm, CustomerRegistrationForm, User, CustomerLoginForm
from dashboard.models import Customer
import re

from accounts import forms 
 
# Create your views here.

# #for showing login button for admin
# def adminLoginView(request):
#     if request.user.is_authenticated:
#         return HttpResponseRedirect('afterlogin')
#     return HttpResponseRedirect('adminlogin')

# def customerSignUpView(request):
#     userForm = forms.CustomerUserForm()
#     customerForm = forms.CustomerForm()
#     mydict={'userForm':userForm,'customerForm':customerForm}
#     if request.method=='POST':
#         userForm=forms.CustomerUserForm(request.POST)
#         customerForm=forms.CustomerForm(request.POST,request.FILES)
#         if userForm.is_valid() and customerForm.is_valid():
#             user=userForm.save()
#             user.set_password(user.password)
#             user.save()
#             customer=customerForm.save(commit=False)
#             customer.user=user
#             customer.save()
#             my_customer_group = Group.objects.get_or_create(name='CUSTOMER')
#             my_customer_group[0].user_set.add(user)
#         return HttpResponseRedirect('customerlogin')
#     return render(request,'account/customersignup.html',context=mydict)

# #-----------for checking user is customer
# def is_customer(user):
#     return user.groups.filter(name='CUSTOMER').exists()


# #---------AFTER ENTERING CREDENTIALS WE CHECK WHETHER USERNAME AND PASSWORD IS OF ADMIN,CUSTOMER
# def afterLoginView(request):
#     if is_customer(request.user):
#         return redirect('home:home.html')
#     else:
#         return redirect('dashboard:index.html')
    



class CustomerRegistrationView(CreateView):
    template_name = "accounts/customerregistration.html"
    form_class = CustomerRegistrationForm
    success_url = reverse_lazy ("home:home")

    def form_valid(self,form):
        full_name = form.cleaned_data.get("full_name")
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("Password")
        address = form.cleaned_data.get("address")
        contact = form.cleaned_data.get("contact")
        Customer = User.objects.create_user(username,email,password)
        form.instance.user = Customer
        login(self.request,Customer)
        return super().form_valid(form)


    def get_success_url(self):
        if "next" in self.request.GET:
            next_url = self.request.GET.get("next")
            return next_url
        else:
            return self.success_url


class CustomerLoginView(FormView):
    template_name = "accounts/customerlogin.html"
    form_class = CustomerLoginForm
    success_url = reverse_lazy("home:home")

    # form_valid method is a type of post method and is available in createview formview and updateview
    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data["password"]
        user = authenticate(username=username, password=password)
        if user is not None and Customer.objects.filter(user=user).exists():
            login(self.request, user)
        else:
            return render(self.request, self.template_name, {"form": self.form_class, "error": "Invalid credentials"})

        return super().form_valid(form)

    def get_success_url(self):
        if "next" in self.request.GET:
            next_url = self.request.GET.get("next")
            return next_url
        else:
            return self.success_url


class AdminLoginViews(FormView):
    template_name = 'accounts/login.html'
    form_class = AdminLoginForm
    

    def form_valid(self, form):
        login(self.request, form.instance)
        return redirect(reverse_lazy('dashboard:home'))


class AdminLogoutViews(FormView):
    def get(self, request, *args, **kwargs):
        logout(self.request)
        return redirect(reverse_lazy('accounts:adminloginform'))



# @login_required
# def adminloginform(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(request, username=username,password=password)

#         if user is not None:
#             if not user.is_staff:
#                 login(request,user)
#                 return redirect('home:home')
#             elif user.is_staff:
#                 login(request,user)
#                 return redirect('dashboard:home')
#         else:
#             messages.info(request,"username or password is invalid")

#     context = {}
#     return render(request, 'accounts/login.html',context)


# def loginform(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user  = authenticate(request, username=username,password=password)

#         if user is not None:
#             login(request,user)
#             return redirect('home:home')
#         else:
#             messages.info(request,"Username or password is invalid")
    
#     context = {}
#     return render(request,'accounts/customerlogin.html', context)

# def registerform(request):
#     n=''
#     if request.method == "POST":
#         username = request.POST.get('username') 
#         password = request.POST.get('password')
#         email = request.POST.get('email')
#         full_name = request.POST.get('full_name')
#         address = request.POST.get('address')
#         contact = request.POST.get('contact')
#         if form.is_valid():
      

#         errors = {}
#         #perform Validation
#         email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#         if not email:
#             errors['email'] = 'email field is requied.'
#         elif not re.match(email_pattern,email):
#             errors['email'] = 'email is not valid.'
#         elif Customer.objects.filter(email=email).exists():
#             errors['email'] = 'email is already taken.'
        
#         password_pattern = r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$'
#         if not password:
#             errors['password'] = 'email field is required.'
#         elif not re.match(password_pattern , password):
#             errors['password'] = 'Invalid password format. It must contain at least 8 characters, including at least one lowercase letter, one uppercase letter, and one digit.'

#         name_pattern = r'^[A-Za-z\s]+$'
#         if not username:
#             errors['username'] = 'name field is required.'
#         elif not re.match(name_pattern,username):
#             errors['username'] = 'Invalid name'

#         contact_pattern = r'^98\d{8}$'
#         if not contact:
#             errors['contact'] = 'contact field is required.'
#         elif not re.match(contact_pattern,contact):
#             errors['contact'] = 'Invalid contact number format. It must start with "98" and have a length of 10 digits.'

#         address_pattern = r'^\d+\s+([A-Za-z]+\s?)+,\s*\w+,\s*\w+\s*\d*$'
#         if not address:
#             errors['address'] = 'address field is required.'
#         elif len(address) <5 :
#             errors['address'] = 'Address must contain 5 letter'

#         if errors:
#             return render(request,'accounts/customerregistration.html',{'errors':errors,'email':email,'password':password,'username':username,
#                                                                 'contact':contact,'address':address})
        
#         else:
#             Customer.objects.create(username = username, password = password ,email= email, 
#                             full_name = full_name, address = address, contact = contact )
#         return redirect(reverse_lazy('accounts:loginform'))
#     else:
#         return render(request, "accounts/customerregistration.html")


# def registerform(request):
#     if request.method=="POST":
#         form= UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             Customer.objects.create(user=user,username=user.username)
#             # messages.add_message(request, messages.SUCCESS, 'You are registered successfully')
#             return redirect('/accounts/loginform')
#         else:
#             # messages.add_message(request, messages.ERROR, 'Unable to register')
#             return render(request, 'accounts/customerregistration.html', {'form':form})
            
#     context={'form':UserCreationForm}
#     return render(request,'accounts/customerregistration.html', context)




def logoutuser(request):
    logout(request)
    return redirect('/accounts/login')



