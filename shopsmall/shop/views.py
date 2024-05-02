from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request, "shopComponents/home.html", {'user': request.user})

def dashboard(request):
    return render(request, "shopComponents/dashboard.html")

def business(request):
    return render(request, "shopComponents/business.html")

def cart(request):
    return render(request, "members/cart.html")

def search(request):
    search_term = request.GET.get('search', '')
    search_form = request.GET.get('SearchForm', '')
    return render(request, "members/search.html",{ 'search_term': search_term, 'search_form': search_form })

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
<<<<<<< Updated upstream
=======


def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        products = Product.objects.filter(name__startswith=searched)
        return render(request, "shopComponents/search.html", {'searched':searched, 'products':products})
    else:
        return render(request, "shopComponents/search.html")
>>>>>>> Stashed changes
