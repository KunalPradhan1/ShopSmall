from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from .forms import SignUpForm, LoginForm
from .models import User, Product
from .models import User, Product, Business, BusinessImage, Cart, CartItem, Orders
from django.contrib.auth.decorators import login_required
from django.http import Http404, JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from django.db import transaction




# Create your views here.
def home(request):
    return render(request, "shopComponents/home.html", {'user': request.user})

@login_required(login_url = "login")
def customerDashboard(request):
    if getattr(request.user, 'is_customer', False):
        print(request.user.is_customer)
        return render(request, "shopComponents/customerDash.html")
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
                profile = Business.objects.filter(businessID = request.user.id)
                if profile.exists():
                    return redirect('bDashboard')
                else: 
                    return redirect('bProfileEdit')
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

# def cart(request):
#     return render(request, "members/cart.html")

# def search(request):
#     search_term = request.GET.get('search', '')
#     search_form = request.GET.get('SearchForm', '')
#     return render(request, "members/search.html",{ 'search_term': search_term, 'search_form': search_form }) 


@login_required(login_url = "login")
def view_profile(request):
    if not getattr(request.user, 'is_customer', False):
        return redirect("login")

    business_id = request.GET.get('business_id')
    findBusiness = get_object_or_404(Business, businessID = business_id)
    findImage = BusinessImage.objects.filter(business_profile = findBusiness)
    if(findImage.exists()):
        print("exists")
    context = {
        'business': findBusiness, 
        'images': findImage
    }
    return render(request, 'customer/viewProfile.html',context)

@login_required(login_url = "login")
def view_products(request):
    if not getattr(request.user, 'is_customer', False):
        return redirect("login")

    business_id = request.GET.get('business_id')
    findProducts = Product.objects.filter(businessID = business_id)
    if(findProducts.exists()):
        print("exists")
    context = {
        'products': findProducts, 
    }
    return render(request, 'customer/viewProducts.html',context)
    

@login_required(login_url = "login")
def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        products = Product.objects.filter(name__startswith=searched)
        business = Business.objects.filter(businessName__startswith=searched)
        search_type = request.POST.get('search_type')
        if search_type is None:
            search_type = "Both"
        return render(request, "shopComponents/search.html", {'searched':searched, 'products':products, 'business':business, 'search_type':search_type})
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
            return render(request, "shopComponents/businessProfileEdit.html")  
    else:
        return redirect("login")


@login_required(login_url = "login")
def createProduct(request):
    if request.method == 'POST':
        name1 = request.POST['name']
        price1 = request.POST['price']
        content1 = request.POST['content']
        inventory = request.POST['inventory']
        date = timezone.now()
        image = request.FILES.get('image')
        findBusiness = Business.objects.filter(businessID = request.user.id)
        for business in findBusiness: 
            busName = business.businessName
        product = Product(name = name1, price = price1, description = content1, inventory = inventory, last_updated = date, image = image, businessID = request.user.id, businessName = busName)
        product.save()
        user_products = Product.objects.filter(businessID = request.user.id)
        context = {
        'title': 'product',
        'products': user_products
         }
        return render(request, "shopComponents/businessDashboard.html", context)


    
    return render(request, "shop/createproduct.html")




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
            if name1 != '':
                product.name = name1

            if price1 != '':
                product.price = price1
            
            if content1 != '':
                product.description = content1

            if inventory != '':
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


@login_required(login_url = "login")
def delete(request):
    if request.method == 'POST':
        oldobj = request.POST['oldproduct']

        product = None
        try:
            product = Product.objects.get(name = oldobj, businessID = request.user.id)
        except Product.DoesNotExist:
            product = None
            raise Http404("No product matches the given query.")

        

        product.delete()

        user_products = Product.objects.filter(businessID = request.user.id)
        context = {
        'title': 'product',
        'products': user_products 
         }
        return render(request, "shopComponents/businessDashboard.html", context)
    return render(request, "shop/deleteproduct.html")


login_required(login_url="login")   
def orderSubmit(request):
    if getattr(request.user, 'is_customer', False):
        cart = get_object_or_404(Cart, user=request.user, completed = False)  # Assuming you need to match cart ID to order_id
        cart_items = CartItem.objects.filter(cart=cart)
        if cart_items.exists(): 
            total = sum(item.product.price * item.quantity for item in cart_items)
            context = {'cost': total}  # Define context outside to ensure availability
            try:
                with transaction.atomic():
                    customerOrder, created = Orders.objects.get_or_create(
                        order=cart, 
                        defaults={'cost': total, 'completed': False, 'customerID': request.user.id}
                    )
                    
                    if created or not customerOrder.order_placed:
                        customerOrder.order_placed = timezone.now()
                        customerOrder.save()

                    cart.completed = True; 
                    cart.save()
                    context['order'] = customerOrder 
                    context['items'] = cart_items
                    
                return render(request, "shopComponents/orderPlaced.html", context=context)
            except Exception as e:
                print(f"Failed to save order: {e}")
                return HttpResponse("Failed to process your order.", status=500)
        else: 
            return HttpResponse("No items in the cart to create an order.", status=400)
    else: 
        return render(request, "shopComponents/login.html")


@login_required(login_url = "login")
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))

    cart, created = Cart.objects.get_or_create(user=request.user, completed=False)

    if not created:
        # If the cart exists and is not completed, use it
        print("Using existing active cart:", cart)
    else:
       
        print("New cart created:", cart)
    
    
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    print("Cart item retrieved or created:", cart_item)

    if not created:
        cart_item.quantity += quantity
    else:
        cart_item.quantity = quantity

    cart_item.save()
    print("Cart item saved")
    
    products = Product.objects.filter(name__startswith=product.name)
    return render(request, "shopComponents/search.html", {'addedCart': product.name, 'products':products})


def cart(request):
    user = request.user
    if user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False) 
        items = cart.items.all()  # Assuming the related_name for CartItem is 'items'
        total = sum(item.product.price * item.quantity for item in items)  # Calculate total price
        return render(request, 'shopComponents/cart.html', {'cart': cart, 'items': items, 'total': total})
    else:
        # Redirect or handle unauthenticated users
        return render(request, 'shopComponents/login.html')



    
