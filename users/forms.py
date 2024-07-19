from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, UserCreationForm

from phonenumber_field.formfields import PhoneNumberField

from users.models import User


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'type':'text'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'Email', 'type':'text'}))
    phone = PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': 'Phone', 'type':'text'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password', 'type':'password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Submit Password', 'type':'password'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'phone', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder':'Enter your email',
        'type':'text'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Enter your password',
        'type':'password'
    }))

    class Meta:
        model = User
        fields = ('email', 'username')



