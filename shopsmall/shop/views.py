from django.shortcuts import render,HttpResponse
from .models import Product

#Dummy Data 
# products = [
#     {
#         'seller': 'Karan',
#         'name': 'car',
#         'price': '$100',
#         'date_posted': 'April 4th',
#         'content': "an vehicle"
#     },
#     {
#         'seller': 'Ryan ',
#         'name': 'water bottle',
#         'price': '$10',
#         'date_posted': 'April 5th',
#         'content': "contians water"

#     }

# ]

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
        'products': Product.objects.all()
    }
    return render(request, "shop/base.html", prod)

def createProduct(request):
   
    if request.method == 'POST':
        seller1 = request.POST['seller']
        name1 = request.POST['name']
        price1 = request.POST['price']
        content1 = request.POST['content']
    
    product = Product(name = name1, price = price1, content = content1, businessID = 2, productID = 1, seller = seller1)
    product.save()
    
    return render(request, "shop/createproduct.html")