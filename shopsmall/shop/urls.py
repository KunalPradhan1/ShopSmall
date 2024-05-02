from django.urls import path
from . import views


urlpatterns = [
    
    path("", views.home, name="home"),
    path("product/", views.product, name = "product"),
    path('base/', views.base, name = "base"),
    path('createproduct/', views.createProduct, name = "createProduct"),
    path("", views.home, name="home"),
    path("customer/dashboard/", views.customerDashboard, name ="cDashboard"), 
    path("login", views.login_view, name = "login"), 
    path("register/", views.register, name = "register"),
    path("business/dashboard/", views.businessDashboard, name = "bDashboard"),
    path("logout/", views.logout, name = "logout"),
    path("business/", views.business, name = "business"),
    path("cart/", views.cart, name = "cart"),
    path("search/", views.search, name = "search")
]