from django.contrib import admin
from .models import *

class ProjectAdmin(admin.ModelAdmin):
    list_display=('id', 'title', 'user', 'created_at', 'updated_at')

admin.site.register (Project, ProjectAdmin)
