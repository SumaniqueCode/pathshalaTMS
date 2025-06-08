from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    class StatusOptions(models.TextChoices):
        PENDING = "Pending", "Pending"
        IN_PROGRESS = "In Progress", "In Progress"
        COMPLETED = "Completed", "Completed"
        CANCELED = "Canceled", "Canceled"

    title = models.CharField(max_length=25)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(choices=StatusOptions, default=StatusOptions.PENDING, max_length=15)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True, editable=False)
