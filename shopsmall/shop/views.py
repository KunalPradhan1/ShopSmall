from django.shortcuts import render,HttpResponse

products = [
    {
        'seller': 'Karan',
        'name': 'car',
        'Price': '$100',
        'date_posted': 'April 4th'
    },
    {
        'seller': 'Ryan ',
        'name': 'water bottle',
        'Price': '$10',
        'date_posted': 'April 5th'
    }

]

# Create your views here.
def home(request):
    return render(request, "shop/home.html")

# request

def about(request):
    context = {
        'products': products
    }
    return render(request, "shop/product.html", context)
