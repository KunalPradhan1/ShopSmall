from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("customer/dashboard/", views.customerDashboard, name ="cDashboard"), 
    path("customer/login/", views.customerLogin, name = "cLogin"), 
    path("customer/register/", views.customerRegister, name = "cRegister"),
    path("business/register/", views.businessRegister, name = "bRegister"),
    path("business/login/", views.businessLogin, name = "bLogin"),
    path("business/dashboard/", views.businessDashboard, name = "bDashboard"),
    path("logout/", views.logout, name = "logout")
]