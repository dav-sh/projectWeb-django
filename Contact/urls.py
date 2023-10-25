from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    # path('thanks/',views.thanks, name='thanks')
]