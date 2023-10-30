from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.
def contact(request):
    contc_form = ContactForm()
    # ctc = Contact.objects.all()
    if request.method == "POST":
        contc_form = ContactForm(data=request.POST)
        if contc_form.is_valid():
            name = request.POST.get('your_name')
            email = request.POST.get('your_email')
            message = request.POST.get('your_message')
            # If I reach this point I gonna redirect the user to the same page but adding the 'value' just to know if it's valid
            mail = EmailMessage('msg from django: '+name,message + ' email: '+email,"?",['davisinn2020@gmail.com'],reply_to=[email])
            try:
                mail.send()
                return redirect('/contact/?value')
            except:
                return redirect('/contact/?invalid')
            

    return render(request, 'contact/contact.html',{'my_form':contc_form})