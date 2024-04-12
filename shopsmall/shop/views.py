from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, "shopComponents/home.html")

def dashboard(request):
    return render(request, "shopComponents/dashboard.html")

def register_user(request): 
    if request.method == "POST": 
        username = request.POST['username']
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        email = request.POST['email']
        password = request.POST['password']
        rePassword = request.POST['rePassword']
        myuser = User.objects.create_user(username, email, password)
        myuser.firstName = firstName
        myuser.lastName = lastName 
        myuser.save()
        messages.success(request, "Your account has been successfully created!")
        return redirect('home')
    return render(request, "members/register.html")
    

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