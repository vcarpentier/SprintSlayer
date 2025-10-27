from django.contrib import admin
from .models import  Task
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Task)
class TaskAdmin(SummernoteModelAdmin):
    list_display = ['title', 'description', 'status', 'assigned_to', 'created_on']
    search_fields = ['title']
    list_filter = ['status']

# Register your models here.
#admin.site.register(Task)
