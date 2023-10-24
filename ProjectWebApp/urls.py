from django.urls import include, path
from ProjectWebApp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('store/', store, name='store'),
    
    path('contact/', contact, name='contact'),
   
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)