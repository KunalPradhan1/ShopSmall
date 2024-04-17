from django.shortcuts import render,HttpResponse
from .models import Product

products = [
    {
        'seller': 'Karan',
        'name': 'car',
        'price': '$100',
        'date_posted': 'April 4th',
        'content': "an vehicle"
    },
    {
        'seller': 'Ryan ',
        'name': 'water bottle',
        'price': '$10',
        'date_posted': 'April 5th',
        'content': "contians water"

    }

]

# Create your views here.
def home(request):
    return render(request, "shop/home.html")

# request

def product(request):
    context = {
        'title': 'product',
        'products': Product.objects.all()
    }
    return render(request, "shop/product.html", context)


def base(request):
    prod = {
        'products': products
    }
    return render(request, "shop/base.html", prod)
