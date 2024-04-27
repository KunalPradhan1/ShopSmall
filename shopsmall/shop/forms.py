from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from shop.models import Customer, Business
from django import forms
from django.forms.widgets import PasswordInput, TextInput


class CustomerRegistrationForm(UserCreationForm): 
    class Meta: 
        model = Customer
        fields = ('username', 'email', 'password', 'location')

class CustomerLoginForm(AuthenticationForm): 
    class Meta:
        model = Customer
        fields = ('username', 'password')

class BusinessRegistrationForm(UserCreationForm): 
    class Meta:
        model = Business
        fields = ('email', 'business_name', 'password')

class BusinessLoginForm(AuthenticationForm): 
    class Meta: 
        model = Business 
        fields = ('email', 'password')
