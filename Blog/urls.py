from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.Blog, name='blog'),

]