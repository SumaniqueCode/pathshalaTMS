from django.shortcuts import redirect, render
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages


def profilePage(request):
    return render(request, "pages/profile.html")

def editProfilePage(request):
    return render(request, "pages/auth/edit_profile.html")
    

def logoutUser(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect("/")

def editProfile(request):
    errors = {}
    if request.method == "POST":
        user = request.user
        profile = user.profile
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        image = request.FILES.get("image")
        phone = request.POST.get("phone")
        dob = request.POST.get("dob")
        address = request.POST.get("address")
        gender = request.POST.get("gender")

        if password != confirm_password:
            errors = {"Password": "Passwords do not match"}
        if len(first_name) < 3:
            errors = {"first_name": "First name must be at least 3 characters long"}
        if len(phone) != 10:
            errors = {"phone": "Phone number must be 10 digits long"}
        if len(address) < 3:
            errors = {"address": "Address must be at least 3 characters long"}
        if errors:
            return render(request, "pages/auth/edit_profile.html", {"errors": errors})

        user.first_name = first_name
        user.last_name = last_name
        if password:
            user.set_password(password)
            authenticated_user = authenticate(request, username=user.username, password=password)
            login( request, authenticated_user)
        if image:
            profile.image = image
        profile.dob = dob
        profile.address = address
        profile.phone = phone
        profile.gender = gender
        user.save()
        profile.save()
        
        messages.success(request, "Profile updated successfully")
        return redirect("/profile")
