from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#category models
class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    image = models.ImageField(upload_to= 'categories/',null=True)
    status = models.BooleanField(default=False, help_text="0_default, 1=Hidden")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ('id',)

    def __str__(self):
        return self.title 
    

#Brand Models
class Brand(models.Model):
    name = models.CharField(max_length=200)
    slug =models.SlugField()

    class Meta:
        verbose_name ="Brand"
        verbose_name_plural = "brands"
        ordering= ('id',)

    def __str__(self):
        return self.name


class SizeVariant(models.Model):
    size_name = models.CharField(max_length=255)

    def  __str__(self) -> str:
        return self.size_name


#Product models
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products' ,null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE,related_name='products' ,null=True)
    name = models.CharField(max_length=200)
    size_variant = models.ManyToManyField(SizeVariant,blank=True)
    image = models.ImageField(upload_to = 'products/')
    price = models.PositiveIntegerField()
    slug = models.SlugField( null=True)
    description = models.CharField(max_length=300)
    is_latest = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'products'
        ordering = ('id',)
    
    def __str__(self):
        return self.name
    
    
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products/")

    def __str__(self):
        return self.product.title
    
# class ProductSize(models.Model):
#     Size = models.ForeignKey(Size, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     count = models.IntegerField(default=1)
    
    
#Customer models
class Customer(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    username = models.CharField(null=True,max_length=200)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=200, null=True)
    # profile_pic= models.ImageField(upload_to='profile_pic/CustomerProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    contact = models.PositiveBigIntegerField(null=True)
    created_date = models.DateTimeField(auto_now_add=True,null=True)
    
    
    def __str__(self):
        return self.username
    



#Cart Models
class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,null=True,blank=True)
    total = models.PositiveIntegerField(default=0)
    # is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    # def get_cart_total(self):
    #     cart_products = self.cart_products.all()
    #     price = []
    #     for cart_product in cart_product:
    #         price.append(cart_product.product.price)
    #         if cart_product.sizes:
    #             sizes_price = cart_product.sizes.price
    #             price.append(sizes_price)

    #     return sum(price)
    def __str__(self):
        return "Cart: " + str(self.id)
    

class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rate = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    size_variant = models.ForeignKey(SizeVariant,on_delete=models.SET_NULL, null=True,blank=True)
    subtotal = models.PositiveIntegerField()

    def __str__(self):
        return "Cart: " + str(self.cart.id) + " CartProduct: " + str(self.id)

    # def get_product_price(self):
    #     price = [self.product.price]

    #     if self.sizes:
    #         sizes_price =self.sizes.price
    #         price.append(sizes_price)
        
    #     return sum(price)
        

ORDER_STATUS = (
    ("Order Received", "Order Received"),
    ("Order Processing", "Order Processing"),
    ("On the way", "On the way"),
    ("Order Completed", "Order Completed"),
    ("Order Canceled", "Order Canceled"),
)

METHOD = (
    ("Cash On Delivery", "Cash On Delivery"),
    ("Khalti", "Khalti"),
    ("Esewa", "Esewa"),
)


class Order(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    ordered_by = models.CharField(max_length=200)
    shipping_address = models.CharField(max_length=200)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(null=True, blank=True)
    subtotal = models.PositiveIntegerField()
    # discount = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    order_status = models.CharField(max_length=50, choices=ORDER_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(
        max_length=20, choices=METHOD, default="Cash On Delivery")
    payment_completed = models.BooleanField(
        default=False, null=True, blank=True)

    def __str__(self):
        return "Order: " + str(self.id)