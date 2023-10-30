from django.contrib import admin
from .models import Store
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=['name','image']


admin.site.register(Store,StoreAdmin)