from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from .forms import CustomerRegistrationForm, BusinessRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.views.generic import CreateView
from .models import User

from . forms import CustomerRegistrationForm, BusinessRegistrationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request, "shopComponents/home.html")

@login_required(login_url = "login")
def customerDashboard(request):
    return render(request, "shopComponents/dashboard.html")

def businessDashboard(request): 
    return render(request, "shopComponents/businessDashboard.html")


class customerRegister(CreateView):
    model = User 
    form_class = CustomerRegistrationForm
    template_name = "shopComponents/register.html"

    def form_valid(self, form): 
        user = form.save()
        login(self.request, user)
        return redirect('dashboard')


class businessRegister(CreateView):
    model = User
    form_class = BusinessRegistrationForm
    template_name = 'shopComponents/businessRegister.html'

    def form_valid(self, form): 
        user = form.save()
        login(self.request, user)
        return redirect(businessDashboard)


def userLogin(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'shopComponents/login.html', context={'form':AuthenticationForm()})


def logout(request): 
    auth.logout(request)
    return redirect("home")