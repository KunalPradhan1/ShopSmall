from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, LoginForm
from .models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request, "shopComponents/home.html")

@login_required(login_url = "login")
def customerDashboard(request):
    return render(request, "shopComponents/dashboard.html")

def businessDashboard(request): 
    return render(request, "shopComponents/businessDashboard.html")


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