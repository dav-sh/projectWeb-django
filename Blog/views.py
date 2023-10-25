from django.shortcuts import render
from .models import Post, Category
# Create your views here.
def Blog(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    # print(posts)
    return render(request, 'blog/blog.html', {'posts':posts,'categories':categories})

def category(request, category_id:int):
    categoria = Category.objects.get(id=category_id)

    posts = Post.objects.filter(category = categoria)
    # print(posts)
    return render(request, 'blog/category.html', {'posts':posts,'categoria':categoria})