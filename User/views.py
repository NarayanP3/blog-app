from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .form import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account is created. Now Logged In for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'User/login.html', {'form' : form})

@login_required
def profile(request):
    return render(request, 'User/profile.html')
