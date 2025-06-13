from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'project')
    
admin.site.register(Task, TaskAdmin)
