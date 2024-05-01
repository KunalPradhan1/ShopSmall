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
    

    
    
