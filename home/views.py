import re
from django.shortcuts import render,redirect
from django.template import RequestContext
from django.views.generic import TemplateView,CreateView,DetailView,View,FormView,UpdateView
from accounts import admin
from  dashboard.forms import *
from django.urls import reverse_lazy, reverse
from dashboard.models import Product, Customer,Category,Cart,CartProduct,SizeVariant,Order
from .forms import CheckoutForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.models import Group
from django.contrib import messages
from django.core.mail import send_mail
from django.http import JsonResponse
from django.conf import settings
from django.db.models import Q
from .models import *
from .forms import *
import requests
from requests import request
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.
def index(request):
    return render(request,"base.html")

def home(request):
    return render(request,"home/home.html")

class IndexView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context["is_latest"] = Product.objects.filter(is_latest=True)
       context["mens"] = Product.objects.filter(category__slug='mens')
       context["womens"] = Product.objects.filter(category__slug='womens')
       context["menjackets"] = Product.objects.filter(category__slug='menjackets')
       context["menpants"] = Product.objects.filter(category__slug='menpants')
       context["mentshirts"] = Product.objects.filter(category__slug='mentshirts')
       context["womenjackets"] = Product.objects.filter(category__slug='womenjackets')
       context["womenpants"] = Product.objects.filter(category__slug='womenpants')
       context["womentshirts"] = Product.objects.filter(category__slug='womentshirts')
       context["allProduct"]= Product.objects.all()
       context["categories"]=Category.objects.all()
       return context

def aboutus(request):
    return render(request, 'aboutus.html')

def contactus(request):
    return render(request, 'contactus.html')

def productDetails(request,pk):
    products = Product.objects.get(id=pk)
    context = {'products' : products}
    if request.GET.get('size'):
        size = request.GET.get('size')
        context['selected_size'] = size
        print(size)
    return render(request,'home/productDetails.html',context)





class AllProductView(TemplateView):
    template_name = "home/allproduct.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all()
        return context
    


def categoryView(request,pk):
    category = Category.objects.get(id = pk)
    products = Product.objects.filter(category=category)
    context ={
        "category":category,
        "products": products,
    }
    return render(request,'home/categories.html',context)

class CategoryView(TemplateView):
    template_name= 'home/categories.html'


class ProductCreateView(CreateView):
    template_name = 'dashboard/products/form.html'
    form_class = ProductForm
    success_url = reverse_lazy('dashboard:products-create')

class CustomerCreateView(CreateView):
    template_name = 'dashboard/customers/form.html'
    form_class = CustomerForm
    success_url=reverse_lazy('dashboard:customers-create')

class OrderCreateView(CreateView):
    template_name = 'dashboard/orders/form.html'
    form_class = OrderForm
    success_url=reverse_lazy('home:home')





# class CustomerRegistrationView(CreateView):
#     template_name = "home/customers/customerregistration.html"
#     form_class = CustomerRegistrationForm
#     success_url = reverse_lazy ("home:home")

#     def form_valid(self,form):
#         username= form.cleaned_data.get("username")
#         email = form.cleaned_data.get("email")
#         password=form.cleaned_data.get("password")
#         address =form.cleaned_data.get("address")
#         contact = form.cleaned_data.get("contact")
#         user = User.objects.create_user(username,email,password)
#         form.instance.user=user




#         login(self.request,user)
#         return super().form_valid(form)
    
#     def get_success_url(self):
#         if "next" in self.request.GET:
#             next_url = self.request.GET.get("next")
#             return next_url
#         else:
#             return self.success_url

    # def CustomerRegistration(request):
    #     n=''
    #     if request.method == "POST":
    #         username = request.POST.get('username') 
    #         password = request.POST.get('password')
    #         email = request.POST.get('email')
    #         address = request.POST.get('address')
    #         contact = request.POST.get('contact')
    #         admin_id = request.POST.get('admin_id')
            

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

    #         if not admin_id:
    #                 errors['admin_id'] = 'Select  the Admin '


    #         if errors:
    #             return render(request,'home/customers:customerregistration.html',{'errors':errors,'email':email,'password':password,'username':username,
    #                                                             'contact':contact,'address':address,'admin_id':admin_id})
        
    #         else:
    #             Customer.objects.create(username = username, password = password ,email= email, 
    #                         address = address, contact = contact, admin_id = admin)
    #         return redirect(reverse_lazy('home/customers:customerlogin'))
    #     else:
    #         return render(request, "home/customers:customerregistration",
    #                       {
    #                 'admins':User.objects.all(),
    #               }
    #               )
        

    
        
class CustomerProfileView(TemplateView):
    template_name = "home/customers/customerprofile.html"

    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated and Customer.objects.filter(user=request.user).exists():
            pass
        else:
            return redirect("login/?next/profile/")
        return super().dispatch(request, *args,**kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = self.request.user.customer
        context['customer'] = customer
        return context


# @login_required(login_url='home:customerlogin')
# # any one can add product to cart, no need of signin
# def add_to_cart_view(request,pk):
#     products=models.Product.objects.all()
    

#     #for cart counter, fetching products ids added by customer from cookies
#     if 'product_ids' in request.COOKIES:
#         product_ids = request.COOKIES['product_ids']
#         counter=product_ids.split('|')
#         product_count_in_cart=len(set(counter))
#     else:
#         product_count_in_cart=1

#     response = render(request, 'home/carts/addtocart.html',{'products':products,'product_count_in_cart':product_count_in_cart})

#     #adding product id to cookies
#     if 'product_ids' in request.COOKIES:
#         product_ids = request.COOKIES['product_ids']
        
#         if product_ids=="":
#             product_ids=str(pk)
#         else:
#             product_ids=product_ids+"|"+str(pk)
#         response.set_cookie('product_ids', product_ids)
#     else:
#         response.set_cookie('product_ids', pk)

#     # product=models.Product.objects.get(id=pk)
#     # messages.info(request, product.name + ' added to cart successfully!')

#     return response



# # for checkout of cart
# def cart_view(request):
#     #for cart counter
#     if 'product_ids' in request.COOKIES:
#         product_ids = request.COOKIES['product_ids']
#         counter=product_ids.split('|')
#         product_count_in_cart=len(set(counter))
#     else:
#         product_count_in_cart=0

#     # fetching product details from db whose id is present in cookie
#     products=None
#     total=0
#     if 'product_ids' in request.COOKIES:
#         product_ids = request.COOKIES['product_ids']
#         if product_ids != "":
#             product_id_in_cart=product_ids.split('|')
#             products=models.Product.objects.all().filter(id__in = product_id_in_cart)
            

#             #for total price shown in cart
#             for p in products:
#                 total=total+p.price
#     return render(request,'home/carts/mycart.html',{'products':products,'total':total,'product_count_in_cart':product_count_in_cart})


# def remove_from_cart_view(request,pk):
#     #for counter in cart
#     if 'product_ids' in request.COOKIES:
#         product_ids = request.COOKIES['product_ids']
#         counter=product_ids.split('|')
#         product_count_in_cart=len(set(counter))
#     else:
#         product_count_in_cart=0

#     # removing product id from cookie
#     total=0
#     if 'product_ids' in request.COOKIES:
#         product_ids = request.COOKIES['product_ids']
#         product_id_in_cart=product_ids.split('|')
#         product_id_in_cart=list(set(product_id_in_cart))
#         product_id_in_cart.remove(str(pk))
#         products=models.Product.objects.all().filter(id__in = product_id_in_cart)
#         #for total price shown in cart after removing product
#         for p in products:
#             total=total+p.price

#         #  for update coookie value after removing product id in cart
#         value=""
#         for i in range(len(product_id_in_cart)):
#             if i==0:
#                 value=value+product_id_in_cart[0]
#             else:
#                 value=value+"|"+product_id_in_cart[i]
#         response = render(request, 'home/carts/mycart.html',{'products':products,'total':total,'product_count_in_cart':product_count_in_cart})
#         if value=="":
#             response.delete_cookie('product_ids')
#         response.set_cookie('product_ids',value)
#         return response


class EcomMixin(object):
    
    def dispatch(self, request, *args, **kwargs):
        cart_id = request.session.get("cart_id")
        if cart_id:
            cart_obj = Cart.objects.get(id=cart_id)
            if request.user.is_authenticated and request.user.customer:
                cart_obj.customer = request.user.customer
                cart_obj.save()
        return super().dispatch(request, *args, **kwargs)  



class AddToCartView(LoginRequiredMixin,EcomMixin, TemplateView):
    login_url = 'accounts:customerlogin'
    REDIRECT_FIELD_NAME = 'home'
    template_name = "home/carts/addtocart.html"
    
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        # get product id from requested url
        product_id = self.kwargs['pro_id']
        # get selected size variant from query parameter
        # size_variant_id = self.request.GET.get('size_variant_id')
       
        # get product and size variant
        product_obj = Product.objects.get(id=product_id)
        # size_variant_obj = SizeVariant.objects.get(id=size_variant_id)

        



        # check if cart exists
        cart_id = self.request.session.get("cart_id", None)
        if cart_id:
            cart_obj = Cart.objects.get(id=cart_id)
            this_product_in_cart = cart_obj.cartproduct_set.filter(
                product=product_obj)

            # item already exists in cart
            if this_product_in_cart.exists():
                cartproduct = this_product_in_cart.last()
                cartproduct.quantity += 1
                cartproduct.subtotal += product_obj.price
                cartproduct.save()
                cart_obj.total += product_obj.price
                cart_obj.save()
                messages.success(self.request,"product added to cart")  
            # new item is added in cart
            else:
                cartproduct = CartProduct.objects.create(
                    cart=cart_obj, product=product_obj, rate=product_obj.price, quantity=1,  subtotal=product_obj.price)
                cart_obj.total += product_obj.price
                cart_obj.save()  
                messages.success(self.request,"product added to cart")        

        else:
            cart_obj = Cart.objects.create(total=0)
            self.request.session['cart_id'] = cart_obj.id
            cartproduct = CartProduct.objects.create(
                cart=cart_obj, product=product_obj, rate=product_obj.price, quantity=1, subtotal=product_obj.price)
            cart_obj.total += product_obj.price
            cart_obj.save()
            

        return context


class ManageCartView(EcomMixin, View):
    def get(self, request, *args, **kwargs):
        cp_id = self.kwargs["cp_id"]
        action = request.GET.get("action")
        cp_obj = CartProduct.objects.get(id=cp_id)
        cart_obj = cp_obj.cart

        if action == "inc":
            cp_obj.quantity += 1
            cp_obj.subtotal += cp_obj.rate
            cp_obj.save()
            cart_obj.total += cp_obj.rate
            cart_obj.save()
        elif action == "dcr":
            cp_obj.quantity -= 1
            cp_obj.subtotal -= cp_obj.rate
            cp_obj.save()
            cart_obj.total -= cp_obj.rate
            cart_obj.save()
            if cp_obj.quantity == 0:
                cp_obj.delete()

        elif action == "rmv":
            cart_obj.total -= cp_obj.subtotal
            cart_obj.save()
            cp_obj.delete()
        else:
            pass
        return redirect("home:mycart")


class EmptyCartView(EcomMixin, View):
    def get(self, request, *args, **kwargs):
        cart_id = request.session.get("cart_id", None)
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
            cart.cartproduct_set.all().delete()
            cart.total = 0
            cart.save()
        return redirect("home:mycart")


class MyCartView(EcomMixin, TemplateView):
    template_name = "home/carts/mycart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get("cart_id", None)
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
        else:
            cart = None
        context['cart'] = cart
        return context
    

class CheckoutView(EcomMixin,CreateView):
    template_name = "home/checkout.html"
    form_class = CheckoutForm
    success_url = reverse_lazy("home:home")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.customer:
            pass
        else:
            return redirect("/login/?next=/checkout/")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get("cart_id", None)
        if cart_id:
            cart_obj = Cart.objects.get(id=cart_id)
        else:
            cart_obj = None
        context['cart'] = cart_obj
        return context

    def form_valid(self, form):
        cart_id = self.request.session.get("cart_id")
        if cart_id:
            cart_obj = Cart.objects.get(id=cart_id)
            form.instance.cart = cart_obj
            form.instance.subtotal = cart_obj.total
            form.instance.discount = 0
            form.instance.total = cart_obj.total
            form.instance.order_status = "Order Received"
            del self.request.session['cart_id']
            pm = form.cleaned_data.get("payment_method")
            order = form.save()
            if pm == "Khalti":
                return redirect(reverse("home:khaltirequest")+ "?o_id=" + str(order.id))
            elif pm == "Esewa":
                return redirect(reverse("home:esewarequest")+ "?o_id=" + str(order.id))
        else:
            return redirect("home:home")
        return super().form_valid(form)
    
class CustomerProfileView(TemplateView):
    template_name = "home/customers/customerprofile.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and Customer.objects.filter(user=request.user).exists():
            pass
        else:
            return redirect("/accounts/login/?next=/profile/")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = self.request.user.customer
        context['customer'] = customer
        orders = Order.objects.filter(cart__customer=customer).order_by("-id")
        context["orders"] = orders
        return context

class MyOrderDetailView(TemplateView):
    template_name = "home/orders/myorder.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and Customer.objects.filter(user=request.user).exists():
            pass
        else:
            return redirect("/login/?next=/profile/")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = self.request.user.customer
        context['customer'] = customer
        orders = Order.objects.filter(cart__customer=customer).order_by("-id")
        context["orders"] = orders
        return context


class CustomerOrderDetailView(DetailView):
    template_name = "home/orders/customerorderdetail.html"
    model = Order
    context_object_name = "ord_obj"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and Customer.objects.filter(user=request.user).exists():
            order_id = self.kwargs["pk"]
            order = Order.objects.get(id=order_id)
            if request.user.customer != order.cart.customer:
                return redirect("home:customerprofile")
        else:
            return redirect("/login/?next=/profile/")
        return super().dispatch(request, *args, **kwargs)
    

class EsewaRequestView(View):
    def get(self, request, *args, **kwargs):
        o_id = request.GET.get("o_id")
        order = Order.objects.get(id=o_id)
        context={
            "order": order
        }

        return render(request,"home/payments/esewarequest.html",context)

class EsewaVerifyView(View):
    def get(self, request, *args, **kwargs):
        import xml.etree.ElementTree as ET
        oid = request.GET.get("oid")
        amt = request.GET.get("amt")
        refId = request.GET.get("refId")

        url = "https://uat.esewa.com.np/epay/transrec"
        d = {
            'amt': amt,
            'scd': 'epay_payment',
            'rid': refId,
            'pid': oid,
        }
        resp = requests.post(url, d)
        root = ET.fromstring(resp.content)
        status = root[0].text.strip()
        order_id = oid.split("_")[1]
        order_obj = Order.objects.get(id=order_id)
        if status == "Success":
            order_obj.payment_completed = True
            order_obj.save()
            return redirect("/")
        else:

            return redirect("/esewa-request/?o_id="+order_id)
        

class KhaltiRequestView(View):
    def get(self, request, *args, **kwargs):
        o_id = request.GET.get("o_id")
        order = Order.objects.get(id=o_id)
        context = {
            "order": order
        }
        return render(request, "home/payments/khaltirequest.html", context)


class KhaltiVerifyView(View):
    def get(self, request, *args, **kwargs):
        token = request.GET.get("token")
        amount = request.GET.get("amount")
        o_id = request.GET.get("order_id")
        print(token, amount, o_id)

        url = "https://khalti.com/api/v2/payment/verify/"
        payload = {
            "token": token,
            "amount": amount
        }
        headers = {
            "Authorization": "Key test_secret_key_f59e8b7d18b4499ca40f68195a846e9b"
        }

        order_obj = Order.objects.get(id=o_id)

        response = requests.post(url, payload, headers=headers)
        resp_dict = response.json()
        if resp_dict.get("idx"):
            success = True
            order_obj.payment_completed = True
            order_obj.save()
        else:
            success = False
        data = {
            "success": success
        }
        return JsonResponse(data)
        



def collections(request):
    category = Category.objects.filter()
    context = {'category' : category }
    return render(request, "home/collections.html",context)

def collectionsviews(request,slug):
    if(Category.objects.filter(slug=slug, status=0)):
        products = Product.objects.filter(category__slug=slug)
        category_name = Category.objects.filter(slug=slug).first()
        context ={'products': products, 'category_name': category_name}
        return render(request, "home/collections/collection.html", context)
    else:
        messages.warning(request, "No such category found")
        return redirect('collections')

    
    
