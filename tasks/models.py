from django.db import models
from django.contrib.auth.models import User
from projects.models import Project


def attachment_path(instance, filename):
    return f'attachments/{instance.id}/{filename}'

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
    status = models.CharField(choices=StatusOptions, default=StatusOptions.PENDING, max_length=30)
    priority = models.CharField (choices=TaskPriorityOptions, default=TaskPriorityOptions.LOW, max_length=6)
    deadline = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    attachment = models.FileField(blank=True, null=True, upload_to=attachment_path)
