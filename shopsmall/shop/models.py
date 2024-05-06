from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


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
    def __str__(self):
        return self.name

# class Business(models.Model):
#     businessName = models.CharField(max_length = 100)
#     introduction = models.TextField()
#     address = 
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')

    def __str__(self):
        return self.user

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
