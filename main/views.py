from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from user.models import Profile

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
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        dob = request.POST.get('dob')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        image = request.POST.get('image')
        
        if User.objects.filter(username=username).exists():
            return render (request, 'pages/auth/register.html',{ "errors":{'username': 'Username already exists.'}})
        if User.objects.filter(email=email).exists():
            return render (request, 'pages/auth/register.html', { "errors":{'email': 'Email already exists'}})
        if password != confirm_password:
            return render (request, 'pages/auth/register.html', { "errors":{'password':'passwords do not match'}})
        if len(phone)!=10:
            return render (request, 'pages/auth/register.html', { "errors":{'phone':'phone number should be 10 digits'}})
        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
        profile = Profile(user=user, dob=dob, phone=phone, address=address, gender=gender, role="employee", image=image)
        profile.save()
        messages.success(request, "User created successfully")
        user.save()
        return redirect('/login')
    
def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user= User.objects.filter(username=username)
        if user:
            authenticated_user = authenticate(request, username=username, password=password)
            if authenticated_user:
                login(request, authenticated_user)
                messages.success(request, "User Logged in successfully")
                if authenticated_user.profile.role == 'employee':
                    return redirect('/employee/dashboard')
                if authenticated_user.profile.role == 'employer':
                    return redirect('/employer/dashboard')
                return redirect('/')
            else:
                return render(request, 'pages/auth/login.html',{"errors":{"password":"Invalid password"}})
        else:
            return render(request, 'pages/auth/login.html',{"errors":{"username":"Invalid Username"}})

def employerDashboard(request):
    return render(request, 'pages/employer/dashboard.html')