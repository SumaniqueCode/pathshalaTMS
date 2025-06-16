from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Task
from projects.models import Project
from django.contrib import messages


@login_required(login_url="/login")
def registerTaskPage(request, id):
    project_id = id
    if request.user.profile.role == "employer":
        return render(
            request,
            "pages/employer/project/task/register_task.html",
            {"project_id": project_id},
        )


def createTask(request):
    errors = {}
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        status = request.POST.get("status")
        priority = request.POST.get("priority")
        deadline = request.POST.get("deadline")
        project_id = request.POST.get("project_id")
        assigned_user = request.POST.get("assigned_user")

        employee = None
        if len(title) < 3:
            errors["title"] = "Title must be at least 3 characters long."
        if description != "" and len(description) < 5:
            errors["description"] = "Description must be at least 5 characters long."
        if assigned_user:
            employee_check = User.objects.filter(email=assigned_user).exists()
            if employee_check:
                employee = get_object_or_404(User, email=assigned_user)
                if employee.profile.role == "employer":
                    errors["assigned_user"] = "You cannot assign a task to an employer."
            else:
                errors["assigned_user"] = "User does not exist."

        if errors:
            return render(request,"pages/employer/project/task/register_task.html",{"errors": errors},)
            
        auth_user = request.user
        project = get_object_or_404(Project, pk=project_id)
        task = Task.objects.create(
            title=title,
            description=description,
            status=status,
            priority=priority,
            user=auth_user,
            assigned_user=employee,
            deadline=deadline,
            project=project,
        )
        task.save()
        messages.success(request, "Task created successfully!")
        return redirect(f"/employer/project-details/{project_id}/")

@login_required(login_url="/login")
def taskDetails(request, id):
    role = request.user.profile.role
    task = Task.objects.get(pk=id)
    if role == "employer":
        return render(request, "pages/employer/project/task/task_details.html",{"task":task})
    elif role == "employee":
        return render(request, "pages/employer/project/task/task_details.html",{"task":task})
    else:
        return redirect("/")