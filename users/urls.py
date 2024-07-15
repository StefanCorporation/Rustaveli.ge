from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('registration/', views.UserRegistrationView.as_view(), name='registration')
]
