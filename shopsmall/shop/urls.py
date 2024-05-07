from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("customer/dashboard/", views.customerDashboard, name ="cDashboard"), 
    path("login/", views.login_view, name = "login"), 
    path("register/", views.register, name = "register"),
    path("business/dashboard/", views.businessDashboard, name = "bDashboard"),
    path("logout/", views.logout, name = "logout"),
    path("business/", views.business, name = "business"),
    path("cart/", views.cart, name = "cart"),
    path("search/", views.search, name = "search"),
    path("productAdd/", views.createProduct, name = "add"),
    path("business/profileEdit/", views.businessProfileEdit, name = "bProfileEdit"), 
    path("business/profile/", views.businessProfile, name = "bProfile"), 
    path("business-profile", views.view_profile, name= "business-profile"), 
    path("business-products", views.view_products, name = "business-products")
]