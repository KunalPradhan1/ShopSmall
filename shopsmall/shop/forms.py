from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    username = forms.CharField(
        label = "",
        widget= forms.TextInput(
            attrs={
<<<<<<< Updated upstream
                "class": "form-control my-custom-class"
=======
                "class": "form-control username-input",
                "placeholder": "Username",
                "style": "height: 50px;"
>>>>>>> Stashed changes
            }
        ) 
    )
    password = forms.CharField(
        label = "",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control password-input",
                "placeholder": "Password",
                "style": "margin-top: 15px; height: 50px;"
            }
        )
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label = "",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "style": "height: 50px;",
                "placeholder": "Username"
            }
        )
    )
    password1 = forms.CharField(
        label = "",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "style": "margin-top: 15px; height: 50px;",
                "placeholder": "Password"
                
            }
        )
    )
    password2 = forms.CharField(
        label = "",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "style": "margin-top: 15px; height: 50px;",
                "placeholder": "Re-enter Password"
            }
        )
    )
    email = forms.CharField(
        label = "",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "style": "margin-top: 15px; height: 50px;",
                "placeholder": "Email"
            }
        )
    )

    is_business = forms.BooleanField(
    label = "Business",
    widget=forms.CheckboxInput(
        attrs={
             "style": "transform: scale(1.25);",
             
            # Add more attributes here...
        }
    ),
    required=False,  # Set to False if you want to make this field optional
)
    
    is_customer = forms.BooleanField(
    label = "Customer",
    widget=forms.CheckboxInput(
        attrs={
             "style": "transform: scale(1.25);",
            # Add more attributes here...
        }
    ),
    required=False,  # Set to False if you want to make this field optional
)
    
    phone_number = forms.IntegerField(
    widget=forms.NumberInput(
        attrs={
            "class": "form-control",
            "placeholder": "1231234567"
            # Add more attributes here...

        }
    ),
    required=True,  # Set to False if you want to make this field optional
)

    location = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control" 
                ,
                "placeholder": "123 Main St, San Jose, CA, 95116"
            }
        )
    )
    

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_business', 'is_customer', 'phone_number', 'location')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists.")
        return email