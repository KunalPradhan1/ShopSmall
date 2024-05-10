from django.contrib import admin
from .models import User, Product, Cart, CartItem, Business, BusinessImage, Orders

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Business)
admin.site.register(BusinessImage)
admin.site.register(Orders)

