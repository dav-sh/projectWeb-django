from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request):
    return render(request, 'ProjectWebApp/home.html')




def store(request):
    return render(request, 'ProjectWebApp/store.html')



    
def contact(request):
    return render(request, 'ProjectWebApp/contact.html')