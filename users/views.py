from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, UpdateView

from common.views import TitleMxin
from users.models import User

def profile(request):
    return render(request, 'profile\profile.html')


class UserProfileView(TitleMxin, UpdateView):
    template_name = 'profile\profile.html'
    model = User
    title = 'profile'

class UserLoginView(TitleMxin, LoginView):
    template_name = 'login.html'

class UserRegistrationView(TitleMxin, LoginView):
    template_name = 'registration.html'
    model = User

