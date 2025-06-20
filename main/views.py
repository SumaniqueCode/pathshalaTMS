from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from user.models import Profile
from django.contrib.auth.decorators import login_required
from tasks.models import Task

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
        image = request.FILES.get('image')
        
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
                return redirect('/dashboard')
            else:
                return render(request, 'pages/auth/login.html',{"errors":{"password":"Invalid password"}})
        else:
            return render(request, 'pages/auth/login.html',{"errors":{"username":"Invalid Username"}})

@login_required(login_url='/login')
def dashboard(request):
    role = request.user.profile.role
    if role == 'employee':
        return redirect('/employee/dashboard')
    elif role == 'employer':
        return redirect('/employer/dashboard')
    else:
        return redirect('/login')
    
@login_required(login_url='/login')    
def employerDashboard(request):
    role = request.user.profile.role
    if role == "employer":
        pendingTasks = Task.objects.filter(status = 'Pending', user = request.user)[ :10]
        completedTasks = Task.objects.filter(status = 'Completed', user = request.user)[ :10]
        inProgressTasks = Task.objects.filter(status = 'In Progress', user = request.user)[ :10]
        return render(request, 'pages/employer/dashboard.html', {'pendingTasks':pendingTasks, 'completedTasks':completedTasks, 'inProgressTasks':inProgressTasks})
    else:
        return redirect('/employee/dashboard')

@login_required(login_url='/login')
def employeeDashboard(request):
    role = request.user.profile.role
    if role == "employee":
        return render(request, 'pages/employee/dashboard.html')
    else:
        return redirect('/employer/dashboard')
