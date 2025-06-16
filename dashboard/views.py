from django.contrib import messages
from random import sample
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView,ListView,CreateView,UpdateView,DeleteView,DetailView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from django.db.models import Sum, Count, Avg
from django.utils import timezone
from datetime import timedelta
from django.db.models.functions import TruncDate



from . models import *
from . forms import *

from django.contrib import admin
# from .models import Sale

class DashboardRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and Admin.objects.filter(user=request.user).exists():
            pass
        else:
            messages.success(self.request,"You must login as admin to enter dashboard") 
            return redirect("/accounts/adminloginform/")
            
        return super().dispatch(request, *args, **kwargs)

class DashboardHomeView(DashboardRequiredMixin, TemplateView):
    template_name= "dashboard/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pendingorders"] = Order.objects.filter(
            order_status="Order Received").order_by("-id")
        return context
    
class DashboardOrderDetailView(DashboardRequiredMixin, DetailView):
    template_name="dashboard/adminorderdetail.html"
    model = Order
    context_object_name = "ord_obj"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["allstatus"] = ORDER_STATUS
        return context


class DashboardOrderListView(DashboardRequiredMixin, ListView):
    template_name = "dashboard/adminorderlist.html"
    queryset = Order.objects.all().order_by("-id")
    context_object_name = "allorders"


class DashboardOrderStatuChangeView(DashboardRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        order_id = self.kwargs["pk"]
        order_obj = Order.objects.get(id=order_id)
        new_status = request.POST.get("status")
        order_obj.order_status = new_status
        order_obj.save()
        return redirect(reverse_lazy("dashboard:adminorderdetail", kwargs={"pk": order_id}))
    
class DashboardOrderDeleteView(DashboardRequiredMixin, DeleteView):
    model = Order
    success_url = reverse_lazy('dashboard:adminorderlist')


def customer_order_report(request):
    ordered_by = Order.objects.filter(ordered_by=ordered_by)
    orders = Order.objects.filter(order_id=orders)
    return render(request, 'dashboard/report_template.html', {'ordered_by': ordered_by, 'orders': orders})

    




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

#Brand view
class BrandListView(LoginRequiredMixin, ListView):
    template_name = 'dashboard/brands/list.html'
    model = Brand

class BrandCreateView(LoginRequiredMixin, CreateView):
    template_name = 'dashboard/brands/form.html'
    form_class = BrandForm
    success_url = reverse_lazy('dashboard:brands-list')


class BrandUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'dashboard/brands/form.html'
    form_class = BrandForm
    model = Brand
    success_url = reverse_lazy('dashboard:brands-list')

class BrandDeleteView(LoginRequiredMixin, DeleteView):
    model = Brand
    success_url = reverse_lazy('dashboard:brands-list')

class BrandDetailView(LoginRequiredMixin, DetailView):
    template_name = 'dashboard/brands/form.html'
    model = Brand



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





# #Cart View
# class CartProductListView(LoginRequiredMixin, ListView):
#     template_name = 'dashboard/carts/list.html'
#     model = CartProduct

# class CartProductCreateView(LoginRequiredMixin, CreateView):
#     template_name = 'dashboard/carts/form.html'
#     form_class = CartForm
#     success_url = reverse_lazy('dashboard:carts-list')


# class CartProductUpdateView(LoginRequiredMixin, UpdateView):
#     template_name = 'dashboard/carts/form.html'
#     form_class = CartForm
#     model = CartProduct
#     success_url = reverse_lazy('dashboard:carts-list')
    

# class CartProductDeleteView(LoginRequiredMixin, DeleteView):
#     model = CartProduct
#     success_url = reverse_lazy('dashboard:carts-list')

# class CartProductDetailView(LoginRequiredMixin, DetailView):
#     template_name = 'dashboard/carts/form.html'
#     model = CartProduct

# def sales_history(request):
#     sales =Sale.objects.all().order_by('-date')
#     context = {
#         'sales': sales
#     }
#     return render(request, 'dashboard/sales/sales_history.html' , context)


class DashboardAnalyticsView(DashboardRequiredMixin, TemplateView):
    template_name = "dashboard/analytics.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["total_sales"] = Order.objects.aggregate(Sum('total'))['total__sum'] or 0
        context["total_orders"] = Order.objects.count()
        context["avg_order_value"] = Order.objects.aggregate(Avg('total'))['total__avg'] or 0
        context["total_customers"] = Customer.objects.count()

        context["top_products"] = (
            Product.objects.annotate(order_count=Count('cartproduct')).order_by('-order_count')[:5]
        )

        # Orders by date
        last_30_days = timezone.now() - timedelta(days=30)
        orders_by_date = (
            Order.objects.filter(created_at__gte=last_30_days)
            .annotate(date=TruncDate('created_at'))
            .values('date')
            .annotate(total=Sum('total'), count=Count('id'))
            .order_by('date')
        )
        context["orders_by_date"] = orders_by_date

        return context

