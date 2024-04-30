from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser): 
    is_business = models.BooleanField('Business', default = False)
    is_customer = models.BooleanField('Customer', default = False)
    phone_number = models.IntegerField(default = 0)
    location = models.CharField(max_length = 45, default = 'Not provided')
