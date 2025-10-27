from django.shortcuts import render
from django.views import generic
from .models import Task
# Create your views here.


class TaskList(generic.ListView):
    queryset = Task.objects.all()
    template_name = 'sprint/index.html'
