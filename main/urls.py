"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from main import settings
from .views import *
from user.views import *
from projects.views import *
from tasks.views import *

employer_urlpatterns = [
    path("dashboard/", employerDashboard),
    path("projects/", employerProjects),
    path("register-project/", registerProjectPage),
    path("create-project", createProject),
    path("project-details/<int:id>/", employerProjectDetails),
    path('edit-project/<int:id>/', editProjectDetailsPage),
    path('update-project/<int:id>', editProjectDetails),
    path('delete-project/<int:id>', deleteProject),
    path('project/<int:id>/register-task/', registerTaskPage),
    path('create-task', createTask),
    path('task/<int:id>/', taskDetails)
]

employee_urlpatterns = [
    path("dashboard/", employeeDashboard),
    path("projects/", employeeProjects),
    path("project-details/<int:id>/", employeeProjectDetails),
    path('task/<int:id>/', taskDetails)
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index),
    path("login/", loginPage),
    path("register/", registerPage),
    path("register-user", registerUser),
    path("login-user", loginUser),
    path("logout", logoutUser),
    path("profile/", profilePage),
    path("edit-profile/", editProfilePage),
    path("update-profile", editProfile),
    path("dashboard/", dashboard),
    path("employer/", include(employer_urlpatterns)),
    path("employee/", include(employee_urlpatterns)),
    path("projects/", projects),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
