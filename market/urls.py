from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from market import views



app_name = 'market'

urlpatterns = [
    path('', views.index, name='market')
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)