from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.urls import reverse
from .forms import UserProfileForm, LoginForm

def Home(request):
    return render(request, 'Home.html')

def Registration(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registration successful.')
            return redirect(reverse('Login'))  # Replace 'login' with the name of your login view
        else:
            messages.error(request, 'Invalid form submission. Please try again.')
    else:
        form = UserProfileForm()

    return render(request, 'Registration.html', {'form': form})

def Login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Authenticate using email and password
            user = authenticate(request, username=email, password=password)

            if user is not None and user.is_active:
                # Login successful
                login(request, user)
                messages.success(request, 'Login successful.')
                return redirect(reverse('Home'))  # Adjust the redirection URL as needed
            else:
                messages.error(request, 'Invalid email or password.')
        else:
            messages.error(request, 'Invalid form submission. Please try again.')
    else:
        form = LoginForm()

    return render(request, 'Login.html', {'form': form})