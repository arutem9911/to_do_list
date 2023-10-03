from django.contrib import admin

from to_do_list.models import *


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'short_description', 'status', 'type', 'created_at', 'updated_at', 'project']
    list_filter = ['status', 'type', 'project']
    search_fields = ['short_description', 'status', 'type', 'project']
    fields = ['short_description', 'description', 'status', 'type', 'project']


class TypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'type']
    list_filter = ['type']
    search_fields = ['type']
    fields = ['type']


class StatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'status']
    list_filter = ['status']
    search_fields = ['status']
    fields = ['status']


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'start_date', 'end_date', 'title', 'description']
    list_filter = ['title', 'description']
    search_fields = ['title', 'description']
    fields = ['start_date', 'end_date', 'title', 'description']


admin.site.register(Tasks, TaskAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Project, ProjectAdmin)

