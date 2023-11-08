from django.contrib import admin

from orders.models import Order, OrderDetail

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','customer']


class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ['order_id','product_id']

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)

