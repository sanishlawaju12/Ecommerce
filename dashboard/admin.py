from django.contrib import admin
from .models import Admin, Product,Order,Customer,Category,Cart,CartProduct,SizeVariant,Brand
# Register your models here.
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(CartProduct)
admin.site.register(Brand)
admin.site.register(Admin)
# admin.site.register(Sale)


@admin.register(SizeVariant)
class SizeVariantAdmin(admin.ModelAdmin):
    list_display =['size_name']
    model = SizeVariant