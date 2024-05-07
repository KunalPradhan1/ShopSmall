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
<<<<<<< HEAD
    path("business/profileEdit/", views.businessProfileEdit, name = "bProfileEdit"), 
    path("business/profile/", views.businessProfile, name = "bProfile"), 
    # path("view_profile/<int:business_id>/", views.view_profile, name=view_profile)
=======
    path("changeproduct/", views.changeproduct, name = "change"), 


>>>>>>> 02344f0d570d25140ec91fd54d8f9fdf622a4558
]