from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
<<<<<<< Updated upstream
    path("dashboard/", views.dashboard, name ="dashboard")
=======
    path("dashboard/", views.dashboard, name ="dashboard"), 
    path("login/", views.login_user, name = "login"),
    path("business/", views.business, name = "business"),
    path("cart/", views.cart, name = "cart"),
    path("search/", views.search, name = "search"),
>>>>>>> Stashed changes
]