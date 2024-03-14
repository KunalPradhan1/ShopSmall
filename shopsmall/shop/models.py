from django.db import models

# Create your models here.
class testTable(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200)
    password = models.CharField(max_length=64, unique=True)
    date_created = models.DateTimeField(auto_now_add = True)

    def _str_(self): 
        return self.firstName + self.lastName
    
    
    