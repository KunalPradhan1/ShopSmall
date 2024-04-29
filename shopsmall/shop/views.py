from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request, "shopComponents/home.html")

def dashboard(request):
    return render(request, "shopComponents/dashboard.html")

<<<<<<< Updated upstream
def navbar(request):
    return render(request, "shopComponents/navbar.html")
  
=======
def business(request):
    return render(request, "shopComponents/business.html")

def cart(request):
    return render(request, "members/cart.html")

def search(request):
    return render(request, "members/search.html")

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
>>>>>>> Stashed changes
