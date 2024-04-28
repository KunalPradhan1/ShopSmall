from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Customer, Business
from django.db import transaction
from django import forms
from django.forms.widgets import PasswordInput, TextInput

class CustomerRegistrationForm(UserCreationForm): 
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    phone_number = forms.CharField(required = True)
    email = forms.EmailField(required=True)
    location = forms.CharField(required = True)
    username = forms.CharField(max_length=150, required=True)

    class Meta(UserCreationForm.Meta): 
        model = User

    @transaction.atomic
    def save(self): 
        user = super().save(commit = False)
        user.is_customer = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        customer = Customer.objects.create(user = user)
        customer.email = self.cleaned_data.get('email')
        customer.phone_number = self.cleaned_data.get('phone_number')
        customer.location = self.cleaned_data.get('location')
        customer.save()
        return user

    
class BusinessRegistrationForm(UserCreationForm): 
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    phone_number = forms.CharField(required = True)
    email = forms.EmailField(required=True)
    businessName = forms.CharField(max_length = 50, required = True)
    location = forms.CharField(required = True)
    username = forms.CharField(max_length=150, required=True)

    class Meta(UserCreationForm.Meta): 
        model = User
    
    @transaction.atomic
    def save(self): 
        user = super().save(commit = False)
        user.is_customer = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        business = Business.objects.create(user = user)
        business.email = self.cleaned_data.get('email')
        business.phone_number = self.cleaned_data.get('phone_number')
        business.location = self.cleaned_data.get('location')
        business.businessName = self.cleaned_data.get('businessName')
        business.save()
        return user