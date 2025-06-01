from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages

def index(request):
    return render(request, 'pages/index.html')

def loginPage(request):
    return render(request, 'pages/auth/login.html')

def registerPage(request):
    return render(request, 'pages/auth/register.html')

def registerUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render (request, 'pages/auth/register.html',)
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return render (request, 'pages/auth/register.html',)
        if password != confirm_password:
            messages.error(request, "Passwords donot match")
            return render (request, 'pages/auth/register.html',)
        user = User.objects.create_user(username, email, password)
        messages.success(request, "User created successfully")
        user.save()
        return redirect('/login')