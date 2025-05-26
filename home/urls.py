from django.contrib import admin
from django.urls import path,include
from home import views
from .views import *
from django.contrib.auth.views import LoginView,LogoutView

app_name = 'home'

urlpatterns =[
    path('/', views.index, name="base"),

    path('', views.IndexView.as_view(), name="home"),

    path('aboutus/', views.aboutus, name="aboutus"),

    path('contactus/', views.contactus, name="contactus"),

    path('allproduct', AllProductView.as_view(), name="allproduct"),

    # path('category/<str:pk>', views.CategoryView.as_view(), name='category'),

    path('create', views.ProductCreateView.as_view(), name='products-create'),

    path('product/<str:pk>',views.productDetails, name='productDetails'),

    path('create', views.CustomerCreateView.as_view(), name='customers-create'),

    path('create',views.OrderCreateView.as_view(), name='orders-create'),

    # path('register/', CustomerRegistrationView.as_view(),name="customerregistration"),

    # path("logout/",CustomerLogoutView.as_view(),name="customerlogout"),

    # path("customerlogin/",CustomerLoginView.as_view(),name="customerlogin"),

    path("profile/",CustomerProfileView.as_view(),name="customerprofile"),
    path("profile/order-<int:pk>/", CustomerOrderDetailView.as_view(),
         name="customerorderdetail"),



    path("myorder/",MyOrderDetailView.as_view(),name="myorder"),

    #cart
    # path("add-to-cart-<int:product_id>/",views.cart_add, name="addtocart"),
    path("add-to-cart-<int:pro_id>/", AddToCartView.as_view(), name="add-to-cart"),
    path("my-cart/", MyCartView.as_view(), name="mycart"),
    path("manage-cart/<int:cp_id>/", ManageCartView.as_view(), name="managecart"),
    path("empty-cart/", EmptyCartView.as_view(), name="emptycart"),

    path("checkout/", CheckoutView.as_view(), name="checkout"),

    

#    path('accounts/', include('accounts.urls', namespace='accounts')),


    #category--collection
    path('collections',views.collections,name="collections"),
    path('collections/<str:slug>',views.collectionsviews, name='collectionsview'),


    #payments   
    path("khalti-request/", KhaltiRequestView.as_view(), name="khaltirequest"),
    path("khalti-verify/", KhaltiVerifyView.as_view(), name="khaltiverify"),
    path("esewa-request/", EsewaRequestView.as_view(), name="esewarequest"),
    path("esewa-verify/", EsewaVerifyView.as_view(), name="esewaverify"),
   

]