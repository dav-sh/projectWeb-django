from django.shortcuts import render, HttpResponse
from Services.models import Service

# Create your views here.

def home(request):
    return render(request, 'ProjectWebApp/home.html')


def services(request):
    services = Service.objects.all()
    return render(request, 'ProjectWebApp/services.html',{"services": services})


def store(request):
    return render(request, 'ProjectWebApp/store.html')


def blog(request):
    return render(request, 'ProjectWebApp/blog.html')

    
def contact(request):
    return render(request, 'ProjectWebApp/contact.html')