from django.contrib import admin
from .models import Profile

class ProfileAdmin (admin.ModelAdmin):
    list_display = ('user', 'address','role')
    
admin.site.register(Profile, ProfileAdmin)