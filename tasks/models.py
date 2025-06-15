from django.db import models
from django.contrib.auth.models import User
from projects.models import Project


class Task(models.Model):
    class StatusOptions(models.TextChoices):
        PENDING = "Pending", "Pending"
        IN_PROGRESS = "In Progress", "In Progress"
        COMPLETED = "Completed", "Completed"
        CANCELED = "Canceled", "Canceled"
    
    class TaskPriorityOptions(models.TextChoices):
        LOW = "Low", "Low"
        MEDIUM = "Medium", "Medium"
        HIGH = "High", "High"

    title = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assigned_user = models.ForeignKey( User, on_delete=models.SET_NULL, related_name="assigned_tasks", null=True, blank=True)
    status = models.CharField(choices=StatusOptions, default=StatusOptions.PENDING)
    priority = models.CharField (choices=TaskPriorityOptions, default=TaskPriorityOptions.LOW)
    deadline = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
