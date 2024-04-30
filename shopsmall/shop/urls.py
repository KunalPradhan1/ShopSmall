from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("customer/dashboard/", views.customerDashboard, name ="cDashboard"), 
    path("login/", views.login_view, name = "login"), 
    path("register/", views.register, name = "register"),
    path("business/dashboard/", views.businessDashboard, name = "bDashboard"),
    path("logout/", views.logout, name = "logout")
]