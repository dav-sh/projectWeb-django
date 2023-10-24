from django.shortcuts import render
from .models import Post
# Create your views here.
def Blog(request):
    blogs = Post.objects.all()
    return render(request, 'blog/blog.html', {'blogs':blogs})