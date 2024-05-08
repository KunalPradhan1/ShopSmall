from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.conf import settings


class User(AbstractUser): 
    is_business = models.BooleanField('Business', default = False)
    is_customer = models.BooleanField('Customer', default = False)
    phone_number = models.IntegerField(default = 0)
    location = models.CharField(max_length = 45, default = 'Not provided')

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/', default = 'images\Balkarandeep_Singh_-_String_project.jpg', null = True, blank = True)
    businessID = models.IntegerField(null = True, default = 0)
    inventory = models.IntegerField(default = 0)
    last_updated = models.DateTimeField(default=timezone.now, null=True)    
    businessName = models.CharField(max_length = 100, default = 'None')
    def __str__(self):
        return self.name

class Business(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE, 
        primary_key = True, 
        related_name = 'business_profile', 
        default = 'Something'
    )
    businessName = models.CharField(max_length = 100)
    about = models.TextField()
    address = models.CharField(max_length = 50)
    businessID = models.IntegerField(null = True, default = 0)

class BusinessImage(models.Model):
    business_profile = models.ForeignKey(Business, related_name='images', on_delete=models.CASCADE)
    images = models.ImageField(null = True, blank = True, upload_to='images/', default = 'images\Balkarandeep_Singh_-_String_project.jpg')
    businessID = models.IntegerField(null = True, default = 0)


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')

    def __str__(self):
        return self.user

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
