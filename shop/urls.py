from django.urls import path
from shop import views


app_name = 'shop'

urlpatterns = [
    path('shop/', views.shop, name='shop'),
    path('contact/', views.contact, name='contact'),
    path('single_product/', views.single_product, name='single_product'),
    
]
