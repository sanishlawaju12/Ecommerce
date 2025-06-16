from django.urls import path, include
from.import views
from dashboard.views import DashboardOrderDeleteView, DashboardOrderDetailView, DashboardOrderListView, DashboardOrderStatuChangeView

app_name= 'dashboard'

urlpatterns =[
    # Admin Side pages
    path('',views.DashboardHomeView.as_view(),name = 'home'),


    

    # path("admin-home/", AdminHomeView.as_view(), name="adminhome"),
    path("admin-order/<int:pk>/", DashboardOrderDetailView.as_view(),
         name="adminorderdetail"),

    path("admin-all-orders/", DashboardOrderListView.as_view(), name="adminorderlist"),

    path("admin-order-<int:pk>-change/",
         DashboardOrderStatuChangeView.as_view(), name="adminorderstatuschange"),
         
     path("admin-order/<int:pk>/delete", DashboardOrderDeleteView.as_view(), name="adminorderdelete"),

    
    #Category
    path('categories',views.CategoryListView.as_view(),name = 'categories-list'),
    path('categories/create',views.CategoryCreateView.as_view(),name = 'categories-create'),
    path('categories/<int:pk>/update',views.CategoryUpdateView.as_view(), name = 'categories-update'),
    path('categories/<int:pk>/delete/',views.CategoryDeleteView.as_view(), name = 'categories-delete'), 
    path('categories/<int:pk>/detail/',views.CategoryDetailView.as_view(), name = 'categories-detail'),

    #Brand
    path('brands',views.BrandListView.as_view(),name = 'brands-list'),
    path('brands/create',views.BrandCreateView.as_view(),name = 'brands-create'),
    path('brands/<int:pk>/update',views.BrandUpdateView.as_view(), name = 'brands-update'),
    path('brands/<int:pk>/delete/',views.BrandDeleteView.as_view(), name = 'brands-delete'), 
    path('brands/<int:pk>/detail/',views.BrandDetailView.as_view(), name = 'brands-detail'),

    #Product
    path('products',views.ProductListView.as_view(),name = 'products-list'),
    path('products/create',views.ProductCreateView.as_view(),name = 'products-create'),
    path('products/<int:pk>/update',views.ProductUpdateView.as_view(), name = 'products-update'),
    path('products/<int:pk>/delete/',views.ProductDeleteView.as_view(), name = 'products-delete'), 
    path('products/<int:pk>/detail/',views.ProductDetailView.as_view(), name = 'products-detail'),

    #Customer 
    path('customers',views.CustomerListView.as_view(), name = 'customers-list'),
    path('customers/create',views.CustomerCreateView.as_view(),name = 'customers-create'),
    path('customers/<int:pk>/update',views.CustomerUpdateView.as_view(), name = 'customers-update'),
    path('customers/<int:pk>/delete/',views.CustomerDeleteView.as_view(), name = 'customers-delete'), 
    path('customers/<int:pk>/detail/',views.CustomerDetailView.as_view(), name = 'customers-detail'),
    
    #Order
    path('orders',views.OrderListView.as_view(), name = 'orders-list'),
    path('orders/create',views.OrderCreateView.as_view(),name = 'orders-create'),
    path('orders/<int:pk>/update',views.OrderUpdateView.as_view(), name = 'orders-update'),
    path('orders/<int:pk>/delete/',views.OrderDeleteView.as_view(), name = 'orders-delete'), 
    path('orders/<int:pk>/detail/',views.OrderDetailView.as_view(), name = 'orders-detail'),

    path('admin-order-<int:pk>-ordered_by/order_report/', views.customer_order_report, name='customer-order-report'),

    path('analytics/', views.DashboardAnalyticsView.as_view(), name='analytics'),


#     #Cart
#     path('carts',views.CartProductListView.as_view(), name = 'carts-list'),
#     path('carts/create',views.CartProductCreateView.as_view(),name = 'carts-create'),
#     path('carts/<int:pk>/update',views.CartProductUpdateView.as_view(), name = 'carts-update'),
#     path('carts/<int:pk>/delete/',views.CartProductDeleteView.as_view(), name = 'carts-delete'), 
#     path('carts/<int:pk>/detail/',views.CartProductDetailView.as_view(), name = 'carts-detail'),

    # #Sales
    # path('sales/history/', views.sales_history, name='sales_history'),

]