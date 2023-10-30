from django.db import models

# Create your models here.





class CategoryProd(models.Model):

    name = models.CharField(max_length=50)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    
    class Meta():
        verbose_name = 'categoria_prod'
        verbose_name_plural = 'categorias_prod'
    
    def __str__(self) -> str:
        return self.name
    

class Product(models.Model):
    image = models.ImageField(upload_to='store', null=True, blank=True)
    name = models.CharField(max_length=80)
    price = models.FloatField()
    disponibility = models.BooleanField(default=True)
    category = models.ForeignKey(CategoryProd, on_delete=models.CASCADE)

    class Meta():
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
    
    def __str__(self) -> str:
        return self.name
    