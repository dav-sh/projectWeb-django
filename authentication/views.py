from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
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
        

def end_session(request):
    logout(request)
    return redirect('home')


def auth_login(request):
    if request.method == "POST":

        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = user_name, password = password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'user not valid')

        else:
            messages.error(request, 'Incorrect data')
    form = AuthenticationForm()
    return render(request, 'login/login.html', {'form': form})
