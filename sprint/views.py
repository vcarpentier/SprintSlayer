from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def my_sprint(request):
    return HttpResponse("Welcome to the Sprint app!")