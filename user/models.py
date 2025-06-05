from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    class RoleOptions(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        EMPLOYER = 'employer', 'Employer'
        EMPLOYEE = 'employee', 'Employee'
        
    class GenderOptions(models.TextChoices):
        MALE = 'male', 'Male'
        FEMALE = 'female', 'Female'
        OTHER = 'other', 'Other'
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(blank=True, null=True,)
    address = models.CharField(blank=True, null=True, max_length=100)
    phone = models.CharField(blank=True, null=True, max_length=10)
    role = models.CharField(choices=RoleOptions, default=RoleOptions.EMPLOYEE, max_length=10)
    gender = models.CharField(choices=GenderOptions, default=GenderOptions.MALE, max_length=6)
    image = models.FileField(upload_to="user_image", blank=True, null=True)
