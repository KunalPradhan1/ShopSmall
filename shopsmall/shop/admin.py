from django.contrib import admin
from .models import testTable
from .models import Product
from .models import Bussiness
from .models import Customers

# Register your models here.
admin.site.register(testTable)
admin.site.register(Product)
admin.site.register(Bussiness)
admin.site.register(Customers)
