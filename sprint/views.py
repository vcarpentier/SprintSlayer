from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Task


class TaskList(generic.ListView):
    queryset = Task.objects.all()
    template_name = 'sprint/index.html'

    def task_detail(request, slug):
        queryset = Task.objects.all()
        task = get_object_or_404(queryset, slug=slug)
        return render(request, 'sprint/task_detail.html', {'task': task})
