from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class testTable(models.Model):
    userName = models.CharField(max_length=20)
    password = models.CharField(max_length=64, unique=True)

class Customers(models.Model):
        name = models.CharField('Customer Name', max_length = 100)
        customerID = models.IntegerField('customer id')
        email = models.EmailField('Email Address')
        # product = models.ForeignKey(Product, blank = True, null = True, on_delete= models.CASCADE)

                
        def __str__(self):
                return self.name
    
class Bussiness(models.Model):
    first_name = models.CharField(max_length = 120)
    last_name = models.CharField(max_length = 120)
    email = models.EmailField('business email')
    # products = models.ManyToManyField(Product, blank = True)

    def __str__(self):
         return self.email

class Product(models.Model):
    name = models.CharField("Product Name", max_length = 120)
    content = models.TextField("Content", default= 'None')
    date_posted = models.DateTimeField('Creation Date', auto_now_add = True)
    seller = models.CharField("Seller Name", max_length = 120, default = "ShopSmall")
    price = models.CharField("Price", max_length = 120, default= "$0")    
    sellerB = models.ForeignKey(Bussiness, on_delete = models.CASCADE, null = True, blank = False)
    businessID = models.IntegerField("Seller")
    productID = models.IntegerField("Product ID")
    productImage = models.ImageField(null = True, blank = True, upload_to="images/")

    def __str__(self):
        return self.name
    
    
# note str has two '_'then str then agian two
        