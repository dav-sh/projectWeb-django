from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request):
    return render(request, 'ProjectWebApp/home.html')


def services(request):
    return render(request, 'ProjectWebApp/services.html')


def store(request):
    return render(request, 'ProjectWebApp/store.html')


def blog(request):
    return render(request, 'ProjectWebApp/blog.html')

    
def contact(request):
    return render(request, 'ProjectWebApp/contact.html')