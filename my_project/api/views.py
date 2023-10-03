from to_do_list.models import Tasks, Project
from api import serializers
from rest_framework.viewsets import ModelViewSet


class TaskViewSet(ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = serializers.TaskGetSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
    method_serializers = {
        'get': serializers.TaskGetSerializer,
        'patch': serializers.TaskPartialUpdateSerializer
    }

    def method_serializer_class(self):
        method = self.request.method.lower()
        if method in self.method_serializers:
            print(method)
            return self.method_serializers.get(method)

        return self.serializer_class


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = serializers.ProjectGetSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
    method_serializers = {
        'get': serializers.ProjectGetSerializer,
        'patch': serializers.TaskPartialUpdateSerializer
    }

    def method_serializer_class(self):
        method = self.request.method.lower()
        if method in self.method_serializers:
            return self.method_serializers.get(method)

        return self.serializer_class

