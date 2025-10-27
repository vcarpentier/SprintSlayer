from django.db import models
from django.contrib.auth.models import User

TASKTYPE = ((0, 'Feature'), (1, 'Bug'), (2, 'refactor'))
STATUS = ((0, 'To Do'), (1, 'In Progress'), (2, 'Done'))

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_tasks', null=True, blank=True)
    type = models.IntegerField(choices=TASKTYPE, default=0)

    def __str__(self):
        return self.title
