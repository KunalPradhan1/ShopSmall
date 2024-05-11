from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.conf import settings
from django.contrib.auth import get_user_model



class User(AbstractUser): 
    is_business = models.BooleanField('Business', default = False)
    is_customer = models.BooleanField('Customer', default = False)
    phone_number = models.IntegerField(default = 0)
    location = models.CharField(max_length = 45, default = 'Not provided')
    reward_points = models.IntegerField(default=0)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/', default = 'images/Balkarandeep_Singh_-_String_project.jpg', null = True, blank = True)
    businessID = models.IntegerField(null = True, default = 0)
    inventory = models.IntegerField(default = 0)
    email = models.CharField(max_length = 45, default = 'Not provided')
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
    images = models.ImageField(null = True, blank = True, upload_to='images/', default = 'images/Balkarandeep_Singh_-_String_project.jpg')
    businessID = models.IntegerField(null = True, default = 0)


class Cart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='cart',
    )
    completed = models.BooleanField(default=False)
   

    def __str__(self):
        return f"{self.user.username}'s Cart - {'Completed' if self.completed else 'Active'}"



class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='items'
    )
    product = models.ForeignKey(
        'Product',  # Assuming the Product model is in the same app and named Product
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} (in {self.cart.user.username}'s Cart)"

class Orders(models.Model): 
    order = models.ForeignKey(
        Cart, 
        on_delete = models.CASCADE, 
        related_name = 'order_made'
    )
    order_placed = models.DateTimeField(default=timezone.now, null=True)  
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    completed = models.CharField(max_length = 100, default = "None")
    customerID = models.IntegerField(null = True, default = 0)
    businessName = models.CharField(max_length = 100, default = 'None')


