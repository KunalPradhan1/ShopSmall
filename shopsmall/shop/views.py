from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from .forms import SignUpForm, LoginForm
from .models import User, Product
from .models import User, Product, Business, BusinessImage, Cart, CartItem, Orders, Review
from django.contrib.auth.decorators import login_required
from django.http import Http404, JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from django.db import transaction
from django.core.mail import EmailMultiAlternatives, send_mail
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from decimal import Decimal
from django.views.decorators.csrf import csrf_exempt





# Create your views here.
def home(request):
    return render(request, "shopComponents/home.html", {'user': request.user})

@login_required(login_url = "login")
def customerDashboard(request):
    if getattr(request.user, 'is_customer', False):
        customer_orders = Orders.objects.filter(customerID = request.user.id)
        context = {
            'title': 'Orders', 
            'orders': customer_orders
        }
        return render(request, "shopComponents/customerDash.html", context = context)
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
    business_profile = get_object_or_404(Business, businessID=business_id)
    findImage = BusinessImage.objects.filter(business_profile=business_profile)
    if(findImage.exists()):
        print("exists")
    context = {
        'images': findImage, 
        'profile':business_profile
    }
    return render(request, 'shopComponents/businessProfile.html',context)

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
        for image in business: 
            print(image.firstImage)
        search_type = request.POST.get('search_type')
        if search_type is None:
            search_type = "Both"
        return render(request, "shopComponents/search.html", {'searched':searched, 'products':products, 'business':business, 'search_type':search_type,})
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
            business = Business.objects.filter(user = request.user)
            business.firstImage = business_images.first().images
            print(vars(business))
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
        email = request.user.email; 
        print(email)
        date = timezone.now()
        image = request.FILES.get('image')
        findBusiness = Business.objects.filter(businessID = request.user.id)
        for business in findBusiness: 
            busName = business.businessName
        product = Product(name = name1, price = price1, description = content1, inventory = inventory, last_updated = date, image = image, businessID = request.user.id, businessName = busName, email = email)
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
        for items in cart_items: 
            print(items.cart.user.email)
            businessName = items.product.businessName
        if cart_items.exists(): 
            total = sum(item.product.price * item.quantity for item in cart_items)
            context = {'cost': total}  # Define context outside to ensure availability
            use_rewards = request.POST.get('rewards') == 'on'
            if use_rewards:
                # Subtract reward_points * 0.1 from the total
                total -= request.user.reward_points 
                # Reset reward_points to 0
                request.user.reward_points = 0
            else:
                # Update reward points
                request.user.reward_points += int(total )

            #request.user.reward_points += int(total * Decimal('0.1'))
            request.user.save()
            try:
                with transaction.atomic():
                    customerOrder, created = Orders.objects.get_or_create(
                        order=cart, 
                        defaults={'cost': total, 'completed': "In Progress", 'customerID': request.user.id, 'businessName': businessName}
                    )
                    
                    if created or not customerOrder.order_placed:
                        customerOrder.order_placed = timezone.now()
                        customerOrder.save()
                        # email sent to customer
                        welcome_message = "Thank you so much for shopping at ShopSmall today " + str(request.user.first_name) + " " + str(request.user.last_name) +  " and choosing to give your business to small businesses! Hundreds of thousands of small businesses all over the country close down due to competition and the struggles of maintaining a business and your business is truly beneficial to everyone! The total for your order is: $" + str(total) + ". You can view your orders within your customer dashboard. Thank you again for your business you will be contacted when your orders are ready. "
                                            
                        subject = "ShopSmall Order Has Been Placed!"
                        email = request.user.email

                        context = {
                            'welcome_message': welcome_message
                        }
                        html_message = render_to_string("shopComponents/email.html", context = context)
                        plain_message = strip_tags(html_message)
                        message = EmailMultiAlternatives(
                            subject = subject, 
                            body = plain_message,
                            from_email = "shopsmallbiz12@gmail.com", 
                            to = [request.user.email]
                        )
                        message.attach_alternative(html_message, "text/html")
                        message.send()

                        business_message = "You have an order! Customer: " + str(request.user.first_name) + " " + str(request.user.last_name) + ". Phone number: " + str(request.user.phone_number) + ". Contact customer when order is placed. Information about order showed in your Business Dashboard"
                        subject = "You Have an Order!"
                        context = {
                            welcome_message: business_message
                        }
                        html_message = render_to_string("shopComponents/email.html", context = context)
                        plain_message = strip_tags(html_message)
                        for items in cart_items: 
                            print(items.product.email)
                            message = EmailMultiAlternatives(
                            subject = subject, 
                            body = plain_message,
                            from_email = "shopsmallbiz12@gmail.com", 
                            to = [items.product.email]
                            )  
                            message.attach_alternative(html_message, "text/html")
                            message.send()

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




def remove_from_cart(request, item_id):
    item = CartItem.objects.get(id=item_id, cart__user=request.user)
    item.delete()
    return redirect('cart')
    

@login_required(login_url='login')   
def write_review(request):
    if not getattr(request.user, 'is_customer', False):
        return HttpResponse("Only customer accounts can access this page.", status=403)
    if request.method == 'POST':
        business_id = request.POST.get('business')
        print("Business ID from form:", business_id)
        review_text = request.POST.get('review')
        review_submitted = True

        if not business_id:
            return HttpResponse("Business ID is required.", status=400)

        # Get the business object based on the selected ID
        business = Business.objects.get(pk=business_id)
        
        # Create a new review object and save it to the database
        Review.objects.create(
            business=business,
            customer=request.user,  # Assuming user is logged in
            review_text=review_text
        )
        
        # Retrieve businesses for rendering the form again
        businesses = Business.objects.all()
        
        # Redirect to a success page or any other page
        return render(request, 'customer/review.html', {'businesses': businesses, 'review_submitted': review_submitted})
    else:
        # Handle GET request to render the form
        businesses = Business.objects.all()
        return render(request, 'customer/review.html', {'businesses': businesses})

