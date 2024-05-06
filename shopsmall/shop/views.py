from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request, "shopComponents/home.html", {'user': request.user})

def dashboard(request):
    return render(request, "shopComponents/dashboard.html")

<<<<<<< Updated upstream
=======
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
        form = SignUpForm(request.POST, label_suffix='')
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
    form = LoginForm(request.POST or None, label_suffix='')
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
>>>>>>> Stashed changes
def business(request):
    return render(request, "shopComponents/business.html")

def cart(request):
    return render(request, "members/cart.html")

<<<<<<< Updated upstream
#def search(request):
  #  search_term = request.GET.get('search', '')
  #  search_form = request.GET.get('SearchForm', '')
  #  return render(request, "members/search.html",{ 'search_term': search_term, 'search_form': search_form })

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



=======
# def search(request):
#     search_term = request.GET.get('search', '')
#     search_form = request.GET.get('SearchForm', '')
#     return render(request, "members/search.html",{ 'search_term': search_term, 'search_form': search_form }) 


@login_required(login_url = "login")
>>>>>>> Stashed changes
def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        products = Product.objects.filter(name__startswith=searched)
        return render(request, "shopComponents/search.html", {'searched':searched, 'products':products})
    else:
        return render(request, "shopComponents/search.html")

