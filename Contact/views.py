from django.shortcuts import render
from .models import Contact
from .forms import ContactForm

# Create your views here.
def contact(request):
    contc_form = ContactForm()
    # ctc = Contact.objects.all()
    return render(request, 'contact/contact.html',{'my_form':contc_form})