from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from .forms import SignUpForm, LoginForm
from .models import User, Product
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.
def home(request):
    return render(request, "shopComponents/home.html", {'user': request.user})

@login_required(login_url = "login")
def customerDashboard(request):
    if getattr(request.user, 'is_customer', False):
        print(request.user.is_customer)
        return render(request, "shopComponents/dashboard.html")
    else:
        return redirect("login")

@login_required(login_url = "login")
def businessDashboard(request): 
    if getattr(request.user, 'is_business', False):
        user_products = Product.objects.filter(businessID = request.user.id)
        context = {
        'title': 'product',
        'products': user_products
         }
        return render(request, "shopComponents/businessDashboard.html", context)
    else:
        return redirect("login")


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'shopComponents/register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_business:
                login(request, user)
                return redirect('bDashboard')
            elif user is not None and user.is_customer:
                login(request, user)
                return redirect('cDashboard')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'shopComponents/login.html', {'form': form, 'msg': msg})



def logout(request): 
    auth.logout(request)
    return redirect("home")
def business(request):
    return render(request, "shopComponents/business.html")

def cart(request):
    return render(request, "members/cart.html")

# def search(request):
#     search_term = request.GET.get('search', '')
#     search_form = request.GET.get('SearchForm', '')
#     return render(request, "members/search.html",{ 'search_term': search_term, 'search_form': search_form }) 


<<<<<<< HEAD
=======
@login_required(login_url = "login")
>>>>>>> 02344f0d570d25140ec91fd54d8f9fdf622a4558
def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        products = Product.objects.filter(name__startswith=searched)
        return render(request, "shopComponents/search.html", {'searched':searched, 'products':products})
    else:
        return render(request, "shopComponents/search.html")
    

@login_required(login_url = "login")
def createProduct(request):
    if request.method == 'POST':
        name1 = request.POST['name']
        price1 = request.POST['price']
        content1 = request.POST['content']
        inventory = request.POST['inventory']
        date = timezone.now()
        image = request.FILES.get('image')
        # print(request.user.businessName)
        product = Product(name = name1, price = price1, description = content1, inventory = inventory, last_updated = date, image = image, businessID = request.user.id)
        product.save()
        user_products = Product.objects.filter(businessID = request.user.id)
        context = {
        'title': 'product',
        'products': user_products
         }
        return render(request, "shopComponents/businessDashboard.html", context)


    
    return render(request, "shop/createproduct.html")



@login_required(login_url = "login")
def base(request):
    businessProducts = Product.objects.filter(businessID = request.user.id)
    prod = {
        'products': Product.objects.all()
    }
    return render(request, "shop/base.html", prod)


@login_required(login_url = "login")
def changeproduct(request):
    if request.method == 'POST':
        oldobj = request.POST['oldproduct']
        name1 = request.POST['name']
        price1 = request.POST['price']
        content1 = request.POST['content']
        inventory = request.POST['inventory']
        date = timezone.now()

        product = None
        try:
            product = Product.objects.get(name = oldobj, businessID = request.user.id)
        except Product.DoesNotExist:
            product = None
            raise Http404("No product matches the given query.")

        
        if product is not None:
            if name1 is not None:
                product.name = name1

            if price1 is not None:
                product.price = price1
            
            if content1 is not None:
                product.description = content1

            if inventory is not None:
                product.inventory = inventory
            
            product.last_updated = date
            product.save()

        user_products = Product.objects.filter(businessID = request.user.id)
        context = {
        'title': 'product',
        'products': user_products
         }
        return render(request, "shopComponents/businessDashboard.html", context)
    return render(request, "shop/product.html")
