from django.urls import include, path
from .import views
from django.conf import settings
from django.conf.urls.static import static

# avoid collisions with other urls (namespace)
app_name = 'shopc'

urlpatterns = [
    
    path('add/<int:product_id>/', views.add_product , name='add'),
    path('delete/<int:product_id>/', views.delete_product , name='delete'),
    path('substract/<int:product_id>/', views.substract_product , name='substract'),
    path('clean/<int:product_id>/', views.clean_products , name='clean'),


   
]

