from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib import messages


def profilePage(request):
    return render(
        request,
        "pages/profile.html",
    )


def logoutUser(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect("/")
