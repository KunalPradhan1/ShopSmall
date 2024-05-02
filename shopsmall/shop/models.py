from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser): 
    is_business = models.BooleanField('Business', default = False)
    is_customer = models.BooleanField('Customer', default = False)
    phone_number = models.IntegerField(default = 0)
    location = models.CharField(max_length = 45, default = 'Not provided')
# Create your models here.
class testTable(models.Model):
    firstName = models.CharField(max_length=200, default='SOME STRING')
    lastName = models.CharField(max_length=200, default='SOME STRING')
    email = models.CharField(max_length=200, default='SOME STRING')
    password = models.CharField(max_length=64, unique=True, default='SOME STRING')
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.firstName + self.lastName
    

    
    


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='static/images/', default = "/static/images/Lightning_McQueen.png")

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')

    def __str__(self):
        return self.user

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
