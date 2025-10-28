from django.urls import path
from .views import TaskList

urlpatterns = [
    path('', TaskList.as_view(), name='home'),  
    path('<slug:slug>/', TaskList.task_detail, name='task_detail'),
]