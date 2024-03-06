from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request, "shopComponents/home.html")

def dashboard(request):
    return render(request, "shopComponents/dashboard.html")

def navbar(request):
    return render(request, "shopComponents/navbar.html")
  