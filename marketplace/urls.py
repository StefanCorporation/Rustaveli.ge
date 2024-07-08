from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from marketplace import views



app_name = 'marketplace'

urlpatterns = [
    path('home/', views.index, name='home')
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)