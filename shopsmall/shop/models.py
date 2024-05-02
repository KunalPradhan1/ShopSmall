from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    name = models.CharField("Product Name", max_length = 120)
    content = models.TextField("Content", default= 'None')
    date_posted = models.DateTimeField('Creation Date', auto_now_add = True)
    seller = models.CharField("Seller Name", max_length = 120, default = "ShopSmall")
    price = models.CharField("Price", max_length = 120, default= "$0")    
    # sellerB = models.ForeignKey(on_delete = models.CASCADE, null = True, blank = False)
    businessID = models.IntegerField("Seller")
    productID = models.IntegerField("Product ID")
    productImage = models.ImageField(null = True, blank = True, upload_to="images/")

    def __str__(self):
        return self.name
    
    
# note str has two '_'then str then agian two
        