from django.urls import path, include
# from . import views
from .views import RegisterView, end_session, auth_login

urlpatterns = [
    
   # path('', views.authenticate, name='authentication'),
   path('',RegisterView.as_view(), name='authentication'),
   path('end_session', end_session, name='end_session'),
   path('login', auth_login, name='v_login'),
]
