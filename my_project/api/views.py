from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
from to_do_list.models import Tasks, Project
from api import serializers
from rest_framework.views import APIView
import json


class IndexTaskView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Tasks.objects.all()
        serializer = serializers.TaskSerializer(qs, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        serializer = serializers.TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse(status=400, data={'errors': serializer.error_messages})


class TasksUpdateView(APIView):
    def update(self, request, id_, partial: bool = True):
        serializer = serializers.TaskSerializer
        if partial:
            serializer = serializers.TaskPartialUpdateSerializer

        instance = Tasks.objects.get(id=id_)
        data = json.loads(request.body)
        serializer = serializer(data=data, instance=instance)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=True)
        else:
            return JsonResponse(status=400, data={'errors': serializer.error_messages})

    def put(self, request, id_, *args, **kwargs):
        return self.update(request, id_, partial=False)

    def patch(self, request, id_, *args, **kwargs):
        return self.update(request, id_, partial=True)

    def delete(self, request, id_, *args, **kwargs):
        instance = Tasks.objects.get(id=id_)
        instance.delete()
        return JsonResponse(data={'success': 'Task wes deleted!'})

    def get(self, request, id_, *args, **kwargs):
        instance = Tasks.objects.get(id=id_)
        serializer = serializers.TaskSerializer(instance)
        return JsonResponse(serializer.data, safe=False)


class IndexProjectView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Project.objects.all()
        serializer = serializers.ProjectSerializer(qs, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        serializer = serializers.ProjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse(status=400, data={'errors': serializer.error_messages})


class ProjectUpdateView(APIView):
    def update(self, request, id_, partial: bool = True):
        serializer = serializers.ProjectSerializer
        if partial:
            serializer = serializers.ProjectPartialUpdateSerializer

        instance = Project.objects.get(id=id_)
        data = json.loads(request.body)
        serializer = serializer(data=data, instance=instance)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=True)
        else:
            return JsonResponse(status=400, data={'errors': serializer.error_messages})

    def put(self, request, id_, *args, **kwargs):
        return self.update(request, id_, partial=False)

    def delete(self, request, id_, *args, **kwargs):
        instance = Project.objects.get(id=id_)
        instance.delete()
        return JsonResponse(data={'success': 'Task wes deleted!'})

    def get(self, request, id_, *args, **kwargs):
        instance = Project.objects.get(id=id_)
        serializer = serializers.ProjectSerializer(instance)
        return JsonResponse(serializer.data, safe=False)

