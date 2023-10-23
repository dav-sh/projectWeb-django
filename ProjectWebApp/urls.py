from django.urls import include, path
from ProjectWebApp.views import *

urlpatterns = [
    path('', home, name='home'),
    path('services/', services, name='services'),
    path('store/', store, name='store'),
    path('blog/', blog, name='blog'),
    path('contact/', contact, name='contact'),
]

