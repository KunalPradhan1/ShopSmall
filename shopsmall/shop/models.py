from django.db import models

# Create your models here.
class testTable(models.Model):
    userName = models.CharField(max_length=20)
    password = models.CharField(max_length=64, unique=True)

class Product(models.Model):
    name = models.CharField("Product Name", max_length = 120)
    creationDate = models.DateTimeField('Creation Date', blank = True)
    businessID = models.IntegerField("Seller")
    productID = models.IntegerField("Product ID")


    def __str__(self):
        return self.name
    
class Customers(models.Model):
        name = models.CharField('Customer Name', max_length = 100)
        customerID = models.IntegerField('customer id')
        email = models.EmailField('Email Address')
        product = models.ForeignKey(Product, blank = True, null = True, on_delete= models.CASCADE)

                
        def __str__(self):
                return self.name
    
class Bussiness(models.Model):
    first_name = models.CharField(max_length = 120)
    last_name = models.CharField(max_length = 120)
    email = models.EmailField('business email')
    products = models.ManyToManyField(Product, blank = True)

    def __str__(self):
         return self.email
    

        