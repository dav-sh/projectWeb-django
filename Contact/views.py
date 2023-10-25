from django.shortcuts import render
# from .models import Contact

# Create your views here.
def contact(request):
    # ctc = Contact.objects.all()
    return render(request, 'contact/contact.html')