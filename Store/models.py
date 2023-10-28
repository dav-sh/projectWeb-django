from django.db import models

# Create your models here.

class Product(models.Model):


    class Meta():
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
    
    def __str__(self) -> str:
        return super().__str__()