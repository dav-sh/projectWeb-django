from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')


#I have 2 models I should have to register them
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)