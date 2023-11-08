from django.db import models
from django.contrib.auth import get_user_model
from Store.models import Product
from django.db.models import F,Sum, FloatField

User  =  get_user_model()

# Create your models here.
class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.id

    @property
    def total(self):
        return self.order_detail_set.aggregate(
            total = Sum(F('price')*F('quantity'), output_field = FloatField())
        )['total']
    



    class Meta:
        db_table = 'pedidos'
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'
        ordering = ['id']






class order_detail(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id =  models.ForeignKey(Product, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.quantity} unidades de {self.product_id.name}'
    

    class Meta:
        db_table = 'order_detail'
        verbose_name = 'order detail'
        verbose_name_plural = 'orders details'
        ordering = ['id']