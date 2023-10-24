from turtle import update
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#when I create my own model I'll need to make migrations and migrate :D
class Category(models.Model):
    name = models.CharField(max_length= 50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
    def __str__(self) -> str:
        return self.name




class Post(models.Model):
    title = models.CharField(max_length= 50)
    image = models.ImageField(upload_to= 'blog', null = True, blank = True)
    content = models.TextField(max_length= 50)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    category = models.ManyToManyField(Category)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name = 'post'
        verbose_name_plural = 'posts'
    def __str__(self) -> str:
        return self.title