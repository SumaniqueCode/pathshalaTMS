from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login")
def projects(request):
    role = request.user.profile.role
    if role=="employer":
        return redirect('/employer/projects')
    elif role == "employee":
        return redirect('/employee/projects')
    else:
        return redirect('/dashboard')

@login_required(login_url="/login")
def employerProjects(request):
    role = request.user.profile.role
    if role =="employer":
        return render(request, "pages/employer/project/project_page.html")
    else:
        return redirect('/employee/projects')
    
@login_required(login_url="/login")
def employeeProjects(request):
    role = request.user.profile.role
    if role == "employee":
        return render(request, "pages/employee/project/project_page.html")
    else:
        return redirect('/employer/projects')

def registerProjectPage(request):
    return render(request, "pages/employer/project/register_project.html")