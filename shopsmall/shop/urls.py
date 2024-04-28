from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("customer/dashboard/", views.customerDashboard, name ="cDashboard"), 
    path("login/", views.userLogin, name = "login"), 
    path("customer/register/", views.customerRegister.as_view(), name = "cRegister"),
    path("business/register/", views.businessRegister.as_view(), name = "bRegister"),
    path("business/dashboard/", views.businessDashboard, name = "bDashboard"),
    path("logout/", views.logout, name = "logout")
]