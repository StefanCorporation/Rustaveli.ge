from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rustaveli/', include('marketplace.urls')),
    path('rustaveli/', include('users.urls')),
    path('rustaveli/', include('shop.urls')),
]
