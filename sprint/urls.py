from django.urls import path
from .views import TaskList

urlpatterns = [
    path('', TaskList.as_view(), name='home'),  
    #path('<title:title>/', views.task_detail, name='task_detail'),
]