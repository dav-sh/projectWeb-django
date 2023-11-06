from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.

class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'auth/auth.html', {'form': form})
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            # add the info in the table auth
            
            user = form.save()

            login(request, user)

            return redirect('home')

        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, 'auth/auth.html', {'form': form})

