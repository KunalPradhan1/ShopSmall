from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("product/", views.product, name = "product"),
    path('base/', views.base, name = "base"),
    path('createproduct/', views.createProduct, name = "createProduct")
]