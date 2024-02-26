from django.db import models

# Create your models here.
class testTable(models.Model):
    userName = models.CharField(max_length=20)
    password = models.CharField(max_length=64, unique=True)



    