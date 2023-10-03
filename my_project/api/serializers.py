from rest_framework import serializers
from to_do_list.models import Tasks, Project


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['id', 'short_description', 'description', 'status', 'type', 'created_at', 'updated_at', 'project']
        read_only_fields = ['id', 'created_at', 'updated_at', 'project']


class TaskPartialUpdateSerializer(serializers.ModelSerializer):
    short_description = serializers.CharField(max_length=100, required=False)
    description = serializers.CharField(max_length=3000, required=False)

    class Meta:
        model = Tasks
        fields = ['id', 'short_description', 'description', 'status', 'type', 'created_at', 'updated_at', 'project']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'start_date', 'end_date', 'title', 'description']
        read_only_fields = ['id']


class ProjectPartialUpdateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100, required=False)
    description = serializers.CharField(max_length=3000, required=False)

    class Meta:
        model = Tasks
        fields = ['id', 'start_date', 'end_date', 'title', 'description']

