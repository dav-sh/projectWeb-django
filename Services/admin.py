from django.contrib import admin
from .models import *
# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title','created']
    readonly_fields = ('created','updated')

admin.site.register(Service, ServiceAdmin)