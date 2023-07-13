from random import sample
from django.views.generic import TemplateView,ListView,CreateView,UpdateView,DeleteView,DetailView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from . models import *
from . forms import *


class DashboardHomeView(LoginRequiredMixin, TemplateView):
    template_name= "dashboard/index.html"

#Category view
class CategoryListView(LoginRequiredMixin, ListView):
    template_name = 'dashboard/categories/list.html'
    model = Category

class CategoryCreateView(LoginRequiredMixin, CreateView):
    template_name = 'dashboard/categories/form.html'
    form_class = CategoryForm
    success_url = reverse_lazy('dashboard:categories-list')


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'dashboard/categories/form.html'
    form_class = CategoryForm
    model = Category
    success_url = reverse_lazy('dashboard:categories-list')

class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('dashboard:categories-list')

class CategoryDetailView(LoginRequiredMixin, DetailView):
    template_name = 'dashboard/categories/form.html'
    model = Category

#Product view
class ProductListView(LoginRequiredMixin, ListView):
    template_name = 'dashboard/products/list.html'
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    template_name = 'dashboard/products/form.html'
    form_class = ProductForm
    success_url = reverse_lazy('dashboard:products-list')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'dashboard/products/form.html'
    form_class = ProductForm
    model = Product
    success_url = reverse_lazy('dashboard:products-list')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('dashboard:products-list')


class ProductDetailView(LoginRequiredMixin, DetailView):
    template_name = 'dashboard/products/form.html'
    model = Product

#Customer View
class CustomerListView(LoginRequiredMixin, ListView):
    template_name = 'dashboard/customers/list.html'
    model = Customer




class CustomerCreateView(LoginRequiredMixin, CreateView):
    template_name = 'dashboard/customers/form.html'
    form_class = CustomerForm
    success_url = reverse_lazy('dashboard:customers-list')

class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'dashboard/customers/form.html'
    form_class = CustomerForm
    model = Customer
    success_url = reverse_lazy('dashboard:customers-list')

class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    model = Customer
    success_url = reverse_lazy('dashboard:customers-list')

class CustomerDetailView(LoginRequiredMixin, DetailView):
    template_name = 'dashboard/customers/form.html'
    model = Customer

#Order view
class OrderListView(LoginRequiredMixin, ListView):
    template_name = 'dashboard/orders/list.html'
    model = Order

class OrderCreateView(LoginRequiredMixin, CreateView):
    template_name = 'dashboard/orders/form.html'
    form_class = OrderForm
    success_url = reverse_lazy('dashboard:orders-list')


class OrderUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'dashboard/orders/form.html'
    form_class = OrderForm
    model = Order
    success_url = reverse_lazy('dashboard:orders-list')

class OrderDeleteView(LoginRequiredMixin, DeleteView):
    model = Order
    success_url = reverse_lazy('dashboard:orders-list')

class OrderDetailView(LoginRequiredMixin, DetailView):
    template_name = 'dashboard/orders/form.html'
    model = Order



#Cart View
class CartProductListView(LoginRequiredMixin, ListView):
    template_name = 'dashboard/carts/list.html'
    model = CartProduct

class CartProductCreateView(LoginRequiredMixin, CreateView):
    template_name = 'dashboard/carts/form.html'
    form_class = CartForm
    success_url = reverse_lazy('dashboard:carts-list')


class CartProductUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'dashboard/carts/form.html'
    form_class = CartForm
    model = CartProduct
    success_url = reverse_lazy('dashboard:carts-list')

class CartProductDeleteView(LoginRequiredMixin, DeleteView):
    model = CartProduct
    success_url = reverse_lazy('dashboard:carts-list')

class CartProductDetailView(LoginRequiredMixin, DetailView):
    template_name = 'dashboard/carts/form.html'
    model = CartProduct