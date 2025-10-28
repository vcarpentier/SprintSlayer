from django.db import models
from django.contrib.auth.models import User

TASKTYPE = ((0, 'Feature'), (1, 'Bug'), (2, 'refactor'))
# not startd, in progress, completed, in backlog
STATUS = ((0, 'Ready for Battle'), (1, 'Fight'), (2, 'Victory'), (3, 'Camp'))

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_tasks', null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    type = models.IntegerField(choices=TASKTYPE, default=0)

    def __str__(self):
        return self.title
