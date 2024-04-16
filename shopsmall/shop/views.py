from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . forms import CreateUserForm, LoginForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request, "shopComponents/home.html")

@login_required(login_url = "login")
def dashboard(request):
    return render(request, "shopComponents/dashboard.html")

def register(request): 
    form = CreateUserForm() 
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    # if request.method == "POST": 
    #     username = request.POST['username']
    #     firstName = request.POST['firstName']
    #     lastName = request.POST['lastName']
    #     email = request.POST['email']
    #     password = request.POST['password']
    #     rePassword = request.POST['rePassword']
    #     myuser = User.objects.create_user(username, email, password)
    #     myuser.firstName = firstName
    #     myuser.lastName = lastName 
    #     myuser.save()
    #     messages.success(request, "Your account has been successfully created!")
    #     return redirect('login')
    context = {'registerform': form}
    return render(request, "shopComponents/register.html", context=context )
    

def login(request): 
    form = LoginForm()
    if request.method == "POST": 
        form = LoginForm(request, data=request.POST)
        if form.is_valid(): 
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password = password)
            if user is not None: 
                auth.login(request,user)
                return redirect("dashboard")

    context = {'loginform':form}
    return render(request, 'shopComponents/login.html', context=context)

def logout(request): 
    auth.logout(request)
    return redirect("home")