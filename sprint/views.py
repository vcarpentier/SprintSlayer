from django.shortcuts import render
from django.views import generic
from .models import Task
# Create your views here.


class PostList(generic.ListView):
    model = Task
    # queryset = Task.objects.all()
