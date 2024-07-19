from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('profile/<int:pk>', views.UserProfileView.as_view(), name='profile'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('registration/', views.UserRegistrationView.as_view(), name='registration'),
]
