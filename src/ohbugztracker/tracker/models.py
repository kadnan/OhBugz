from django.db import models


# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    progress = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    severity = models.SmallIntegerField(default=0)
    open_date = models.DateTimeField()
    close_date = models.DateTimeField()
    status = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.title
