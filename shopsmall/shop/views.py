from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, LoginForm
from .models import User, Product
from django.contrib.auth.decorators import login_required

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
        return render(request, "shopComponents/businessDashboard.html")
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

def login_user(request): 
    if request.method == "POST": 
        pass 
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('shopComponenets/home.html')

        else:
            messages.success(request, ("Incorrect Username or Password"))
            return render(request, 'shopComponents/home.html')
    else: 
        return render(request, 'members/login.html')


def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        products = Product.objects.filter(name__startswith=searched)
        return render(request, "shopComponents/search.html", {'searched':searched, 'products':products})
    else:
        return render(request, "shopComponents/search.html")
        return render(request, "members/search.html")
    


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
        context = {
        'title': 'product',
        'products': Product.objects.all()
         }
        return render(request, "shop/product.html", context)


    
    return render(request, "shop/createproduct.html")
