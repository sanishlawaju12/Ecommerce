# from django.db import models
# from django.contrib.auth.models import AbstractUser, BaseUserManager

# # Create your models here.
# class User(AbstractUser):
#     class Role(models.TextChoices):
#         ADMIN = "ADMIN","Admin"
#         CUSTOMER = "CUSTOMER","Custom"

#     role = models.CharField(max_length=50,choices=Role.choices,default=Role.ADMIN)


# class CustomerManager(BaseUserManager):
#     def create_user(self,email,password=None,**extra_fields):
#         extra_fields.setdefault("role", User.Role.CUSTOMER)
#         extra_fields.setdefault("is_staff", False)
#         extra_fields.setdefault("is_superuser", False)

#         if not email:
#             raise ValueError("The Email field must be set")

#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def get_queryset(self, *args, **kwargs):
#         results = super().get_queryset(*args, **kwargs)
#         return results.filter(role=User.Role.CUSTOMER)


# class Customer(User):
#     base_role = User.Role.CUSTOMER
#     objects = CustomerManager()

#     class Meta:
#         proxy = True

#     def welcome(self):
#         return "only for customers"


# class CustomerProfile(models.Model):
#     user = models.OneToOneField(
#         User, on_delete=models.CASCADE, related_name="customer_profile", null=True
#     )
#     cus_email = models.CharField(max_length=50, blank=True, null=True)
#     cus_pwd = models.CharField(max_length=255, blank=True, null=True)
#     cus_name = models.CharField(max_length=50, blank=True, null=True)
#     cus_contact = models.PositiveBigIntegerField(blank=True, null=True)
#     reg_date = models.DateField(null=True, blank=True)
#     is_active = models.BooleanField(default=True)
#     admin_id = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE,
#         related_name="admin_customer_profiles",
#         blank=False,
#     )

#     class Meta:
#         verbose_name = "Customer"
#         verbose_name_plural = "Customers"
#         ordering = ("id",)

#     def __str__(self):
#         return self.cus_name 