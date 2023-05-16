from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'finished_at')
    list_display_links = ('name', 'description', 'created_at', 'finished_at')
    search_fields = ('name', 'description',)
    list_filter = ('name', 'description',)
    ordering = ('name', 'description', 'created_at', 'finished_at')


admin.site.register(Task, TaskAdmin)
