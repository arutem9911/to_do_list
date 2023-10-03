from django.urls import path
from api.views import *


urlpatterns = [
    path('tasks/', IndexTaskView.as_view()),
    path('tasks/<int:id_>', TasksUpdateView.as_view()),
    path('projects/', IndexProjectView.as_view()),
    path('projects/<int:id_>', ProjectUpdateView.as_view()),

]
