from django.urls import path
from .views import my_sprint

urlpatterns = [
    path('', my_sprint, name='my_sprint'),  
]