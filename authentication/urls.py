from django.urls import path, include
# from . import views
from .views import RegisterView
urlpatterns = [
    
   # path('', views.authenticate, name='authenticate'),
   path('',RegisterView.as_view(), name='authenticate'),
]
