from django.contrib import admin
from tasks import models


@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'deadline', 'priority']
    list_filter = ['priority']
    search_fields = ['title']


@admin.register(models.TaskList)
class TaskListAdmin(admin.ModelAdmin):
    pass
