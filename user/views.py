from django.shortcuts import render

def profilePage(request):
    return render(request, 'pages/profile.html',)
