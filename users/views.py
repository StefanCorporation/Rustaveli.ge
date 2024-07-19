from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin

from common.views import TitleMxin
from .models import User
from .forms import UserRegistrationForm, UserLoginForm



class UserProfileView(TitleMxin, UpdateView):
    template_name = 'profile.html'
    model = User
    title = 'Profile'


class UserLoginView(TitleMxin, LoginView):
    template_name = 'login_registration.html'
    model = User
    form_class = UserLoginForm
    title = 'Login'


class UserRegistrationView(TitleMxin, SuccessMessageMixin, CreateView):
    form_class = UserRegistrationForm
    template_name = 'login_registration.html'
    title = 'Registration'
    success_message = 'Congratulations! You have registered!'
