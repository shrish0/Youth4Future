
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.core.exceptions import ValidationError

class SignupForm(UserCreationForm):
    disability_choices = [
        ('blind', 'Blind'),
        ('handicapped', 'Handicapped'),
        ('mute', 'Mute'),
        ('deaf', 'Deaf'),
    ]
    
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter User-Name"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter Email"}))
    phone = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Phone"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Enter Password"}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control", "placeholder": "Confirm Password"
            }
        )
    )
    disability = forms.ChoiceField(choices=disability_choices, 
                                    widget=forms.RadioSelect(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ('username', 'disability', 'email', 'phone', 'password1', 'password2')

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not (phone.isdigit() or len(phone) == 10):
            raise ValidationError("Please enter a valid 10-digit phone number.")
        return phone

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError("User name already exists.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists.")
        return email

class LoginForm(forms.Form):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


