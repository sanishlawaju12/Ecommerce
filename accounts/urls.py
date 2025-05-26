from django.urls import path,include
from . import views 
from .views import *
from django.contrib.auth.views import LoginView, LogoutView





app_name = 'accounts'

urlpatterns = [
   # path('adminclick', views.adminLoginView),
   # path('adminlogin', LoginView.as_view(template_name='account/adminlogin.html'),name='adminlogin'),
   # path('afterlogin', views.afterlogin_view,name='afterlogin'),
   # path('logout', LogoutView.as_view(template_name='ecom/logout.html'),name='logout'),
   # path('logout', views.customerSignUpView(), name = 'logout')


   path("register/",
         CustomerRegistrationView.as_view(), name="customerregistration"),

    path("logout/", CustomerLogoutView.as_view(), name="customerlogout"),
    path("login/", CustomerLoginView.as_view(), name="customerlogin"), 


   # path('login',views.AdminLoginViews.as_view(),name='login'),
   path('adminlogout',views.AdminLogoutViews.as_view(),name='adminlogout'),


   # path("registerform/",views.registerform, name="registerform"),
   # path("loginform/",views.loginform, name="loginform"),
   path("adminloginform/",AdminLoginViews.as_view(), name="adminloginform"),
   # path('logout/', views.logoutuser),



]