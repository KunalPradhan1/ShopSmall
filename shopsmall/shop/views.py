from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . forms import CustomerRegistrationForm, CustomerLoginForm, BusinessLoginForm, BusinessRegistrationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request, "shopComponents/home.html")

@login_required(login_url = "login")
def customerDashboard(request):
    return render(request, "shopComponents/dashboard.html")

def businessDashboard(request): 
    return render(request, "shopComponents/businessDashboard.html")


def customerRegister(request): 
    form = CustomerRegistrationForm()
    if request.method == "POST":
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cLogin")
    context = {'customerRegister': form}
    return render(request, "shopComponents/register.html", context = context)

def customerLogin(request): 
    form = CustomerLoginForm()
    if request.method == "POST":
        form = CustomerLoginForm(request, data = request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            customer = authenticate(username = username, password = password)
            
            if customer is not None:
                request.session['customer_username'] = customer.username
                auth.login(request, customer)
                return redirect("cDashboard")
    context = {'customerLogin':form}
    return render(request, "shopComponents/login.html", context = context)


#Business Views
def businessRegister(request): 
    form = BusinessRegistrationForm()
    if request.method == "POST":
        form = BusinessRegistrationForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect("bLogin")
    context = {'businessRegister': form}
    return render(request, "shopComponents/businessRegister.html", context=context)


def businessLogin(request):
    form = BusinessLoginForm()
    if request.method == "POST":
        form = BusinessLoginForm(request, data=request.POST)
        if form.is_valid(): 
            email = request.POST.get('email')
            password = request.POST.get('password')
            business = authenticate(email=email, password=password)
            if business is not None: 
               # request.session['business_email'] = business.email
                auth.login(request,business)
                return redirect("bDashboard")
    context = {'businessLogin': form}
    return render(request, 'shopComponents/login.html', context=context)

def logout(request): 
    auth.logout(request)
    return redirect("home")