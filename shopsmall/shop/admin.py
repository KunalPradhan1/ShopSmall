from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Customer, Business


class CustomerAdmin(UserAdmin):
    model = Customer
    list_display = ['email', 'username', 'location', 'is_active']

class BusinessAdmin(UserAdmin):
    model = Business
    list_display = ['email', 'username', 'business_name', 'location', 'is_active']


# Register your models here.
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Business, CustomerAdmin)
admin.site.register()
