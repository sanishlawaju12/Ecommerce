from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import CreateView, FormView
from .models import *
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth import login,logout,authenticate
from .forms import AdminLoginForm, User,CustomerLoginForm,CustomerRegistrationForm
from dashboard.models import Admin, Customer
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
import re


 
# Create your views here.

# class AdminLoginViews(FormView):
#     template_name = 'accounts/login.html'
#     form_class = AdminLoginForm
    

#     def form_valid(self, form):
#         login(self.request, form.instance)
#         return redirect(reverse_lazy('dashboard:home'))
    

# def AdminLoginViews(request):
#     msg = None
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)

#         if user is not None and user.is_staff:
#             login(request, user)
#             # Redirect to admin dashboard or wherever you want
#             msg = "admin logged in successfully"
#             return redirect('dashboard:home')
#         else:
#             # Display an error message
#             msg = "Invalid credential"
#             error_message = "Invalid credentials. Please try again."
#             return render(request, 'accounts/login.html', {'error_message': error_message})
#     else:
#         return render(request, 'accounts/login.html')
class AdminLoginViews(FormView):
    template_name = "accounts/login.html"
    form_class = CustomerLoginForm
    success_url = reverse_lazy("dashboard:home")

    def form_valid(self, form):
        uname = form.cleaned_data.get("username")
        pword = form.cleaned_data["password"]
        usr = authenticate(username=uname, password=pword)
        if usr is not None and Admin.objects.filter(user=usr).exists():
            login(self.request, usr)
        else:
            return render(self.request, self.template_name, {"form": self.form_class, "error": "Invalid credentials"})
        return super().form_valid(form)



class AdminLogoutViews(FormView):
    def get(self, request, *args, **kwargs):
        logout(self.request)
        return redirect(reverse_lazy('accounts:adminloginform'))


class CustomerRegistrationView(CreateView):
    template_name = "accounts/customerregistration.html"
    form_class = CustomerRegistrationForm
    success_url = reverse_lazy('home:home')

    def form_valid(self,form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")
        user = User.objects.create_user(username, email, password)
        form.instance.user = user
        login(self.request, user)
        return super().form_valid(form)

    def get_success_url(self):
        if "next" in self.request.GET:
            next_url = self.request.GET.get("next")
            return next_url
        else:
            return self.success_url




class CustomerLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("home:home")


class CustomerLoginView(FormView):
    template_name = "accounts/customerlogin.html"
    form_class = CustomerLoginForm
    success_url = reverse_lazy("home:home")

    # form_valid method is a type of post method and is available in createview formview and updateview
    def form_valid(self, form):
        uname = form.cleaned_data.get("username")
        pword = form.cleaned_data["password"]
        usr = authenticate(username=uname, password=pword)
        if usr is not None and Customer.objects.filter(user=usr).exists():
            login(self.request, usr)
        else:
            return render(self.request, self.template_name, {"form": self.form_class, "error": "Invalid credentials"})

        return super().form_valid(form)

    def get_success_url(self):
        if "next" in self.request.GET:
            next_url = self.request.GET.get("next")
            return next_url
        else:
            return self.success_url


# def logoutuser(request):
#     logout(request)
#     return redirect('/accounts/login')





