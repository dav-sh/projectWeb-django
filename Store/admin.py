from django.contrib import admin
from .models import Product, CategoryProd
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=['name','image']


class CategoryAdmin(admin.ModelAdmin):
    list_display=['name']


admin.site.register(Product,ProductAdmin)

admin.site.register(CategoryProd,CategoryAdmin)