from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from .forms import SignUpForm, LoginForm
from .models import User, Product, Business, BusinessImage
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




def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        products = Product.objects.filter(name__startswith=searched)
        return render(request, "shopComponents/search.html", {'searched':searched, 'products':products})
    else:
        return render(request, "shopComponents/search.html")
    
@login_required(login_url = "login")
def businessProfileEdit(request):
    if not getattr(request.user, 'is_business', False):
        return redirect("login")

    if request.method == 'POST':
        businessName = request.POST.get('name')
        address = request.POST.get('address')
        about = request.POST.get('content')
        profile, created = Business.objects.update_or_create(
            user = request.user,
            defaults={
                'businessName': businessName,
                'address': address,
                'about': about, 
                'businessID': request.user.id
            }
        )
        BusinessImage.objects.filter(business_profile=profile).delete()
        for images in request.FILES.getlist('images'):
            BusinessImage.objects.create(
                business_profile = profile, 
                images = images,
                businessID = request.user.id
            )
        business_images = BusinessImage.objects.filter(business_profile=profile)
        context = {
            'images': business_images, 
            'profile': profile

        }
        return render(request, "shopComponents/businessProfile.html", context)
    return render(request, 'shopComponents/businessProfileEdit.html' )
       
@login_required(login_url = "login")
def businessProfile(request): 
    if getattr(request.user, 'is_business', False):
        try:
            profile = request.user.business_profile
            business_images = profile.images.all()
            context = {
                'images': business_images, 
                'profile': profile
            }
            return render(request, "shopComponents/businessProfile.html", context)
        except Business.DoesNotExist:
            return render(request, "shopComponents/register.html")  
    else:
        return redirect("login")


@login_required(login_url = "login")
def createProduct(request):
    if not getattr(request.user, 'is_business', False):
        return redirect("login")

    if request.method == 'POST':
        name1 = request.POST['name']
        price1 = request.POST['price']
        content1 = request.POST['content']
        inventory = request.POST['inventory']
        date = timezone.now()
        image = request.FILES.get('image')
        product = Product(name = name1, price = price1, description = content1, inventory = inventory, last_updated = date, image = image, businessID = request.user.id)
        product.save()
        user_products = Product.objects.filter(businessID = request.user.id)
        context = {
        'title': 'product',
        'products': user_products
        }
        return render(request, "shopComponents/businessDashboard.html", context)
    return render(request, "shop/createproduct.html")
