from django.urls import path, include
from api.views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register('tasks', TaskViewSet)
router.register('projects', ProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
