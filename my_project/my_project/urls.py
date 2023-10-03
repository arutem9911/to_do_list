"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.urls import path, include
from to_do_list.views import *
from accounts.views import LoginView, LogoutView

urlpatterns = [
    # path('admin/', admin.site.urls),

    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('', TaskIndexView.as_view(), name='all_tasks'),
    path('new/', CreateTaskView.as_view(), name='new_task'),
    path('new_project_task/<int:id>', ProjectTaskCreateView.as_view(), name='new_project_task'),
    path('delete/<int:id>', DeleteTaskView.as_view(), name='delete_task'),
    path('update/<int:id>', UpdateTaskView.as_view(), name='update_task'),
    path('detail/<int:id>', TaskDetailView.as_view(), name='detail_task'),
    path('projects/', ProjectsIndexView.as_view(), name='all_projects'),
    path('project/new/', CreateProjectView.as_view(), name='new_project'),
    path('project/detail/<int:id>', ProjectDetailView.as_view(), name='detail_project'),
    path('project/update/<int:id>', UpdateProjectView.as_view(), name='update_project'),
    path('project/delete/<int:id>', DeleteProjectView.as_view(), name='delete_project'),
    path('api/', include('api.urls'))
]
